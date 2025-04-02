# import pickle
# import sys

# WORK_DIRECTORY = "D:/WarnoAntlr-main/"
# sys.path.append(WORK_DIRECTORY)

# import config
# import antlr4
# from antlr4 import *

# from src.parsers.parser.NdfGrammarLexer import NdfGrammarLexer
# from src.parsers.parser.NdfGrammarParser import NdfGrammarParser
# from src.parsers.syntax_tree.actions import semantic_actions_generator
# from src.parsers.syntax_tree.nodes.syntax_node_assignment import *
# from src.parsers.syntax_tree.nodes.syntax_node_collection import *

# # 为了实现直接导入，必须在这里以固定位置导入模组，之后需要考虑放在其他位置
# import src.extractor.extract_class
# import src.extractor.refined_class


# # 以下为流程说明：
# # 1. 从目标文件提取结构，生成类结构：此过程先注册对象然后注册模板，在过程中其会不断合并成员域,然后生成Python类结构 extract(file,mode="register")->generate_class_from_dict
# # 2. 从目标文件生成对象，利用之前整理的Python类结构，生成对象 extract(file,mode="generate_object")
# # 3. 对生成的对象进行引用替换，将对象中的引用替换为实际的对象
# # 现在的问题是：对象引用这里处理的太糟了，我们或许可以设计解析顺序从而防止到最后一步才能进行引用处理的情况，另外一个问题是很大程度上在解析过程种我们就需要使用引用
# # 这意味着我们需要将解析的结果实时送到写一次提取中以防止引用无法被处理，另外一个核心是路径信息程序需要一定程度上的能够确认引用路径信息并定位相关内容
# # 所以我们确定几个信息，1.还是只能够按照两遍遍历的形式实现注册与生成，这是由Python特性决定的因此无法更改 2.然而我们可以做到的是在第一遍的过程中完成结构补充，在第二遍的过程中完成引用替换
# # 基于这个想法，我们准备：1.使用一个新的数据结构使得其能够支持路径信息 2.在语义动作上添加对路径的解析和替换


# import os

    
# # 用于合并结构
# def merge_dicts(dict1, dict2):
#     result = dict1.copy()
#     for key, value in dict2.items():
#         if key in result:
#             if isinstance(result[key], dict) and isinstance(value, dict):
#                 result[key] = merge_dicts(result[key], value)
#             elif result[key] is None:
#                 result[key] = value
#         else:
#             result[key] = value
#     return result


# # 宏替换，目前已经无用
# def apply_macro_replacements(content: str):
#     macro_rules = {
#         "Metre": 2.92198967,
#     }
#     for key, value in macro_rules.items():
#         content = content.replace(key, str(value))
#     return content


# # 从目标文件提取结构，当前模式有三种：
# # generate: 生成类结构
# # register_object: 注册对象
# # register_template: 注册模板
# def extract(file_name: str, name_space="/", reference_dict={}, mode="generate_object"):
#     input_stream = antlr4.InputStream(
#         apply_macro_replacements(str(FileStream(file_name, encoding="utf8")))
#     )
#     lexer = NdfGrammarLexer(input_stream)
#     stream = CommonTokenStream(lexer)
#     parser = NdfGrammarParser(stream)
#     tree = parser.ndf_file()
#     listener = semantic_actions_generator.Generator(
#         parser, name_space=name_space, reference_dict=reference_dict, mode=mode
#     )
#     walker = ParseTreeWalker()
#     walker.walk(listener, tree)
#     if mode == "generate_object":
#         return listener.generator
#     elif mode == "register_object" or mode == "register_template":
#         return listener.register


# # 将字符串进行引用替换
# def refer(target, dictionary):
#     if isinstance(target, dict):
#         for key, value in target.items():
#             if isinstance(value, str):
#                 if (
#                     value in dictionary
#                     and not isinstance(dictionary[value], (str, int, float, bool))
#                     and target != dictionary[value]
#                 ):
#                     target[key] = dictionary[value]

#             else:
#                 refer(value, dictionary)

#     elif isinstance(target, (list, tuple)):
#         target = list(target)
#         for index, item in enumerate(target):
#             if isinstance(item, str):
#                 if (
#                     item in dictionary
#                     and not isinstance(dictionary[item], (str, int, float, bool))
#                     and target != dictionary[item]
#                 ):
#                     target[index] = dictionary[item]
#             else:
#                 refer(item, dictionary)

#     elif hasattr(target, "__dict__"):
#         for attr_name, attr_value in target.__dict__.items():
#             # KeyName是一个特殊属性，不能替换
#             if attr_name != "KeyName":
#                 if isinstance(attr_value, str):
#                     if (
#                         attr_value in dictionary
#                         and not isinstance(
#                             dictionary[attr_value], (str, int, float, bool)
#                         )
#                         and target != dictionary[attr_value]
#                     ):
#                         setattr(target, attr_name, dictionary[attr_value])
#                 else:
#                     refer(attr_value, dictionary)
#     return target


# # 生成Python类结构
# # 给定一个字典，生成对应的类结构到指定文件
# def generate_class_from_dict(data_dict, py_file):
#     class_definitions = []

#     for class_name, data in data_dict.items():
#         attributes = data.get("attributes", {})
#         base = data.get("base") or {}
#         base_name = base.get("name", "BaseDescription")
#         base_attributes = base.get("attributes", {})
#         # 生成类定义
#         class_definition = f"class {class_name}({base_name}):\n"
#         # 子类自己的参数
#         current_params = ", ".join(
#             [
#                 f'{key}="{value}"' if isinstance(value, str) else f"{key}={value}"
#                 for key, value in attributes.items()
#             ]
#         )
#         # 父类的初始化参数，去掉@
#         super_params = ", ".join(
#             [
#                 (
#                     f"{key}={value.lstrip('@')}"
#                     if isinstance(value, str) and value.startswith("@")
#                     else (
#                         f'{key}="{value}"'
#                         if isinstance(value, str) and not value.startswith("@")
#                         else f"{key}={value}"
#                     )
#                 )
#                 for key, value in base_attributes.items()
#             ]
#         )
#         # __init__ 方法
#         if current_params:
#             class_definition += f"    def __init__(self, {current_params}):\n"
#             if super_params:
#                 class_definition += f"        super().__init__({super_params})\n"
#             for key in attributes.keys():
#                 class_definition += f"        self.{key} = {key}\n"
#         else:
#             # 如果没有当前类的属性，只有父类的初始化
#             class_definition += "    def __init__(self):\n"
#             if super_params:
#                 class_definition += f"        super().__init__({super_params})\n"
#             else:
#                 class_definition += "        pass\n"

#         class_definitions.append(class_definition)

#     # 将生成的类写入文件
#     complete_class_definitions = "\n\n".join(class_definitions)
#     with open(py_file, "w") as py_file_obj:
#         py_file_obj.write(complete_class_definitions)
#     print(f"Classes successfully written to {py_file}")


# def main():
#     global_dict = {}
#     for file in config.PROCESS_FILE_LIST:
#         file = config.RAW_DATA_PATH + file
#         class_regist = extract(file,mode="register_object")
#         global_dict = merge_dicts(global_dict,class_regist)
#     generate_class_from_dict(global_dict,"TClass.py")
#     for file in config.PROCESS_FILE_LIST:
#         file = config.RAW_DATA_PATH + file
#         class_regist = extract(file, mode="register_template")
#         global_dict = merge_dicts(global_dict, class_regist)
#     generate_class_from_dict(global_dict, "TClass.py")

#     with open("global.pkl", "rb") as f:
#         global_dict = pickle.load(f)

#     for file in config.PROCESS_FILE_LIST:
#         file = config.RAW_DATA_PATH + file
#         class_generate = extract(file, mode="generate_object")
#         global_dict.update(class_generate)

#     with open("global.pkl", "wb") as f:
#         pickle.dump(global_dict, f)

#     with open("global.pkl", "rb") as f:
#         global_dict = pickle.load(f)

#     global_dict = refer(global_dict, global_dict)
#     # # global_dict = ParserInterface.backup_instance_name(global_dict)
#     with open("global.pkl", "wb") as f:
#         pickle.dump(global_dict, f)

#     stop = 1


# if __name__ == "__main__":
#     main()



# # 我们设计一个ObjectManger其可以做以下事情： 注册一个