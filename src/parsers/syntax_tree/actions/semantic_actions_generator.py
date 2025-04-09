from antlr4 import *
from typing import Any  # 添加这行
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
import src.extractor.test_class


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
        return "".join(map(str, self._stack))


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
        """注册一个对象类型
        
        Args:
            name: 类型名称
            attributes: 属性字典 {属性名: 属性值}
            base_name: 基类名称(可选)
            base_attributes: 基类属性字典(可选) {属性名: 属性值}
        """
        if name not in self.register:
            # 新类型注册
            self.register[name] = {
                "attributes": attributes,
                "base": {
                    "name": base_name, 
                    "attributes": base_attributes
                } if base_name else None
            }
        else:
            # 更新已有类型
            entry = self.register[name]
            # 更新属性
            for attr, value in attributes.items():
                if attr not in entry["attributes"] or value is not None:
                    entry["attributes"][attr] = value
            # 更新基类信息
            if base_name:
                if not entry.get("base") or entry["base"]["name"] != base_name:
                    entry["base"] = {"name": base_name, "attributes": base_attributes}
                else:
                    for attr, value in base_attributes.items():
                        if attr not in entry["base"]["attributes"] or value is not None:
                            entry["base"]["attributes"][attr] = value

    def generate_object(self, name, value):
        """根据类型生成对象实例
        
        Args:
            name: 类型名称
            value: 初始值
        """
        if DISABLE_CALCULATING:
            return
            
        if name not in self.generator:
            self.generator[name] = value
        else:
            current = self.generator[name]
            if isinstance(current, list):
                current.append(value)
            else:
                self.generator[name] = [current, value]

    def instantiate_class(self, class_name, **kwargs):
        get_class = lambda name: getattr(
            src.extractor.test_class, name, None
        ) or getattr(src.extractor.extract_class, name, None)
        class_ = get_class(class_name)
        return class_(**kwargs) if class_ is not None else None

    #-----------------------------------------
    # 2.2 赋值语句处理优化
    #-----------------------------------------
    def enterNormal_assignment(self, ctx):
        if self.ignore > 0:
            return
        self.stack.push(Assignment())

    def exitNormal_assignment(self, ctx): 
        """处理普通赋值语句的完成
        MyVar IS 100
        """
        if self.ignore > 0:
            return
            
        value = self.stack.pop()
        assignment = self.stack.top()
        
        # 设置content和value
        assignment.content = value
        if self.mode in {"generate_object", "register_template"}:
            assignment.value = value.value if hasattr(value, 'value') else None
            
        # 处理最终赋值
        if len(self.stack) == 1:
            assignment = self.stack.pop()
            self.assignments.append(assignment)
            if self.mode == "generate_object":
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

    def enterTemplate_assignment(self, ctx):
        """处理模板赋值"""
        if self.ignore > 0:
            return
            
        assignment = Assignment()
        assignment.is_template = True
        self.stack.push(assignment)

    def exitTemplate_assignment(self, ctx):
        """处理模板赋值的完成
        template MyTemplate[T: int = 1] is Base(...)
        """
        if self.ignore > 0:
            return
                
        # 获取值和参数列表
        value = self.stack.pop()       # 基类对象
        params = self.stack.pop()      # 参数列表
        assignment = self.stack.top()  # 模板赋值

        # 设置content
        assignment.content = value
        
        if self.mode == "register_template":
            # 收集参数定义
            param_dict = {}
            for param in params.content:
                param_type = param.content.value if hasattr(param.content, 'value') else None
                param_default = param.value if hasattr(param, 'value') else None
                param_dict[param.id] = {
                    'type': param_type,
                    'default': param_default
                }
                
            # 注册模板
            base_attributes = {}
            if hasattr(value, 'content'):
                for m in value.content:
                    if hasattr(m, 'id') and hasattr(m, 'value'):
                        base_attributes[m.id] = m.value
                        
            self.register_object(
                name=assignment.id,
                attributes=param_dict,
                base_name=value.object_type,
                base_attributes=base_attributes
            )

    #-----------------------------------------
    # 2.3 前缀修饰符处理
    #-----------------------------------------
    def enterExport_prefix(self, ctx):
        """处理导出前缀修饰符"""
        if self.ignore > 0:
            return
        self.stack.top().is_export = True

    def enterTemplate_prefix(self, ctx):
        if self.ignore > 0:
            return
        self.stack.top().is_template = True

    def enterPrivate_prefix(self, ctx):
        """处理私有前缀修饰符"""
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
    # 2.5 值系统处理优化 
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
        
        if self.mode in {"generate_object", "register_template"}:
            entity.value = float(ctx.getText())
            
        self.stack.push(entity)

    def enterFloat2_value(self, ctx):
        """处理二维向量值的开始"""
        if self.ignore > 0:
            return
        
        entity = Base()
        entity.nodetype = NodeType.Float2
        self.stack.push(entity)

    def exitFloat2_value(self, ctx):
        """处理二维向量值的完成
        float2[1.0, 2.0]
        """
        if self.ignore > 0:
            return
        
        # 从栈中获取两个值并验证
        values = []
        for i in range(2):
            value_node = self.stack.pop()
            if not value_node.nodetype in {NodeType.Integer, NodeType.Float}:
                logging.warning(f"Invalid float2 value type: {value_node.nodetype}")
                return
                
            # 获取数值
            if hasattr(value_node, 'value') and value_node.value is not None:
                val = value_node.value
            elif hasattr(value_node, 'content') and value_node.content is not None:
                val = value_node.content
            else:
                logging.error("Float2 value node has no valid value or content")
                return
                
            values.insert(0, float(val))
        
        # 获取float2实体并设置值
        entity = self.stack.top()
        entity.content = values
        if self.mode in {"generate_object", "register_template"}:
            entity.value = tuple(values)  # 使用tuple保证不可变性

    def enterFloat3_value(self, ctx):
        """处理三维向量值的开始"""
        if self.ignore > 0:
            return
        
        entity = Base()
        entity.nodetype = NodeType.Float3
        self.stack.push(entity)

    def exitFloat3_value(self, ctx):
        """处理三维向量值的完成
        float3[1.0, 2.0, 3.0]
        """
        if self.ignore > 0:
            return
        
        # 从栈中获取三个值并验证
        values = []
        for i in range(3):
            value_node = self.stack.pop()
            if not value_node.nodetype in {NodeType.Integer, NodeType.Float}:
                logging.warning(f"Invalid float3 value type: {value_node.nodetype}")
                return
                
            # 获取数值
            if hasattr(value_node, 'value') and value_node.value is not None:
                val = value_node.value
            elif hasattr(value_node, 'content') and value_node.content is not None:
                val = value_node.content
            else:
                logging.error("Float3 value node has no valid value or content")
                return
                
            values.insert(0, float(val))
        
        # 获取float3实体并设置值
        entity = self.stack.top()
        entity.content = values
        if self.mode in {"generate_object", "register_template"}:
            entity.value = tuple(values)  # 使用tuple保证不可变性

    def enterString_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.String
        entity.content = str(ctx.getText()[1:-1])
        
        if self.mode in {"register_template", "generate_object"}:
            entity.value = str(ctx.getText()[1:-1])
            
        self.stack.push(entity)

    def enterHex_value(self, ctx):
        """十六进制值的处理"""
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.Hex
        hex_str = ctx.getText()
        entity.content = int(hex_str, 16)
        
        if self.mode in {"generate_object", "register_template" }:
            entity.value = int(hex_str, 16)
            
        self.stack.push(entity)

    def enterGuid_value(self, ctx):
        """处理GUID值"""
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.GUID
        guid_str = ctx.getText()
        entity.content = guid_str
        
        if self.mode in {"generate_object", "register_template"}:
            entity.value = guid_str
            
        self.stack.push(entity)

    def enterRgba_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.RGBA
        text = ctx.getText().replace(" ", "").removeprefix("RGBA[").removeprefix("rgba[").removesuffix("]")
        entity.content = [int(x) for x in text.split(",")]
        
        if self.mode in {"generate_object", "register_template"}:
            entity.value = [int(x) for x in text.split(",")]
            
        self.stack.push(entity)

    def enterPrimitive_value(self, ctx):
        """基础值类型的进入处理"""
        if self.ignore > 0:
            return
        # 不需要特殊处理,由具体类型处理

    def enterSpecial_value(self, ctx):
        """特殊值类型的进入处理"""
        if self.ignore > 0:
            return
        # 特殊值由具体类型处理器处理

    def enterVector_value(self, ctx):
        """处理向量值
        [1, 2, 3] 或 ["a", "b", "c"]
        """
        if self.ignore > 0:
            return
        vector = Vector()
        vector.nodetype = NodeType.Vector
        self.stack.push(vector)
        self.stack.push(StackMarker())

    def exitVector_value(self, ctx):
        """完成向量值处理"""
        if self.ignore > 0:
            return
            
        # 收集向量元素
        vector_values = []
        while type(self.stack.top()) != StackMarker:
            vector_values.append(self.stack.pop())
        vector_values.reverse()
        self.stack.pop()  # 移除标记
        
        # 设置向量内容
        vector = self.stack.top()
        for value in vector_values:
            vector.append(value)
            
        # 设置最终值
        if self.mode in {"generate_object", "register_template"}:
            vector.value = [
                value.value if hasattr(value, 'value') else None 
                for value in vector_values
            ]

    #-----------------------------------------
    # 2.6 复合类型值处理
    #-----------------------------------------
    # 2.6.1 向量处理
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
            pair.value = (pair_values[0].value, pair_values[1].value)

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
            _map.value = {str(value.value[0]): value.value[1] for value in map_values}

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

    def enterData_structure_value(self, ctx):
        """复合数据结构的进入处理"""
        if self.ignore > 0:
            return
        # 具体类型由各自的处理器处理

    def exitData_structure_value(self, ctx):
        """复合数据结构的退出处理"""
        if self.ignore > 0:
            return
        # 具体类型由各自的处理器处理

    #-----------------------------------------
    # 2.7 引用和替换值处理
    #-----------------------------------------
    def enterObj_reference_value(self, ctx):
        """处理引用值
        直接存储原始路径字符串，在需要时从reference字典中获取实际值
        """
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.Reference
        entity.content = ctx.getText()  # 直接存储原始引用路径
        
        # 在生成模式下，尝试从reference字典获取实际值
        if self.mode in {"generate_object", "register_template"} and self.reference is not None:
            path = entity.content.lstrip('~$/').strip()  # 移除路径前缀
            if "|" in path:  # 处理多路径引用
                paths = [p.strip() for p in path.split("|")]
                values = []
                for p in paths:
                    if p in self.reference:
                        values.append(self.reference[p])
                entity.value = values[0] if len(values) == 1 else values
            else:
                if path in self.reference:
                    entity.value = self.reference[path]
                
        self.stack.push(entity)

    def exitObj_reference_value(self, ctx):
        """完成引用值的处理"""
        if self.ignore > 0:
            self.ignore -= 1
            return
        
        # 可以在这里添加额外的引用处理逻辑
        if self.mode in {"register_object"}:
            # 在注册对象模式下不需要立即解析引用
            pass

    def enterReplace_value(self, ctx):
        if self.ignore > 0:
            return
            
        # 创建替换实体
        entity = Base()
        entity.nodetype = NodeType.Replacer

        # 设置content和value        
        entity.content = ctx.getText()
        if self.mode in {"generate_object", "register_template"}:
            entity.value = "@" + ctx.getText()[1:-1]  # 移除首尾的@符号
            
            
        self.stack.push(entity)

    def exitReplace_value(self, ctx):
        if self.ignore > 0:
            self.ignore -= 1

    def enterConcatination(self, ctx):
        """处理引用路径的连接"""
        if self.ignore > 0:
            return
        
        if ctx.getChildCount() > 1:  # 有连接操作
            entity = Base()
            entity.nodetype = NodeType.Reference
            self.stack.push(entity)

    def exitConcatination(self, ctx):
        """完成引用路径的连接"""
        if self.ignore > 0:
            return
        
        if ctx.getChildCount() > 1:  # 有连接操作
            ref2 = self.stack.pop()
            ref1 = self.stack.pop()
            concat = self.stack.top()
            
            # 合并路径
            concat.content = f"{ref1.content} | {ref2.content}"
            
            # 在生成模式下合并值
            if self.mode in {"generate_object", "register_template"}:
                values = []
                if hasattr(ref1, 'value') and ref1.value is not None:
                    values.append(ref1.value)
                if hasattr(ref2, 'value') and ref2.value is not None:
                    values.append(ref2.value)
                concat.value = values[0] if len(values) == 1 else values

    #-----------------------------------------
    # 2.8 模板系统处理
    #-----------------------------------------
    def enterTemplate_param(self, ctx):
        """处理模板参数定义"""
        if self.ignore > 0:
            return
            
        # 创建参数赋值节点
        assignment = Assignment()
        assignment.is_template = True
        assignment.is_member = True
        self.stack.push(assignment)

    def exitTemplate_param(self, ctx):
        """完成模板参数处理
        支持以下形式:
        1. id: type = value  # 完整形式
        2. id: type         # 仅类型标注
        3. id = value      # 仅默认值
        4. id              # 仅标识符
        """
        if self.ignore > 0:
            return
            
        assignment = self.stack.top()
        child_count = ctx.getChildCount()
        
        # 处理不同形式的参数声明
        if child_count > 3:  # id ':' type '=' value
            value = self.stack.pop()      # 弹出值
            type_info = self.stack.pop()  # 弹出类型信息
            
            # 设置内容和值
            assignment.content = type_info
            
            if self.mode in {"register_template"}:
                # 获取类型字符串并尝试转换
                type_str = type_info.content.lower()
                
                # 类型转换映射
                type_converters = {
                    "bool": bool,
                    "int": int,
                    "float": float,
                    "string": str,
                    "guid": str
                }
                
                # 进行类型转换
                if type_str in type_converters and hasattr(value, 'value'):
                    try:
                        assignment.value = type_converters[type_str](value.value)
                    except (ValueError, TypeError):
                        # 转换失败时保持原值
                        assignment.value = value.value
                else:
                    assignment.value = value.value
                    
        elif child_count > 2:  # id ':' type 或 id '=' value
            top = self.stack.pop()
            if ctx.getChild(1).getText() == ':':  # id ':' type
                # 类型标注形式
                assignment.content = top
                if self.mode in {"register_template"}:
                    assignment.value = top.content
            else:  # id '=' value
                # 默认值形式
                assignment.content = None
                if self.mode in {"register_template"}:
                    assignment.value = top.value if hasattr(top, 'value') else None
        
        # id 形式不需要额外处理,因为id已在enterTemplate_id中设置

    def enterTemplate_param_list(self, ctx):
        """处理模板参数列表"""
        if self.ignore > 0:
            return
            
        vector = Vector()
        vector.nodetype = NodeType.STRUCTURAL
        self.stack.push(vector)
        self.stack.push(StackMarker())

    def exitTemplate_param_list(self, ctx):
        """完成模板参数列表处理"""
        if self.ignore > 0:
            return
            
        params = []
        while type(self.stack.top()) != StackMarker:
            params.append(self.stack.pop())
        params.reverse()
        self.stack.pop()  # 移除标记
        
        vector = self.stack.top()
        for param in params:
            vector.append(param)

    def enterTemplate_id(self, ctx:NdfGrammarParser.Template_idContext):
        """处理模板参数标识符
        
        当进入template_id规则时:
        1. 获取标识符文本
        2. 设置栈顶Assignment的id属性
        """
        if self.ignore > 0:
            return
            
        # 获取标识符文本
        id_text = ctx.getText()
        
        # 设置栈顶元素的id
        assignment = self.stack.top()
        if assignment is not None:
            assignment.id = id_text

    #-----------------------------------------
    # 2.9 类型标签处理
    #-----------------------------------------
    def enterType_label(self, ctx):
        """处理类型标签"""
        if self.ignore > 0:
            return

        entity = Base()
        entity.nodetype = NodeType.STRUCTURAL
        entity.content = ctx.getText()

        if self.mode in {"register_template"}:
            entity.value = ctx.getText()

        self.stack.push(entity)

    def exitType_label(self, ctx):
        """完成类型标签处理"""
        if self.ignore > 0:
            return

        # 获取栈顶节点
        entity = self.stack.top()
        type_str = ctx.getText().lower()  # 统一转换为小写
        
        # 只在有值需要转换时处理
        if hasattr(entity, 'value') and entity.value is not None:
            # 类型转换映射
            type_converters = {
                "bool": bool,
                "int": int,
                "float": float,
                "string": str,
                "guid": str
            }
            
            # 如果存在对应的转换器,则执行转换
            if type_str in type_converters:
                try:
                    entity.value = type_converters[type_str](entity.value)
                except (ValueError, TypeError):
                    logging.warning(f"Failed to convert value {entity.value} to type {type_str}")

    def enterList_label(self, ctx):
        """处理列表类型标签"""
        if self.ignore > 0:
            return

        entity = Base()
        entity.nodetype = NodeType.STRUCTURAL
        entity.content = ctx.getText()

        if self.mode in {"register_template"}:
            entity.value = "list"  # 统一使用小写

        self.stack.push(entity)

    def exitList_label(self, ctx):
        """完成列表类型标签处理"""
        if self.ignore > 0:
            return

        # 获取栈顶节点
        entity = self.stack.top()
        
        # 如果有值,尝试转换为列表
        if hasattr(entity, 'value') and entity.value is not None:
            if not isinstance(entity.value, list):
                entity.value = list(entity.value) if hasattr(entity.value, '__iter__') else [entity.value]

    def enterMap_label(self, ctx):
        """处理映射类型标签"""
        if self.ignore > 0:
            return

        entity = Base()
        entity.nodetype = NodeType.STRUCTURAL
        entity.content = ctx.getText()

        if self.mode in {"register_template"}:
            entity.value = "map"  # 统一使用小写

        self.stack.push(entity)

    def exitMap_label(self, ctx):
        """完成映射类型标签处理"""
        if self.ignore > 0:
            return

        # 获取栈顶节点    
        entity = self.stack.top()
        
        # 如果有值,尝试转换为字典
        if hasattr(entity, 'value') and entity.value is not None:
            if not isinstance(entity.value, dict):
                if isinstance(entity.value, (list, tuple)) and len(entity.value) % 2 == 0:
                    # 将键值对列表转换为字典
                    entity.value = dict(zip(entity.value[::2], entity.value[1::2]))

    #-----------------------------------------
    # 2.10 对象系统处理
    #-----------------------------------------
    def enterObject(self, ctx):
        """处理对象"""
        if self.ignore > 0:
            return

        # object已在object_type中被创建并压栈
        pass

    def enterObject_type(self, ctx):
        """处理对象类型"""
        if self.ignore > 0:
            return

        obj = Object()
        obj.object_type = ctx.getText()
        self.stack.push(obj)
        self.stack.push(StackMarker())

    def enterBlock(self, ctx):
        """处理对象成员块"""
        if self.ignore > 0:
            return
        # 由具体的赋值语句处理

    def exitBlock(self, ctx):
        """完成对象成员块处理"""
        if self.ignore > 0:
            return
        # 由具体的赋值语句处理

    def exitObject(self, ctx):
        """完成对象处理"""
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
    # 2.11 数值特化处理
    #-----------------------------------------
    def enterNumeric_specialization(self, ctx):
        """处理数值特化"""
        if self.ignore > 0:
            return
        # 由具体的值类型处理器处理(int_value/float_value/arithmetic)

    def exitNumeric_specialization(self, ctx):
        """完成数值特化处理"""
        if self.ignore > 0:
            return
        
        # 确保特化值是数值类型
        spec = self.stack.top()
        if spec.nodetype not in {NodeType.Integer, NodeType.Float, NodeType.Arithmetic}:
            logging.warning(f"Invalid specialization type: {spec.nodetype}")

    #-----------------------------------------
    # 2.12 右值表达式处理
    #-----------------------------------------
    def enterR_value(self, ctx):
        """处理右值表达式"""
        if self.ignore > 0:
            return
        # 由具体类型处理器处理

    def exitR_value(self, ctx):
        """完成右值表达式处理"""
        if self.ignore > 0:
            return
        # 确保值已正确生成
        value = self.stack.top()
        if value.value is None and self.mode in {"generate_object", "register_template"}:
            logging.warning(f"Value not generated for r_value: {value.content}")

    #-----------------------------------------
    # 2.13 辅助功能完善
    #-----------------------------------------
    def _resolve_reference(self, path: str) -> Any:
        """解析引用路径
        
        Args:
            path: 引用路径
            
        Returns:
            解析后的值，如果找不到返回None
        """
        if not path:
            return None
            
        path = path.lstrip('~$/').strip()
        
        # 处理多路径引用
        if "|" in path:
            paths = [p.strip() for p in path.split("|")]
            values = []
            for p in paths:
                if p in self.reference:
                    values.append(self.reference[p])
            return values[0] if len(values) == 1 else values
            
        # 处理单一路径
        if path in self.reference:
            return self.reference[path]
            
        return None

    def _validate_type(self, node: Base, expected_types: set) -> bool:
        """验证节点类型
        
        Args:
            node: 要验证的节点
            expected_types: 期望的类型集合
            
        Returns:
            类型是否匹配
        """
        return node.nodetype in expected_types

    def _handle_error(self, msg: str, ctx = None):
        """处理错误
        
        Args:
            msg: 错误信息
            ctx: 语法上下文(可选)
        """
        if ctx:
            line = ctx.start.line if hasattr(ctx, 'start') else '?'
            col = ctx.start.column if hasattr(ctx, 'start') else '?'
            text = ctx.getText() if hasattr(ctx, 'getText') else ''
            logging.error(f"Line {line}:{col} - {msg} near '{text}'")
        else:
            logging.error(msg)
        self.ignore += 1

    def enterType_initialization(self, ctx):
        """处理类型初始化 如 float2(1.0)"""
        if self.ignore > 0:
            return
        # TODO: 实现类型初始化逻辑
