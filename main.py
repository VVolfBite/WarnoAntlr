import pickle
import sys
import config

WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)

from antlr4 import *
from src.parsers.parser.NdfGrammarLexer import NdfGrammarLexer
from src.parsers.parser.NdfGrammarParser import NdfGrammarParser
from src.parsers.syntax_tree.actions import semantic_actions_generator
from src.parsers.parser_interface import ParserInterface
# from src.parsers.register_class.RClass import *
# from src.extractor.refined_class import *


def main():
    global_dict = {}
    for file in config.PROCESS_FILE_LIST:
        file = config.RAW_DATA_PATH + file
        node = ParserInterface.generate_node_object(file)
        value = ParserInterface.value_from_node(node)
        global_dict.update(value)        
        # ParserInterface.set_class_json(config.CLASS_JSON)
        # ParserInterface.generate_class_json_from_ndf_folder(config.RAW_DATA_PATH)
        # ParserInterface.generate_class_from_json(config.CLASS_JSON, config.CLASS_PY)
        # ParserInterface.set_class_py(config.CLASS_PY)
        # ParserInterface.register_class(node)



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

