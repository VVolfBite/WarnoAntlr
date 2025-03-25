# import os
# import config
# import json
# import importlib
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
# class ParserInterface:
#     class_register = {}
#     class_json = None
#     class_py = None
#     # 宏替换操作
#     @staticmethod
#     def apply_macro_replacements(content: str):
#         macro_rules = {
#             "Metre": 2.92198967,
#         }
#         for key, value in macro_rules.items():
#             content = content.replace(key, str(value))
#         return content

#     # 生成节点对象
#     @staticmethod
#     def generate_node_object(file_name: str, mode = "default"):
#         input_stream = antlr4.InputStream(
#             ParserInterface.apply_macro_replacements(
#                 str(FileStream(file_name, encoding="utf8"))
#             )
#         )
#         lexer = NdfGrammarLexer(input_stream)
#         stream = CommonTokenStream(lexer)
#         parser = NdfGrammarParser(stream)
#         tree = parser.ndf_file()
#         listener = semantic_actions_generator.Generator(parser,mode = mode)
#         walker = ParseTreeWalker()
#         walker.walk(listener, tree)
#         if mode == "defalut":
#             return File(listener.assignments)
#         else:
#             return listener.dict

#     @staticmethod
#     def set_class_json(json_file):
#         ParserInterface.class_json =json_file
#         if os.path.exists(json_file):
#             with open(json_file, "r") as f:
#                 ParserInterface.class_register = json.load(f)
#         else:
#             ParserInterface.class_register = {}

#     @staticmethod
#     def set_class_py(py_file):
#         ParserInterface.class_py = py_file

#     @staticmethod
#     def generate_class_from_json(json_file, py_file):
#         class_definitions = []

#         with open(json_file, "r") as file:
#             json_data = json.load(file)

#         for class_name, attributes in json_data.items():
#             class_def = f"class {class_name}( BaseDescription ):\n"
#             if attributes:
#                 # 生成带默认值的参数列表
#                 params = ", ".join([f"{attr}=None" for attr in attributes])
#                 class_def += f"    def __init__(self, {params}):\n"
#                 for attribute in attributes:
#                     class_def += f"        self.{attribute} = {attribute}\n"
#             else:
#                 class_def += "    def __init__(self):\n"
#                 class_def += "        pass\n"

#             class_definitions.append(class_def)
#         complete_class_definitions = "\n\n".join(class_definitions)
#         with open(py_file, "w") as py_file:
#             py_file.write(complete_class_definitions)
#         print(f"Classes successfully written to {py_file}")

#     @staticmethod
#     def register_class(entity):
#         if isinstance(entity, Object):
#             class_name = entity.object_type
#             class_member = {item.id: None for item in entity.value}
#             # 对 Object 类型的 entity 进行处理
#             ParserInterface._register_classes(class_name=class_name , class_members=class_member)
#             for item in entity.value:
#                 ParserInterface.register_class(item)
#         elif isinstance(entity, Assignment) and entity.is_template:
#             class_name = entity.id
#             obj = entity.value
#             class_member = {item.id : item.value for item in obj.value}
#             ParserInterface._register_classes(class_name=class_name , class_members=class_member)
#             ParserInterface.register_class(obj)                 

#         elif isinstance(entity, (Map, Pair, Vector, Collection, File, Assignment)):
#             # 遍历这些结构的值，递归查找 Object 类型
#             if isinstance(entity, Map):
#                 for value in entity.map.values():
#                     ParserInterface.register_class(value)
#             elif isinstance(entity, Pair):
#                 ParserInterface.register_class(entity.value[0])
#                 ParserInterface.register_class(entity.value[1])
#             elif isinstance(entity, Vector):
#                 for value in entity.value:
#                     ParserInterface.register_class(value)
#             elif isinstance(entity, Collection):
#                 for value in entity.value:
#                     ParserInterface.register_class(value)
#             elif isinstance(entity, File):
#                 for assignment in entity.value:
#                     ParserInterface.register_class(assignment)
#             elif isinstance(entity, Assignment):
#                 ParserInterface.register_class(entity.value)

#     @staticmethod
#     def refer(entity, dictionary):

#         # 检查是否为字典
#         if isinstance(entity, dict):
#             for key, value in entity.items():
#                 if isinstance(value, str):
#                     # 检查字典中是否有这个键，且其值是一个对象
#                     if value in dictionary and not isinstance(dictionary[value], (str, int, float, bool)) and entity!= dictionary[value]:
#                         entity[key] = dictionary[value]  # 替换为对应的对象
                        
#                 else:
#                     # 递归处理嵌套的字典或其他类型
#                     ParserInterface.refer(value, dictionary)
        
#         # 检查是否为列表或元组
#         elif isinstance(entity, (list, tuple)):
#             entity = list(entity)
#             for index, item in enumerate(entity):
#                 if isinstance(item, str):
#                     # 检查字典中是否有这个键，且其值是一个对象
#                     if item in dictionary and not isinstance(dictionary[item], (str, int, float, bool)) and entity!= dictionary[item]:
#                         entity[index] = dictionary[item]  # 替换为对应的对象
#                 else:
#                     # 递归处理嵌套的结构
#                     ParserInterface.refer(item, dictionary)
        
#         # 检查是否为自定义对象
#         elif hasattr(entity, '__dict__'):
#             for attr_name, attr_value in entity.__dict__.items():
#                 if attr_name != "KeyName":
#                     if isinstance(attr_value, str):
#                         # 检查字典中是否有这个键，且其值是一个对象
#                         if attr_value in dictionary and not isinstance(dictionary[attr_value], (str, int, float, bool)) and entity!= dictionary[attr_value]:
#                             setattr(entity, attr_name, dictionary[attr_value])  # 替换为对应的对象
#                     else:
#                         # 递归处理对象的嵌套属性
#                         ParserInterface.refer(attr_value, dictionary)
#         return entity

#     @staticmethod
#     def backup_instance_name(dictionary):
#         for key, value in dictionary.items():
#             # 检查 value 是否为类的实例
#             if isinstance(value, object) and not isinstance(value, (str, int, float, list, dict, tuple)):
#                 value.KeyName = key
#         return dictionary

#     @staticmethod
#     def generate_class_json_from_ndf_folder(folder: str):
#         ndf_files = []
#         # 使用 os.walk 递归遍历目录及子目录
#         for root, _, files in os.walk(folder):
#             for file in files:
#                 if file.endswith(".ndf"):
#                     ndf_files.append(os.path.join(root, file))

#         # 对每个 .ndf 文件进行处理
#         for ndf_file in ndf_files:
#             print(f"正在处理文件: {ndf_file}")
#             try:
#                 node = ParserInterface.generate_node_object(ndf_file)
#                 ParserInterface.register_class(node)
#             except Exception as e:
#                 print(f"处理文件 {ndf_file} 时发生错误: {e}")
                
#     @staticmethod
#     def _register_classes(class_name, class_members):
#         if class_name in ParserInterface.class_register:
#             # 更新类的成员
#             existing_members = ParserInterface.class_register[class_name]
#             existing_members.update(class_members)
#         else:
#             # 注册新类
#             ParserInterface.class_register[class_name] = class_members
#         ParserInterface._save_classes()

#     @staticmethod
#     def _save_classes():
#         with open(ParserInterface.class_json, "w") as f:
#             json.dump(ParserInterface.class_register, f, indent=4)

#     @staticmethod
#     def _instantiate_class(class_name, **kwargs):
#         get_class = lambda name: getattr(src.extractor.refined_class, name, None) or getattr(src.src.extractor.extract_class, name, None)
#         class_ = get_class(class_name)
#         return class_(**kwargs) if class_ is not None else None

    
#     @staticmethod
#     def value_from_node(entity):
#         if isinstance(entity, Map):
#             # ParserInterface.value_from_node(key)
#             return {
#                 str(ParserInterface.value_from_node(key)): ParserInterface.value_from_node(value)
#                 for key, value in entity.map.items()
#             }
#         elif isinstance(entity, Pair):
#             key = tuple(ParserInterface.value_from_node(entity.value[0])) if isinstance(ParserInterface.value_from_node(entity.value[0]), list) else ParserInterface.value_from_node(entity.value[0])
#             value = ParserInterface.value_from_node(entity.value[1])
#             return {key : value}
#         elif isinstance(entity, Vector):
#             return tuple([ParserInterface.value_from_node(value) for value in entity.value])
#         elif isinstance(entity, Assignment):
#             return ParserInterface.value_from_node(entity.value)
#         elif isinstance(entity, File):
#             py_dict = {}
#             for assignment in entity.value:
#                 py_dict.update({assignment.id :ParserInterface.value_from_node(assignment)})
#             return py_dict

#         elif isinstance(entity, Object):
#             class_name = entity.object_type
#             kwargs = {val.id : ParserInterface.value_from_node(val) for val in entity.value}
#             return ParserInterface._instantiate_class(class_name=class_name, **kwargs)
#             # return {
#             #     entity.object_type: {
#             #         k: v
#             #         for val in entity.value
#             #         for k, v in ParserInterface.value_from_node(val).items()
#             #     }
#             # }
#         elif isinstance(entity, Collection):
#             return [ParserInterface.value_from_node(value) for value in entity.value]

#         # Handling primitive data types based on `entity.nodetype`
#         match entity.nodetype:
#             case NodeType.Integer:
#                 return int(entity.value)
#             case NodeType.Boolean:
#                 return bool(entity.value)
#             case NodeType.Float:
#                 return float(entity.value)
#             case NodeType.Reference:
#                 reference_str = str(entity.value)
#                 if '|' in reference_str:
#                     # 处理组合引用，拆分并返回最后的部分作为列表
#                     references = reference_str.split('|')
#                     return [ref.strip().split('/')[-1] for ref in references]
#                 else:
#                     # 处理单一引用，直接返回最后部分
#                     return reference_str.split('/')[-1]
#             case NodeType.Nil:
#                 return None
#             case _:

#                 return str(entity.value)

#     # 导出为JSON
#     @staticmethod
#     def export_json(data, file_name):
#         json_output = json.dumps(data, indent=4, ensure_ascii=False)
#         with open(f"{file_name}.json", "w", encoding="utf-8") as json_file:
#             json_file.write(json_output)
