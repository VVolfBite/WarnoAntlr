import logging
from pathlib import Path
from src.parsers.syntax_tree.nodes.syntax_node_base import *
from src.parsers.syntax_tree.nodes.syntax_node_assignment import *

#=============================================
# 1. 基础集合类
#=============================================
class Collection(Base):
    """Collection是一种中间形式，用于存储各种复合数据类型
    包括:
    1. 文件: [assignment1, assignment2, ...]
    2. 对象: Object(member1=value1, member2=value2)
    3. 向量: [value1, value2, value3]
    4. 键值对: (key, value)
    5. 映射: Map[(key1,value1), (key2,value2)]
    """
    def __init__(self):
        super().__init__()
        self.content = []        # 存储实际内容
        self.lookup = {}        # 快速查找表

    def append(self, data: Base):
        """添加新元素"""
        self.content.append(data)
        if isinstance(data, Assignment):
            self.lookup[data.id] = len(self.content) - 1
        elif isinstance(data, Object):
            self.lookup[data.object_type] = len(self.content) - 1

    def get_value(self, path: str, default=None):
        """按路径获取值"""
        current = path.split("\\")[0]
        remaining = path.removeprefix(current).removeprefix("\\")
        
        if current == "":
            return self.content
        elif self.lookup.__contains__(current):
            return self.content[self.lookup[current]].get_value(remaining, default)
        return default

    def set_value(self, path: str, value):
        """按路径设置值"""
        current = path.split("\\")[0]
        remaining = path.removeprefix(current).removeprefix("\\")
        
        if current == "":
            self.content = value
        elif self.lookup.__contains__(current):
            self.content[self.lookup[current]].set_value(remaining, value)

#=============================================
# 2. 具体集合类型
#=============================================
class Object(Collection):
    """对象节点，表示一个具体的对象实例"""
    def __init__(self):
        super().__init__()
        self.object_type = ""           # 对象类型
        self.nodetype = NodeType.Object
        self.template_args = {}         # 模板参数

    def __str__(self):
        template_info = f"[{', '.join(f'{k}={v}' for k,v in self.template_args.items())}]" if self.template_args else ""
        attributes = ", ".join(f"{item.id}={item.value}" for item in self.content)
        return f"{self.object_type}{template_info}({attributes})"

class Pair(Collection):
    """键值对节点，限制只能有两个元素"""
    def __init__(self):
        super().__init__()
        self.nodetype = NodeType.Pair

    def append(self, data: Base):
        if len(self.content) < 2:
            super().append(data)

class Vector(Collection):
    """向量节点，表示一个值的列表"""
    def __init__(self):
        super().__init__()
        self.nodetype = NodeType.Vector

class Map(Collection):
    """映射节点，表示键值对的集合"""
    def __init__(self):
        super().__init__()
        self.map = {}                   # 实际存储的映射关系
        self.nodetype = NodeType.Map

    def append(self, data: Pair):
        super().append(data)
        if len(data.content) == 2:
            key, value = data.content[0].content, data.content[1]
            self.map[key] = value
            self.lookup[str(key)] = len(self.content) - 1

#=============================================
# 3. 特殊向量类型
#=============================================
class Float2(Vector):
    """二维向量，限制只能有2个数值元素"""
    def __init__(self):
        super().__init__()
        self.nodetype = NodeType.Float2

    def append(self, data: Base):
        if len(self.content) < 2 and data.is_numeric():
            super().append(data)

class Float3(Vector):
    """三维向量，限制只能有3个数值元素"""
    def __init__(self):
        super().__init__()
        self.nodetype = NodeType.Float3

    def append(self, data: Base):
        if len(self.content) < 3 and data.is_numeric():
            super().append(data)