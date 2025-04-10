import logging
from src.parsers.syntax_tree.nodes.syntax_node_base import *

class Assignment(Base):
    """赋值语句节点"""
    def __init__(self):
        super().__init__()
        self.id = None
        self.content = None
        self.value = None
        self.type_spec = None  # 添加类型标注字段
        
        # 修饰符标记
        self.is_export = False
        self.is_private = False
        self.is_template = False
        self.is_member = False
        self.is_unnamed = False

    def convert_value(self):
        """根据类型标注转换值"""
        if not self.type_spec or not hasattr(self, 'value'):
            return

        type_str = self.type_spec.lower()
        converters = {
            "bool": bool,
            "int": int,
            "float": float,
            "string": str,
            "guid": str,
            "list": list,
            "map": dict
        }
        
        if type_str in converters:
            try:
                self.value = converters[type_str](self.value)
            except (ValueError, TypeError):
                logging.warning(f"Failed to convert {self.value} to {type_str}")

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