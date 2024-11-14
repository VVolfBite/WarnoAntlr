bonusPrecision = 3

SuccessiveHitModifiersTable = [
    {0:  0},
    {1:  1 * bonusPrecision},
    {2:  2 * bonusPrecision},
    {3:  3 * bonusPrecision},
    {4:  4 * bonusPrecision},
    {5:  5 * bonusPrecision},
    {6:  6 * bonusPrecision},
    {7:  7 * bonusPrecision},
    {8:  8 * bonusPrecision},
    {9:  9 * bonusPrecision},
    {10: 10 * bonusPrecision},
]

def get_bonus_precision(hit_count):

    successive_hit_modifiers_list = [[key, value] for item in SuccessiveHitModifiersTable for key, value in item.items()]
    successive_hit_modifiers_list = sorted(successive_hit_modifiers_list, key=lambda x: x[0])
    for mod in successive_hit_modifiers_list:
        if hit_count == mod[0]:
            return mod[1]
    # 如果超出范围，返回最后一个值
    return 0

# 示例用法
hit_count = 4
result = get_bonus_precision(hit_count)
print(f"Bonus precision for hit count {hit_count}: {result}")
