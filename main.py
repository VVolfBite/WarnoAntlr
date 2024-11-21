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
    result = dict1.copy() 
    for key, value in dict2.items():
        if key not in result:
            result[key] = value
        else:
            for member, value in value.items():
                if member not in result[key]:
                    result[key][member] = value
                elif value is not None:
                    result[key][member] = value
    return result

def apply_macro_replacements(content: str):
    macro_rules = {
        "Metre": 2.92198967,
    }
    for key, value in macro_rules.items():
        content = content.replace(key, str(value))
    return content

def generate_target_object(file_name: str, mode = "generate"):
    input_stream = antlr4.InputStream(
        apply_macro_replacements(
            str(FileStream(file_name, encoding="utf8"))
        )
    )
    lexer = NdfGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = NdfGrammarParser(stream)
    tree = parser.ndf_file()
    listener = semantic_actions_generator.Generator(parser,mode = mode)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    if mode == "generate":
        return listener.generate_dict
    elif mode == "regist_object" or mode == "regist_template":
        return listener.regist_dict

def generate_class_from_dict(dict, py_file):
    class_definitions = []
    for class_name, attributes in dict.items():
        class_def = f"class {class_name}(BaseDescription):\n"
        if attributes:
            # 生成带默认值的参数列表
            params = ", ".join([f"{key}={value}" for key,value in attributes.items()])
            class_def += f"    def __init__(self, {params}):\n"
            for key,value in attributes.items():
                class_def += f"        self.{key} = {key}\n"
        else:
            class_def += "    def __init__(self):\n"
            class_def += "        pass\n"

        class_definitions.append(class_def)
    complete_class_definitions = "\n\n".join(class_definitions)
    with open(py_file, "w") as py_file:
        py_file.write(complete_class_definitions)
    print(f"Classes successfully written to {py_file}")

def refer_class(entity, dictionary):
    if isinstance(entity, dict):
        for key, value in entity.items():
            if isinstance(value, str):
                if value in dictionary and not isinstance(dictionary[value], (str, int, float, bool)) and entity!= dictionary[value]:
                    entity[key] = dictionary[value] 
                    
            else:
                refer_class(value, dictionary)

    elif isinstance(entity, (list, tuple)):
        entity = list(entity)
        for index, item in enumerate(entity):
            if isinstance(item, str):
                if item in dictionary and not isinstance(dictionary[item], (str, int, float, bool)) and entity!= dictionary[item]:
                    entity[index] = dictionary[item] 
            else:
                refer_class(item, dictionary)
    
    elif hasattr(entity, '__dict__'):
        for attr_name, attr_value in entity.__dict__.items():
            if attr_name != "KeyName":
                if isinstance(attr_value, str):
                    if attr_value in dictionary and not isinstance(dictionary[attr_value], (str, int, float, bool)) and entity!= dictionary[attr_value]:
                        setattr(entity, attr_name, dictionary[attr_value]) 
                else:
                    refer_class(attr_value, dictionary)
    return entity

def main():
    global_dict = {}
    # for file in config.PROCESS_FILE_LIST:
    #     file = config.RAW_DATA_PATH + file
    #     class_regist = generate_target_object(file,mode="regist_object")
    #     global_dict = merge_dicts(global_dict,class_regist)
    # generate_class_from_dict(global_dict,"TClass.py")
    # for file in config.PROCESS_FILE_LIST:
    #     file = config.RAW_DATA_PATH + file
    #     class_regist = generate_target_object(file,mode="regist_template")
    #     global_dict = merge_dicts(global_dict,class_regist)
    # generate_class_from_dict(global_dict,"TClass.py")

    global_dict = {}    
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

