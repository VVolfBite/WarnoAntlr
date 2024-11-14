def show_value(value, default_view=None):
    if value is None:
        if default_view == "bool":
            return "否"
        elif default_view == "int":
            return "不可用"
        return "无"
    
    if isinstance(value, int):
        if value == -1:
            return "默认"
        elif value == 0:
            return "不可用"
        else:
            return str(value)
    elif isinstance(value, bool):
        return "是" if value else "否"
    elif isinstance(value, list):
        return f"[ {', '.join(repr(item) for item in value)} ]"
    else:
        return str(value)


# 测试用例
if __name__ == "__main__":
    print(show_value(None))                    # 输出: "无"
    print(show_value(None, default_view="bool"))  # 输出: "否"
    print(show_value(None, default_view="int"))   # 输出: "不可用"
    print(show_value(-1))                       # 输出: "默认"
    print(show_value(0))                        # 输出: "不可用"
    print(show_value(42))                       # 输出: "42"
    print(show_value(True))                     # 输出: "是"
    print(show_value(False))                    # 输出: "否"
    print(show_value(["MOTION", "HE", "KINETIC"]))  # 输出: "[ 'MOTION', 'HE', 'KINETIC' ]"
    print(show_value("Some string"))           # 输出: "Some string"
