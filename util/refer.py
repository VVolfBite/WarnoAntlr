# 示例类定义
class Ammo:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Ammo: {self.name}>"

class Weapon:
    def __init__(self, name, ammo_type):
        self.name = name
        self.ammo_type = ammo_type  # 这是一个字符串，会在替换时指向 Ammo 实例

    def __repr__(self):
        return f"<Weapon: {self.name}, Ammo: {self.ammo_type}>"

class Unit:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon  # 这是一个字符串，会在替换时指向 Weapon 实例

    def __repr__(self):
        return f"<Unit: {self.name}, Weapon: {self.weapon}>"
def refer_class(entity, dictionary):
    """
    递归遍历嵌套结构，查找字符串值。如果字符串值在字典中存在且是一个对象，则用该对象替换字符串值。
    """
    # 检查是否为字典
    if isinstance(entity, dict):
        for key, value in entity.items():
            if isinstance(value, str):
                # 检查字典中是否有这个键，且其值是一个对象
                if value in dictionary and not isinstance(dictionary[value], (str, int, float, bool)):
                    entity[key] = dictionary[value]  # 替换为对应的对象
            else:
                # 递归处理嵌套的字典或其他类型
                refer_class(value, dictionary)
    
    # 检查是否为列表或元组
    elif isinstance(entity, (list, tuple)):
        for index, item in enumerate(entity):
            if isinstance(item, str):
                # 检查字典中是否有这个键，且其值是一个对象
                if item in dictionary and not isinstance(dictionary[item], (str, int, float, bool)):
                    entity[index] = dictionary[item]  # 替换为对应的对象
            else:
                # 递归处理嵌套的结构
                refer_class(item, dictionary)
    
    # 检查是否为自定义对象
    elif hasattr(entity, '__dict__'):
        for attr_name, attr_value in entity.__dict__.items():
            if isinstance(attr_value, str):
                # 检查字典中是否有这个键，且其值是一个对象
                if attr_value in dictionary and not isinstance(dictionary[attr_value], (str, int, float, bool)):
                    setattr(entity, attr_name, dictionary[attr_value])  # 替换为对应的对象
            else:
                # 递归处理对象的嵌套属性
                refer_class(attr_value, dictionary)
    
    return entity

# 创建对象字典
ammo_instance = Ammo("AP_23mm")
weapon_instance = Weapon("Cannon", "AP_23mm")  # 使用 ammo_instance 的名称
unit_instance = Unit("Tank", "Cannon")         # 使用 weapon_instance 的名称

# 字典包含对象，用于替换字符串
object_dict = {
    "AP_23mm": ammo_instance,
    "Cannon": weapon_instance
}

# 测试的嵌套结构
nested_structure = {
    "unit": unit_instance,
    "details": {
        "weapons": ["Cannon", "Missile"],
        "ammo_types": ["AP_23mm", "HE_35mm"]
    },
    "inventory": [
        {"type": "Weapon", "name": "Cannon"},
        {"type": "Ammo", "name": "AP_23mm"}
    ]
}

# 执行 refer_class 替换
result = refer_class(nested_structure, object_dict)

# # 打印结果
# print("转换后的结构:")
# print(result)
