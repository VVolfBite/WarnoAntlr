# provides common functionality for any  object


class NodeType:
    (
        UNKNOWN,
        STRUCTURAL,
        Nil,
        Boolean,
        Integer,
        HexInteger,
        Float,
        String_single,
        String_double,
        GUID,
        RGBA, 
        Reference,
        Pair,
        Vector,
        Map,
        Arithmetic,
        Object,
        Replacer
    ) = range(18)


# 语法节点树的基类
# 规定 datatype描述的是节点类型
# 规定 value描述的是节点的内容物
# 规定 
class Base:
    def __init__(self):
        self.nodetype = NodeType.UNKNOWN
        self.value = None
        self.python_value = None

    def __str__(self):
        return "{type: " + str(self.nodetype) + ", value: " + str(self.value) + "}"

    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        return self.nodetype == other.nodetype and self.value == other.value

    def __hash__(self):
        return hash((self.nodetype, self.value))

    def get_value(self, path: str, default=None):
        # to be implemented by subclasses
        print(self)
        print("not implemented")
        return default

    def set_value(self, path: str, value):
        # to be implemented by subclasses
        print(self)
        print("not implemented")
