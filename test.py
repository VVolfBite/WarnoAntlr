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

    def parse_and_get_first(self, text: str, mode="default") -> Any:
        """解析文本并返回第一个赋值结果"""
        parser = self.parse_text(text)
        tree = parser.ndf_file()
        
        generator = Generator(parser, reference=self.reference, mode=mode)
        walker = ParseTreeWalker()
        walker.walk(generator, tree)
        
        return generator.assignments[0] if generator.assignments else None

    #-----------------------------------------
    # 1. 基本文件结构测试
    #-----------------------------------------
    def test_1_file_structure(self):
        """测试文件结构"""
        print("\n=== 测试文件结构 ===")
        
        # 1.1 空文件
        node = self.parse_and_get_first("")
        self.assertIsNone(node)
        
        # 1.2 单个赋值
        node = self.parse_and_get_first("Test IS 100")
        self.assertIsNotNone(node)
        
        # 1.3 多个赋值
        text = """
            Val1 IS 100
            Val2 IS 200
            Val3 IS 300
        """
        parser = self.parse_text(text)
        tree = parser.ndf_file()
        generator = Generator(parser)
        walker = ParseTreeWalker()
        walker.walk(generator, tree)
        self.assertEqual(len(generator.assignments), 3)

    #-----------------------------------------
    # 2. 赋值语句类型测试
    #-----------------------------------------
    def test_2_assignment_types(self):
        """测试赋值语句类型"""
        print("\n=== 测试赋值语句类型 ===")
        
        # 2.1 普通赋值
        tests = [
            # 基本赋值
            "Val1 IS 100",
            # 带修饰符
            "export Val2 IS 200",
            "private Val3 IS 300",
            # 带类型标注
            "Val4:int IS 400",
            # 数组访问
            "Array[0] IS 500"
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)
            
        # 2.2 成员赋值
        tests = [
            # 基本成员
            "member = 100",
            # 嵌套成员
            "obj.member = 200",
            # 数组成员
            "array[0] = 300",
            "obj.array[0] = 400"
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)
            self.assertTrue(node.is_member)
            
        # 2.3 未命名赋值
        node = self.parse_and_get_first("UNNAMED ~/test/path")
        self.assertIsNotNone(node)
        self.assertTrue(node.is_unnamed)
        
        # 2.4 模板赋值
        text = """
            template MyTemplate[
                T: int = 1,
                S: string = "test"
            ] is TBaseObject(
                value = <T>,
                name = <S>
            )
        """
        node = self.parse_and_get_first(text, mode="register_template")
        self.assertIsNotNone(node)
        self.assertTrue(node.is_template)

    #-----------------------------------------
    # 3. 类型系统测试
    #-----------------------------------------
    def test_3_type_system(self):
        """测试类型系统"""
        print("\n=== 测试类型系统 ===")
        
        # 3.1 内置类型
        tests = [
            ("Val1:bool IS True", NodeType.Boolean),
            ("Val2:string IS 'test'", NodeType.String),
            ("Val3:int IS 100", NodeType.Integer),
            ("Val4:float IS 3.14", NodeType.Float)
        ]
        for text, type_ in tests:
            node = self.parse_and_get_first(text)
            self.assertEqual(node.content.nodetype, type_)
            
        # 3.2 复合类型
        tests = [
            # 键值对
            """Val1:pair<string,int> IS ("key", 100)""",
            # 列表
            """Val2:list<int> IS [1, 2, 3]""",
            # 映射
            """Val3:map<string,int> IS MAP[("k1",1), ("k2",2)]"""
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)
            
        # 3.3 特殊类型
        tests = [
            "Vec2:float2 IS float2[1.0, 2.0]",
            "Vec3:float3 IS float3[1.0, 2.0, 3.0]",
            "Color:rgba IS RGBA[255, 0, 0, 255]"
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)

    #-----------------------------------------
    # 4. 值系统测试
    #-----------------------------------------
    def test_4_value_system(self):
        """测试值系统"""
        print("\n=== 测试值系统 ===")
        
        # 4.1 基本值
        tests = [
            # 布尔值
            ("Bool1 IS True", True),
            ("Bool2 IS False", False),
            # 空值
            ("Nil1 IS nil", None),
            # 字符串
            ("Str1 IS 'single'", "single"),
            ("Str2 IS \"double\"", "double"),
            # 整数
            ("Int1 IS 100", 100),
            ("Int2 IS -50", -50),
            ("Int3 IS 0xFF", 255),
            # 浮点数
            ("Float1 IS 3.14", 3.14),
            ("Float2 IS -2.718", -2.718),
            ("Float3 IS 1.23e-4", 0.000123),
            # GUID
            ("Guid1 IS GUID:{123-456}", "GUID:{123-456}")
        ]
        for text, expected in tests:
            node = self.parse_and_get_first(text)
            self.assertEqual(node.content.value, expected)
            
        # 4.2 数据结构
        tests = [
            # 空结构
            "Empty1 IS []",
            "Empty2 IS MAP[]",
            # 简单结构
            "List1 IS [1, 2, 3]",
            "Map1 IS MAP[('a',1), ('b',2)]",
            # 嵌套结构
            "Nested1 IS [1, [2, 3], [4, [5, 6]]]",
            "Nested2 IS MAP[('a',[1,2]), ('b',MAP[('x',3)])]"
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)

    #-----------------------------------------
    # 5. 引用系统测试
    #-----------------------------------------
    def test_5_reference_system(self):
        """测试引用系统"""
        print("\n=== 测试引用系统 ===")
        
        # 5.1 基本路径
        tests = [
            # 相对路径
            "Ref1 IS ~/test/path",
            # 系统路径
            "Ref2 IS $/system/value",
            # 成员访问
            "Ref3 IS ~/obj/member/value",
            # 数组访问
            "Ref4 IS ~/array/data[2]"
        ]
        for text in tests:
            node = self.parse_and_get_first(text, mode="generate_object")
            self.assertIsNotNone(node)
            
        # 5.2 多重引用
        node = self.parse_and_get_first(
            "Ref5 IS ~/test/path | ~/system/value", 
            mode="generate_object"
        )
        self.assertEqual(node.content.value, 100)

    #-----------------------------------------
    # 6. 算术系统测试
    #-----------------------------------------
    def test_6_arithmetic_system(self):
        """测试算术系统"""
        print("\n=== 测试算术系统 ===")
        
        tests = [
            # 基本运算
            "Math1 IS 1 + 2",
            "Math2 IS 10 - 5",
            "Math3 IS 3 * 4", 
            "Math4 IS 15 div 3",
            # 复合运算
            "Math5 IS (1 + 2) * 3",
            "Math6 IS -5 + 10",
            "Math7 IS (10 + 5 * 2) div 4",
            # 引用运算
            "Math8 IS ~/test/path + 50",
            "Math9 IS ~/test/path div 2"
        ]
        for text in tests:
            node = self.parse_and_get_first(text, mode="generate_object")
            self.assertIsNotNone(node)

    #-----------------------------------------
    # 7. 对象系统深入测试
    #-----------------------------------------
    def test_7_object_system(self):
        """测试对象系统"""
        print("\n=== 测试对象系统 ===")
        
        # 7.1 基本对象
        tests = [
            # 简单对象
            """
            Obj1 IS TBaseObject(
                name = "test",
                value = 100
            )
            """,
            # 带数组的对象
            """
            Obj2 IS TArrayObject(
                values = [1, 2, 3],
                size = 3
            )
            """,
            # 带嵌套对象
            """
            Obj3 IS TParentObject(
                child = TChildObject(
                    name = "child",
                    value = 200
                ),
                count = 1
            )
            """
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)
            
        # 7.2 对象成员访问
        tests = [
            # 直接成员
            """
            obj.name = "new name"
            """,
            # 嵌套成员
            """
            obj.child.value = 300
            """,
            # 数组成员
            """
            obj.values[0] = 100
            """,
            # 复合访问
            """
            obj.children[0].name = "child 1"
            """
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)
            self.assertTrue(node.is_member)

    #-----------------------------------------
    # 8. 模板系统深入测试
    #-----------------------------------------
    def test_8_template_system(self):
        """测试模板系统"""
        print("\n=== 测试模板系统 ===")
        
        # 8.1 基本模板
        tests = [
            # 单参数模板
            """
            template Single[T: int = 1] is TBase(
                value = <T>
            )
            """,
            # 多参数模板
            """
            template Multi[
                T: int = 1,
                S: string = "test",
                L: list<int> = [1,2,3]
            ] is TComplex(
                id = <T>,
                name = <S>,
                data = <L>
            )
            """,
            # 嵌套泛型
            """
            template Nested[
                M: map<string, list<int>> = MAP[]
            ] is TContainer(
                data = <M>
            )
            """
        ]
        for text in tests:
            node = self.parse_and_get_first(text, mode="register_template")
            self.assertTrue(node.is_template)
            
        # 8.2 模板特化
        tests = [
            # 类型特化
            """
            template TypeSpec<int> is TNumberContainer(
                type = "integer"
            )
            """,
            # 值特化
            """
            template ValueSpec<100> is TSizedContainer(
                capacity = 100
            )
            """,
            # 表达式特化
            """
            template ExprSpec<1 + 2 * 3> is TCalculated(
                result = 7
            )
            """
        ]
        for text in tests:
            node = self.parse_and_get_first(text, mode="register_template")
            self.assertTrue(node.is_template)

    #-----------------------------------------
    # 9. 边界情况测试
    #-----------------------------------------
    def test_9_edge_cases(self):
        """测试边界情况"""
        print("\n=== 测试边界情况 ===")
        
        # 9.1 空值和特殊字符
        tests = [
            # 空字符串
            'EmptyStr IS ""',
            # 特殊字符串
            r'SpecialStr IS "Hello\nWorld\t!"',
            # Unicode字符串
            'UnicodeStr IS "你好世界"',
            # 转义字符
            r'EscapeStr IS "\"quoted\""'
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)
            
        # 9.2 数值边界
        tests = [
            # 大整数
            "BigInt IS 999999999",
            # 小数精度
            "SmallFloat IS 0.0000001",
            # 科学计数
            "SciFloat IS 1.23e-10",
            # 16进制边界
            "BigHex IS 0xFFFFFFFF"
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)
            
        # 9.3 复杂嵌套
        tests = [
            # 深度嵌套列表
            "DeepList IS [1,[2,[3,[4,[5]]]]]",
            # 复杂对象嵌套
            """
            DeepObj IS TParent(
                child1 = TChild(
                    data = TData(
                        values = [
                            TValue(x=1),
                            TValue(x=2)
                        ]
                    )
                )
            )
            """,
            # 混合嵌套
            """
            Mixed IS MAP[
                ("key1", [1, (2, [3, 4])]),
                ("key2", TObj(
                    val = MAP[("x", 1)]
                ))
            ]
            """
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)

    #-----------------------------------------
    # 10. 类型转换测试
    #-----------------------------------------
    def test_10_type_conversion(self):
        """测试类型转换"""
        print("\n=== 测试类型转换 ===")
        
        tests = [
            # 数值转换
            "Int1 IS float(100)",
            "Float1 IS int(3.14)",
            # 向量转换
            "Vec1 IS float2([1, 2])",
            "Vec2 IS float3([1.0, 2.0, 3.0])",
            # 列表转换
            "List1 IS list<int>([1, 2, 3])",
            "List2 IS list<float>([1.5, 2.5])",
            # 映射转换
            """Map1 IS map<string,int>([
                ("a", 1),
                ("b", 2)
            ])""",
            # 复杂转换
            """Map2 IS map<string,list<int>>([
                ("x", [1, 2]),
                ("y", [3, 4])
            ])"""
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)

    #-----------------------------------------
    # 11. 复杂表达式测试
    #-----------------------------------------
    def test_11_complex_expressions(self):
        """测试复杂表达式"""
        print("\n=== 测试复杂表达式 ===")
        
        tests = [
            # 条件表达式
            """
            Result1 IS TCondition(
                test = True,
                then = 100,
                else = 200
            )
            """,
            # 函数调用
            """
            Result2 IS TFunction(
                name = "test",
                args = [1, 2, 3],
                kwargs = MAP[
                    ("x", 10),
                    ("y", 20)
                ]
            )
            """,
            # 路径组合
            """
            Path1 IS TPathCombine(
                base = ~/base/path,
                sub = "sub/path",
                result = ~/base/path/sub/path
            )
            """,
            # 复杂算术
            "Math1 IS (1 + 2 * 3) div (4 - 2) * -5",
            # 引用计算
            "Ref1 IS (~/value1 + ~/value2) * ~/value3"
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)

    #-----------------------------------------
    # 12. 注释和文档测试
    #-----------------------------------------
    def test_12_comments_and_docs(self):
        """测试注释和文档"""
        print("\n=== 测试注释和文档 ===")
        
        tests = [
            # 单行注释
            """
            // 这是单行注释
            Value1 IS 100
            """,
            # 多行注释
            """
            /* 这是多行注释
               第二行
               第三行 */
            Value2 IS 200
            """,
            # 混合注释
            """
            // 注释1
            Value3 IS 300 // 行尾注释
            /* 块注释 */
            Value4 IS 400
            """,
            # 嵌套注释
            """
            /* 外层注释
               /* 内层注释 */
               继续外层 */
            Value5 IS 500
            """
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)

    #-----------------------------------------
    # 13. 错误处理测试
    #-----------------------------------------
    def test_13_error_handling(self):
        """测试错误处理"""
        print("\n=== 测试错误处理 ===")
        
        def verify_error(text):
            """验证解析是否产生错误"""
            try:
                node = self.parse_and_get_first(text)
                return False
            except Exception:
                return True
        
        error_tests = [
            # 语法错误
            "Val1 IS",  # 缺少值
            "IS 100",   # 缺少标识符
            "Val2 = 100",  # 错误的赋值符号
            
            # 类型错误
            "Val3:int IS 'string'",  # 类型不匹配
            "Val4:float IS True",    # 类型不匹配
            
            # 引用错误
            "Val5 IS ~/non/exist/path",  # 不存在的路径
            "Val6 IS $/invalid/path",    # 无效的系统路径
            
            # 数组索引错误
            "Val7 IS array[-1]",     # 负索引
            "Val8 IS array[9999]",   # 越界索引
            
            # 模板错误
            """template Invalid[] is TBase(
                value = <Missing>  // 未定义的参数
            )""",
            
            # 对象错误
            """Obj1 IS TObject(
                unknown = 100  // 未知属性
            )""",
            
            # 算术错误
            "Val9 IS 1 div 0",  # 除零错误
            "Val10 IS 'str' + 100"  # 类型不匹配
        ]
        
        for text in error_tests:
            self.assertTrue(verify_error(text))

    #-----------------------------------------
    # 14. 性能边界测试
    #-----------------------------------------
    def test_14_performance_boundaries(self):
        """测试性能边界"""
        print("\n=== 测试性能边界 ===")
        
        # 14.1 大型数据结构
        large_list = ",".join(str(i) for i in range(1000))
        large_map = ",".join(f'("{i}",{i})' for i in range(1000))
        
        tests = [
            # 大列表
            f"LargeList IS [{large_list}]",
            # 大映射
            f"LargeMap IS MAP[{large_map}]",
            # 深度嵌套
            "DeepNest IS " + "["*100 + "1" + "]"*100,
            # 长标识符
            f"{'Very'*100}LongName IS 100",
            # 复杂表达式
            "ComplexExpr IS " + " + ".join(str(i) for i in range(100))
        ]
        
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)

    #-----------------------------------------
    # 15. 特殊语法特性测试
    #-----------------------------------------
    def test_15_special_features(self):
        """测试特殊语法特性"""
        print("\n=== 测试特殊语法特性 ===")
        
        tests = [
            # 末尾逗号
            """
            List1 IS [
                1,
                2,
                3,  // 允许末尾逗号
            ]
            """,
            # 空行和缩进
            """
            
            Obj1 IS TObject(
                
                value1 = 100,
                
                value2 = 200,
                
            )
            
            """,
            # 特殊字符
            """
            SpecialChars IS MAP[
                ("tab\t", 1),
                ("newline\n", 2),
                ("quote\"", 3),
                ("unicode\u0001", 4)
            ]
            """,
            # 混合换行符
            "Line1 IS 100\nLine2 IS 200\rLine3 IS 300\r\n",
            # 二进制数据
            "Binary IS GUID:{00-00-FF-FF}"
        ]
        for text in tests:
            node = self.parse_and_get_first(text)
            self.assertIsNotNone(node)

if __name__ == '__main__':
    unittest.main(verbosity=2)