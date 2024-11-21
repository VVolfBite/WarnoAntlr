class BaseDescription:
    def __init__(self):
        self.KeyName = None
    def reverse(self):
        # 获取所有非私有变量
        attributes = [
            f"{key}={value.reverse() if isinstance(value, BaseDescription) else repr(value)}"
            for key, value in self.__dict__.items()
        ]
        # 拼接为格式化的类定义
        return f"{self.__class__.__name__}({', '.join(attributes)})"