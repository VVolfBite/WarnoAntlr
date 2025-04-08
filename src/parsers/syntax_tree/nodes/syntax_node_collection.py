import logging
from pathlib import Path
from src.parsers.syntax_tree.nodes.syntax_node_base import *
from src.parsers.syntax_tree.nodes.syntax_node_assignment import *

#=============================================
# 1. 基础集合类
#=============================================
class Collection(Base):
    """Collection是一种中间形式，用于描述出去Assignment后的所有基本结构的基类
    如 [v1,v2,v3] Map[(k1,v1),(k2,v2)] (p1,p2)等等
    lookup是一个快速查阅检索的字典，主要用于查询Assignment的字段内容
    """
    def __init__(self):
        super().__init__()
        self.content = []
        self.lookup = {}

    def append(self, data: Base):
        self.content.append(data)
        if isinstance(data, Assignment):
            self.lookup[data.id] = len(self.content) - 1
        elif isinstance(data, Object):
            self.lookup[data.object_type] = len(self.content) - 1

    def get_value(self, path: str, default=None):
        # 获取当前ID
        current = path.split("\\")[0]
        # 构建剩余路径
        remaining = path.removeprefix(current)
        remaining = remaining.removeprefix("\\")
        
        if current == "":
            return self.content
        elif self.lookup.__contains__(current):
            return self.content[self.lookup[current]].get_value(remaining, default)
        else:
            print("Could not find value for " + str(path) + " on " + str(self))
            return default

    def set_value(self, path: str, value):
        current = path.split("\\")[0]
        remaining = path.removeprefix(current)
        remaining = remaining.removeprefix("\\")
        
        if current == "":
            self.content = value
        elif self.lookup.__contains__(current):
            self.content[self.lookup[current]].set_value(remaining, value)
        else:
            print("could not find " + path + "\nremaining: " + remaining)

    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        if not len(self.content) == len(other.content):
            return False
        for i in range(len(self.content)):
            if not self.content[i] == other.content[i]:
                return False
        return True

    def __len__(self):
        return len(self.content)

    def contains(self, item):
        return self.content.__contains__(item)

#=============================================
# 2. 具体集合类型
#=============================================
# 2.1 文件类型
class File(Collection):
    """File是对文件的基本描述，即一个Ndf文件本身，它将文件视为Assignments的集合
    即 [A1,A2,A3]
    """
    def __init__(self, assignments=[]):
        super().__init__()
        self.nodetype = NodeType.STRUCTURAL
        for assignment in assignments:
            self.append(assignment)

    def __str__(self):
        return "{type: file, value: " + "".join(map(str, self.content)) + "}"

# 2.2 对象类型
class Object(Collection):
    """Object是对对象的描述，类似面向对象语言的实例化
    支持以下形式:
    1. 普通对象: ClassA(Member = Value)
    2. 模板对象: ClassA[T1=v1,T2=v2](Member = Value)
    请确保get_class在规约完成时调用
    """
    def __init__(self):
        super().__init__()
        self.content = []
        self.object_type = ""
        self.nodetype = NodeType.Object
        self.template_args = {}  # 新增：存储实例化时的模板参数

    def __str__(self):
        template_info = ""
        if self.template_args:
            args = ", ".join(f"{k}={v}" for k, v in self.template_args.items())
            template_info = f"[{args}]"
            
        attributes = ", ".join(
            f"{item.id}={None}"
            for item in self.content
        )
        return f"{self.object_type}{template_info}({attributes})"

    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        if self.object_type != other.object_type or self.content != other.content:
            return False
        return super().__eq__(other)
    
    def get_class(self):
        return (
            self.object_type,
            {
                "attributes": {item.id : None for item in self.content},
                "template_args": self.template_args
            }
        )

# 2.3 键值对类型
class Pair(Collection):
    """Pair是对对的描述，是NDF中特有的数据类型，即(P1,P2)
    因此Value是两个数据值
    """
    def __init__(self):
        super().__init__()
        self.content = []
        self.nodetype = NodeType.Pair

    def append(self, data: Base):
        super().append(data)
        if len(self.content) > 2:
            logging.warning(
                "Tried to append " + str(data) + " to a full Pair. Discarded"
            )
            del self.content[2]

    def __str__(self):
        return "{type: pair, value: " + "".join(map(str, self.content)) + "}"

# 2.4 向量类型
class Vector(Collection):
    """Vector是对数组的描述，即[V1,V2,V3]
    因此Value是列表中的数据值
    """
    def __init__(self):
        super().__init__()
        self.content = []
        self.nodetype = NodeType.Vector

    def __str__(self):
        return "{type: vector, value: " + "".join(map(str, self.content)) + "}"
    
    def __hash__(self):
        return hash((self.nodetype, tuple(self.content)))

# 2.4.1 特殊向量类型 - Float2
class Float2(Vector):
    """Float2是2D向量类型，形如 float2[x, y]"""
    def __init__(self):
        super().__init__()
        self.nodetype = NodeType.Float2
        
    def append(self, data: Base):
        super().append(data)
        if len(self.content) > 2:
            logging.warning("Float2 can only have 2 components")
            del self.content[2:]

    def __str__(self):
        return "{type: float2, value: " + ",".join(map(str, self.content)) + "}"

# 2.4.2 特殊向量类型 - Float3
class Float3(Vector):
    """Float3是3D向量类型，形如 float3[x, y, z]"""
    def __init__(self):
        super().__init__()
        self.nodetype = NodeType.Float3
        
    def append(self, data: Base):
        super().append(data)
        if len(self.content) > 3:
            logging.warning("Float3 can only have 3 components")
            del self.content[3:]

    def __str__(self):
        return "{type: float3, value: " + ",".join(map(str, self.content)) + "}"

# 2.5 映射类型
class Map(Collection):
    """Map是对字典的描述，即Map[(k1,v1),(k2,v2)]
    因此Value是字典的pair value表 而map是键值对
    """
    def __init__(self):
        super().__init__()
        self.content = []
        self.map = {}
        self.nodetype = NodeType.Map

    def append(self, data: Pair):
        super().append(data)
        self.map[data.content[0].content] = data.content[1]
        self.lookup[str(data.content[0].content)] = len(self.content) - 1

    def get_value(self, path: str, default=None):
        current = path.split("\\")[0]
        remaining = path.removeprefix(current)
        remaining = remaining.removeprefix("\\")
        
        if current == "":
            return self.content
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
            self.content = value
        elif self.lookup.__contains__(current) and remaining == "":
            self.content[self.lookup[current]].content[1] = value
        elif self.lookup.__contains__(current):
            self.map[current].set_value(remaining, value)
        else:
            print("could not find " + path + "\nremaining: " + remaining)

    def __str__(self):
        return "{type: map, value: " + "".join(map(str, self.content)) + "}"