from src.parsers.syntax_tree.nodes.syntax_node_assignment import *
from src.parsers.syntax_tree.nodes.syntax_node_collection import *

INDENT_SIZE = 4


# 一个将内存中的对象转换为Ndf文本的函数
class ToNdfConverter:
    def __init__(self):
        self.indent = 0

    def increase_indent(self):
        self.indent += INDENT_SIZE

    def decrease_indent(self):
        self.indent -= INDENT_SIZE
        self.indent = max(0, self.indent)

    def convert(self, _file: File) -> str:
        return self.convert_entity(_file)

    def convert_entity(self, entity: Base) -> str:
        match entity.nodetype:
            # 说明Pair的Value是两个对值
            case NodeType.Pair:
                result_str = (
                    "("
                    + self.convert_entity(entity.value[0])
                    + ", "
                    + self.convert_entity(entity.value[1])
                    + ")"
                )
            # 说明Vector的Value是列表值
            case NodeType.Vector:
                result_str = "["
                for i in range(len(entity.value)):
                    result_str += self.convert_entity(entity.value[i])
                    if i < len(entity.value) - 1:
                        result_str += ", "
                result_str += "]"
            # 说明Map的Value是列表格式的Pair对
            case NodeType.Map:
                result_str = "MAP\n"
                result_str += (self.indent - INDENT_SIZE) * " " + "[\n"
                for i in range(len(entity.value)):
                    result_str += self.indent * " "
                    result_str += self.convert_entity(entity.value[i])
                    if i < len(entity.value) - 1:
                        result_str += ","
                    result_str += "\n"
                result_str += (self.indent - INDENT_SIZE) * " " + "]"
            case NodeType.String_single:
                result_str = "'" + str(entity.value) + "'"
            case NodeType.String_double:
                result_str = '"' + str(entity.value) + '"'
            # 说明RGBA的Value是四色数值
            case NodeType.RGBA:
                result_str = "RGBA["
                for i in range(4):
                    result_str += str(entity.value[i])
                    if i < 3:
                        result_str += ","
                result_str += "]"
            # 说明Object本身是实例化描述的形式 Type是实例化的类型描述，而Value是成员列表
            case NodeType.Object:
                result_str = ""
                if entity.object_type != "":
                    result_str = entity.object_type + "\n"
                result_str += (self.indent - INDENT_SIZE) * " " + "(\n"
                for i in range(len(entity.value)):
                    result_str += self.convert_entity(entity.value[i])
                result_str += (self.indent - INDENT_SIZE) * " " + ")"
            # 说明Assigment的ID对应文件的字段而value对应了值
            # 将Member和IS都视为赋值并分开处理
            case NodeType.STRUCTURAL:
                if type(entity) == Assignment:
                    result_str = ""
                    if type(entity.value) == Object:
                        result_str += "\n"
                    result_str += self.indent * " "
                    if entity.export:
                        result_str = "export "
                    if entity.unnamed:
                        result_str += "unnamed "
                    if entity.member and not entity.unnamed:
                        result_str += entity.id + " = "
                    elif not entity.member and not entity.unnamed:
                        result_str += entity.id + " is "
                    val_entity = entity.value
                    self.increase_indent()
                    result_str += self.convert_entity(val_entity) + "\n"
                    self.decrease_indent()
                elif type(entity) == File:
                    result_str = ""
                    for val in entity.value:
                        result_str += self.convert_entity(val)
                else:
                    result_str = ""
            case _:
                result_str = str(entity.value)
        return result_str
