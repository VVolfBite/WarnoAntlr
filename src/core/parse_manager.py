"""NDF解析管理器模块
提供NDF文件的解析、注册和对象生成功能

主要功能:
1. 文件解析 - NDF文件的解析和处理
2. 对象注册 - 类定义的注册和管理
3. 对象生成 - 实例对象的生成和引用处理
"""

import re
import logging
from pathlib import Path
from typing import List, Tuple, Dict, Any, Optional
from threading import Lock
from datetime import datetime

import antlr4
from antlr4 import CommonTokenStream
from antlr4.tree.Tree import ParseTreeWalker
from antlr4 import FileStream, CommonTokenStream, PredictionMode, Parser

from .config_manager import ConfigManager
from .path_resolver import PathResolver
from ..parsers.parser.NdfGrammarLexer import NdfGrammarLexer
from ..parsers.parser.NdfGrammarParser import NdfGrammarParser
from ..parsers.syntax_tree.actions import semantic_actions_generator
from ..extractor.base_class import BaseDescription

class ParseManager:
    """NDF解析管理器"""
    def __init__(self, config: ConfigManager):
        self.config = config
        self.register_dict = {}  # 普通字典，存储注册信息
        self.path_resolver = PathResolver()  # 路径解析器，用于生成对象
        
        # 工具设置
        self.merge_lock = Lock()
        self.max_workers = 4
        
        # 日志设置
        self.log_file = config.version_output_dir / "parse.log"

    def log(self, message: str):
        """记录日志"""
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
        except Exception as e:
            print(f"Failed to write log: {e}")

    def _extract_single(self, content: str, namespace: str, mode: str = "generate_object") -> Dict:
        """解析单个文件内容"""
        try:
            input_stream = antlr4.InputStream(content)
            lexer = NdfGrammarLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = NdfGrammarParser(stream)
            parser._interp.predictionMode = PredictionMode.SLL
            
            tree = parser.ndf_file()
            reference = self.path_resolver if mode == "generate_object" else None
            
            listener = semantic_actions_generator.Generator(
                parser,
                config=self.config,
                name_space=namespace,
                reference=reference,
                mode=mode
            )
            
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            
            return listener.generator if mode == "generate_object" else listener.register
        except Exception as e:
            self.log(f"Error parsing content: {str(e)}")
            raise

    def extract(self, file_path: Path, namespace: str, mode: str = "generate_object", chunk_size: Optional[int] = None) -> Dict:
        """解析文件，支持分块处理"""
        try:
            with open(file_path, 'r', encoding='utf8') as f:
                content = f.read()
                
            if chunk_size is None:
                return self._extract_single(content, namespace, mode)
                
            # 按export语句分块处理
            chunks = []
            current_chunk = []
            export_count = 0
            
            for line in content.splitlines():
                if line.strip().startswith('export'):
                    if export_count >= chunk_size:
                        chunks.append('\n'.join(current_chunk))
                        current_chunk = []
                        export_count = 0
                    export_count += 1
                current_chunk.append(line)
                
            if current_chunk:
                chunks.append('\n'.join(current_chunk))
                
            # 处理所有分块
            result = {}
            for i, chunk in enumerate(chunks):
                chunk_result = self._extract_single(chunk, namespace, mode)
                result = self.merge(result, chunk_result)
                self.log(f"Processed chunk {i+1}/{len(chunks)} of {file_path}")
                    
            return result
            
        except Exception as e:
            self.log(f"Error processing file {file_path}: {str(e)}")
            raise

    def merge(self, dict1: dict, dict2: dict) -> dict:
        """合并字典
        合并规则：
        1. 字典结构只能扩充不能缩短（保留所有已有字段）
        2. 不能覆盖template中定义的值
        3. 对于新的字段，可以添加
        
        例子 - 合并类定义：
        dict1 = {
            "TCriticalEffectModuleDescriptor": {
                "base": {"name": "BaseDescription"},
                "attributes": {
                    "Bounds": "(1,200)",
                    "TerrainCriticalEffectTimer": "1"
                }
            }
        }
        dict2 = {
            "TCriticalEffectModuleDescriptor": {
                "base": {"name": "BaseDescription"},
                "attributes": {
                    "Bounds": "(1,10)",
                    "TerrainCriticalEffectTimer": "5.0",
                    "NewField": "value"
                }
            }
        }
        结果: {
            "TCriticalEffectModuleDescriptor": {
                "base": {"name": "BaseDescription"},
                "attributes": {
                    "Bounds": "(1,200)",  # 保留原值
                    "TerrainCriticalEffectTimer": "1",  # 保留原值
                    "NewField": "value"  # 添加新字段
                }
            }
        }
        """
        result = dict1.copy()
        
        for key, value in dict2.items():
            if key not in result:
                # 如果是新key，直接添加
                result[key] = value
            else:
                # 如果key已存在
                if isinstance(result[key], dict) and isinstance(value, dict):
                    # 如果两边都是字典，递归处理
                    if "attributes" in result[key] and "attributes" in value:
                        # 特殊处理attributes字典
                        result[key]["attributes"] = {
                            **value["attributes"],  # 先放新的attributes
                            **result[key]["attributes"]  # 然后用旧的覆盖（保留原值）
                        }
                        # 处理其他字段（如base等）
                        for k, v in value.items():
                            if k != "attributes":
                                if k not in result[key]:
                                    result[key][k] = v
                    else:
                        # 对于非attributes的字典，递归合并
                        for k, v in value.items():
                            if k not in result[key]:
                                result[key][k] = v
                            elif isinstance(result[key][k], dict) and isinstance(v, dict):
                                result[key][k] = self.merge(result[key][k], v)
                # 如果不是字典，保留原值（不覆盖）
                
        return result

    def register_objects(self, file_list: List[Tuple[str, str]], batch_name: str, chunk_size: Optional[int] = None):
        """注册对象"""
        for file_path, namespace in file_list:
            full_path = self.config.version_data_dir / file_path
            if not full_path.exists():
                self.log(f"File not found: {full_path}")
                continue
                
            try:
                result = self.extract(full_path, namespace, "register_object", chunk_size)
                self.register_dict = self.merge(self.register_dict, result)  # 使用merge合并字典
                STOP = 1
            except Exception as e:
                self.log(f"Error registering objects from {file_path}: {str(e)}")
                raise

    def register_templates(self, file_list: List[Tuple[str, str]], batch_name: str, chunk_size: Optional[int] = None):
        """注册模板"""
        for file_path, namespace in file_list:
            full_path = self.config.version_data_dir / file_path
            if not full_path.exists() or not self.has_template(full_path):
                continue
                
            try:
                result = self.extract(full_path, namespace, "register_template", chunk_size)
                self.register_dict = self.merge(self.register_dict, result)  # 使用merge合并字典
            except Exception as e:
                self.log(f"Error registering templates from {file_path}: {str(e)}")
                raise

    def generate_objects(self, file_list: List[Tuple[str, str]], batch_name: str, chunk_size: Optional[int] = None):
        """生成对象"""
        for file_path, namespace in file_list:
            full_path = self.config.version_data_dir / file_path
            if not full_path.exists():
                self.log(f"File not found: {full_path}")
                continue
                
            try:
                result = self.extract(full_path, namespace, "generate_object", chunk_size)
                # self.path_resolver.merge(result, namespace)  # 使用路径解析器合并
            except Exception as e:
                self.log(f"Error generating objects from {file_path}: {str(e)}")
                raise

    def has_template(self, file_path: Path) -> bool:
        """检查文件是否包含模板"""
        try:
            with open(file_path, 'r', encoding='utf8') as f:
                content = f.read()
                return bool(re.search(r'\b(private\s+)?template\b', content))
        except Exception:
            return False

    def export(self, file_path: Optional[Path] = None):
        """导出类定义"""
        try:
            if file_path is None:
                file_path = self.base_dir / "classes.py"
                
            file_path.parent.mkdir(parents=True, exist_ok=True)

            def format_value(value):
                if isinstance(value, BaseDescription):
                    return value.reverse()
                elif isinstance(value, (list, tuple)):
                    items = [format_value(item) for item in value]
                    return f"[{', '.join(items)}]"
                elif isinstance(value, dict):
                    items = [f'"{k}": {format_value(v)}' for k, v in value.items()]
                    return f"{{{', '.join(items)}}}"
                elif isinstance(value, str):
                    return f'"{value}"'
                else:
                    return str(value)

            def format_param_default(key, value, is_base_only):
                if is_base_only:
                    return f"{key}=None"
                if isinstance(value, dict) and 'default' in value:
                    default = value['default']
                    if isinstance(default, str):
                        return f'{key}="{default}"'
                    return f"{key}={default if default is not None else 'None'}"
                elif isinstance(value, str):
                    if value.startswith('@'):
                        return f"{key}={value.lstrip('@')}"
                    return f'{key}="{value}"'
                else:
                    return f"{key}={format_value(value)}"

            imports = "from src.extractor.base_class import BaseDescription\n\n"
            
            # 将类按继承关系排序
            sorted_classes = []
            base_classes = []  # 直接继承BaseDescription的类
            other_classes = []  # 其他类
            
            for class_name, data in self.register_dict.items():
                base = data.get("base") or {}
                base_name = base.get("name", "BaseDescription")
                if base_name == "BaseDescription":
                    base_classes.append((class_name, data))
                else:
                    other_classes.append((class_name, data))
                    
            # 合并排序后的类列表
            sorted_classes = base_classes + other_classes
            
            class_definitions = []
            for class_name, data in sorted_classes:
                attributes = data.get("attributes", {})
                base = data.get("base") or {}
                base_name = base.get("name", "BaseDescription")
                base_attributes = base.get("attributes", {})
                class_definition = f"class {class_name}({base_name}):\n"
                is_base_only = base_name == "BaseDescription"
                current_params = ", ".join(
                    format_param_default(key, value, is_base_only)
                    for key, value in attributes.items()
                )
                if not is_base_only:
                    super_params = ", ".join(
                        format_param_default(key, value, False)
                        for key, value in base_attributes.items()
                    )
                if current_params:
                    class_definition += f"    def __init__(self, {current_params}):\n"
                    if not is_base_only:
                        class_definition += f"        super().__init__({super_params})\n"
                    for key in attributes.keys():
                        class_definition += f"        self.{key} = {key}\n"
                else:
                    class_definition += f"    def __init__(self):\n"
                    class_definition += f"        pass\n"
                class_definitions.append(class_definition)

            complete_class_definitions = imports + "\n\n".join(class_definitions)
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(complete_class_definitions)
                
            self.log(f"Successfully exported classes to {file_path}")
            
        except Exception as e:
            self.log(f"Error exporting classes: {str(e)}")
            raise

    def refer(self):
        """建立索引"""
        def _refer_recursive(obj: Any, visited: set = None):
            if visited is None:
                visited = set()
                
            if id(obj) in visited:
                return
            visited.add(id(obj))
            
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(k, str):
                        resolved = self.path_resolver.get(k)
                        if resolved is not None:
                            obj[k] = resolved
                    _refer_recursive(v, visited)
            elif isinstance(obj, (list, tuple)):
                for item in obj:
                    _refer_recursive(item, visited)
            elif hasattr(obj, '__dict__'):
                _refer_recursive(obj.__dict__, visited)
                
        _refer_recursive(self.path_resolver.to_dict())

