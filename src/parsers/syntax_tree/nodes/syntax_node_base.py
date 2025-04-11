"""语法节点基类模块
提供语法树节点的基本类型和基类实现

主要功能:
1. 节点类型枚举定义
2. 节点基类实现
3. 节点基本操作
"""

#=============================================
# 1. 节点类型枚举
#=============================================
class NodeType:
    """节点类型枚举"""
    (
        #-------------------------
        # 1.1 基础类型
        #-------------------------
        UNKNOWN,        # 未知类型
        STRUCTURAL,     # 结构类型
        
        #-------------------------
        # 1.2 简单数据类型
        #-------------------------
        Nil,           # 空值
        Boolean,       # 布尔值
        Integer,       # 整数
        Hex,           # 十六进制数
        Float,         # 浮点数
        String,        # 字符串
        GUID,          # GUID
        
        #-------------------------
        # 1.3 复合数据类型
        #-------------------------
        Reference,     # 引用
        Pair,         # 键值对
        Vector,       # 向量
        Map,          # 映射
        Object,       # 对象
        Template,     # 模板
        
        #-------------------------
        # 1.4 特殊类型
        #-------------------------
        Float2,       # 二维向量
        Float3,       # 三维向量
        RGBA,         # RGBA颜色
        
        #-------------------------
        # 1.5 表达式类型
        #-------------------------
        Arithmetic,   # 算术表达式
        
        #-------------------------
        # 1.6 模板系统
        #-------------------------
        Parameter,    # 模板参数
        Replacer,     # 替换值
        
        #-------------------------
        # 1.7 对象系统
        #-------------------------
        Member        # 对象成员
    ) = range(22)    # 枚举范围

#=============================================
# 2. 节点基类
#=============================================
class Base:
    """语法节点基类"""
    
    def __init__(self):
        """初始化基本属性"""
        # 节点基本信息
        self.nodetype = NodeType.UNKNOWN  # 节点类型
        self.content = None               # 原始内容
        self.value = None                 # 实际值

    def __str__(self) -> str:
        """字符串表示
        Returns:
            str: 节点的字符串描述
        """
        info = f"type: {self.nodetype}, value: {self.value}"
        return info + "}"

    def __eq__(self, other) -> bool:
        """相等比较
        Args:
            other: 要比较的对象
        Returns:
            bool: 是否相等
        """
        if not isinstance(other, Base):
            return False
        return (self.nodetype == other.nodetype and 
                self.value == other.value)

    def __hash__(self) -> int:
        """计算哈希值
        Returns:
            int: 节点的哈希值
        """
        return hash((self.nodetype, self.value))

    def clone(self) -> 'Base':
        """创建节点副本
        Returns:
            Base: 新的节点实例
        """
        new_node = Base()
        new_node.nodetype = self.nodetype
        new_node.content = self.content
        new_node.value = self.value
        return new_node