"""集合节点模块
提供各种复合数据类型的节点实现

主要功能:
1. 基础集合类 - 通用集合功能
2. 具体集合类型 - 对象、键值对等
3. 特殊向量类型 - 二维和三维向量
"""

import logging
from pathlib import Path
from typing import Any, Optional, Dict, List, Tuple

from src.parsers.syntax_tree.nodes.syntax_node_base import *
from src.parsers.syntax_tree.nodes.syntax_node_assignment import *

#=============================================
# 1. 基础集合类
#=============================================
class Collection(Base):
    """基础集合类
    作为中间形式存储各种复合数据类型:
    1. 文件列表: [assignment1, assignment2, ...]
    2. 对象成员: Object(member1=value1, member2=value2)
    3. 值向量: [value1, value2, value3]
    4. 键值对: (key, value)
    5. 映射表: Map[(key1,value1), (key2,value2)]
    """
    
    def __init__(self):
        """初始化集合"""
        super().__init__()
        self.content: List[Base] = []    # 存储实际内容
        self.lookup: Dict[str, int] = {} # 快速查找表

    def append(self, data: Base) -> None:
        """添加新元素
        Args:
            data: 要添加的节点元素
        """
        self.content.append(data)
        if isinstance(data, Assignment):
            self.lookup[data.id] = len(self.content) - 1
        elif isinstance(data, Object):
            self.lookup[data.object_type] = len(self.content) - 1

    def get_value(self, path: str, default: Any = None) -> Any:
        """按路径获取值
        Args:
            path: 访问路径
            default: 默认值
        Returns:
            路径对应的值或默认值
        """
        current = path.split("\\")[0]
        remaining = path.removeprefix(current).removeprefix("\\")
        
        if current == "":
            return self.content
        elif current in self.lookup:
            return self.content[self.lookup[current]].get_value(remaining, default)
        return default

    def set_value(self, path: str, value: Any) -> None:
        """按路径设置值
        Args:
            path: 访问路径
            value: 要设置的值
        """
        current = path.split("\\")[0]
        remaining = path.removeprefix(current).removeprefix("\\")
        
        if current == "":
            self.content = value
        elif current in self.lookup:
            self.content[self.lookup[current]].set_value(remaining, value)

#=============================================
# 2. 具体集合类型
#=============================================
class Object(Collection):
    """对象节点类"""
    
    def __init__(self):
        super().__init__()
        self.object_type: Optional[str] = None
        self.nodetype = NodeType.Object

    def get_class(self) -> Tuple[str, Dict[str, Any]]:
        """获取类信息
        Returns:
            Tuple[类名, 属性字典]
        """
        # 获取类名
        class_name = self.object_type
        
        # 收集属性
        attributes = {}
        for member in self.content:
            if hasattr(member, 'id') and hasattr(member, 'content'):
                if hasattr(member.content, 'content'):
                    attributes[member.id] = member.content.content
                else:
                    attributes[member.id] = member.content
                    
        return class_name, attributes

class Pair(Collection):
    """键值对节点
    限制只能有两个元素:key和value
    """
    def __init__(self):
        super().__init__()
        self.nodetype = NodeType.Pair

    def append(self, data: Base):
        if len(self.content) < 2:
            super().append(data)

class Vector(Collection):
    """向量节点
    表示一个值的列表
    """
    def __init__(self):
        super().__init__()
        self.nodetype = NodeType.Vector

class Map(Collection):
    """映射节点
    表示键值对的集合
    """
    def __init__(self):
        super().__init__()
        self.map: Dict[Any, Any] = {}   # 实际存储的映射关系
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
    """二维向量节点
    限制只能有2个数值元素
    """
    def __init__(self):
        super().__init__()
        self.nodetype = NodeType.Float2

    def append(self, data: Base):
        if len(self.content) < 2 and data.is_numeric():
            super().append(data)

class Float3(Vector):
    """三维向量节点
    限制只能有3个数值元素
    """
    def __init__(self):
        super().__init__()
        self.nodetype = NodeType.Float3

    def append(self, data: Base):
        if len(self.content) < 3 and data.is_numeric():
            super().append(data)