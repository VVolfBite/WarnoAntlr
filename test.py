import sys
import os
from typing import Any  # 添加这行
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
        """解析文本并验证结果
        
        Args:
            text: 要解析的文本
            expected_values: 期望值字典 {mode: expected_value}
        """
        modes = ["register_object", "register_template", "generate_object"]
        
        for mode in modes:
            print(f"Testing in {mode} mode")
            parser = self.parse_text(text)
            tree = parser.ndf_file()
            generator = Generator(parser, reference=self.reference, mode=mode)
            walker = ParseTreeWalker()
            walker.walk(generator, tree)
            
            if not generator.assignments:
                self.fail(f"No assignment generated in {mode} mode")
                
            node = generator.assignments[0]
            expected = expected_values[mode]
            
            if mode == "register_object":
                # register_object模式检查content
                self.assertEqual(node.content.content, expected)
            else:
                # 其他模式检查value
                self.assertEqual(node.content.value, expected)

    #-----------------------------------------
    # 1. 基础值类型测试
    #-----------------------------------------
    def test_01_basic_values(self):
        """基础值类型测试"""
        print("\n=== 测试基础值类型 ===")
        
        test_cases = [
            # 布尔值测试
            ("Bool1 IS True", {
                "register_object": True,
                "register_template": True,
                "generate_object": True
            }),
            # 整数测试
            ("Int1 IS 100", {
                "register_object": 100,
                "register_template": 100,
                "generate_object": 100
            }),
            # 浮点数测试
            ("Float1 IS 3.14", {
                "register_object": 3.14,
                "register_template": 3.14,
                "generate_object": 3.14
            }),
            # 字符串测试
            ("String1 IS 'test'", {
                "register_object": "test",
                "register_template": "test",
                "generate_object": "test"
            }),
            # 十六进制测试
            ("Hex1 IS 0xFF", {
                "register_object": 255,
                "register_template": 255,
                "generate_object": 255
            }),
            # GUID测试
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
            # float2测试
            ("Vec2 IS float2[1.0, 2.0]", {
                "register_object": [1.0, 2.0],
                "register_template": [1.0, 2.0],
                "generate_object": (1.0, 2.0)
            }),
            # float3测试
            ("Vec3 IS float3[1.0, 2.0, 3.0]", {
                "register_object": [1.0, 2.0, 3.0],
                "register_template": [1.0, 2.0, 3.0],
                "generate_object": (1.0, 2.0, 3.0)
            }),
            # 列表测试
            ("List1 IS [1, 2, 3]", {
                "register_object": [1, 2, 3],
                "register_template": [1, 2, 3],
                "generate_object": [1, 2, 3]
            }),
            # 键值对测试
            ("Pair1 IS ('key', 100)", {
                "register_object": ('key', 100),
                "register_template": ('key', 100),
                "generate_object": ('key', 100)
            }),
            # 映射测试
            ("Map1 IS MAP[('a', 1), ('b', 2)]", {
                "register_object": {'a': 1, 'b': 2},
                "register_template": {'a': 1, 'b': 2},
                "generate_object": {'a': 1, 'b': 2}
            }),
            # RGBA测试
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
    # 3. 路径引用测试
    #-----------------------------------------
    def test_03_path_references(self):
        """路径引用测试"""
        print("\n=== 测试路径引用 ===")
        
        test_cases = [
            # 相对路径
            ("Ref1 IS ~/test/path", {
                "register_object": '~/test/path',
                "register_template": '~/test/path',
                "generate_object": 100
            }),
            # 系统路径
            ("Ref2 IS $/system/value", {
                "register_object": '$/system/value',
                "register_template": '$/system/value',
                "generate_object": "system"
            }),
            # 多重引用
            ("Ref3 IS ~/test/path | ~/system/value", {
                "register_object": '~/test/path | ~/system/value',
                "register_template": '~/test/path | ~/system/value',
                "generate_object": 100
            }),
            # 数组访问
            ("Ref4 IS ~/array/data[2]", {
                "register_object": '~/array/data[2]',
                "register_template": '~/array/data[2]',
                "generate_object": 3
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 4. 对象系统测试
    #-----------------------------------------
    def test_04_objects(self):
        """对象系统测试"""
        print("\n=== 测试对象系统 ===")
        
        test_cases = [
            # 简单对象
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
            # 嵌套对象
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
    # 5. 模板系统测试
    #-----------------------------------------
    def test_05_templates(self):
        """模板系统测试"""
        print("\n=== 测试模板系统 ===")
        
        test_cases = [
            # 基本模板
            ("""
            template Simple[T: int = 1] is TBaseObject(
                value = <T>
            )
            """, {
                "register_object": None,
                "register_template": {
                    "params": {"T": {"type": "int", "default": 1}},
                    "base": {"name": "TBaseObject", "attrs": {"value": "<T>"}}
                },
                "generate_object": None
            }),
            # 多参数模板
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
                "register_template": {
                    "params": {
                        "T": {"type": "int", "default": 1},
                        "S": {"type": "string", "default": "test"}
                    },
                    "base": {
                        "name": "TBaseObject",
                        "attrs": {"value": "<T>", "name": "<S>"}
                    }
                },
                "generate_object": None
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 6. 类型标注测试
    #-----------------------------------------
    def test_06_type_annotations(self):
        """类型标注测试"""
        print("\n=== 测试类型标注 ===")
        
        test_cases = [
            # 基本类型标注
            ("Val1:int IS 100", {
                "register_object": 100,
                "register_template": 100,
                "generate_object": 100
            }),
            # 复合类型标注
            ("List1:list<int> IS [1, 2, 3]", {
                "register_object": [1, 2, 3],
                "register_template": [1, 2, 3],
                "generate_object": [1, 2, 3]
            }),
            # 泛型类型标注
            ("Map1:map<string,int> IS MAP[('a', 1)]", {
                "register_object": {'a': 1},
                "register_template": {'a': 1},
                "generate_object": {'a': 1}
            }),
            # 对象类型标注
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
    # 7. 修饰符测试
    #-----------------------------------------
    def test_07_modifiers(self):
        """修饰符测试"""
        print("\n=== 测试修饰符 ===")
        
        test_cases = [
            # export修饰符
            ("export Val1 IS 100", {
                "register_object": 100,
                "register_template": 100,
                "generate_object": 100
            }),
            # private修饰符
            ("private Val2 IS 200", {
                "register_object": 200,
                "register_template": 200,
                "generate_object": 200
            }),
            # unnamed修饰符
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
    # 8. 算术表达式测试
    #-----------------------------------------
    def test_08_arithmetic(self):
        """算术表达式测试"""
        print("\n=== 测试算术表达式 ===")
        
        test_cases = [
            # 基本运算
            ("Math1 IS 1 + 2", {
                "register_object": 3,
                "register_template": 3,
                "generate_object": 3
            }),
            # 复合运算
            ("Math2 IS (10 + 5) * 2", {
                "register_object": 30,
                "register_template": 30,
                "generate_object": 30
            }),
            # 引用运算
            ("Math3 IS ~/test/path + 50", {
                "register_object": "~/test/path + 50",
                "register_template": "~/test/path + 50",
                "generate_object": 150
            }),
            # div运算
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
    # 9. 成员访问测试
    #-----------------------------------------
    def test_09_member_access(self):
        """成员访问测试"""
        print("\n=== 测试成员访问 ===")
        
        test_cases = [
            # 直接成员访问
            ("obj.member = 100", {
                "register_object": 100,
                "register_template": 100,
                "generate_object": 100
            }),
            # 数组成员访问
            ("obj.array[0] = 200", {
                "register_object": 200,
                "register_template": 200,
                "generate_object": 200
            }),
            # 嵌套成员访问
            ("obj.child.value = 300", {
                "register_object": 300,
                "register_template": 300,
                "generate_object": 300
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 10. 边界情况测试
    #-----------------------------------------
    def test_10_edge_cases(self):
        """边界情况测试"""
        print("\n=== 测试边界情况 ===")
        
        test_cases = [
            # 空值
            ("Nil1 IS nil", {
                "register_object": None,
                "register_template": None,
                "generate_object": None
            }),
            # 空列表
            ("Empty1 IS []", {
                "register_object": [],
                "register_template": [],
                "generate_object": []
            }),
            # 空MAP
            ("Empty2 IS MAP[]", {
                "register_object": {},
                "register_template": {},
                "generate_object": {}
            }),
            # Unicode字符串
            ("Unicode1 IS '测试'", {
                "register_object": "测试",
                "register_template": "测试",
                "generate_object": "测试"
            }),
            # 转义字符
            (r'Escape1 IS "test\ntest"', {
                "register_object": "test\ntest",
                "register_template": "test\ntest",
                "generate_object": "test\ntest"
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 11. 混合特性测试
    #-----------------------------------------
    def test_11_mixed_features(self):
        """混合特性测试"""
        print("\n=== 测试混合特性 ===")
        
        test_cases = [
            # 修饰符+类型标注+对象
            ("""
            export ComplexObj:TComplexObject IS TComplexObject(
                value = 100,
                list = [1, 2, 3],
                map = MAP[('a', 1)]
            )
            """, {
                "register_object": {
                    "value": 100,
                    "list": [1, 2, 3],
                    "map": {"a": 1}
                },
                "register_template": {
                    "value": 100,
                    "list": [1, 2, 3],
                    "map": {"a": 1}
                },
                "generate_object": {
                    "value": 100,
                    "list": [1, 2, 3],
                    "map": {"a": 1}
                }
            }),
            # 引用+算术+类型转换
            ("""
            Result IS float(~/test/path + 50) * 2
            """, {
                "register_object": "float(~/test/path + 50) * 2",
                "register_template": "float(~/test/path + 50) * 2",
                "generate_object": 300.0
            }),
            # 复杂对象嵌套
            ("""
            NestedObj IS TParent(
                name = "parent",
                child = TChild(
                    name = "child",
                    data = TData(
                        list = [1, 2],
                        map = MAP[('x', 100)]
                    )
                )
            )
            """, {
                "register_object": {
                    "name": "parent",
                    "child": {
                        "name": "child",
                        "data": {
                            "list": [1, 2],
                            "map": {"x": 100}
                        }
                    }
                },
                "register_template": {
                    "name": "parent",
                    "child": {
                        "name": "child",
                        "data": {
                            "list": [1, 2],
                            "map": {"x": 100}
                        }
                    }
                },
                "generate_object": {
                    "name": "parent",
                    "child": {
                        "name": "child",
                        "data": {
                            "list": [1, 2],
                            "map": {"x": 100}
                        }
                    }
                }
            }),
            # 模板特化嵌套
            ("""
            template NestedTemplate[
                T: int = 1,
                S: string = "test"
            ] is TBaseTemplate(
                value = <T>,
                child = TChildTemplate(
                    name = <S>,
                    list = [<T>, <T> * 2]
                )
            )
            """, {
                "register_object": None,
                "register_template": {
                    "params": {
                        "T": {"type": "int", "default": 1},
                        "S": {"type": "string", "default": "test"}
                    },
                    "base": {
                        "type": "TBaseTemplate",
                        "attrs": {
                            "value": "<T>",
                            "child": {
                                "type": "TChildTemplate",
                                "attrs": {
                                    "name": "<S>",
                                    "list": ["<T>", "<T> * 2"]
                                }
                            }
                        }
                    }
                },
                "generate_object": None
            })
        ]
        
        for text, expected_values in test_cases:
            print(f"\nTesting: {text}")
            self.parse_and_get_first(text, expected_values)

    #-----------------------------------------
    # 12. 错误处理测试
    #-----------------------------------------
    def test_12_error_handling(self):
        """错误处理测试"""
        print("\n=== 测试错误处理 ===")
        
        def verify_error(text):
            """验证是否产生预期错误"""
            try:
                self.parse_and_get_first(text, {
                    "register_object": None,
                    "register_template": None,
                    "generate_object": None
                })
                return False
            except Exception:
                return True
        
        error_cases = [
            # 语法错误
            "Invalid IS",  # 缺少值
            "IS 100",     # 缺少标识符
            "Obj IS TObject(,)",  # 无效的参数列表
            
            # 类型错误
            "Typed:int IS 'string'",  # 类型不匹配
            "Vec:float2 IS [1,2,3]",  # 向量维度错误
            
            # 引用错误
            "Ref IS ~/invalid/path",  # 无效路径
            "Arr IS ~/array/data[10]", # 数组越界
            
            # 模板错误
            """
            template Invalid[T] is TBase(
                value = <S>  # 未定义的参数
            )
            """,
            
            # 对象错误
            """
            Obj IS TObject(
                unknown = 100  # 未知属性
            )
            """
        ]
        
        for text in error_cases:
            print(f"\nTesting error case: {text}")
            self.assertTrue(verify_error(text))

if __name__ == '__main__':
    unittest.main(verbosity=2)