import pickle
import sys
import os
import config
import antlr4
from antlr4 import *
from src.extractor.base_class import BaseDescription
from src.parsers.parser.NdfGrammarLexer import NdfGrammarLexer
from src.parsers.parser.NdfGrammarParser import NdfGrammarParser
from src.parsers.syntax_tree.actions import semantic_actions_generator
from src.parsers.syntax_tree.nodes.syntax_node_assignment import *
from src.parsers.syntax_tree.nodes.syntax_node_collection import *
from typing import List, Tuple, Dict, Any, Union, Optional

#=============================================
# 1. 全局配置
#=============================================
WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)

#=============================================
# 2. 统一管理器类
#=============================================
class Manager:
    """统一管理器类
    
    提供功能:
    - 注册对象(register_object)
    - 注册模板(register_template) 
    - 生成对象(generate)
    - 导出类(export)
    - 路径解析(resolve_path)
    - 文件读写(save/load)
    """
    def __init__(
        self, 
        file_list: List[Tuple[str, str]], 
        register_file: str = "register.pkl",
        generate_file: str = "global.pkl",
        log_file: str = "log.txt",
        export_file: str = "TClass.py"
    ):
        self.file_list = file_list
        self.register_dict = {}  # 存储注册信息
        self.dict = {}          # 存储生成信息
        self.register_file = register_file
        self.generate_file = generate_file
        self.log_file = log_file
        self.export_file = export_file

    def save(self, mode: str = "generate"):
        """保存到文件"""
        if mode == "register":
            with open(self.register_file, "wb") as f:
                pickle.dump(self.register_dict, f)
        else:
            with open(self.generate_file, "wb") as f:
                pickle.dump(self.dict, f)

    def load(self, mode: str = "generate"):
        """从文件加载"""
        if mode == "register":
            with open(self.register_file, "rb") as f:
                self.register_dict = pickle.load(f)
        else:
            with open(self.generate_file, "rb") as f:
                self.dict = pickle.load(f)

    def log(self, message: str):
        """写入日志"""
        with open(self.log_file, "a") as f:
            f.write(message + "\n")

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

    def extract(self, file_name: str, name_space: str, reference: Any, mode: str = "generate_object") -> Dict:
        """解析NDF文件"""
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

    def check_file_exist(self) -> Dict[str, bool]:
        """检查文件是否存在"""
        file_status = {}
        for file, _ in self.file_list:
            full_path = os.path.join(config.RAW_DATA_PATH, file)
            exists = os.path.exists(full_path)
            if not exists:
                self.log(f"Warning: File not found: {full_path}")
            file_status[file] = exists
        return file_status

    def _resolve_path(self, path: Union[str, List[str]], namespace: Optional[str]) -> str:
        """解析路径"""
        if isinstance(path, list):
            path = '/' + '/'.join(str(p) for p in path)
        elif not isinstance(path, str):
            raise TypeError("路径必须是字符串或列表")

        path = path.strip()
        if path.startswith("$/"):
            return path[2:].strip('/')
        if path.startswith("~/"):
            if not namespace or not namespace.startswith('/'):
                raise ValueError(f"Namespace '{namespace}' 必须以 '/' 开头")
            return f"{namespace.rstrip('/')}/{path[2:].strip('/')}"
        return path.strip('/')

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
        """批量设置值"""
        if not isinstance(data_dict, dict):
            raise TypeError("data_dict 必须是一个字典")
        for key, value in data_dict.items():
            self.set(key, value, namespace=current_namespace)

    def register(self, reference: Optional[Any] = None):
        """执行完整注册流程"""
        self.register_object(reference)
        self.export()
        self.register_template(reference)
        self.export()
    
    def register_template(self, reference: Optional[Any] = None):
        """注册模板"""
        for file, name_space in self.file_list:
            file = config.RAW_DATA_PATH + file
            template = self.extract(
                file,
                name_space=name_space,
                reference=reference,
                mode="register_template"
            )
            self.register_dict = self.merge(self.register_dict, template)

    def register_object(self, reference: Optional[Any] = None):
        """注册对象"""
        for file, name_space in self.file_list:
            file = config.RAW_DATA_PATH + file
            object = self.extract(
                file,
                name_space=name_space,
                reference=reference,
                mode="register_object"
            )
            self.register_dict = self.merge(self.register_dict, object)

    def generate(self, reference: Optional[Any] = None):
        """生成对象"""
        for file, name_space in self.file_list:
            file = config.RAW_DATA_PATH + file
            object = self.extract(
                file,
                name_space=name_space,
                reference=reference,
                mode="generate_object"
            )
            self.set_batch(object, "/")

    def export(self):
        """导出类定义"""
        class_definitions = []
        for class_name, data in self.register_dict.items():
            # 获取类信息
            attributes = data.get("attributes", {})
            base = data.get("base") or {}
            base_name = base.get("name", "BaseDescription")
            base_attributes = base.get("attributes", {})
            
            # 生成类定义
            class_definition = f"class {class_name}({base_name}):\n"
            
            # 处理参数
            def format_value(value):
                """格式化值为字符串表示"""
                if isinstance(value, dict) and 'default' in value:
                    # 如果是模板参数描述,直接使用default值
                    default_value = value['default']
                    if isinstance(default_value, str):
                        return f'"{default_value}"'
                    return str(default_value) if default_value is not None else 'None'
                elif isinstance(value, BaseDescription):
                    return value.reverse()
                elif isinstance(value, str):
                    return f'"{value}"'
                elif isinstance(value, (list, tuple)):
                    items = [format_value(item) for item in value]
                    return f"[{', '.join(items)}]"
                elif isinstance(value, dict):
                    items = [f'"{k}": {format_value(v)}' for k, v in value.items()]
                    return f"{{{', '.join(items)}}}"
                else:
                    return str(value)
            
            # 生成当前类参数
            current_params = ", ".join(
                f"{key}={format_value(value)}"
                for key, value in attributes.items()
            )
            
            # 生成父类参数
            super_params = ", ".join(
                f"{key}={value.lstrip('@')}" if isinstance(value, str) and value.startswith('@')
                else f"{key}={format_value(value)}"
                for key, value in base_attributes.items()
            )
            
            # 生成__init__方法
            if current_params:
                class_definition += f"    def __init__(self, {current_params}):\n"
                if super_params:
                    class_definition += f"        super().__init__({super_params})\n"
                for key in attributes.keys():
                    class_definition += f"        self.{key} = {key}\n"
            else:
                class_definition += "    def __init__(self):\n"
                if super_params:
                    class_definition += f"        super().__init__({super_params})\n"
                else:
                    class_definition += "        pass\n"

            class_definitions.append(class_definition)

        # 写入文件
        complete_class_definitions = "\n\n".join(class_definitions)
        with open(self.export_file, "w") as f:
            f.write(complete_class_definitions)
        print(f"Classes successfully written to {self.export_file}")

#=============================================
# 3. 主函数
#=============================================
def main():
    """主函数"""
    file_list = config.PROCESS_FILE_LIST
    reference = {
            "test/path": 100,
            "system/value": "system",
            "obj/member": {"value": 200},
            "array/data": [1, 2, 3, 4, 5]
        }
    # 创建管理器
    manager = Manager(
        file_list=file_list,
        register_file="register.pkl",
        generate_file="global.pkl",
        log_file="log.txt",
        export_file="TClass.py"
    )
    
    # 检查文件
    manager.check_file_exist()
    
    # 注册对象和模板
    manager.register(reference=reference)
    manager.save(mode="register")
    
    # 生成对象
    manager.generate(reference=reference)
    manager.save(mode="generate")

if __name__ == "__main__":
    main()