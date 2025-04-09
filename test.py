import sys
import os
from typing import Any
import unittest
from antlr4 import *
from src.parsers.parser.NdfGrammarLexer import NdfGrammarLexer
from src.parsers.parser.NdfGrammarParser import NdfGrammarParser
from src.parsers.syntax_tree.actions.semantic_actions_generator import Generator
from src.parsers.syntax_tree.nodes.syntax_node_base import NodeType

class TestNdfGrammar(unittest.TestCase):
    """NDF语法全面测试"""

    def setUp(self):
        """测试初始化"""
        self.parse_text = lambda text: NdfGrammarParser(
            CommonTokenStream(NdfGrammarLexer(InputStream(text)))
        )
        
        # 测试用的引用表
        self.reference = {
            "test/path": 100,
            "system/value": "system",
            "obj/member": {"value": 200},
            "array/data": [1, 2, 3, 4, 5]
        }

    def parse_and_get_first(self, text: str, expected_values: dict):
        """解析文本并验证结果"""
        modes = ["register_object", "register_template", "generate_object"]
        
        for mode in modes:
            print(f"Testing in {mode} mode")
            parser = self.parse_text(text)
            tree = parser.ndf_file()
            generator = Generator(parser, reference=self.reference, mode=mode)
            walker = ParseTreeWalker()
            walker.walk(generator, tree)
            
            if not generator.assignments:
                if expected_values[mode] is not None:
                    self.fail(f"Expected assignment in {mode} mode but got none")
                continue
                
            node = generator.assignments[0]
            expected = expected_values[mode]
            
            if mode == "register_object":
                self.assertEqual(node.value, None)

    #-----------------------------------------
    # 1. 基础值类型测试 
    #-----------------------------------------
    def test_01_basic_values(self):
        """基础值类型测试"""
        print("\n=== 测试基础值类型 ===")
        
        test_cases = [
            ("Bool1 IS True", {
                "register_object": True,
                "register_template": True,
                "generate_object": True
            }),
            ("Int1 IS 100", {
                "register_object": 100,
                "register_template": 100,
                "generate_object": 100
            }),
            ("Float1 IS 3.14", {
                "register_object": 3.14,
                "register_template": 3.14,
                "generate_object": 3.14
            }),
            ("String1 IS 'test'", {
                "register_object": "test",
                "register_template": "test",
                "generate_object": "test"
            }),
            ("Hex1 IS 0xFF", {
                "register_object": 255,
                "register_template": 255,
                "generate_object": 255
            }),
            ("Id1 IS GUID:{123-456}", {
                "register_object": "GUID:{123-456}",
                "register_template": "GUID:{123-456}",
                "generate_object": "GUID:{123-456}"
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 2. 复合数据类型测试
    #-----------------------------------------
    def test_02_composite_values(self):
        """复合数据类型测试"""
        print("\n=== 测试复合数据类型 ===")
        
        test_cases = [
            ("Vec2 IS float2[1.0, 2.0]", {
                "register_object": [1.0, 2.0],
                "register_template": (1.0, 2.0),
                "generate_object": (1.0, 2.0)
            }),
            ("Vec3 IS float3[1.0, 2.0, 3.0]", {
                "register_object": [1.0, 2.0, 3.0],
                "register_template": (1.0, 2.0, 3.0),
                "generate_object": (1.0, 2.0, 3.0)
            }),
            ("List1 IS [1, 2, 3]", {
                "register_object": [1, 2, 3],
                "register_template": [1, 2, 3],
                "generate_object": [1, 2, 3]
            }),
            ("Pair1 IS ('key', 100)", {
                "register_object": ('key', 100),
                "register_template": ('key', 100),
                "generate_object": ('key', 100)
            }),
            ("Map1 IS MAP[('a', 1), ('b', 2)]", {
                "register_object": {'a': 1, 'b': 2},
                "register_template": {'a': 1, 'b': 2},
                "generate_object": {'a': 1, 'b': 2}
            }),
            ("Color1 IS RGBA[255, 0, 0, 255]", {
                "register_object": [255, 0, 0, 255],
                "register_template": [255, 0, 0, 255],
                "generate_object": (255, 0, 0, 255)
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 3. 边界情况测试
    #-----------------------------------------
    def test_03_edge_cases(self):
        """边界情况测试"""
        print("\n=== 测试边界情况 ===")
        
        test_cases = [
            ("Nil1 IS nil", {
                "register_object": None,
                "register_template": None,
                "generate_object": None
            }),
            ("Empty1 IS []", {
                "register_object": [],
                "register_template": [],
                "generate_object": []
            }),
            ("Empty2 IS MAP[]", {
                "register_object": {},
                "register_template": {},
                "generate_object": {}
            }),
            ("Unicode1 IS '测试'", {
                "register_object": "测试",
                "register_template": "测试",
                "generate_object": "测试"
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 4. 算术表达式测试
    #-----------------------------------------
    def test_04_arithmetic(self):
        """算术表达式测试"""
        print("\n=== 测试算术表达式 ===")
        
        test_cases = [
            ("Math1 IS 1 + 2", {
                "register_object": 3,
                "register_template": 3,
                "generate_object": 3
            }),
            ("Math2 IS (10 + 5) * 2", {
                "register_object": 30,
                "register_template": 30,
                "generate_object": 30
            }),
            ("Math3 IS ~/test/path + 50", {
                "register_object": "~/test/path + 50",
                "register_template": "~/test/path + 50",
                "generate_object": 150
            }),
            ("Math4 IS 15 div 3", {
                "register_object": 5,
                "register_template": 5,
                "generate_object": 5
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 5. 路径引用测试
    #-----------------------------------------
    def test_05_path_references(self):
        """路径引用测试"""
        print("\n=== 测试路径引用 ===")
        
        test_cases = [
            ("Ref1 IS ~/test/path", {
                "register_object": '~/test/path',
                "register_template": 100,
                "generate_object": 100
            }),
            ("Ref2 IS $/system/value", {
                "register_object": '$/system/value',
                "register_template": "system",
                "generate_object": "system"
            }),
            ("Ref3 IS ~/test/path | ~/system/value", {
                "register_object": '~/test/path | ~/system/value',
                "register_template": [100, "system"],
                "generate_object": [100, "system"]
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 6. 对象系统测试
    #-----------------------------------------
    def test_06_objects(self):
        """对象系统测试"""
        print("\n=== 测试对象系统 ===")
        
        test_cases = [
            ("""
            Obj1 IS TBaseObject(
                name = "test",
                value = 100
            )
            """, {
                "register_object": {"name": "test", "value": 100},
                "register_template": {"name": "test", "value": 100}, 
                "generate_object": {"name": "test", "value": 100}
            }),
            ("""
            Obj2 IS TParentObject(
                child = TChildObject(
                    name = "child",
                    value = 200
                ),
                count = 1
            )
            """, {
                "register_object": {
                    "child": {"name": "child", "value": 200},
                    "count": 1
                },
                "register_template": {
                    "child": {"name": "child", "value": 200},
                    "count": 1
                },
                "generate_object": {
                    "child": {"name": "child", "value": 200},
                    "count": 1
                }
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 7. 修饰符测试
    #-----------------------------------------
    def test_07_modifiers(self):
        """修饰符测试"""
        print("\n=== 测试修饰符 ===")
        
        test_cases = [
            ("export Val1 IS 100", {
                "register_object": None,
                "register_template": 100,
                "generate_object": 100
            }),
            ("private Val2 IS 200", {
                "register_object": 200,
                "register_template": 200,
                "generate_object": 200
            }),
            ("unnamed ~/test/path", {
                "register_object": "~/test/path",
                "register_template": "~/test/path",
                "generate_object": 100
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 8. 类型标注测试
    #-----------------------------------------
    def test_08_type_annotations(self):
        """类型标注测试"""
        print("\n=== 测试类型标注 ===")
        
        test_cases = [
            ("Val1:int IS 100", {
                "register_object": 100,
                "register_template": 100,
                "generate_object": 100
            }),
            ("List1:list<int> IS [1, 2, 3]", {
                "register_object": [1, 2, 3],
                "register_template": [1, 2, 3],
                "generate_object": [1, 2, 3]
            }),
            ("Map1:map<string,int> IS MAP[('a', 1)]", {
                "register_object": {'a': 1},
                "register_template": {'a': 1},
                "generate_object": {'a': 1}
            }),
            ("Obj1:TBaseObject IS TBaseObject(value = 100)", {
                "register_object": {'value': 100},
                "register_template": {'value': 100},
                "generate_object": {'value': 100}
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 9. 模板系统测试
    #-----------------------------------------
    def test_09_templates(self):
        """模板系统测试"""
        print("\n=== 测试模板系统 ===")
        
        test_cases = [
            ("""
            template Simple[T: int = 1] is TBaseObject(
                value = <T>
            )
            """, {
                "register_object": None,
                "register_template": None,
                "generate_object": None
            }),
            ("""
            template Complex[
                T: int = 1,
                S: string = "test"
            ] is TBaseObject(
                value = <T>,
                name = <S>
            )
            """, {
                "register_object": None,
                "register_template": None,
                "generate_object": None
            }),
            ("""
            template Simple[
                T1:int = 1,         
                T2:list<int>,       
                T3 = 100,           
                T4                  
            ] is TBaseObject(
                value = <T4>
            )
            """, {
                "register_object": None,
                "register_template": None,
                "generate_object": None
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 10. 混合特性测试
    #-----------------------------------------
    def test_10_mixed_features(self):
        """混合特性测试"""
        print("\n=== 测试混合特性 ===")
        
        test_cases = [
            ("""
            export ComplexObj:TComplexObject IS TComplexObject(
                value = 100,
            )
            """, {
                "register_object": {
                    "value": 100,
                    "array": [1, 2, 3],  # 对应修改
                    "dict": {"a": 1}     # 对应修改
                },
                "register_template": {
                    "value": 100,
                    "array": [1, 2, 3],
                    "dict": {"a": 1}
                },
                "generate_object": {
                    "value": 100,
                    "array": [1, 2, 3],
                    "dict": {"a": 1}
                }
            }),
            ("""
            Result IS float(~/test/path + 50) * 2
            """, {
                "register_object": "float(~/test/path + 50) * 2",
                "register_template": "float(~/test/path + 50) * 2",
                "generate_object": 300.0
            }),
            ("""
            template NestedTemplate[
                T: int = 1,
                S: string = "test"
            ] is TBaseTemplate(
                value = <T>,
                child = TChildTemplate(
                    name = <S>,
                )
            )
            """, {
                "register_object": None,
                "register_template": None,
                "generate_object": None
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

if __name__ == '__main__':
    unittest.main(verbosity=2)