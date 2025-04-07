#=============================================
# 1. 节点类型枚举
#=============================================
class NodeType:
    """节点类型枚举
    用于标识语法树中不同节点的类型
    """
    (
        # 1.1 基础类型
        UNKNOWN,        # 未知类型
        STRUCTURAL,     # 结构类型
        
        # 1.2 简单数据类型
        Nil,           # 空值类型
        Boolean,       # 布尔类型
        Integer,       # 整数类型
        HexInteger,    # 十六进制整数
        Float,         # 浮点数类型
        String_single, # 单引号字符串
        String_double, # 双引号字符串
        GUID,         # GUID类型
        RGBA,         # RGBA颜色类型
        
        # 1.3 复合数据类型
        Reference,     # 引用类型
        Pair,         # 键值对类型
        Vector,       # 向量类型
        Map,          # 映射类型
        Arithmetic,   # 算术表达式
        Object,       # 对象类型
        Replacer      # 替换类型
    ) = range(18)


#=============================================
# 2. 语法节点基类
#=============================================
class Base:
    """语法节点树的基类
    
    规定:
    - nodetype: 描述节点类型
    - content: 存储原始输入内容
    - value: 存储转换后的实际值
    """
    def __init__(self):
        """初始化基础节点"""
        self.nodetype = NodeType.UNKNOWN  # 节点类型
        self.content = None               # 原始内容
        self.value = None                # 实际值

    def __str__(self) -> str:
        """返回节点的字符串表示
        格式: {type: <节点类型>, value: <节点值>}
        """
        return "{type: " + str(self.nodetype) + ", value: " + str(self.value) + "}"

    def __eq__(self, other) -> bool:
        """判断两个节点是否相等
        
        Args:
            other: 要比较的另一个节点
            
        Returns:
            bool: 如果类型和值都相等则返回True
        """
        if not type(other) == type(self):
            return False
        return self.nodetype == other.nodetype and self.value == other.value

    def __hash__(self) -> int:
        """返回节点的哈希值
        基于节点类型和值计算
        """
        return hash((self.nodetype, self.value))

    def get_value(self, path: str, default=None):
        """获取指定路径的值
        
        Args:
            path: 值的访问路径
            default: 默认返回值
            
        Returns:
            找到的值或默认值
            
        Note:
            需要被子类实现
        """
        print(self)
        print("not implemented")
        return default

    def set_value(self, path: str, value):
        """设置指定路径的值
        
        Args:
            path: 要设置的值的路径
            value: 要设置的值
            
        Note:
            需要被子类实现
        """
        print(self)
        print("not implemented")