import logging

from pathlib import Path

from src.parsers.syntax_tree.nodes.syntax_node_base import *
from src.parsers.syntax_tree.nodes.syntax_node_assignment import *


# Collection是一种中间形式，用于描述出去Assigment后的所有基本结构的基类
# 如 [v1,v2,v3] Map[(k1,v1),(k2,v2)] (p1,p2)等等
# lookup是一个快速查阅检索的字典，主要用于查询Assigment的字段内容
class Collection(Base):
    def __init__(self):
        super().__init__()
        self.value = []
        self.lookup = {}

    def append(self, data: Base):
        self.value.append(data)
        if isinstance(data, Assignment):
            self.lookup[data.id] = len(self.value) - 1
        elif isinstance(data, Object):
            self.lookup[data.object_type] = len(self.value) - 1
    
    def extend(self, data: list):
        for item in data:
            self.append(item)

    def get_value(self, path: str, default=None):
        # get current ID
        current = path.split("\\")[0]
        # build remaining path
        remaining = path.removeprefix(current)
        remaining = remaining.removeprefix("\\")
        # if nothing remains, return own value
        if current == "":
            return self.value
        # otherwise, call function on own value
        elif self.lookup.__contains__(current):
            return self.value[self.lookup[current]].get_value(remaining, default)
        else:
            print("Could not find value for " + str(path) + " on " + str(self))
            return default

    def set_value(self, path: str, value):
        current = path.split("\\")[0]
        remaining = path.removeprefix(current)
        remaining = remaining.removeprefix("\\")
        if current == "":
            self.value = value
        elif self.lookup.__contains__(current):
            self.value[self.lookup[current]].set_value(remaining, value)
        else:
            print("could not find " + path + "\nremaining: " + remaining)

    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        if not len(self.value) == len(other.value):
            return False
        for i in range(len(self.value)):
            if not self.value[i] == other.value[i]:
                return False
        return True

    def __len__(self):
        return len(self.value)

    def contains(self, item):
        return self.value.__contains__(item)


# File是对文件的基本描述，即一个Ndf文件本身，它将文件视为Assignments的集合
# 即 [A1,A2,A3]
class File(Collection):
    def __init__(self, assignments=[]):
        super().__init__()
        self.nodetype = NodeType.STRUCTURAL
        for assignment in assignments:
            self.append(assignment)

    def __str__(self):
        return "{type: file, value: " + "".join(map(str, self.value)) + "}"


# Object是对对象的描述，类似面向对象语言的实例化即 ClassA(Member = Value)
# 因此Value是对象列表
# 请确保get_class在规约完成时调用
class Object(Collection):
    def __init__(self):
        super().__init__()
        self.value = []
        self.object_type = ""
        self.nodetype = NodeType.Object

    def __str__(self):
        attributes = ", ".join(
            f"{item.id}={None}"
            for item in self.value
        )
        return f"{self.object_type}({attributes})"

    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        if self.object_type != other.object_type or self.value != other.value:
            return False
        return super().__eq__(other)
    
    def get_class(self):
        return (self.object_type, {item.id : None for item in self.value})

# Pair是对对的描述，是NDF中特有的数据类型，即(P1,P2)
# 因此Value是两个数据值
class Pair(Collection):
    def __init__(self):
        super().__init__()
        self.value = []
        self.nodetype = NodeType.Pair

    def append(self, data: Base):
        super().append(data)
        if len(self.value) > 2:
            logging.warning(
                "Tried to append " + str(data) + " to a full Pair. Discarded"
            )
            del self.value[2]

    def __str__(self):
        return "{type: pair, value: " + "".join(map(str, self.value)) + "}"


# Vector是对数组的描述，即[V1,V2,V3]
# 因此Value是列表中的数据值
class Vector(Collection):
    def __init__(self):
        super().__init__()
        self.value = []
        self.nodetype = NodeType.Vector

    def __str__(self):
        return "{type: vector, value: " + "".join(map(str, self.value)) + "}"
    
    def __hash__(self):
        # 使用 tuple 来确保 value 是可哈希的
        return hash((self.nodetype, tuple(self.value)))


# Map是对字典的描述，即Map[(k1,v1),(k2,v2)]
# 因此Value是字典的pair value表 而map是键值对
class Map(Collection):
    def __init__(self):
        super().__init__()
        self.value = []
        self.map = {}
        self.nodetype = NodeType.Map

    def append(self, data: Pair):
        super().append(data)
        # key =  data.value[0].value
        # value = data.value[1]
        self.map[data.value[0]] = data.value[1]
        self.lookup[str(data.value[0].value)] = len(self.value) - 1

    def get_value(self, path: str, default=None):
        current = path.split("\\")[0]
        remaining = path.removeprefix(current)
        remaining = remaining.removeprefix("\\")
        if current == "":
            return self.value
        elif self.lookup.__contains__(current) and remaining == "":
            return self.map[current]
        elif self.lookup.__contains__(current):
            return self.map[current].get_value(remaining, default)
        else:
            print("Could not find value for " + str(path) + " on " + str(self))
            return default

    def set_value(self, path: str, value):
        current = path.split("\\")[0]
        remaining = path.removeprefix(current)
        remaining = remaining.removeprefix("\\")
        if current == "":
            self.value = value
        elif self.lookup.__contains__(current) and remaining == "":
            self.value[self.lookup[current]].value[1] = value
        elif self.lookup.__contains__(current):
            self.map[current].set_value(remaining, value)
        else:
            print("could not find " + path + "\nremaining: " + remaining)

    def __str__(self):
        return "{type: map, value: " + "".join(map(str, self.value)) + "}"
