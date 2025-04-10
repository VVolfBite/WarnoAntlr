class BaseDescription:
    def __init__(self):
        pass

    def reverse(self):
        """将对象转换为其定义时的形式"""
        # 获取所有非私有变量，并处理占位符
        attributes = []
        for key, value in self.__dict__.items():
            if isinstance(value, list):
                # 处理列表类型
                value_str = [
                    item.reverse() if isinstance(item, BaseDescription)
                    else item.lstrip('@') if isinstance(item, str) and item.startswith('@')
                    else f'"{item}"' if isinstance(item, str)
                    else str(item)
                    for item in value
                ]
                attributes.append(f"{key}=[{', '.join(value_str)}]")
            elif isinstance(value, dict):
                # 处理字典类型
                value_str = {
                    k: v.reverse() if isinstance(v, BaseDescription)
                    else v.lstrip('@') if isinstance(v, str) and v.startswith('@')
                    else f'"{v}"' if isinstance(v, str)
                    else str(v)
                    for k, v in value.items()
                }
                attributes.append(f"{key}={value_str}")
            elif isinstance(value, BaseDescription):
                # 处理对象类型
                attributes.append(f"{key}={value.reverse()}")
            elif isinstance(value, str):
                # 处理字符串类型
                if value.startswith('@'):
                    attributes.append(f"{key}={value.lstrip('@')}")
                else:
                    attributes.append(f'{key}="{value}"')
            else:
                # 处理其他类型
                attributes.append(f"{key}={value}")

        # 拼接为格式化的类定义
        return f"{self.__class__.__name__}({', '.join(attributes)})"

#=============================================
# 测试样例
#=============================================
if __name__ == "__main__":
    # 1. 基础对象测试
    class TestObject(BaseDescription):
        def __init__(self, value=100, name="test"):
            super().__init__()
            self.value = value 
            self.name = name

    obj = TestObject()
    print("基础对象测试:", obj.reverse())  # 期望: TestObject(value=100, name="test")

    # 2. 嵌套对象测试
    class ChildObject(BaseDescription):
        def __init__(self, id=1):
            super().__init__()
            self.id = id

    class ParentObject(BaseDescription):
        def __init__(self, child=None, name="parent"):
            super().__init__()
            self.child = child or ChildObject()
            self.name = name

    parent = ParentObject()
    print("嵌套对象测试:", parent.reverse())  # 期望: ParentObject(child=ChildObject(id=1), name="parent")

    # 3. 列表成员测试
    class ListContainer(BaseDescription):
        def __init__(self, items=None):
            super().__init__()
            self.items = items or [ChildObject(id=i) for i in range(2)]

    list_obj = ListContainer()
    print("列表成员测试:", list_obj.reverse())  # 期望: ListContainer(items=[ChildObject(id=0), ChildObject(id=1)])

    # 4. 字典成员测试
    class DictContainer(BaseDescription):
        def __init__(self, data=None):
            super().__init__()
            self.data = data or {"obj": ChildObject(), "value": 100}

    dict_obj = DictContainer()
    print("字典成员测试:", dict_obj.reverse())  # 期望: DictContainer(data={'obj': ChildObject(id=1), 'value': 100})

    # 5. 引用路径测试
    class RefObject(BaseDescription):
        def __init__(self, path="@/test/path"):
            super().__init__()
            self.path = path

    ref_obj = RefObject()
    print("引用路径测试:", ref_obj.reverse())  # 期望: RefObject(path=/test/path)
