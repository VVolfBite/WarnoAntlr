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


# 用于合并结构
def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_dicts(result[key], value)
            elif result[key] is None:
                result[key] = value
        else:
            result[key] = value
    return result


# 宏替换，目前已经无用
def apply_macro_replacements(content: str):
    macro_rules = {
        "Metre": 2.92198967,
    }
    for key, value in macro_rules.items():
        content = content.replace(key, str(value))
    return content


# 从目标文件提取结构，当前模式有三种：
# generate: 生成类结构
# register_object: 注册对象
# register_template: 注册模板
def extract(file_name: str, mode="generate"):
    input_stream = antlr4.InputStream(
        apply_macro_replacements(str(FileStream(file_name, encoding="utf8")))
    )
    lexer = NdfGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = NdfGrammarParser(stream)
    tree = parser.ndf_file()
    listener = semantic_actions_generator.Generator(parser, mode=mode)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    if mode == "generate":
        return listener.generator
    elif mode == "register_object" or mode == "register_template":
        return listener.register


# 生成Python类结构
# 给定一个字典，生成对应的类结构到指定文件
def generate_class_from_dict(data_dict, py_file):
    class_definitions = []

    for class_name, data in data_dict.items():
        attributes = data.get("attributes", {})
        base = data.get("base", {})
        base_name = base.get("name", "BaseDescription")
        base_attributes = base.get("attributes", {})
        # 生成类定义
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
    with open(py_file, "w") as py_file_obj:
        py_file_obj.write(complete_class_definitions)
    print(f"Classes successfully written to {py_file}")

# 将字符串进行引用替换
def refer(target, dictionary):
    if isinstance(target, dict):
        for key, value in target.items():
            if isinstance(value, str):
                if (
                    value in dictionary
                    and not isinstance(dictionary[value], (str, int, float, bool))
                    and target != dictionary[value]
                ):
                    target[key] = dictionary[value]

            else:
                refer(value, dictionary)

    elif isinstance(target, (list, tuple)):
        target = list(target)
        for index, item in enumerate(target):
            if isinstance(item, str):
                if (
                    item in dictionary
                    and not isinstance(dictionary[item], (str, int, float, bool))
                    and target != dictionary[item]
                ):
                    target[index] = dictionary[item]
            else:
                refer(item, dictionary)

    elif hasattr(target, "__dict__"):
        for attr_name, attr_value in target.__dict__.items():
            # KeyName是一个特殊属性，不能替换
            if attr_name != "KeyName":
                if isinstance(attr_value, str):
                    if (
                        attr_value in dictionary
                        and not isinstance(
                            dictionary[attr_value], (str, int, float, bool)
                        )
                        and target != dictionary[attr_value]
                    ):
                        setattr(target, attr_name, dictionary[attr_value])
                else:
                    refer(attr_value, dictionary)
    return target


def main():
    # global_dict = {}
    # for file in config.PROCESS_FILE_LIST:
    #     file = config.RAW_DATA_PATH + file
    #     class_regist = extract(file,mode="register_object")
    #     global_dict = merge_dicts(global_dict,class_regist)
    # generate_class_from_dict(global_dict,"TClass.py")
    # for file in config.PROCESS_FILE_LIST:
    #     file = config.RAW_DATA_PATH + file
    #     class_regist = extract(file, mode="register_template")
    #     global_dict = merge_dicts(global_dict, class_regist)
    # generate_class_from_dict(global_dict, "TClass.py")

    with open("global.pkl", "rb") as f:
        global_dict = pickle.load(f)

    for file in config.PROCESS_FILE_LIST:
        file = config.RAW_DATA_PATH + file
        class_generate = extract(file, mode="generate")
        global_dict.update(class_generate)

    with open("global.pkl", "wb") as f:
        pickle.dump(global_dict, f)

    with open("global.pkl", "rb") as f:
        global_dict = pickle.load(f)

    global_dict = refer(global_dict, global_dict)
    # # global_dict = ParserInterface.backup_instance_name(global_dict)
    with open("global.pkl", "wb") as f:
        pickle.dump(global_dict, f)

    stop = 1


if __name__ == "__main__":
    main()
