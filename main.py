import pickle
import sys
import config

WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)

import os
import config
import json
import importlib
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


def merge_dicts(dict1, dict2):
    result = dict1.copy()  # 创建一个副本，避免修改原始字典
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            # 如果当前键的值是字典，则递归合并
            result[key] = merge_dicts(result[key], value)
        elif key in result:
            # 如果键存在且当前值为 None，允许覆盖
            if result[key] is None:
                result[key] = value
        else:
            # 如果键不存在，直接添加
            result[key] = value
    return result



def apply_macro_replacements(content: str):
    macro_rules = {
        "Metre": 2.92198967,
    }
    for key, value in macro_rules.items():
        content = content.replace(key, str(value))
    return content


def generate_target_object(file_name: str, mode="generate"):
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
        return listener.generate_dict
    elif mode == "regist_object" or mode == "regist_template":
        return listener.regist_dict


def generate_class_from_dict(data_dict, py_file):
    class_definitions = []

    for class_name, data in data_dict.items():
        attributes = data.get("attributes") or {}  # 确保 attributes 为字典
        base = data.get("base") or {}  # 确保 base 为字典
        base_name = base.get("name") or "BaseDescription"  # 确保 base_name 有默认值
        base_attributes = base.get("attributes") or {}  # 确保 base_attributes 为字典

        # 生成类定义
        class_def = f"class {class_name}({base_name}):\n"
        # 子类自己的参数
        current_params = ", ".join(
            [
                f'{key}="{value}"' if isinstance(value, str) else f"{key}={value}"
                for key, value in attributes.items()
            ]
        )
        # 父类的初始化调用，去掉@
        super_params = ", ".join(
            [
                f"{key}={value.lstrip('@')}" if isinstance(value, str) and value.startswith('@')
                else f'{key}="{value}"' if isinstance(value, str) and not value.startswith('@')
                else f"{key}={value}"
                for key, value in base_attributes.items()
            ]
        )
        # 处理 __init__ 方法
        if current_params:
            class_def += f"    def __init__(self, {current_params}):\n"
            # 初始化父类，去掉@
            if super_params:
                class_def += f"        super().__init__({super_params})\n"
            # 初始化子类自身属性
            for key in attributes.keys():
                class_def += f"        self.{key} = {key}\n"
        else:
            # 如果没有当前类的属性，只有父类的初始化
            class_def += "    def __init__(self):\n"
            if super_params:
                class_def += f"        super().__init__({super_params})\n"
            else:
                class_def += "        pass\n"

        class_definitions.append(class_def)

    # 将生成的类写入文件
    complete_class_definitions = "\n\n".join(class_definitions)
    with open(py_file, "w") as py_file_obj:
        py_file_obj.write(complete_class_definitions)
    print(f"Classes successfully written to {py_file}")

def refer_class(entity, dictionary):
    if isinstance(entity, dict):
        for key, value in entity.items():
            if isinstance(value, str):
                if (
                    value in dictionary
                    and not isinstance(dictionary[value], (str, int, float, bool))
                    and entity != dictionary[value]
                ):
                    entity[key] = dictionary[value]

            else:
                refer_class(value, dictionary)

    elif isinstance(entity, (list, tuple)):
        entity = list(entity)
        for index, item in enumerate(entity):
            if isinstance(item, str):
                if (
                    item in dictionary
                    and not isinstance(dictionary[item], (str, int, float, bool))
                    and entity != dictionary[item]
                ):
                    entity[index] = dictionary[item]
            else:
                refer_class(item, dictionary)

    elif hasattr(entity, "__dict__"):
        for attr_name, attr_value in entity.__dict__.items():
            if attr_name != "KeyName":
                if isinstance(attr_value, str):
                    if (
                        attr_value in dictionary
                        and not isinstance(
                            dictionary[attr_value], (str, int, float, bool)
                        )
                        and entity != dictionary[attr_value]
                    ):
                        setattr(entity, attr_name, dictionary[attr_value])
                else:
                    refer_class(attr_value, dictionary)
    return entity


def main():
    # global_dict = {}
    # for file in config.PROCESS_FILE_LIST:
    #     file = config.RAW_DATA_PATH + file
    #     class_regist = generate_target_object(file,mode="regist_object")
    #     global_dict = merge_dicts(global_dict,class_regist)
    # generate_class_from_dict(global_dict,"TClass.py")
    # for file in config.PROCESS_FILE_LIST:
    #     file = config.RAW_DATA_PATH + file
    #     class_regist = generate_target_object(file, mode="regist_template")
    #     global_dict = merge_dicts(global_dict, class_regist)
    # generate_class_from_dict(global_dict, "TClass.py")

    with open("global.pkl",'rb') as f:
        global_dict  = pickle.load(f)

    for file in config.PROCESS_FILE_LIST:
        file = config.RAW_DATA_PATH + file
        class_generate = generate_target_object(file,mode="generate")
        global_dict.update(class_generate)

    with open("global.pkl",'wb') as f:
        pickle.dump(global_dict, f)

    with open("global.pkl",'rb') as f:
        global_dict  = pickle.load(f)

    global_dict = refer_class(global_dict,global_dict)
    # # global_dict = ParserInterface.backup_instance_name(global_dict)
    with open("global.pkl",'wb') as f:
        pickle.dump(global_dict, f)

    stop = 1


if __name__ == "__main__":
    main()
