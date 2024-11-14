RangeModifiersTable = [
    {0.05: 300},
    {0.17: 70},
    {0.33: 50},
    {0.50: 30},
    {0.67: 15},
    {1.00: 0},
    {9999: 0}
]

def get_interpolated_value(value):
    # 将每个集合转换为包含 (bound, val) 的列表
    range_modifiers_list = [[key, value] for item in RangeModifiersTable for key, value in item.items()]
    # 按照第一个值（bound）排序，因为集合没有顺序
    range_modifiers_list.sort(key=lambda x: x[0])

    # 遍历 RangeModifiersTable，找到区间
    for i in range(1, len(range_modifiers_list)):
        lower_bound, lower_value = range_modifiers_list[i - 1]
        upper_bound, upper_value = range_modifiers_list[i]

        if lower_bound <= value <= upper_bound:
            # 计算线性插值
            ratio = (value - lower_bound) / (upper_bound - lower_bound)
            interpolated_value = lower_value + ratio * (upper_value - lower_value)
            return interpolated_value

    # 如果超出范围，返回最后一个值
    return range_modifiers_list[-1][1]

# 示例用法
value = 0.67
result = get_interpolated_value(value)
print(f"Interpolated value for {value}: {result}")
