from antlr4 import *
from numpy import isin
from src.parsers.parser.NdfGrammarListener import NdfGrammarListener
from src.parsers.parser.NdfGrammarParser import NdfGrammarParser

from src.parsers.syntax_tree.nodes.syntax_node_assignment import *
from src.parsers.syntax_tree.nodes.syntax_node_collection import *

import logging

import pickle
import sys
import config

WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)
import src.extractor.base_class
import src.extractor.extract_class
import src.extractor.refined_class

# 此文件实际充当了语义指导的功能，以堆栈的形式实现了规约和递进时的语义逻辑
DISABLE_CALCULATING = False


# Stack类模拟语法栈
class Stack:
    def __init__(self):
        self._stack = []

    def push(self, elem):
        self._stack.append(elem)

    def pop(self):
        return self._stack.pop()

    # 不弹出顶端部件
    def top(self):
        if len(self._stack) > 0:
            return self._stack[len(self._stack) - 1]
        else:
            return None

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        "".join(map(str, self._stack))


# 一个Marker，标识某个结构的结束
class StackMarker:
    pass


class Generator(NdfGrammarListener):

    # RuleName其实没用，Generator的任务是解析一个Ndf文件并将其中的所有结构以Assignment的形式记录，其以Stack完成语法语义动作
    # Ignore标识在某个结构下应当进行何种忽视动作，比如路径引用/计算过程中其实不应该出现赋值、对象创建等过程
    # ClassRegister是我新加的，用于提取类似类结构的类名和成员名，以便以后直接制作Python类进行数据处理，这里的关键是Ndf中一个类并非所有的成员都会一次出现，因此需要多次提取，需要支持类的存储，更新扩展
    def __init__(
        self,
        parser: NdfGrammarParser,
        name_space="/",
        reference_dict={},
        mode="default",
    ):
        super().__init__()
        self.rule_names = parser.ruleNames
        self.assignments = []
        # 推入Stack，此时堆栈为 Bottom ->
        self.stack = Stack()
        self.ignore = 0
        self.name_space = name_space
        self.reference_dict = reference_dict
        self.mode = mode
        self.generator = {}
        self.register = {}

    def register_object(self, name, attributes, base_name=None, base_attributes=None):
        if name not in self.register:
            self.register[name] = {
                "attributes": attributes,
                "base": (
                    {"name": base_name, "attributes": base_attributes}
                    if base_name
                    else None
                ),
            }
        else:
            entry = self.register[name]

            # 更新当前类的属性
            for attr, value in attributes.items():
                if attr not in entry["attributes"] or value is not None:
                    entry["attributes"][attr] = value

            # 更新父类信息
            if base_name:
                if not entry.get("base") or entry["base"]["name"] != base_name:
                    entry["base"] = {"name": base_name, "attributes": base_attributes}
                else:
                    for attr, value in base_attributes.items():
                        if attr not in entry["base"]["attributes"] or value is not None:
                            entry["base"]["attributes"][attr] = value

    def generate_object(self, name, value):
        if name not in self.generator:
            self.generator[name] = value

    def instantiate_class(self, class_name, **kwargs):
        get_class = lambda name: getattr(
            src.extractor.refined_class, name, None
        ) or getattr(src.extractor.extract_class, name, None)
        class_ = get_class(class_name)
        return class_(**kwargs) if class_ is not None else None

    def enterNormal_assignment(self, ctx: NdfGrammarParser.Normal_assignmentContext):
        if self.ignore > 0:
            return
        # 推入Assignment，此时堆栈为 Top | Assignment ->
        self.stack.push(Assignment())

    def exitNormal_assignment(self, ctx: NdfGrammarParser.Normal_assignmentContext):
        if self.ignore > 0:
            return

        # 弹出 Assignment 的 Value，此时堆栈结构：Top(Assignment) | Value
        value = self.stack.pop()
        assignment = self.stack.top()
        assignment.value = value.python_value

        if self.mode in {"generate_object", "register_template"}:
            assignment.python_value = value.python_value
            assignment.python_value.KeyName = assignment.id

        # 弹出 Assignment，此时堆栈结构：Bottom | Top(Assignment)
        if len(self.stack) == 1:
            assignment = self.stack.pop()

            if self.mode in {"generate_object"}:
                self.generate_object(assignment.id, assignment.python_value)
            # 也许下边没用了
            self.assignments.append(assignment)

    def enterMember_assignment(self, ctx: NdfGrammarParser.Member_assignmentContext):
        if self.ignore > 0:
            return
        assignment = Assignment()
        assignment.is_member = True
        # 推入一个Assignment，此时堆栈为 Top | Assignment  ->
        self.stack.push(assignment)

    def exitMember_assignment(self, ctx: NdfGrammarParser.Member_assignmentContext):
        if self.ignore > 0:
            return
        # 弹出一个Assignment值表，此时堆栈为 Top | Assignment | Value(Entity / Assignment) <-
        value = self.stack.pop()
        assignment = self.stack.top()
        assignment.value = value
        if self.mode in {"generate_object", "register_template"}:
            assignment.python_value = value.python_value

    def enterUnnamed_assignment(self, ctx: NdfGrammarParser.Unnamed_assignmentContext):
        if self.ignore > 0:
            return
        assignment = Assignment()
        assignment.is_unnamed = True
        # 推入一个Assignment，此时堆栈为 Top | Assignment  ->
        self.stack.push(assignment)

    def exitUnnamed_assignment(self, ctx: NdfGrammarParser.Unnamed_assignmentContext):
        if self.ignore > 0:
            return
        # 弹出一个Assignment值表，此时堆栈为 Top | Assignment | Value(Entity / Assignment) <-
        value = self.stack.pop()
        assignment = self.stack.top()
        assignment.value = value
        assignment.id = "Unnamed-" + str(hash(str(value)))
        if self.mode in {"generate_object", "register_template"}:
            assignment.python_value = value.python_value
        # 弹出一个Assignment，此时堆栈为 Bottom | Assignment <-
        if len(self.stack) == 1:
            assignment = self.stack.pop()
            self.assignments.append(assignment)
            if self.mode in {"generate_object", "register_template"}:
                self.generate_object(assignment.id, assignment.python_value)

    # Enter a parse tree produced by NdfGrammarParser#template_assignment.
    def enterTemplate_assignment(
        self, ctx: NdfGrammarParser.Template_assignmentContext
    ):
        if self.ignore > 0:
            return
        assignment = Assignment()
        assignment.is_template = True
        # 推入一个Assignment，此时堆栈为 Top | Assignment  ->
        self.stack.push(assignment)

    # Exit a parse tree produced by NdfGrammarParser#template_assignment.
    def exitTemplate_assignment(self, ctx: NdfGrammarParser.Template_assignmentContext):
        if self.ignore > 0:
            return

        # 弹出 Assignment 的 Value 和 Vector，此时堆栈结构：Top(Assignment) | VECTOR | Value
        value = self.stack.pop()
        vector = self.stack.pop()
        assignment = self.stack.top()

        assignment.value = value

        if self.mode in {"generate_object", "register_template"}:
            assignment.python_value = value.python_value
            class_name = value.object_type
            class_attrs = {
                attr: None
                for attr in dir(value.python_value)
                if not callable(getattr(value.python_value, attr))
                and not attr.startswith("__")
            }
            self.register_object(class_name=class_name, class_attrs=class_attrs)

        if self.mode == "register_template":
            class_name = assignment.id
            class_attrs = {
                val.id if isinstance(val, Assignment) else val.python_value: (
                    val.python_value if isinstance(val, Assignment) else None
                )
                for val in vector.value
            }
            base_class_name = value.object_type
            base_class_attrs = {
                attr: (
                    getattr(value.python_value, attr).reverse()
                    if isinstance(
                        getattr(value.python_value, attr),
                        src.extractor.base_class.BaseDescription,
                    )
                    else getattr(value.python_value, attr)
                )
                for attr in dir(value.python_value)
                if not callable(getattr(value.python_value, attr))
                and not attr.startswith("__")
            }

            self.register_object(
                class_name=class_name,
                class_attrs=class_attrs,
                base_class_name=base_class_name,
                base_class_attrs=base_class_attrs,
            )

        # 弹出 Assignment，此时堆栈结构：Bottom | Top(Assignment)
        if len(self.stack) == 1:
            assignment = self.stack.pop()
            self.assignments.append(assignment)

    def enterArithmetic(self, ctx: NdfGrammarParser.ArithmeticContext):
        if self.ignore > 0:
            return
        # 如果没有进入Arithmetic而是只是一个值，那么不要进行任何处理
        if len(ctx.children) <= 1 and self.ignore <= 0:
            return

        arithmetic = Base()
        arithmetic.nodetype = NodeType.Arithmetic
        text = ctx.getText()
        text = text.replace("+", " + ")
        text = text.replace("-", " - ")
        text = text.replace("*", " * ")
        text = text.replace("div", " div ")
        text = text.replace("DIV", " div ")
        # 推入一个Entity，此时堆栈为 Top | Entity(Arithmetic)  ->
        self.stack.push(arithmetic)

    def exitArithmetic(self, ctx: NdfGrammarParser.ArithmeticContext):
        if self.ignore > 0:
            return
        # 单值直接返回即可
        if ctx.getChildCount() == 1:
            return
        # 单目运算形式 即 -Op1形式，转为负数并返回
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "-":
            # 弹出操作数Op1，此时堆栈为 Top | Entity(Arithmetic) | '-'  Op1 <-
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.value = -op1.value
            return
        # 双目运算的括号形式，即(Op1),什么都不做直接返回
        elif (
            ctx.getChildCount() == 3
            and ctx.getChild(0).getText() == "("
            and ctx.getChild(2).getText() == ")"
        ):
            # 弹出操作数Op1，此时堆栈为 Top | Entity(Arithmetic) | '('  Op1 ')' <-
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.value = op1.value
            return
        # 正常双目运算形式
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "+":
            # 弹出操作数Op1，此时堆栈为 Top | Entity(Arithmetic) | Op1 '+' | Op2 <-
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.value = op1.value + op2.value
            return
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "-":
            # 弹出操作数Op1，此时堆栈为 Top | Entity(Arithmetic) | Op1 '-' | Op2 <-
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.value = op1.value - op2.value
            return
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "*":
            # 弹出操作数Op1，此时堆栈为 Top | Entity(Arithmetic) | Op1 '*' | Op2 <-
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.value = op1.value * op2.value
            return
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText().lower() == "div":
            # 弹出操作数Op1，此时堆栈为 Top | Entity(Arithmetic) | Op1 'div' | Op2 <-
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.value = op1.value / op2.value
            return

    def enterOp(self, ctx: NdfGrammarParser.Object_typeContext):
        pass

    def enterVector_value(self, ctx: NdfGrammarParser.Vector_valueContext):
        if self.ignore > 0:
            return
        # 推入一个Vector，此时堆栈为 Top | Vector  ->
        self.stack.push(Vector())
        # 推入一个Marker，此时堆栈为 Top | Vector | Marker  ->
        self.stack.push(StackMarker())

    def exitVector_value(self, ctx: NdfGrammarParser.Vector_valueContext):
        if self.ignore > 0:
            return

        vector_values = []
        # 弹出 Vector 值，直到遇到 StackMarker
        while not isinstance(self.stack.top(), StackMarker):
            vector_values.append(self.stack.pop())

        # 还原顺序并移除 Marker
        vector_values.reverse()
        self.stack.pop()

        # 获取 Vector 并填充数据
        vector = self.stack.top()
        vector.extend(vector_values)

        # 如果模式符合，设置 python_value
        if self.mode in {"generate_object", "register_template"}:
            vector.python_value = [value.python_value for value in vector.value]

    def enterPair_value(self, ctx: NdfGrammarParser.Pair_valueContext):
        if self.ignore > 0:
            return
        # 推入一个Pair，此时堆栈为 Top | Pair  ->
        self.stack.push(Pair())
        # 推入一个Marker，此时堆栈为 Top | Pair | Marker  ->
        self.stack.push(StackMarker())

    def exitPair_value(self, ctx: NdfGrammarParser.Pair_valueContext):
        if self.ignore > 0:
            return
        pair_values = []
        # 弹出 Pair 值，直到遇到 StackMarker
        while not isinstance(self.stack.top(), StackMarker):
            pair_values.append(self.stack.pop())
        # 还原顺序并移除 Marker
        pair_values.reverse()
        self.stack.pop()
        # 获取 Pair 并填充数据
        pair = self.stack.top()
        pair.extend(pair_values)
        # 如果模式符合，构造 python_value
        if self.mode in {"generate_object", "register_template"}:
            key = (
                tuple(pair.value[0].python_value)
                if isinstance(pair.value[0].python_value, list)
                else pair.value[0].python_value
            )
            pair.python_value = {key: pair.value[1].python_value}

    def enterMap_value(self, ctx: NdfGrammarParser.Map_valueContext):
        if self.ignore > 0:
            return
        # 推入一个Map，此时堆栈为 Top | Map  ->
        self.stack.push(Map())
        # 推入一个Marker，此时堆栈为 Top | Map | Marker  ->
        self.stack.push(StackMarker())

    def exitMap_value(self, ctx: NdfGrammarParser.Map_valueContext):
        if self.ignore > 0:
            return
        map_values = []
        # 弹出Map值列表，此时堆栈为 Top | Map | Marker | MapValue0 | MapValue1 <-
        while not isinstance(self.stack.top(), StackMarker):
            map_values.append(self.stack.pop())
        # 还原顺序并移除 Marker
        map_values.reverse()
        self.stack.pop()
        # 获取 Map 并填充数据
        _map = self.stack.top()
        _map.extend(map_values)
        # 处理 python_value
        if self.mode in {"generate_object", "register_template"}:
            _map.python_value = {
                str(key.python_value): value.python_value
                for key, value in _map.map.items()
            }

    def enterObject_type(self, ctx: NdfGrammarParser.Object_typeContext):
        if self.ignore > 0:
            return
        # 推入Object，此时堆栈为 Top | Object ->
        obj = Object()
        obj.object_type = ctx.getText()
        self.stack.push(obj)
        # 推入Object，此时堆栈为 Top | Object | Marker ->
        self.stack.push(StackMarker())

    def exitObject(self, ctx: NdfGrammarParser.ObjectContext):
        if self.ignore > 0:
            return
        members = []
        # 弹出Member列表，此时堆栈为  Top | Object | Marker | Member0 | Member1 |Member2 <-
        while not isinstance(self.stack.top(), StackMarker):
            members.append(self.stack.pop())
        members.reverse()
        # 弹出Marker，此时堆栈为  Top | Object | Marker <-
        self.stack.pop()
        # 弹出object，此时堆栈为  Top | Object <-
        obj = self.stack.top()
        obj.extend(members)

        if self.mode == "register_object":
            class_name, class_attrs = obj.get_class()
            self.register_object(name=class_name, class_attrs=class_attrs)
        elif self.mode in {"generate_object", "register_template"}:
            class_name = obj.object_type
            kwargs = {val.id: val.python_value for val in obj.value}
            obj.python_value = self.instantiate_class(class_name, **kwargs)

    def enterExport_prefix(self, ctx: NdfGrammarParser.Export_prefixContext):
        if self.ignore > 0:
            return
        # 更新属性，此时的堆栈为  Top(Assignment)
        self.stack.top().is_export = True

    def enterTemplate_prefix(self, ctx: NdfGrammarParser.Template_prefixContext):
        if self.ignore > 0:
            return
        # 更新属性，此时的堆栈为  Top(Assignment)
        self.stack.top().is_template = True

    def enterPrivate_prefix(self, ctx: NdfGrammarParser.Private_prefixContext):
        if self.ignore > 0:
            return
        # 更新属性，此时的堆栈为  Top(Assignment)
        self.stack.top().is_private = True

    def enterId(self, ctx: NdfGrammarParser.IdContext):
        if self.ignore > 0:
            return
        # 更新属性，此时的堆栈为  Top(Assignment/Member ...)
        self.stack.top().id = ctx.getText()

    def enterNil_value(self, ctx: NdfGrammarParser.Nil_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.nodetype = NodeType.Nil
        entity.value = None
        if self.mode in {"generate_object", "register_template"}:
            entity.python_value = entity.value
        # 推入一个Entity，此时堆栈为 Top | Base(Nil)  ->
        self.stack.push(entity)

    def enterBool_value(self, ctx: NdfGrammarParser.Bool_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.nodetype = NodeType.Boolean
        if ctx.getText().lower() == "false":
            entity.value = False
        else:
            entity.value = True
        if self.mode in {"generate_object", "register_template"}:
            entity.python_value = entity.value
        # 推入一个Entity，此时堆栈为 Top | Base(Bool)  ->
        self.stack.push(entity)

    def enterInt_value(self, ctx: NdfGrammarParser.Int_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.nodetype = NodeType.Integer
        entity.value = int(ctx.getText())
        if self.mode in {"generate_object", "register_template"}:
            entity.python_value = int(entity.value)
        # 推入一个Entity，此时堆栈为 Top | Base(Int)  ->
        self.stack.push(entity)

    def enterString_value(self, ctx: NdfGrammarParser.String_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        value = ctx.getText()
        if value[0] == "'":
            entity.nodetype = NodeType.String_single
        else:
            entity.nodetype = NodeType.String_double
        entity.value = value
        if self.mode in {"generate_object", "register_template"}:
            entity.python_value = str(entity.value)
        # 推入一个Entity，此时堆栈为 Top | Base(String)  ->
        self.stack.push(entity)

    def enterHex_value(self, ctx: NdfGrammarParser.Hex_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.nodetype = NodeType.HexInteger
        entity.value = ctx.getText()
        if self.mode in {"generate_object", "register_template"}:
            entity.python_value = entity.value
        # 推入一个Entity，此时堆栈为 Top | Base(Hex)  ->
        self.stack.push(entity)

    def enterFloat_value(self, ctx: NdfGrammarParser.Float_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.nodetype = NodeType.Float
        entity.value = float(ctx.getText())
        if self.mode in {"generate_object", "register_template"}:
            entity.python_value = float(entity.value)
        # 推入一个Entity，此时堆栈为 Top | Base(Float)  ->
        self.stack.push(entity)

    def enterGuid_value(self, ctx: NdfGrammarParser.Guid_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.nodetype = NodeType.GUID
        entity.value = ctx.getText()
        if self.mode in {"generate_object", "register_template"}:
            entity.python_value = str(entity.value)
        # 推入一个Entity，此时堆栈为 Top | Base(GUID)  ->
        self.stack.push(entity)

    def enterRgba_value(self, ctx: NdfGrammarParser.Rgba_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.nodetype = NodeType.RGBA

        text = ctx.getText()
        text = text.replace(" ", "")
        text = text.removeprefix("RGBA[")
        text = text.removeprefix("rgba[")
        text = text.removesuffix("]")

        nums = text.split(",")
        entity.value = [int(x) for x in nums]
        if self.mode in {"generate_object", "register_template"}:
            entity.python_value = entity.value
        # 推入一个Entity，此时堆栈为 Top | Base(RGBA(List))  ->
        self.stack.push(entity)

    def enterObj_reference_value(
        self, ctx: NdfGrammarParser.Obj_reference_valueContext
    ):
        self.ignore += 1
        if self.ignore > 1:
            return
        entity = Base()
        entity.nodetype = NodeType.Reference
        entity.value = ctx.getText()

        if self.mode == "generate_object" or self.mode == "register_template":
            reference_str = str(entity.value)
            if "|" in reference_str:
                references = reference_str.split("|")
                entity.python_value = [
                    str(ref.strip().split("/")[-1] for ref in references)
                ]
            else:
                entity.python_value = str(reference_str.split("/")[-1])

        # 推入一个Entity，此时堆栈为 Top | Base(ObjReference)  ->
        self.stack.push(entity)

    def exitObj_reference_value(self, ctx: NdfGrammarParser.Obj_reference_valueContext):
        if self.ignore > 0:
            self.ignore -= 1
        # 什么都不做，由后续的赋值语句完成弹出

    # Enter a parse tree produced by NdfGrammarParser#replace_value.
    def enterReplace_value(self, ctx: NdfGrammarParser.Replace_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.nodetype = NodeType.Replacer
        entity.value = ctx.getText()
        if self.mode == "generate_object" or self.mode == "register_template":
            entity.python_value = "@" + entity.value[1:-1]
        # 推入一个Entity，此时堆栈为 Top | Base(GUID)  ->
        self.stack.push(entity)

    def exitReplace_value(self, ctx: NdfGrammarParser.Replace_valueContext):
        if self.ignore > 0:
            self.ignore -= 1
