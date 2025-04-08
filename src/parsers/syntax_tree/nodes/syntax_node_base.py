#=============================================
# 1. 节点类型枚举
#=============================================
class NodeType:
    """节点类型枚举"""
    (
        # 1.1 基础类型
        UNKNOWN,        # 未知类型
        STRUCTURAL,     # 结构类型
        
        # 1.2 简单数据类型
        Nil,           # 空值
        Boolean,       # 布尔值
        Integer,       # 整数
        Float,         # 浮点数
        String,        # 字符串
        GUID,         # GUID
        
        # 1.3 复合数据类型
        Reference,     # 引用
        Pair,         # 键值对
        Vector,       # 向量
        Map,          # 映射
        Object,       # 对象
        Template,     # 模板
        
        # 1.4 特殊类型
        Float2,       # 二维向量
        Float3,       # 三维向量
        RGBA         # RGBA颜色
    ) = range(17)

#=============================================
# 2. 语法节点基类
#=============================================
class Base:
    """语法节点基类"""
    
    def __init__(self):
        """初始化"""
        self.nodetype = NodeType.UNKNOWN  # 节点类型
        self.content = None               # 原始内容
        self.value = None                 # 实际值
        self.operator = None              # 运算符
        self.template_params = {}         # 模板参数

    def __str__(self) -> str:
        """字符串表示"""
        info = f"{{type: {self.nodetype}, value: {self.value}"
        if self.operator:
            info += f", operator: {self.operator}"
        return info + "}"

    def __eq__(self, other) -> bool:
        """相等比较"""
        if not isinstance(other, Base):
            return False
        return self.nodetype == other.nodetype and self.value == other.value

    def __hash__(self) -> int:
        """哈希值"""
        return hash((self.nodetype, self.value))

    def clone(self):
        """创建副本"""
        new_node = Base()
        new_node.nodetype = self.nodetype
        new_node.content = self.content
        new_node.value = self.value
        new_node.operator = self.operator
        new_node.template_params = self.template_params.copy()
        return new_node