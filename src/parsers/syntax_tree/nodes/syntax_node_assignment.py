from src.parsers.syntax_tree.nodes.syntax_node_base import *

class Assignment(Base):
    """赋值语句节点
    
    支持的语法形式:
    1. export/private id is value        # 普通赋值
    2. id = value                        # 成员赋值
    3. template id[params] is value      # 模板定义
    4. UNNAMED ~/Reference               # 匿名赋值
    """
    
    def __init__(self):
        super().__init__()
        # 基本属性
        self.id = ""                     # 标识符
        self.nodetype = NodeType.STRUCTURAL
        
        # 修饰符标记
        self.is_export = False           # export标记
        self.is_private = False          # private标记
        self.is_unnamed = False          # unnamed标记
        self.is_member = False           # 成员标记
        
        # 模板相关
        self.is_template = False         # 模板标记
        self.template_params = []        # 模板参数列表
        self.base_type = None           # 模板基类

    def __str__(self):
        """字符串表示"""
        result = [
            f"{{id: {self.id}",
            f"type: assignment",
            f"export: {self.is_export}",
            f"private: {self.is_private}",
            f"member: {self.is_member}"
        ]
        
        # 模板信息
        if self.is_template:
            result.extend([
                f"template: {self.is_template}",
                f"template_params: {self.template_params}",
                f"base_type: {self.base_type}"
            ])
            
        result.append(f"value: {self.content}")
        return ", ".join(result) + "}"

    def __eq__(self, other):
        """相等比较"""
        if not isinstance(other, Assignment):
            return False
            
        return (self.nodetype == other.nodetype
                and self.id == other.id
                and self.is_export == other.is_export
                and self.is_member == other.is_member
                and self.is_unnamed == other.is_unnamed
                and self.is_template == other.is_template
                and self.content == other.content)

    def get_value(self, path: str, default=None):
        """获取指定路径的值
        
        Args:
            path: 值的访问路径
            default: 默认值
        """
        current = path.split("\\")[0]
        if current == "":
            return self.content
        elif isinstance(self.content, Base):
            return self.content.get_value(path, default)
        return default

    def set_value(self, path: str, value):
        """设置指定路径的值
        
        Args:
            path: 值的访问路径
            value: 要设置的值
        """
        current = path.split("\\")[0]
        if current == "":
            self.content = value
        elif isinstance(self.content, Base):
            self.content.set_value(path, value)