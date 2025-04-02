import pickle
import sys

WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)

import config
import antlr4
from antlr4 import *

from src.parsers.parser.NdfGrammarLexer import NdfGrammarLexer
from src.parsers.parser.NdfGrammarParser import NdfGrammarParser
from src.parsers.syntax_tree.actions import semantic_actions_generator
from src.parsers.syntax_tree.nodes.syntax_node_assignment import *
from src.parsers.syntax_tree.nodes.syntax_node_collection import *

# 为了实现直接导入，必须在这里以固定位置导入模组，之后需要考虑放在其他位置
import src.extractor.extract_class
import src.extractor.refined_class


# 以下为流程说明：
# 1. 从目标文件提取结构，生成类结构：此过程先注册对象然后注册模板，在过程中其会不断合并成员域,然后生成Python类结构 extract(file,mode="register")->generate_class_from_dict
# 2. 从目标文件生成对象，利用之前整理的Python类结构，生成对象 extract(file,mode="generate_object")
# 3. 对生成的对象进行引用替换，将对象中的引用替换为实际的对象
# 现在的问题是：对象引用这里处理的太糟了，我们或许可以设计解析顺序从而防止到最后一步才能进行引用处理的情况，另外一个问题是很大程度上在解析过程种我们就需要使用引用
# 这意味着我们需要将解析的结果实时送到写一次提取中以防止引用无法被处理，另外一个核心是路径信息程序需要一定程度上的能够确认引用路径信息并定位相关内容
# 所以我们确定几个信息，1.还是只能够按照两遍遍历的形式实现注册与生成，这是由Python特性决定的因此无法更改 2.然而我们可以做到的是在第一遍的过程中完成结构补充，在第二遍的过程中完成引用替换
# 基于这个想法，我们准备：1.使用一个新的数据结构使得其能够支持路径信息 2.在语义动作上添加对路径的解析和替换


import os


# 我们设计一个ObjectManger其可以做以下事情： 注册一个
# save
# load
# export
# set
# register -obj template
# generate

class Manger:
    def __init__(self,file_list, output_file="global.pkl",log_file="log.txt"):
        self.dict = {}
        self.file_list = file_list
        self.output_file = output_file
        self.log_file = log_file
    def save(self):
        with open(self.output_file, "wb") as f:
            pickle.dump(self.dict, f)

    def load(self):
        with open(self.output_file, "rb") as f:
            self.dict = pickle.load(f)

    def set_dict(self, dict):
        self.dict = dict
    def set_file_list(self, file_list):
        self.file_list = file_list
    def set_output_file(self, output_file):
        self.output_file = output_file
    def set_log_file(self, log_file):
        self.log_file = log_file
    def log(self, message):
        with open(self.log_file, "a") as f:
            f.write(message + "\n")

    def merge(self,dic):
        for key, value in dic.items():
            if key in self.dict:
                if isinstance(self.dict[key], dict) and isinstance(value, dict):
                    self.dict[key] = self.merge(value)
                elif self.dict[key] is None:
                    self.dict[key] = value
            else:
                self.dict[key] = value


    def extract(self, file_name, name_space, reference, mode="generate_object"):
        input_stream = antlr4.InputStream(
            str(FileStream(file_name, encoding="utf8"))
        )
        lexer = NdfGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = NdfGrammarParser(stream)
        tree = parser.ndf_file()
        listener = semantic_actions_generator.Generator(
            parser, name_space=name_space, reference = reference, mode=mode
        )
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        if mode == "generate_object":
            return listener.generator
        elif mode == "register_object" or mode == "register_template":
            return listener.register

class RegisterManger(Manger):
    def  __init__(self, file_list, output_file="global.pkl", export_file="TClass.py"):
        super().__init__(file_list, output_file)
        self.export_file = export_file
    
    def set_export_file(self, export_file):
        self.export_file = export_file

    def register(self,file_name):
        self.set_file_list(file_name)
        self.register_object()
        self.register_template()
        self.export()
    
    def register_template(self):
        for file, name_space in self.file_list:
            file = config.RAW_DATA_PATH + file
            template = self.extract(file,name_space=name_space,reference=None, mode="register_template")
            self.merge(template)

    def register_object(self):
        for file, name_space in self.file_list:
            file = config.RAW_DATA_PATH + file
            object = self.extract(file,name_space=name_space,reference=None, mode="register_object")
            self.merge(object)

    def add(self, dict):
        self.merge(dict)

    def export(self):
        class_definitions = []
        for class_name, data in self.dict.items():
            attributes = data.get("attributes", {})
            base = data.get("base") or {}
            base_name = base.get("name", "BaseDescription")
            base_attributes = base.get("attributes", {})
            class_definition = f"class {class_name}({base_name}):\n"
            # 子类自己的参数
            current_params = ", ".join(
                [
                    f'{key}="{value}"' if isinstance(value, str) else f"{key}={value}"
                    for key, value in attributes.items()
                ]
            )
            # 父类的初始化参数，去掉@
            super_params = ", ".join(
                [
                    (
                        f"{key}={value.lstrip('@')}"
                        if isinstance(value, str) and value.startswith("@")
                        else (
                            f'{key}="{value}"'
                            if isinstance(value, str) and not value.startswith("@")
                            else f"{key}={value}"
                        )
                    )
                    for key, value in base_attributes.items()
                ]
            )
            # __init__ 方法
            if current_params:
                class_definition += f"    def __init__(self, {current_params}):\n"
                if super_params:
                    class_definition += f"        super().__init__({super_params})\n"
                for key in attributes.keys():
                    class_definition += f"        self.{key} = {key}\n"
            else:
                # 如果没有当前类的属性，只有父类的初始化
                class_definition += "    def __init__(self):\n"
                if super_params:
                    class_definition += f"        super().__init__({super_params})\n"
                else:
                    class_definition += "        pass\n"

            class_definitions.append(class_definition)

        # 将生成的类写入文件
        complete_class_definitions = "\n\n".join(class_definitions)
        with open(self.export_file, "w") as self.export_file_obj:
            self.export_file_obj.write(complete_class_definitions)
        print(f"Classes successfully written to {self.export_file}")

class GenerateManger(Manger):
    def set(self, path, value, namespace=None):
        """设置值，支持绝对路径和相对路径"""
        full_path = self._resolve_path(path, namespace)
        keys = full_path.strip('/').split('/')
        current = self.dict

        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]

        current[keys[-1]] = value

    def get(self, path, namespace=None):
        """获取值，支持绝对路径和相对路径"""
        full_path = self._resolve_path(path, namespace)
        keys = full_path.strip('/').split('/')
        current = self.dict

        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            elif hasattr(current, key):  # 访问对象成员变量
                current = getattr(current, key)
            else:
                # 没找到则返回去掉 ~/ 或 $/ 后的路径
                self.log(f"Warning: {path} not found in {namespace}")
                return full_path.lstrip("$~/")

        return current


    def set_batch(self, data_dict, current_namespace):
        """批量插入，将 data_dict 的 key-value 以 current_namespace 为前缀存储"""
        if not isinstance(data_dict, dict):
            raise TypeError("data_dict 必须是一个字典")
        for key, value in data_dict.items():
            self.set(key, value, namespace=current_namespace)

    def _resolve_path(self, path, namespace):
        """解析路径，支持绝对路径（$/）和相对路径（~/）"""
        if isinstance(path, list):
            path = '/' + '/'.join(path)
        elif not isinstance(path, str):
            raise TypeError("路径必须是字符串或列表")

        path = path.strip()

        # 处理 $/ 绝对路径，去掉 `$`
        if path.startswith("$/"):
            return path[2:].strip('/')

        # 处理 ~/ 相对路径，将 `~` 替换为 `namespace`
        if path.startswith("~/"):
            if not namespace or not namespace.startswith('/'):
                raise ValueError(f"Namespace '{namespace}' 必须以 '/' 开头")
            return f"{namespace.rstrip('/')}/{path[2:].strip('/')}"

        return path.strip('/')

    
    def generate(self):
        for file, name_space in self.file_list:
            file = config.RAW_DATA_PATH + file
            object = self.extract(file,name_space=name_space,reference=self, mode="generate_object")
            self.set_batch(object, "/")
    
def main():
    # 1. 注册对象与模板
    file_list = config.PROCESS_FILE_LIST
    register_manger = RegisterManger(file_list, output_file="register.pkl", export_file="TClass.py")
    register_manger.register(file_list)
    register_manger.save()
    

    # # 2. 生成对象
    # generate_manger = GenerateManger(file_list, output_file="global.pkl")
    # generate_manger.generate()

    # # 3. 保存对象
    # generate_manger.save()


if __name__ == "__main__":
    main()