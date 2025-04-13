"""NDF管理器模块
提供NDF文件的解析、注册和对象生成功能

主要功能:
1. 基础设施 - 初始化、日志和错误处理
2. 文件处理 - 文件检查、路径解析和内容提取
3. 对象注册 - 串行和并行对象注册
4. 模板系统 - 模板检查和注册
5. 对象生成 - 串行和并行对象生成
6. 数据管理 - 序列化、导出和值操作
"""

#---------------------------------------------
# 1. 导入声明
#---------------------------------------------
# 标准库
import sys
import re
import logging
from pathlib import Path
from typing import List, Tuple, Dict, Any, Union, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from datetime import datetime
import json

# 第三方库
import dill
import antlr4
from antlr4 import FileStream, CommonTokenStream, PredictionMode, Parser
from antlr4.tree.Tree import ParseTreeWalker

from antlr4.atn.PredictionMode import PredictionMode

# 本地导入
try:
    from .config_manager import ConfigManager
    from ..parsers.parser.NdfGrammarLexer import NdfGrammarLexer
    from ..parsers.parser.NdfGrammarParser import NdfGrammarParser
    from ..parsers.syntax_tree.actions import semantic_actions_generator
    from ..extractor.base_class import BaseDescription
except ImportError:
    from core.config_manager import ConfigManager
    from src.parsers.parser.NdfGrammarLexer import NdfGrammarLexer
    from src.parsers.parser.NdfGrammarParser import NdfGrammarParser
    from src.parsers.syntax_tree.actions import semantic_actions_generator
    from src.extractor.base_class import BaseDescription

#---------------------------------------------
# 2. 管理器类定义
#---------------------------------------------
class ParseManager:
    """NDF解析管理器"""
    
    #-------------------------
    # 2.1 基础设施
    #-------------------------
    def __init__(self, base_dir: Path = None):
        """初始化管理器"""
        sys.setrecursionlimit(10000)  # 设置为10000
        
        self.config = ConfigManager.get_instance()
        if not self.config.version:
            raise ValueError("Config version not set")
            
        self.base_dir = base_dir or self.config.output_dir / self.config.version
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
        self.register_dict = {}    # 注册信息字典
        self.generate_dict = {}    # 生成对象字典
        
        self.log_file = self.base_dir / "parse.log"
        self.merge_lock = Lock()   # 添加线程锁
        self.max_workers = 4       # 控制并发数量

    def log(self, message: str):
        """记录日志"""
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(f"{message}\n")
        except Exception as e:
            print(f"Failed to write log: {e}")
        
    def _handle_error(self, msg: str, ctx: Optional[Any] = None):
        """处理错误"""
        if ctx:
            line = getattr(ctx.start, 'line', '?')
            col = getattr(ctx.start, 'column', '?')
            text = getattr(ctx, 'getText', lambda: '')()
            logging.error(f"Line {line}:{col} - {msg} near '{text}'")
        else:
            logging.error(msg)
            
        self.ignore += 1

    #-------------------------
    # 2.2 文件处理
    #-------------------------
    def check_files(self, file_list: List[Tuple[str, str]]) -> Dict[str, bool]:
        """检查文件列表"""
        file_status = {}
        for file, _ in file_list:
            file_path = self.config.get_full_path(file)
            file_status[file] = file_path.exists()
        return file_status

    def _resolve_path(self, path: Union[str, List[str]], namespace: Optional[str]) -> str:
        """解析路径"""
        if isinstance(path, list):
            path = '/' + '/'.join(str(p) for p in path)
        elif not isinstance(path, str):
            raise TypeError("路径必须是字符串或列表")
            
        path = path.strip()
        
        if path.startswith('$'):
            return path.lstrip('$/').strip('/')
            
        if path.startswith('~/'):
            if not namespace:
                raise ValueError("相对路径必须提供命名空间")
                
            if namespace.startswith('$'):
                namespace = namespace.lstrip('$/')
            elif not namespace.startswith('/'):
                raise ValueError(f"Namespace '{namespace}' 必须以 '/' 或 '$' 开头")
                
            return f"{namespace.rstrip('/')}/{path[2:].strip('/')}"
            
        return path.strip('/')
        
    def _extract_single(self, content: str, name_space: str, reference: Any, mode: str = "generate_object") -> Dict:
        """解析单个文件内容块
        Args:
            content: 要解析的文本内容
            name_space: 命名空间  
            reference: 引用对象
            mode: 解析模式
        Returns:
            解析结果字典
        """
        try:
            input_stream = antlr4.InputStream(content)
            lexer = NdfGrammarLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = NdfGrammarParser(stream)
            parser._interp.predictionMode = PredictionMode.SLL
            tree = parser.ndf_file()
            listener = semantic_actions_generator.Generator(
                parser,
                name_space=name_space, 
                reference=reference,
                mode=mode
            )
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            return (listener.generator if mode == "generate_object" else listener.register)
        except Exception as e:
            self.log(f"Error parsing content: {str(e)}")
            raise

    def extract(self, file_name: str, name_space: str, reference: Any, mode: str = "generate_object", chunk_size: Optional[int] = None) -> Dict:
        """解析文件,支持分块处理
        Args:
            file_name: 文件名
            name_space: 命名空间
            reference: 引用对象
            mode: 解析模式 
            chunk_size: 每个分块包含的export数量,None表示不分块
        Returns:
            解析结果字典
        """
        try:
            with open(file_name, 'r', encoding='utf8') as f:
                content = f.read()
                
            if chunk_size is None:
                # 不分块
                return self._extract_single(content, name_space, reference, mode)
                
            # 按export语句分块
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
                
            # 添加最后一块
            if current_chunk:
                chunks.append('\n'.join(current_chunk))
                
            # 处理每个分块
            result = {}
            for i, chunk in enumerate(chunks):
                chunk_result = self._extract_single(chunk, name_space, reference, mode)
                result.update(chunk_result)
                self.log(f"Processed chunk {i+1}/{len(chunks)} of {file_name}")
                    
            return result
            
        except Exception as e:
            self.log(f"Error processing file {file_name}: {str(e)}")
            raise

    #-------------------------
    # 2.3 对象注册
    #-------------------------
    def register_objects(self, file_list: List[Tuple[str, str]], batch_name: str, chunk_size: Optional[int] = None):
        """串行注册对象"""
        print(f"\nStarting object registration for batch {batch_name}...")
        
        for file, namespace in file_list:
            file_path = self.config.get_full_path(file)
            object_dict = self.extract(
                str(file_path),
                namespace,
                None,
                mode="register_object",
                chunk_size=chunk_size
            )
            self.register_dict = self.merge(self.register_dict, object_dict)

    def register_objects_parallel(self, file_list: List[Tuple[str, str]], batch_name: str, chunk_size: Optional[int] = None):
        """并行注册对象"""
        print(f"\nStarting object registration for batch {batch_name}...")
    
        try:
            # 检查文件
            file_status = self.check_files(file_list)
            if not all(file_status.values()):
                missing_files = [f for f, exists in file_status.items() if not exists]
                raise FileNotFoundError(f"Following files not found:\n" + "\n".join(missing_files))
            
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = []
                for file, namespace in file_list:
                    file_path = self.config.get_full_path(file)
                    future = executor.submit(
                        self.extract,
                        str(file_path),
                        namespace,
                        None,
                        "register_object",
                        chunk_size
                    )
                    futures.append((future, file))
                
                for future, file in futures:
                    try:
                        object_dict = future.result()
                        with self.merge_lock:
                            self.register_dict = self.merge(self.register_dict, object_dict)
                    except Exception as e:
                        # 记录错误上下文
                        context = {
                            "file": file,
                            "stage": "register_objects",
                            "processed_files": [f for f, _ in file_list]
                        }
                        self._save_error_state(batch_name, e, context)
                        raise
                        
            print(f"Object registration completed for batch {batch_name}")
            
        except Exception as e:
            self.log(f"Error in batch {batch_name}: {str(e)}")
            raise

    #-------------------------
    # 2.4 模板系统
    #-------------------------
    def has_template(self, file_path: Path) -> bool:
        """检查模板"""
        try:
            with open(file_path, 'r', encoding='utf8') as f:
                content = f.read()
                if 'template' not in content:
                    return False
                return bool(re.search(r'\b(private\s+)?template\b', content))
        except Exception as e:
            self.log(f"Error checking template in {file_path}: {str(e)}")
            return False
        
    def register_templates(self, file_list: List[Tuple[str, str]], batch_name: str, chunk_size: Optional[int] = None):
        """串行注册模板"""
        print(f"\nStarting template registration for batch {batch_name}...")
        
        try:
            for file, namespace in file_list:
                try:
                    file_path = self.config.get_full_path(file)
                    if not self.has_template(file_path):
                        self.log(f"Skipping file without templates: {file}")
                        continue
                        
                    template_dict = self.extract(
                        str(file_path),
                        namespace,
                        self,
                        mode="register_template",
                        chunk_size=chunk_size
                    )
                    self.register_dict = self.merge(self.register_dict, template_dict)
                    
                except Exception as e:
                    # 记录错误上下文
                    context = {
                        "file": file,
                        "stage": "register_templates",
                        "processed_files": [f for f, _ in file_list]
                    }
                    self._save_error_state(batch_name, e, context)
                    raise
                    
            print(f"Template registration completed for batch {batch_name}")
            
        except Exception as e:
            self.log(f"Error in batch {batch_name}: {str(e)}")
            raise
        
    def register_templates_parallel(self, file_list: List[Tuple[str, str]], batch_name: str, chunk_size: Optional[int] = None):
        """并行注册模板"""
        print(f"\nStarting template registration for batch {batch_name}...")
        
        try:
            # 获取包含模板的文件
            template_files = []
            for file, namespace in file_list:
                file_path = self.config.get_full_path(file)
                if self.has_template(file_path):
                    template_files.append((file, namespace))
                else:
                    self.log(f"Skipping file without templates: {file}")
                    
            if not template_files:
                print(f"No template files found in batch {batch_name}, skipping")
                return
                
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = []
                for file, namespace in template_files:
                    file_path = self.config.get_full_path(file)
                    future = executor.submit(
                        self.extract,
                        str(file_path),
                        namespace,
                        self,
                        "register_template",
                        chunk_size
                    )
                    futures.append((future, file))
                
                for future, file in futures:
                    try:
                        template_dict = future.result()
                        with self.merge_lock:
                            self.register_dict = self.merge(self.register_dict, template_dict)
                    except Exception as e:
                        # 记录错误上下文
                        context = {
                            "file": file,
                            "stage": "register_templates_parallel",
                            "processed_files": [f for f, _ in file_list]
                        }
                        self._save_error_state(batch_name, e, context)
                        raise
                        
            print(f"Template registration completed for batch {batch_name}")
            
        except Exception as e:
            self.log(f"Error in batch {batch_name}: {str(e)}")
            raise

    #-------------------------
    # 2.5 对象生成
    #-------------------------
    def generate_objects(self, file_list: List[Tuple[str, str]], batch_name: str, chunk_size: Optional[int] = None):
        """串行生成对象"""
        print(f"\nStarting object generation for batch {batch_name}...")
        
        try:
            for file, namespace in file_list:
                try:
                    file_path = self.config.get_full_path(file)
                    object_dict = self.extract(
                        str(file_path),
                        namespace,
                        self,
                        mode="generate_object",
                        chunk_size=chunk_size
                    )
                    self.set_batch(object_dict, namespace)
                    
                except Exception as e:
                    # 记录错误上下文
                    context = {
                        "file": file,
                        "stage": "generate_objects",
                        "processed_files": [f for f, _ in file_list]
                    }
                    self._save_error_state(batch_name, e, context)
                    raise
                    
            print(f"Object generation completed for batch {batch_name}")
            
        except Exception as e:
            self.log(f"Error in batch {batch_name}: {str(e)}")
            raise
        
    def generate_objects_parallel(self, file_list: List[Tuple[str, str]], batch_name: str, chunk_size: Optional[int] = None):
        """并行生成对象"""
        print(f"\nStarting object generation for batch {batch_name}...")
        
        try:
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = []
                for file, namespace in file_list:
                    file_path = self.config.get_full_path(file)
                    future = executor.submit(
                        self.extract,
                        str(file_path),
                        namespace,
                        self,
                        "generate_object",
                        chunk_size
                    )
                    futures.append((future, (file, namespace)))
                    
                for future, (file, namespace) in futures:
                    try:
                        object_dict = future.result()
                        with self.merge_lock:
                            self.set_batch(object_dict, namespace)
                    except Exception as e:
                        # 记录错误上下文
                        context = {
                            "file": file,
                            "stage": "generate_objects_parallel",
                            "processed_files": [f for f, _ in file_list]
                        }
                        self._save_error_state(batch_name, e, context)
                        raise
                        
            print(f"Object generation completed for batch {batch_name}")
            
        except Exception as e:
            self.log(f"Error in batch {batch_name}: {str(e)}")
            raise

    #-------------------------
    # 2.6 数据管理
    #-------------------------
    def _clean_for_serialization(self, obj: Any) -> Any:
        """清理对象以准备序列化,只保留必要数据"""
        if isinstance(obj, dict):
            return {k: self._clean_for_serialization(v) for k, v in obj.items()}
                
        elif isinstance(obj, (list, tuple)):
            return [self._clean_for_serialization(x) for x in obj]
            
        elif hasattr(obj, '__dict__'):
            # 只保留真正需要的数据属性
            data_dict = {}
            for k, v in vars(obj).items():
                # 跳过所有非数据属性
                if (k.startswith('_') or  # 跳过私有属性
                    callable(v) or        # 跳过方法
                    isinstance(v, type)): # 跳过类引用
                    continue
                data_dict[k] = self._clean_for_serialization(v)
            return data_dict
            
        # 只保留基本类型数据
        elif isinstance(obj, (int, float, str, bool, type(None))):
            return obj
        else:
            return str(obj)  # 其他类型转为字符串

    def save(self, mode: str = "generate", file_path: Optional[Path] = None):
        """保存数据"""
        try:
            if file_path is None:
                file_path = self.base_dir / f"{mode}.dill"
                
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 清理并序列化数据
            data = self.register_dict if mode == "register" else self.generate_dict
            clean_data = self._clean_for_serialization(data)
                
            with open(file_path, "wb") as f:
                dill.dump(clean_data, f)
                    
            self.log(f"Successfully saved {mode} data to {file_path}")
            
        except Exception as e:
            self.log(f"Error saving to file: {str(e)}")
            raise

    def load(self, mode: str = "generate", file_path: Optional[Path] = None):
        """加载数据"""
        try:
            if file_path is None:
                file_path = self.base_dir / f"{mode}.dill"
                
            if not file_path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
                
            with open(file_path, "rb") as f:
                data = dill.load(f)
                
                # 验证加载的数据
                if not isinstance(data, dict):
                    raise TypeError(f"Loaded data must be a dictionary")
                    
                if mode == "register":
                    self.register_dict = data
                else:
                    self.generate_dict = data
                    
            self.log(f"Successfully loaded {mode} data from {file_path}")
            
        except Exception as e:
            self.log(f"Error loading from file: {str(e)}")
            raise
        
    def export(self, file_path: Optional[Path] = None, batch_name: Optional[str] = None):
        """导出类定义
        Args:
            file_path: 可选的自定义输出路径
            batch_name: 批次名称,用于获取默认输出文件名
        """
        try:
            # 确定输出路径
            if file_path is None:
                if not self.config.version:
                    raise ValueError("Config version not set")
                    
                if batch_name:
                    # 使用批次配置的导出文件名
                    export_file = self.config.get_batch_export_file(batch_name)
                else:
                    # 默认导出文件名
                    export_file = "classes.py"
                    
                file_path = self.config.get_output_path(export_file)

            # 确保目录存在
            file_path.parent.mkdir(parents=True, exist_ok=True)

            # ...existing code for class generation...

            self.log(f"Successfully exported classes to {file_path}")
                
        except Exception as e:
            self.log(f"Error exporting classes: {str(e)}")
            raise

    def merge(self, dict1: dict, dict2: dict) -> dict:
        """合并字典"""
        for key, value in dict2.items():
            if key in dict1:
                if isinstance(dict1[key], dict) and isinstance(value, dict):
                    dict1[key] = self.merge(dict1[key], value)
                elif dict1[key] is None:
                    dict1[key] = value
            else:
                dict1[key] = value
        return dict1
        
    def get(self, path: Union[str, List[str]], namespace: Optional[str] = None) -> Any:
        """获取值"""
        try:
            full_path = self._resolve_path(path, namespace)
            keys = full_path.strip('/').split('/')
            current = self.generate_dict
            for key in keys:
                if isinstance(current, dict) and key in current:
                    current = current[key]
                elif hasattr(current, key):
                    current = getattr(current, key)
                else:
                    self.log(f"Warning: Path '{path}' not found in namespace '{namespace}'")
                    return full_path.lstrip("$~/")
            return current
        except Exception as e:
            self.log(f"Error accessing path '{path}': {str(e)}")
            return None
        
    def set(self, path: str, value: Any, namespace: Optional[str] = None):
        """设置值"""
        full_path = self._resolve_path(path, namespace)
        keys = full_path.strip('/').split('/')
        current = self.generate_dict
        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]
        current[keys[-1]] = value
        
    def set_batch(self, data_dict: dict, current_namespace: str):
        """批量设置"""
        if not isinstance(data_dict, dict):
            raise TypeError("data_dict 必须是一个字典")
        for key, value in data_dict.items():
            self.set(key, value, namespace=current_namespace)

    def _save_error_state(self, batch_name: str, error: Exception, context: dict):
        """保存错误状态
        Args:
            batch_name: 当前处理的批次名
            error: 发生的错误
            context: 错误发生时的上下文信息
        """
        try:
            # 创建错误记录目录
            error_dir = self.base_dir / "errors" / batch_name
            error_dir.mkdir(parents=True, exist_ok=True)
            
            # 保存错误信息
            error_info = {
                "timestamp": datetime.now().isoformat(),
                "error_type": type(error).__name__,
                "error_msg": str(error),
                "context": context
            }
            
            # 保存错误记录
            with open(error_dir / "error.json", "w", encoding="utf-8") as f:
                json.dump(error_info, f, ensure_ascii=False, indent=2)
                
            # 保存当前状态
            self.save(mode="register", file_path=error_dir / "register.dill")
            self.save(mode="generate", file_path=error_dir / "generate.dill")
            
            self.log(f"Error state saved to {error_dir}")
            
        except Exception as e:
            self.log(f"Failed to save error state: {e}")

    def refer(self, current: Any = None, visited: Optional[set] = None) -> None:
        """递归解析引用"""
        if visited is None:
            visited = set()
        if current is None:
            current = self.generate_dict
            
        current_id = id(current)
        if current_id in visited:
            return
        visited.add(current_id)
        
        try:
            # 处理字典
            if isinstance(current, dict):
                for key, value in current.items():
                    if isinstance(value, str):
                        resolved = self.get(value)
                        if resolved is not None and resolved != value:
                            self.log(f"Reestablish reference for [{value}]")
                            current[key] = resolved
                    else:
                        self.refer(value, visited)
                        
            # 处理列表或元组
            elif isinstance(current, (list, tuple)):
                for i, value in enumerate(current):
                    if isinstance(value, str):
                        resolved = self.get(value)
                        if resolved is not None and resolved != value:
                            if isinstance(current, list):
                                self.log(f"Reestablish reference for [{value}]")
                                current[i] = resolved
                    else:
                        self.refer(value, visited)
                        
            # 处理对象
            elif hasattr(current, "__dict__"):
                for key, value in vars(current).items():
                    if isinstance(value, str):
                        resolved = self.get(value)
                        if resolved is not None and resolved != value:
                            self.log(f"Reestablish reference for [{value}]")
                            setattr(current, key, resolved)
                    else:
                        self.refer(value, visited)
                        
        except Exception as e:
            self.log(f"Error during reference resolution: {str(e)}")

