import sys

WORK_DIRECTORY = "D:/Workspace/InProgress/WarnoAntlr/"
sys.path.append(WORK_DIRECTORY)

import os
import re
import unittest
from diff_match_patch import diff_match_patch

from antlr4 import *
import antlr4
from antlr4.tree.Trees import Trees

from src.parsers.parser.NdfGrammarLexer import NdfGrammarLexer
from src.parsers.parser.NdfGrammarParser import NdfGrammarParser

from src.parsers.syntax_tree.actions import semantic_actions_generator
from src.parsers.syntax_tree.nodes.syntax_node_assignment import *
from src.parsers.syntax_tree.nodes.syntax_node_collection import *
from src.parsers.util import ndf_converter


# 将两份Ndf文件非关键内容删除，以比较两个文件的实际内容是否一致
def compare_strings(orig: str, generated: str) -> (str, str, bool):  # type: ignore
    orig = re.sub(r"//.*", "", orig)
    generated = re.sub(r"//.*", "", generated)
    for char in [" ", "\n", "\r", "\t"]:
        orig = orig.replace(char, "")
        generated = generated.replace(char, "")
    orig = orig.lower()
    generated = generated.lower()

    return orig, generated, orig == generated


# 将一个Ndf文件转换为Python对象格式
def generate_(file_name: str) -> [Assignment]:  # type: ignore
    input = antlr4.InputStream(str(FileStream(file_name, encoding="utf8")))
    lexer = NdfGrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = NdfGrammarParser(stream)
    tree = parser.ndf_file()
    semantic_actions_generator.DISABLE_CALCULATING = True
    listener = semantic_actions_generator.Generator(parser)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return File(listener.assignments)


# 进行轮回产生，即将一个Ndf文件转为python对象 ， 再将Python对象改回Ndf文件
def _roundtrip(file_name: str):
    converter = ndf_converter.ToNdfConverter()
    _file = generate_(file_name)
    return converter.convert(_file), _file


# 打印语法树
def print_tree(tree, parser):
    print(Trees.toStringTree(tree, None, parser))


class Test(unittest.TestCase):
    def test_primitives(self):
        self.roundtrip_test(
            WORK_DIRECTORY + "/tests/test_parsers/test_sample/Test_Primitives.ndf"
        )

    def test_datastructures(self):
        self.roundtrip_test(
            WORK_DIRECTORY + "/tests/test_parsers/test_sample/Test_Datastructures.ndf"
        )

    def test_object(self):
        self.roundtrip_test(
            WORK_DIRECTORY + "/tests/test_parsers/test_sample/Test_Nil.ndf"
        )

    def test_gd_contantes(self):
        self.object_comparison_test(
            WORK_DIRECTORY + "/tests/test_parsers/test_sample/TestM_GDConstantes.ndf"
        )
        self.roundtrip_test(
            WORK_DIRECTORY + "/tests/test_parsers/test_sample/TestM_GDConstantes.ndf"
        )

    def test_get_val_constantes(self):
        self.get_val_test(
            WORK_DIRECTORY + "/tests/test_parsers/test_sample/TestM_GDConstantes.ndf",
            "EShowGhostOverSpecificTerrainConditionFilterType\\None",
            0,
        )
        self.get_val_test(
            WORK_DIRECTORY + "/tests/test_parsers/test_sample/TestM_GDConstantes.ndf",
            "Constantes\\DefaultGhostColors\\GhostColor",
            [255, 255, 255, 255],
        )

    def test_set_val_constantes(self):
        self.set_val_test(
            WORK_DIRECTORY + "/tests/test_parsers/test_sample/TestM_GDConstantes.ndf",
            "EShowGhostOverSpecificTerrainConditionFilterType\\None",
            10,
            [NodeType.Integer],
        )
        self.set_val_test(
            WORK_DIRECTORY + "/tests/test_parsers/test_sample/TestM_GDConstantes.ndf",
            "Constantes\\DefaultGhostColors\\GhostColor",
            [1, 1, 1, 1],
            [NodeType.Integer] * 4,
        )

    def roundtrip_test(self, file_name: str):
        with open(file_name, encoding="utf-8") as f:
            orig = f.read()
        generated, _ = _roundtrip(file_name)
        orig_cmp, generated_cmp, equal = compare_strings(orig, generated)
        try:
            self.assertTrue(equal)
        except AssertionError as e:
            dmp = diff_match_patch()
            patches = dmp.patch_make(orig_cmp, generated_cmp)
            diff = dmp.patch_toText(patches)
            print(diff)
            print("original:\n")
            print(orig)
            print("generated:\n")
            print(generated)
            raise e

    def object_comparison_test(self, file_name: str):
        with open(file_name, encoding="utf-8") as f:
            orig = f.read()
        generated, orig_ = _roundtrip(file_name)
        with open("tmp.txt", encoding="utf-8", mode="x") as f:
            f.write(generated)
            generated_ = generate_("tmp.txt")
        os.remove("tmp.txt")
        if orig_ != generated_:
            raise Exception("Assignments not equal")

    def get_val_test(self, file_name: str, path: str, expected):
        _file = generate_(file_name)
        res = _file.get_raw_value(path)
        if res != expected:
            print("found:\n")
            print(res)
            print(type(res))
            print("expected:\n")
            print(expected)
            print(type(expected))
            raise Exception("Find results not equal")

    def set_val_test(self, file_name: str, path: str, value, dtypes: [NodeType]):  # type: ignore
        _file = generate_(file_name)
        _file.set_raw_value(path, value, dtypes)
        converter = ndf_converter.ToNdfConverter()
        _str = converter.convert(_file)
        with open("tmp.txt", encoding="utf-8", mode="x") as f:
            f.write(_str)
            generated_ = generate_("tmp.txt")
        os.remove("tmp.txt")

        res = generated_.get_raw_value(path)
        if res != value:
            print("found:\n")
            print(res)
            print(type(res))
            print("expected:\n")
            print(value)
            print(type(value))
            raise Exception("Find results not equal after setting value")


if __name__ == "__main__":
    unittest.main()
    # test = Test()
    # test.test_primitives()
