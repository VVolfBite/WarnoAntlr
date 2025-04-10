class TBaseObject:
    """基础对象类"""
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

class TChildObject:
    """子对象类"""
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

class TParentObject:
    """父对象类"""
    def __init__(self, child=None, count=None):
        self.child = child  # TChildObject类型
        self.count = count

class Simple(TBaseObject):
    """由模板生成的类
    template Simple[T: int = 1] is TBaseObject(
        value = <T>
    )
    """
    def __init__(self, T: int = 1):
        super().__init__(value=T)
        # 模板参数存储
        self.T = T

class Complex(TBaseObject):
    """由模板生成的类
    template Complex[
        T: int = 1,
        S: string = "test"
    ] is TBaseObject(
        value = <T>,
        name = <S>
    )
    """
    def __init__(self, T: int = 1, S: str = "test"):
        super().__init__(value=T)
        self.name = S
        # 模板参数存储
        self.T = T
        self.S = S

class TComplexObject:
    """复杂对象类"""
    def __init__(self, value=None, array=None):
        self.value = value
        self.array = array

class TChild:
    """嵌套子对象类"""
    def __init__(self, name=None, data=None):
        self.name = name
        self.data = data

class TData:
    """数据容器类"""
    def __init__(self, list=None, map=None):
        self.list = list
        self.map = map 

class TParent:
    """嵌套父对象类"""
    def __init__(self, name=None, child=None):
        self.name = name  
        self.child = child  # TChild类型

class TChildTemplate:
    """子模板类
    用在嵌套模板中:
    TChildTemplate(
        name = <S>,
        list = [<T>, <T> * 2]
    )
    """
    def __init__(self, name: str = None, list: list = None):
        self.name = name


class TBaseTemplate:
    """基础模板类"""
    def __init__(self, value=None, child=None):
        self.value = value
        self.child = child  # TChildTemplate类型

class NestedTemplate(TBaseTemplate):
    """嵌套模板示例
    template NestedTemplate[
        T: int = 1,
        S: string = "test"
    ] is TBaseTemplate(
        value = <T>,
        child = TChildTemplate(
            name = <S>,
            list = [<T>, <T> * 2]
        )
    )
    """
    def __init__(self, T: int = 1, S: str = "test"):
        super().__init__()
        self.value = T
        self.child = TChildTemplate(
            name=S,
            list=[T, T * 2]
        )
        # 模板参数存储
        self.T = T
        self.S = S
