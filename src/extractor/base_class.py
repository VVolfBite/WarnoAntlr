class BaseDescription:
    def __init__(self):
        self.KeyName = None
    def reverse(self):
        # 获取所有非私有变量，并处理占位符
        attributes = [
            f"{key}="
            + (
                value.reverse()  # 如果值是 BaseDescription 类型，调用 reverse()
                if isinstance(value, BaseDescription)
                else value.lstrip('@')  # 如果是以 '@' 开头的字符串，移除 '@'
                if isinstance(value, str) and value.startswith('@')
                else f'"{value}"'  # 如果是普通字符串，包裹在双引号中
                if isinstance(value, str) and not value.startswith('@')
                else value  # 其他类型直接输出
            )
            for key, value in self.__dict__.items()
        ]

        # 拼接为格式化的类定义
        return f"{self.__class__.__name__}({', '.join(attributes)})"
