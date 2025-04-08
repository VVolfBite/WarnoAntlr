from src.parsers.syntax_tree.nodes.syntax_node_base import *


# Assignment是一个描述文件中基本语句的节点类
# 基本结构是:
# 1. export/private id is value
# 2. member形式: id = value
# 3. template形式: template id[params] is value
class Assignment(Base):
    def __init__(self):
        super().__init__()
        self.id = ""
        self.nodetype = NodeType.STRUCTURAL
        self.is_export = False
        self.is_private = False
        self.is_unnamed = False
        self.is_member = False
        self.is_template = False
        self.template_params = []    # 新增: 模板参数列表
        self.base_type = None       # 新增: 模板基类

    def __str__(self):
        result = (
            "{id: "
            + self.id
            + " type: assignment, export: "
            + str(self.is_export)
            + ", private: "
            + str(self.is_private)
            + ", member: "
            + str(self.is_member)
            + ", template: "
            + str(self.is_template)
        )
        if self.is_template:
            result += (
                ", template_params: "
                + str(self.template_params)
                + ", base_type: "
                + str(self.base_type)
            )
        result += ", value: " + str(self.content) + "}"
        return result

    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        ret = (
            self.nodetype == other.nodetype
            and self.id == other.id
            and self.is_export == other.is_export
            and self.is_member == other.is_member
            and self.is_unnamed == other.is_unnamed
            and self.is_template == other.is_template
            and self.content == other.content
        )
        return ret

    def get_value(self, path: str, default=None):

        current = path.split("\\")[0]
        if current == "":
            return self.content
        elif isinstance(self.content, Base):
            return self.content.get_value(path, default)
        else:
            return default

    def set_value(self, path: str, value):

        current = path.split("\\")[0]
        if current == "":
            self.content = value
        elif isinstance(self.content, Base):
            self.content.set_value(path, value)
        else:
            print("could not find " + path + "\ncurrent: " + current)