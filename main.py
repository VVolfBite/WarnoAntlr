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

def generate_target_object(file_name: str, mode = "default"):
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
    if mode == "defalut":
        return File(listener.assignments)
    else:
        return listener.dict


def main():
    global_dict = {}
    for file in config.PROCESS_FILE_LIST:
        file = config.RAW_DATA_PATH + file
        class_regist = generate_target_object(file,mode="regist_class")
       
        # ParserInterface.set_class_json(config.CLASS_JSON)
        # # ParserInterface.generate_class_json_from_ndf_folder(config.RAW_DATA_PATH)
        # ParserInterface.register_class(node)
        # ParserInterface.generate_class_from_json(config.CLASS_JSON, config.CLASS_PY)
        # ParserInterface.set_class_py(config.CLASS_PY)
        
        # value = ParserInterface.value_from_node(node)
        global_dict = merge_dicts(global_dict,class_regist)


    # with open("global.pkl",'wb') as f:
    #     pickle.dump(global_dict, f)
    
    # with open("global.pkl",'rb') as f:
    #     global_dict  = pickle.load(f)
    # global_dict = ParserInterface.refer_class(global_dict,global_dict)
    # global_dict = ParserInterface.backup_instance_name(global_dict)
    # with open("global.pkl",'wb') as f:
    #     pickle.dump(global_dict, f)
    
    stop = 1


if __name__ == "__main__":
    main()

