"""NDF管理器模块
提供NDF文件的解析、注册和对象生成功能

模块组成:
1. 基础设施 - 初始化和配置
2. 对象注册 - 类型注册和处理
3. 模板系统 - 模板解析和处理 
4. 对象生成 - 实例创建和管理
5. 序列化 - 数据存储和加载
6. 工具函数 - 辅助功能实现
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

# 第三方库
import dill
import antlr4
from antlr4 import FileStream, CommonTokenStream
from antlr4.tree.Tree import ParseTreeWalker

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
        
        self.config = ConfigManager().get_instance()
        if not self.config.version:
            raise ValueError("Config version not set")
            
        self.base_dir = base_dir or self.config.output_dir / self.config.version
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
        self.register_dict = {}  # 注册信息
        self.dict = {}          # 生成对象
        
        self.log_file = self.base_dir / "parse.log"

        self.merge_lock = Lock()  # 添加线程锁
        self.max_workers = 4      # 控制并发数量

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
    # 2.2 对象注册
    #-------------------------
    def register_objects(self, file_list: List[Tuple[str, str]], batch_name: str):
        """串行注册对象"""
        print(f"\n开始 {batch_name} 批次的对象注册...")
        
        file_status = self.check_files(file_list)
        if not all(file_status.values()):
            missing_files = [f for f, exists in file_status.items() if not exists]
            raise FileNotFoundError(f"以下文件未找到:\n" + "\n".join(missing_files))
            
        for file, namespace in file_list:
            file_path = self.config.get_full_path(file)
            object_dict = self.extract(
                str(file_path),
                namespace,
                None,
                mode="register_object"
            )
            self.register_dict = self.merge(self.register_dict, object_dict)
            
        print(f"{batch_name} 批次对象注册完成")
        
    def register_objects_parallel(self, file_list: List[Tuple[str, str]], batch_name: str):
        """并行注册对象"""
        print(f"\n开始 {batch_name} 批次的对象注册...")
        
        file_status = self.check_files(file_list)
        if not all(file_status.values()):
            missing_files = [f for f, exists in file_status.items() if not exists]
            raise FileNotFoundError(f"以下文件未找到:\n" + "\n".join(missing_files))
            
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            for file, namespace in file_list:
                file_path = self.config.get_full_path(file)
                future = executor.submit(
                    self.extract,
                    str(file_path),
                    namespace,
                    None,
                    "register_object"
                )
                futures.append((future, file))
            
            for future, file in futures:
                try:
                    object_dict = future.result()
                    with self.merge_lock:
                        self.register_dict = self.merge(self.register_dict, object_dict)
                except Exception as e:
                    self.log(f"处理文件 {file} 时出错: {str(e)}")
                    raise
                    
        print(f"{batch_name} 批次对象注册完成")

    #-------------------------
    # 2.3 模板系统
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
            self.log(f"检查模板时出错 {file_path}: {str(e)}")
            return False
        
    def register_templates(self, file_list: List[Tuple[str, str]], batch_name: str):
        """串行注册模板"""
        print(f"\nStarting template registration for batch {batch_name}...")
        
        for file, namespace in file_list:
            file_path = self.config.get_full_path(file)
            if not self.has_template(file_path):
                self.log(f"Skipping file without templates: {file}")
                continue
                
            template_dict = self.extract(
                str(file_path),
                namespace,
                self,
                mode="register_template"
            )
            self.register_dict = self.merge(self.register_dict, template_dict)
            
        print(f"Template registration completed for batch {batch_name}")
        
    def register_templates_parallel(self, file_list: List[Tuple[str, str]], batch_name: str):
        """并行注册模板"""
        print(f"\n开始 {batch_name} 批次的模板注册...")
        
        template_files = []
        for file, namespace in file_list:
            file_path = self.config.get_full_path(file)
            if self.has_template(file_path):
                template_files.append((file, namespace))
            else:
                self.log(f"跳过无模板文件: {file}")
                
        if not template_files:
            print(f"{batch_name} 批次无模板文件,跳过")
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
                    "register_template"
                )
                futures.append((future, file))
            
            for future, file in futures:
                try:
                    template_dict = future.result()
                    with self.merge_lock:
                        self.register_dict = self.merge(self.register_dict, template_dict)
                except Exception as e:
                    self.log(f"处理文件 {file} 时出错: {str(e)}")
                    raise
                    
        print(f"{batch_name} 批次模板注册完成")

    #-------------------------
    # 2.4 对象生成
    #-------------------------
    def generate_objects(self, file_list: List[Tuple[str, str]], batch_name: str):
        """串行生成对象"""
        print(f"\n开始 {batch_name} 批次的对象生成...")
        
        for file, namespace in file_list:
            file_path = self.config.get_full_path(file)
            object_dict = self.extract(
                str(file_path),
                namespace,
                self,
                mode="generate_object"
            )
            self.set_batch(object_dict, namespace)
            
        print(f"{batch_name} 批次对象生成完成")
        
    def generate_objects_parallel(self, file_list: List[Tuple[str, str]], batch_name: str):
        """并行生成对象"""
        print(f"\n开始 {batch_name} 批次的对象生成...")
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            for file, namespace in file_list:
                file_path = self.config.get_full_path(file)
                future = executor.submit(
                    self.extract,
                    str(file_path),
                    namespace,
                    self,
                    "generate_object"
                )
                futures.append((future, (file, namespace)))
            
            for future, (file, namespace) in futures:
                try:
                    object_dict = future.result()
                    with self.merge_lock:
                        self.set_batch(object_dict, namespace)
                except Exception as e:
                    self.log(f"处理文件 {file} 时出错: {str(e)}")
                    raise
                    
        print(f"{batch_name} 批次对象生成完成")

    #-------------------------
    # 2.5 序列化
    #-------------------------
    def save(self, mode: str = "generate", file_path: Optional[Path] = None):
        """保存数据"""
        try:
            if file_path is None:
                file_path = self.base_dir / f"{mode}.dill"
                
            file_path.parent.mkdir(parents=True, exist_ok=True)
                
            with open(file_path, "wb") as f:
                if mode == "register":
                    dill.dump(self.register_dict, f)
                else:
                    dill.dump(self.dict, f)
                    
            self.log(f"Successfully saved {mode} data to {file_path}")
            
        except Exception as e:
            self.log(f"Error saving to file: {str(e)}")
            raise
        
    def load(self, mode: str = "generate", file_path: Optional[Path] = None):
        """加载数据"""
        try:
            if file_path is None:
                file_path = self.base_dir / f"{mode}.dill"
                
            with open(file_path, "rb") as f:
                data = dill.load(f)
                if mode == "register":
                    self.register_dict = data
                else:
                    self.dict = data
                    
            self.log(f"Successfully loaded {mode} data from {file_path}")
            
        except Exception as e:
            self.log(f"Error loading from file: {str(e)}")
            raise
        
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
            class_definitions = []
            for class_name, data in self.register_dict.items():
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

    #-------------------------
    # 2.6 工具函数
    #-------------------------
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
            current = self.dict
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
        current = self.dict
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
        
    def extract(self, file_name: str, name_space: str, reference: Any, mode: str = "generate_object") -> Dict:
        """解析文件"""
        try:
            input_stream = antlr4.InputStream(str(FileStream(file_name, encoding="utf8")))
            lexer = NdfGrammarLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = NdfGrammarParser(stream)
            tree = parser.ndf_file()
            listener = semantic_actions_generator.Generator(
                parser, 
                name_space=name_space,
                reference=reference,
                mode=mode
            )
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            return (listener.generator if mode == "generate_object" 
                    else listener.register)
        except FileNotFoundError:
            self.log(f"Error: File not found: {file_name}")
            raise
        except Exception as e:
            self.log(f"Error parsing file {file_name}: {str(e)}")
            raise
