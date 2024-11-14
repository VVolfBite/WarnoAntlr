import logging
import os
import re

# @NOTE 这份工具存在部分问题


# 获取赋值语句的字段表
def get_assignment_ids(mod_base: str, file_name: str) -> [str]:  # type: ignore
    file_name = os.path.join(mod_base, file_name)
    with open(file_name, mode="r", encoding="utf-8") as f:
        file_content = f.read()

    current_index = 0
    assignment_regex = re.compile("(\\w+)\\sis\\s")
    ids = []

    while True:
        res = assignment_regex.search(
            file_content, current_index, file_content.find("(", current_index)
        )
        if not res:
            break
        ids.append(res.group(1))

        current_index = traverse_object(file_content, current_index)

    return ids


# get start and end index of a given top level object in an NDF file
def get_object_range(mod_base: str, file_name: str, object_name: str) -> (str, int, int):  # type: ignore
    file_name = os.path.join(mod_base, file_name)
    with open(file_name, mode="r", encoding="utf-8") as f:
        file_content = f.read()
    try:
        start = file_content.index(object_name)
    except Exception as e:
        logging.warning(
            "Object " + object_name + " not found in " + file_name + ": " + str(e)
        )
        return "", -1, -1

    end = traverse_object(file_content, start)
    return file_content[start:end], start, end


def get_map_value_range(mod_base: str, file_name: str, map_name: str, map_key: str) -> (str, int, int):  # type: ignore
    file_name = os.path.join(mod_base, file_name)
    with open(file_name, mode="r", encoding="utf-8") as f:
        file_content = f.read()

    try:
        map_start = file_content.index(map_name)
    except Exception as e:
        logging.warning(
            "Map " + map_name + " not found in " + file_name + ": " + str(e)
        )
        return "", -1, -1

    map_end = traverse_object(file_content, map_start, ["[", "]"])
    current_index = file_content.find("(", map_start, map_end) + 1

    while True:
        # go to opening bracket
        current_index = file_content.find("(", current_index, map_end)
        if current_index < 0 or current_index > map_end:
            logging.warning("Entry " + map_key + " not found map " + map_name)
            return "", -1, -1

        next_open = file_content.find("(", current_index + 1, map_end)
        next_close = file_content.find(")", current_index, map_end)
        key_pos = file_content.find(map_key, current_index, map_end)
        if key_pos < 0:
            logging.warning("Entry " + map_key + " not found map " + map_name)
            return "", -1, -1

        if key_pos > next_open or key_pos > next_close:
            current_index = traverse_object(file_content, current_index)
        else:
            start = current_index
            end = traverse_object(file_content, current_index)
            return file_content[start:end], start, end


# walk over an ndf object, return end index
def traverse_object(file_content: str, current_index: int, limit_chars: [str] = ["(", ")"]) -> int:  # type: ignore
    current_index = file_content.find(limit_chars[0], current_index) + 1
    level = 1
    while level > 0:
        next_open = file_content.find(limit_chars[0], current_index)
        next_close = file_content.find(limit_chars[1], current_index)
        if next_close < 0:
            break
        if next_close > next_open > 0:
            level += 1
            current_index = next_open + 1
        else:
            level -= 1
            current_index = next_close + 1
    return current_index
