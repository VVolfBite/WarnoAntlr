import pickle
import sys
import os
import config
import antlr4
from antlr4 import *
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
# 2. 基础管理器类
#=============================================
class Manager:
    """基础管理器类
    
    提供对象管理的基本功能:
    - 文件读写(save/load)
    - 字典操作(merge)
    - 属性设置(set_xxx)
    - 文件解析(extract)
    """
    def __init__(self, file_list: List[Tuple[str, str]], output_file: str = "global.pkl", log_file: str = "log.txt"):
        """初始化管理器
        
        Args:
            file_list: 要处理的文件列表，每个元素为(文件路径, 命名空间)的元组
            output_file: 输出文件路径
            log_file: 日志文件路径
        """
        self.dict = {}
        self.file_list = file_list
        self.output_file = output_file
        self.log_file = log_file

    def save(self):
        """保存字典到文件"""
        with open(self.output_file, "wb") as f:
            pickle.dump(self.dict, f)

    def load(self):
        """从文件加载字典"""
        with open(self.output_file, "rb") as f:
            self.dict = pickle.load(f)

    def log(self, message):
        """写入日志信息"""
        with open(self.log_file, "a") as f:
            f.write(message + "\n")

    def set_dict(self, dict):
        self.dict = dict

    def set_file_list(self, file_list):
        self.file_list = file_list

    def set_output_file(self, output_file):
        self.output_file = output_file

    def set_log_file(self, log_file):
        self.log_file = log_file

    def merge(self, dict1, dict2):
        """合并两个字典
        
        规则:
        1. 键不存在时直接添加
        2. 键存在且都是字典时递归合并
        3. 键存在且原值为None时覆盖
        """
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
        """解析NDF文件
        
        Args:
            file_name: 文件名
            name_space: 命名空间
            reference: 引用管理器
            mode: 解析模式(generate_object/register_object/register_template)
        
        Returns:
            解析结果(generator或register)
            
        Raises:
            FileNotFoundError: 文件不存在
            antlr4.error.Errors.ParseCancellationException: 解析错误
        """
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
        """检查文件列表中的文件是否存在
        
        Returns:
            文件存在状态的字典 {文件路径: 是否存在}
        """
        file_status = {}
        for file, _ in self.file_list:
            full_path = os.path.join(config.RAW_DATA_PATH, file)
            exists = os.path.exists(full_path)
            if not exists:
                self.log(f"Warning: File not found: {full_path}")
            file_status[file] = exists
        return file_status

#=============================================
# 3. 注册管理器类
#=============================================
class RegisterManger(Manager):
    """注册管理器
    
    负责对象和模板的注册、导出等功能
    """
    def __init__(self, file_list, output_file="global.pkl", export_file="TClass.py"):
        super().__init__(file_list, output_file)
        self.export_file = export_file
    
    def set_export_file(self, export_file):
        self.export_file = export_file

    def register(self, file_name):
        """执行完整的注册流程"""
        self.set_file_list(file_name)
        self.register_object()
        self.export()
        self.register_template()
        self.export()
    
    def register_template(self):
        """注册模板"""
        for file, name_space in self.file_list:
            file = config.RAW_DATA_PATH + file
            template = self.extract(
                file,
                name_space=name_space,
                reference=None,
                mode="register_template"
            )
            self.dict = self.merge(self.dict, template)

    def register_object(self):
        """注册对象"""
        for file, name_space in self.file_list:
            file = config.RAW_DATA_PATH + file
            object = self.extract(
                file,
                name_space=name_space,
                reference=None,
                mode="register_object"
            )
            self.dict = self.merge(self.dict, object)

    def add(self, dict):
        """添加字典"""
        self.dict = self.merge(self.dict, dict)

    def export(self):
        """导出类定义到Python文件"""
        class_definitions = []
        for class_name, data in self.dict.items():
            # 获取类信息
            attributes = data.get("attributes", {})
            base = data.get("base") or {}
            base_name = base.get("name", "BaseDescription")
            base_attributes = base.get("attributes", {})
            
            # 生成类定义
            class_definition = f"class {class_name}({base_name}):\n"
            
            # 处理参数
            current_params = ", ".join(
                f'{key}="{value}"' if isinstance(value, str) 
                else f"{key}={value}"
                for key, value in attributes.items()
            )
            
            super_params = ", ".join(
                f"{key}={value.lstrip('@')}" 
                if isinstance(value, str) and value.startswith("@")
                else f"{key}={value}"
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
# 4. 生成管理器类
#=============================================
class GenerateManager(Manager):
    """生成管理器
    
    负责对象的生成、路径解析等功能
    """
    def _resolve_path(self, path: Union[str, List[str]], namespace: Optional[str]) -> str:
        """解析路径处理
        
        Args:
            path: 路径字符串或路径片段列表
            namespace: 当前命名空间
            
        Returns:
            解析后的完整路径
            
        Raises:
            TypeError: 路径类型错误
            ValueError: 命名空间格式错误
        """
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
        """获取指定路径的值
        
        Args:
            path: 路径字符串或路径片段列表
            namespace: 当前命名空间(可选)
            
        Returns:
            路径对应的值，如果路径无效则返回处理过的路径字符串
        """
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

    def set(self, path, value, namespace=None):
        """设置值
        支持绝对路径($/...)和相对路径(~/...)
        """
        full_path = self._resolve_path(path, namespace)
        keys = full_path.strip('/').split('/')
        current = self.dict

        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]

        current[keys[-1]] = value

    def set_batch(self, data_dict, current_namespace):
        """批量设置值"""
        if not isinstance(data_dict, dict):
            raise TypeError("data_dict 必须是一个字典")
        for key, value in data_dict.items():
            self.set(key, value, namespace=current_namespace)

    def generate(self):
        """生成对象"""
        for file, name_space in self.file_list:
            file = config.RAW_DATA_PATH + file
            object = self.extract(
                file,
                name_space=name_space,
                reference=self,
                mode="generate_object"
            )
            self.set_batch(object, "/")

#=============================================
# 5. 主函数
#=============================================
def main():
    """主函数"""
    # 1. 注册对象与模板
    file_list = config.PROCESS_FILE_LIST
    register_manger = RegisterManger(
        file_list=file_list,
        output_file="register.pkl",
        export_file="TClass.py"
    )
    register_manger.check_file_exist()
    register_manger.register(file_list)
    register_manger.save()
    
    # 2. 生成对象
    generate_manger = GenerateManager(file_list, output_file="global.pkl")
    generate_manger.generate()

    # 3. 保存对象
    # generate_manger.save()

if __name__ == "__main__":
    main()