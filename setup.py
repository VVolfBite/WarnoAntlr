import pickle
import sys
import config
import os
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

# 获取当前脚本所在的目录
WORK_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# 将工作目录添加到 sys.path
sys.path.append(WORK_DIRECTORY)

# 合并字典的函数
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

# 宏替换函数
def apply_macro_replacements(content: str):
    macro_rules = {
        "Metre": 2.92198967,
    }
    for key, value in macro_rules.items():
        content = content.replace(key, str(value))
    return content

# 生成目标对象的函数
def generate_target_object(file_name: str, mode="generate"):
    try:
        input_stream = antlr4.InputStream(
            apply_macro_replacements(str(FileStream(file_name, encoding="utf8"))))
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
    except Exception as e:
        raise Exception(f"Error processing file {file_name}: {str(e)}")

# 初始化全局字典
global_dict = {}

# 遍历文件列表并生成字典
try:
    for file in config.PROCESS_FILE_LIST:
        file_path = config.RAW_DATA_PATH + file
        class_regist = generate_target_object(file_path, mode="regist_object")
        global_dict = merge_dicts(global_dict, class_regist)

    for file in config.PROCESS_FILE_LIST:
        file_path = config.RAW_DATA_PATH + file
        class_regist = generate_target_object(file_path, mode="regist_template")

    for file in config.PROCESS_FILE_LIST:
        file_path = config.RAW_DATA_PATH + file
        class_generate = generate_target_object(file_path, mode="generate")
        global_dict.update(class_generate)

    # 如果字典生成成功，提供一些总结信息
    print("global_dict has been successfully populated.")

    # 输出一些关于字典的总结信息
    dict_size = sys.getsizeof(global_dict)
    num_keys = len(global_dict)
    sample_keys = list(global_dict.keys())[:5]  # 输出前5个键作为示例

    print(f"Summary of global_dict:")
    print(f"  - Number of keys: {num_keys}")
    print(f"  - Size in memory: {dict_size} bytes")
    print(f"  - Sample keys: {sample_keys}")

    # 保存 global_dict 为 JSON 文件
    output_file = 'global_dict.json'
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(global_dict, json_file, ensure_ascii=False, indent=4)

    print(f"global_dict has been saved as {output_file}")

except Exception as e:
    print(f"An error occurred during setup: {str(e)}")
