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
        Replacer,     # 替换类型
        
        # 1.4 新增数据类型
        Float2,       # 二维向量
        Float3,       # 三维向量
        Template      # 模板定义
    ) = range(21)


#=============================================
# 2. 语法节点基类
#=============================================
class Base:
    """语法节点树的基类
    
    规定:
    - nodetype: 描述节点类型
    - content: 存储原始输入内容
    - value: 存储转换后的实际值
    - operator: 存储运算符(用于算术和引用组合)
    - template_params: 存储模板参数(仅用于Template类型)
    """
    def __init__(self):
        """初始化基础节点"""
        self.nodetype = NodeType.UNKNOWN  # 节点类型
        self.content = None               # 原始内容
        self.value = None                 # 实际值
        self.operator = None              # 运算符
        self.template_params = {}         # 模板参数字典

    def __str__(self) -> str:
        """返回节点的字符串表示"""
        base_info = "{type: " + str(self.nodetype) + ", value: " + str(self.value)
        if self.operator:
            base_info += f", operator: {self.operator}"
        if self.template_params:
            base_info += f", template_params: {self.template_params}"
        return base_info + "}"

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

    def add_template_param(self, name: str, param_type: str, default_value=None):
        """添加模板参数
        
        Args:
            name: 参数名
            param_type: 参数类型
            default_value: 默认值(可选)
        """
        if self.nodetype != NodeType.Template:
            raise ValueError("Can only add template parameters to Template nodes")
        
        self.template_params[name] = {
            'type': param_type,
            'default': default_value
        }

    def get_operator_precedence(self) -> int:
        """获取运算符优先级
        
        Returns:
            int: 运算符优先级(数字越大优先级越高)
        """
        if not self.operator:
            return 0
            
        precedences = {
            '*': 3, 'DIV': 3,
            '+': 2, '-': 2,
            '|': 1
        }
        return precedences.get(self.operator, 0)