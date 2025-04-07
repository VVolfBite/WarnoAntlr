from antlr4 import *
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

DISABLE_CALCULATING = False

#=============================================
# 1. 基础类定义
#=============================================
class Stack:
    def __init__(self):
        self._stack = []

    def push(self, elem):
        self._stack.append(elem)

    def pop(self):
        return self._stack.pop()

    def top(self):
        if len(self._stack) > 0:
            return self._stack[len(self._stack) - 1]
        else:
            return None

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        "".join(map(str, self._stack))


class StackMarker:
    pass

#=============================================
# 2. 主生成器类
#=============================================
class Generator(NdfGrammarListener):
    #-----------------------------------------
    # 2.1 初始化和工具函数
    #-----------------------------------------
    def __init__(self, parser: NdfGrammarParser, name_space="/", reference=None, mode="default"):
        super().__init__()
        self.rule_names = parser.ruleNames
        self.assignments = []
        self.stack = Stack()
        self.ignore = 0
        self.name_space = name_space
        self.reference = reference
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
            for attr, value in attributes.items():
                if attr not in entry["attributes"] or value is not None:
                    entry["attributes"][attr] = value
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

    #-----------------------------------------
    # 2.2 赋值语句处理
    #-----------------------------------------
    # 2.2.1 普通赋值
    def enterNormal_assignment(self, ctx):
        if self.ignore > 0:
            return
        self.stack.push(Assignment())

    def exitNormal_assignment(self, ctx): 
        if self.ignore > 0:
            return
            
        value = self.stack.pop()
        assignment = self.stack.top()
        
        # 设置content和value
        assignment.content = value
        if self.mode in {"generate_object", "register_template"}:
            assignment.value = value.value
            
        # 处理最终赋值
        if len(self.stack) == 1:
            assignment = self.stack.pop()
            self.assignments.append(assignment)
            if self.mode in {"generate_object"}:
                self.generate_object(assignment.id, assignment.value)
            

    # 2.2.2 成员赋值
    def enterMember_assignment(self, ctx):
        if self.ignore > 0:
            return
        assignment = Assignment()
        assignment.is_member = True
        self.stack.push(assignment)

    def exitMember_assignment(self, ctx):
        if self.ignore > 0:
            return
            
        value = self.stack.pop()
        assignment = self.stack.top()
        
        # 设置content和value
        assignment.content = value
        if self.mode in {"generate_object", "register_template"}:
            assignment.value = value.value

    # 2.2.3 匿名赋值
    def enterUnnamed_assignment(self, ctx):
        if self.ignore > 0:
            return
        assignment = Assignment()
        assignment.is_unnamed = True
        self.stack.push(assignment)

    def exitUnnamed_assignment(self, ctx):
        if self.ignore > 0:
            return
            
        value = self.stack.pop()
        assignment = self.stack.top()
        
        # 设置content、id和value
        assignment.id = "Unnamed-" + str(hash(str(value)))
        assignment.content = value
        
        if self.mode in {"generate_object", "register_template"}:
            assignment.value = value.value

        # 处理最终赋值
        if len(self.stack) == 1:
            assignment = self.stack.pop()
            self.assignments.append(assignment)
            if self.mode in {"generate_object", "register_template"}:
                self.generate_object(assignment.id, assignment.value)


    # 2.2.4 模板赋值
    def enterTemplate_assignment(self, ctx):
        if self.ignore > 0:
            return
        assignment = Assignment()
        assignment.is_template = True
        self.stack.push(assignment)

    def exitTemplate_assignment(self, ctx):
        if self.ignore > 0:
            return
            
        value = self.stack.pop()
        vector = self.stack.pop()
        assignment = self.stack.top()
        
        # 根据不同模式设置content和value
        assignment.content = value
        if self.mode in {"register_object"}:
            # 注册对象模式
            class_name = value.object_type
            class_attrs = {attr.id: None for attr in value.content}
            self.register_object(name=class_name, attributes=class_attrs)
            
        elif self.mode in {"register_template"}:
            # 注册模板模式
            class_name = assignment.id
            class_attrs = {
                val.id if isinstance(val, Assignment) else val.value: (
                    val.value if isinstance(val, Assignment) else None
                )
                for val in vector.content
            }
            base_class_name = value.object_type
            base_class_attrs = {
                attr: (
                    getattr(value.value, attr).reverse()
                    if isinstance(getattr(value.value, attr),
                        src.extractor.base_class.BaseDescription)
                    else getattr(value.value, attr)
                )
                for attr in dir(value.value)
                if not callable(getattr(value.value, attr))
                and not attr.startswith("__")
            }
            self.register_object(
                name=class_name,
                attributes=class_attrs,
                base_name=base_class_name,
                base_attributes=base_class_attrs
            )
            
        elif self.mode in {"generate_object"}:
            # 生成对象模式
            assignment.value = value.value
            
        # 处理最终赋值
        if len(self.stack) == 1:
            assignment = self.stack.pop()
            self.assignments.append(assignment)

    #-----------------------------------------
    # 2.3 前缀修饰符处理
    #-----------------------------------------
    def enterExport_prefix(self, ctx):
        if self.ignore > 0:
            return
        self.stack.top().is_export = True

    def enterTemplate_prefix(self, ctx):
        if self.ignore > 0:
            return
        self.stack.top().is_template = True

    def enterPrivate_prefix(self, ctx):
        if self.ignore > 0:
            return
        self.stack.top().is_private = True

    #-----------------------------------------
    # 2.4 标识符和算术运算处理
    #-----------------------------------------
    def enterId(self, ctx):
        if self.ignore > 0:
            return
            
        # 设置标识符
        if ctx.getChildCount() == 1:
            self.stack.top().id = ctx.getText()
        else:
            self.stack.top().id = ctx.getChild(0).getText()

    def enterArithmetic(self, ctx):
        if self.ignore > 0:
            return
            
        # 检查是否需要创建算术节点
        if len(ctx.children) <= 1 and self.ignore <= 0:
            return
            
        # 创建算术实体
        arithmetic = Base()
        arithmetic.nodetype = NodeType.Arithmetic
        
        # 格式化算术表达式文本
        text = ctx.getText()
        text = text.replace("+", " + ")
        text = text.replace("-", " - ")
        text = text.replace("*", " * ")
        text = text.replace("div", " div ")
        text = text.replace("DIV", " div ")
        
        arithmetic.content = text
        self.stack.push(arithmetic)

    def exitArithmetic(self, ctx):
        if self.ignore > 0:
            return
            
        # 单一值,不需要处理
        if ctx.getChildCount() == 1:
            return
            
        # 处理负数
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "-":
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.content = -op1.content
            arithmetic.value = -op1.value
            return
            
        # 处理括号表达式
        elif (ctx.getChildCount() == 3 
              and ctx.getChild(0).getText() == "(" 
              and ctx.getChild(2).getText() == ")"):
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.content = op1.content
            arithmetic.value = op1.value
            return
            
        # 处理加法
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "+":
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.content = op1.content + op2.content
            arithmetic.value = op1.value + op2.value
            return
            
        # 处理减法
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "-":
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.content = op1.content - op2.content
            arithmetic.value = op1.value - op2.value
            return
            
        # 处理乘法
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "*":
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.content = op1.content * op2.content
            arithmetic.value = op1.value * op2.value
            return
            
        # 处理除法
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText().lower() == "div":
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.content = op1.content / op2.content
            arithmetic.value = op1.value / op2.value
            return

    def enterOp(self, ctx):
        # 操作符处理在exitArithmetic中完成
        pass

    #-----------------------------------------
    # 2.5 基本类型值处理
    #-----------------------------------------
    def enterNil_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.Nil
        entity.content = None
        
        if self.mode in {"generate_object", "register_template", "register_object"}:
            entity.value = None
            
        self.stack.push(entity)

    def enterBool_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.Boolean
        entity.content = True if ctx.getText().lower() == "true" else False
        
        if self.mode in {"generate_object", "register_template"}:
            entity.value = True if ctx.getText().lower() == "true" else False
            
        self.stack.push(entity)

    def enterInt_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.Integer
        entity.content = int(ctx.getText())
        
        if self.mode in {"generate_object", "register_template"}:
            entity.value = int(ctx.getText())
            
        self.stack.push(entity)

    def enterFloat_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.Float
        entity.content = float(ctx.getText())
        
        if self.mode in {"generate_object", "register_template", "register_object"}:
            entity.value = float(ctx.getText())
            
        self.stack.push(entity)

    def enterString_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.String_single if ctx.getText()[0] == "'" else NodeType.String_double
        entity.content = str(ctx.getText())
        
        if self.mode in {"register_template", "generate_object"}:
            entity.value = str(ctx.getText())
            
        self.stack.push(entity)

    def enterHex_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.HexInteger
        entity.content = ctx.getText()
        
        if self.mode in {"generate_object", "register_template"}:
            entity.value = ctx.getText()
            
        self.stack.push(entity)

    def enterGuid_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.GUID
        entity.content = ctx.getText()
        
        if self.mode in {"generate_object", "register_template", "register_object"}:
            entity.value = str(ctx.getText())
            
        self.stack.push(entity)

    def enterRgba_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.RGBA
        text = ctx.getText().replace(" ", "").removeprefix("RGBA[").removeprefix("rgba[").removesuffix("]")
        entity.content = [int(x) for x in text.split(",")]
        
        if self.mode in {"generate_object", "register_template", "register_object"}:
            entity.value = [int(x) for x in text.split(",")]
            
        self.stack.push(entity)

    #-----------------------------------------
    # 2.6 复合类型值处理
    #-----------------------------------------
    # 2.6.1 向量处理
    def enterVector_value(self, ctx):
        if self.ignore > 0:
            return
        self.stack.push(Vector())
        self.stack.push(StackMarker())

    def exitVector_value(self, ctx):
        if self.ignore > 0:
            return
            
        # 收集向量值
        vector_values = []
        while type(self.stack.top()) != StackMarker:
            vector_values.append(self.stack.pop())
        vector_values.reverse()
        self.stack.pop()
        
        # 获取向量对象
        vector = self.stack.top()
        
        # 设置content和value
        for vector_value in vector_values:
            vector.append(vector_value)
            
        if self.mode in {"generate_object", "register_template"}:
            vector.value = [value.value for value in  vector_values]

    # 2.6.2 键值对处理
    def enterPair_value(self, ctx):
        if self.ignore > 0:
            return
        self.stack.push(Pair())
        self.stack.push(StackMarker())

    def exitPair_value(self, ctx):
        if self.ignore > 0:
            return
            
        # 收集键值对
        pair_values = []
        while type(self.stack.top()) != StackMarker:
            pair_values.append(self.stack.pop())
        pair_values.reverse()
        self.stack.pop()
        
        # 获取键值对对象
        pair = self.stack.top()
        
        # 设置content和value
        for pair_value in pair_values:
            pair.append(pair_value)
            
        if self.mode in {"generate_object", "register_template"}:
            key = (
                tuple(pair_values[0].value)
                if isinstance((pair_values[0].value), list)
                else pair_values[0].value
            )
            value = pair_values[1].value
            pair.value = {key: value}

    # 2.6.3 映射处理
    def enterMap_value(self, ctx):
        if self.ignore > 0:
            return
        self.stack.push(Map())
        self.stack.push(StackMarker())

    def exitMap_value(self, ctx):
        if self.ignore > 0:
            return
            
        # 收集映射值
        map_values = []
        while type(self.stack.top()) != StackMarker:
            map_values.append(self.stack.pop())
        map_values.reverse()
        self.stack.pop()
        
        # 获取映射对象
        _map = self.stack.top()
        
        # 设置content和value
        for map_value in map_values:
            _map.append(map_value)
            
        if self.mode in {"generate_object", "register_template"}:
            _map.value = {str(key): value.value for key, value in _map.map.items()}

    # 2.6.4 对象处理
    def enterObject_type(self, ctx):
        if self.ignore > 0:
            return
        obj = Object()
        obj.object_type = ctx.getText()
        self.stack.push(obj)
        self.stack.push(StackMarker())

    def exitObject(self, ctx):
        if self.ignore > 0:
            return
            
        # 收集成员值
        members = []
        while type(self.stack.top()) != StackMarker:
            member = self.stack.pop()
            members.append(member)
        members.reverse()
        self.stack.pop()
        
        # 获取对象
        obj = self.stack.top()
        
        # 设置content
        for member in members:
            obj.append(member)
            
        # 设置value
        if self.mode in {"generate_object", "register_template"}:
            class_name = obj.object_type
            kwargs = {val.id: val.value for val in obj.content}
            obj.value = self.instantiate_class(class_name, **kwargs)
            
        elif self.mode in {"register_object"}:
            class_name, class_attrs = obj.get_class()
            self.register_object(name=class_name, attributes=class_attrs)

    #-----------------------------------------
    # 2.7 引用和替换值处理
    #-----------------------------------------
    def enterObj_reference_value(self, ctx):
        self.ignore += 1
        if self.ignore > 1:
            return
            
        # 创建引用实体
        entity = Base()
        entity.nodetype = NodeType.Reference
        reference_str = str(ctx.getText())
        
        # 设置content和value
        entity.content = reference_str
        
        if (self.mode in {"generate_object", "register_template"} 
            and self.reference is not None):
            # 处理引用字符串,支持单引用和多引用(用|分隔)
            entity.value = (
                [str(ref.strip().split("/")[-1]) for ref in reference_str.split("|")]
                if "|" in reference_str
                else str(reference_str.split("/")[-1])
            )

        self.stack.push(entity)

    def exitObj_reference_value(self, ctx):
        if self.ignore > 0:
            self.ignore -= 1

    def enterReplace_value(self, ctx):
        if self.ignore > 0:
            return
            
        # 创建替换实体
        entity = Base()
        entity.nodetype = NodeType.Replacer

        # 设置content和value        
        entity.content = ctx.getText()
        if self.mode in {"generate_object", "register_template", "register_object"}:
            entity.value = "@" + ctx.getText()[1:-1]  # 移除首尾的@符号
            
            
        self.stack.push(entity)

    def exitReplace_value(self, ctx):
        if self.ignore > 0:
            self.ignore -= 1
