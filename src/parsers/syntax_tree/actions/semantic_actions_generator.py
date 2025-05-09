from antlr4 import *
from typing import Any, Optional, Dict, TYPE_CHECKING  # 添加TYPE_CHECKING
from src.parsers.parser.NdfGrammarListener import NdfGrammarListener
from src.parsers.parser.NdfGrammarParser import NdfGrammarParser

from src.parsers.syntax_tree.nodes.syntax_node_assignment import *
from src.parsers.syntax_tree.nodes.syntax_node_collection import *

import logging
import src.extractor.refined_class
import src.extractor.extract_class
import src.extractor.backup_class
import src.extractor.base_class

# 在文件顶部import区域添加
try:
    from src.core.config_manager import ConfigManager
    from src.core.path_resolver import PathResolver
except ImportError:
    from core.config_manager import ConfigManager
    from core.path_resolver import PathResolver

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
    """语义动作生成器
    处理NDF语法树的语义动作，生成对应的Python对象

    主要功能:
    1. 语法树遍历 - 遍历ANTLR生成的语法树
    2. 语义动作 - 执行相应的语义动作
    3. 对象生成 - 生成Python对象和类定义
    """
    
    #-----------------------------------------
    # 1. 基础设施
    #-----------------------------------------
    def __init__(self, parser: Parser, config: ConfigManager, name_space: str = "/", reference: Optional[PathResolver] = None, mode: str = "default"):
        """初始化生成器
        Args:
            parser: ANTLR解析器
            config: 配置管理器
            name_space: 命名空间
            reference: 路径解析器，用于解析引用
            mode: 解析模式 ("register_object"|"register_template"|"generate_object")
        """
        super().__init__()
        self.config = config
        self.rule_names = parser.ruleNames
        self.assignments = []
        self.stack = Stack()
        self.ignore = 0
        self.name_space = name_space
        self.mode = mode
        
        # 生成的对象使用普通字典
        self.generator = {}
        # 注册的类型使用普通字典
        self.register = {}
        
        # reference必须是PathResolver
        if reference is not None and not isinstance(reference, PathResolver):
            raise TypeError("reference must be an instance of PathResolver")
        self.reference = reference or PathResolver()
        
        self.current_class = None
        self.current_template = None

    def register_object(self, name: str, attributes: dict, base_name: Optional[str] = None, base_attributes: Optional[dict] = None) -> None:
        """注册一个对象类型"""
        # 参数检查
        if not name:
            self._handle_error("Empty object name")
            return
            
        if not attributes:
            attributes = {}  # 使用空字典而不是None
            
        # 主要逻辑
        if name not in self.register:
            logging.info(f"Registering new class: {name}")
            self.register[name] = {
                "attributes": attributes,
                "base": {
                    "name": base_name,
                    "attributes": base_attributes or {}  # 使用空字典而不是None
                } if base_name else None
            }
        else:
            entry = self.register[name]
            if not entry:  # 检查entry是否有效
                self._handle_error(f"Invalid registry entry for {name}")
                return
                
            # 更新属性
            for attr, value in attributes.items():
                if attr not in entry["attributes"] or value is not None:
                    entry["attributes"][attr] = value
                    
            # 更新基类信息
            if base_name:
                if not entry.get("base") or entry["base"]["name"] != base_name:
                    entry["base"] = {
                        "name": base_name,
                        "attributes": base_attributes or {}
                    }
                else:
                    base = entry.get("base")
                    if base and base_attributes:  # 检查base和base_attributes存在
                        for attr, value in base_attributes.items():
                            if attr not in base["attributes"] or value is not None:
                                base["attributes"][attr] = value


    def generate_object(self, name: str, value: Any) -> None:
        """根据类型生成对象实例"""
        # 参数检查
        if not name:
            self._handle_error("Empty object name")
            return
            
        # 主要逻辑
        if name not in self.generator:
            logging.info(f"Generating new object: {name}")
            self.generator[name] = value
        else:
            current = self.generator.get(name)  # 使用get而不是直接访问
            if current is None:  # 检查current是否存在
                self._handle_error(f"Invalid generator entry for {name}")
                return
                
            if isinstance(current, list):
                current.append(value)
            else:
                self.generator[name] = [current, value]
        

    def instantiate_class(self, class_name: str, **kwargs) -> Optional[Any]:
        """按优先级从模块实例化类"""
        # 直接从多个模块获取类
        get_class = lambda name: (            
            getattr(src.extractor.extract_class, name, None) or
            getattr(src.extractor.backup_class, name, None) or
            getattr(src.extractor.refined_class, name, None) or
            getattr(src.extractor.base_class, name, None)
        )
        class_ = get_class(class_name)
        return class_(**kwargs) if class_ is not None else None


    def _resolve_reference(self, path: str) -> Any:
        """解析引用路径
        
        Args:
            path: 引用路径字符串,可能包含多个路径用'|'分隔
            
        Returns:
            解析到的第一个有效值,如果都无效则返回None
        """
        if not path or not self.reference:
            return None
            
        # 处理多路径选择
        paths = [p.strip() for p in path.split('|')]
        
        # 尝试每个路径,返回第一个有效值
        for p in paths:
            if p:  # 确保路径非空
                value = self.reference.get(p, self.name_space)
                if value is not None:
                    return value
                    
        return None

    def _validate_type(self, node: Base, expected_types: set) -> bool:
        """
        验证节点类型是否符合预期
        
        Args:
            node: 需要验证的节点
            expected_types: 预期的类型集合
            
        Returns:
            True: 类型符合预期
            False: 类型不符合预期
        """
        return bool(node and node.nodetype in expected_types)

    def _handle_error(self, msg: str, ctx: Optional[Any] = None) -> None:
        """
        处理错误并记录日志
        
        Args:
            msg: 错误信息
            ctx: 解析上下文(可选)
            
        Side Effects:
            - 增加ignore计数
            - 记录错误日志
        """
        if ctx:
            line = getattr(ctx.start, 'line', '?')
            col = getattr(ctx.start, 'column', '?')
            text = getattr(ctx, 'getText', lambda: '')()
            logging.error(f"Line {line}:{col} - {msg} near '{text}'")
        else:
            logging.error(msg)
            
        self.ignore += 1

    #-----------------------------------------
    # 2. 标识符系统
    #-----------------------------------------
    def enterId(self, ctx):
        """处理标识符"""
        if self.ignore > 0:
            return
            
        assignment = None
        for item in reversed(self.stack._stack):
            if isinstance(item, Assignment):
                assignment = item
                break
                
        if not assignment:
            return
            
        assignment.id = ctx.getChild(0).getText()

    def exitId(self, ctx):
        """处理标识符完成"""
        if self.ignore > 0:
            return

    def enterArray_access(self, ctx):
        """处理数组访问"""
        if self.ignore > 0:
            return
            
        assignment = None
        for item in reversed(self.stack._stack):
            if isinstance(item, Assignment):
                assignment = item
                break
                
        if assignment:
            assignment.is_array_access = True
            assignment.array_index = None

    def exitArray_access(self, ctx):
        """完成数组访问处理"""
        if self.ignore > 0:
            return
            
        index = int(ctx.getChild(2).getText())
        
        for item in reversed(self.stack._stack):
            if isinstance(item, Assignment):
                item.array_index = index
                break

    #-----------------------------------------
    # TODO: 成员访问功能
    #-----------------------------------------
    # 在NDF文件中发现的成员访问模式:
    # 1. 数组索引访问: array[index]
    #    - 用于访问预定义数组
    #    - 在模板参数中使用
    #    - 例如: MagnifiableWidthHeight = [~/SmartGroupUnitButtonSize[0], 215.0]
    #
    # 2. 内部引用访问:
    #    - 对象内部属性间的引用
    #    - 变量作用域问题
    #    - 求值顺序问题
    #
    # 实现优先级:
    # 1. 优先实现基础功能
    # 2. 后续再考虑添加成员访问支持
    # 3. 需要完整的作用域和依赖管理系统

    #-----------------------------------------
    # 3. 赋值系统
    #-----------------------------------------
    def enterNormal_assignment(self, ctx):
        if self.ignore > 0:
            return
        self.stack.push(Assignment())

    def exitNormal_assignment(self, ctx):
        """处理普通赋值语句的完成
        
        同时:
        1. 添加到assignments列表
        2. 生成对象(如果是generate模式)
        3. 添加到引用索引(如果有命名空间)
        """
        if self.ignore > 0:
            return
            
        value = self.stack.pop() if len(self.stack) > 0 else None
        if not value:
            self._handle_error("No value found for assignment", ctx)
            return
        
        assignment = None
        for item in reversed(self.stack._stack):
            if isinstance(item, Assignment):
                assignment = item
                break

        if not assignment:
            self._handle_error("No assignment found", ctx)
            return
                
        assignment.content = value
        if self.mode in {"generate_object", "register_template"}:
            assignment.value = value.value if hasattr(value, 'value') else None
            assignment.convert_value()

        # 检查堆栈长度
        if len(self.stack) == 1:
            # 1. 添加到assignments列表
            self.assignments.append(assignment)
            self.stack.pop()
            
            if self.mode in {"generate_object", "register_template"}:
                # 2. 生成对象
                if hasattr(assignment, 'id') and assignment.id is not None:
                    self.generate_object(assignment.id, assignment.value)
                    
                    # 3. 添加到引用索引
                    if self.name_space and self.reference:
                        # 添加到引用字典
                        self.reference.set("~/"+assignment.id,assignment.value,self.name_space)

    def enterMember_assignment(self, ctx):
        if self.ignore > 0:
            return
        assignment = Assignment()
        assignment.is_member = True
        self.stack.push(assignment)

    def exitMember_assignment(self, ctx):
        """处理成员赋值语句的完成"""
        if self.ignore > 0:
            return
            
        value = self.stack.pop()
        assignment = None
        
        for item in reversed(self.stack._stack):
            if isinstance(item, Assignment):
                assignment = item
                break
                
        if assignment:
            assignment.content = value
            if self.mode in {"generate_object", "register_template"}:
                assignment.value = value.value if hasattr(value, 'value') else None
                assignment.convert_value()

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
        
        assignment.id = "Unnamed-" + str(hash(str(value)))
        assignment.content = value
        
        if self.mode in {"generate_object", "register_template"}:
            assignment.value = value.value

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
        """处理模板赋值的完成"""
        if self.ignore > 0:
            return
            
        value = self.stack.pop()  # 可能为None
        params = self.stack.pop()  # 可能为None
        assignment = self.stack.top()  # 可能为None
        
        if not value or not params or not assignment:  # 添加检查
            self._handle_error("Missing required values for template assignment", ctx)
            return
            
        if not hasattr(value, 'content'):  # 添加属性检查
            self._handle_error("Value node has no content", ctx)
            return
        
        assignment.content = value
        
        if self.mode == "register_template":
            param_dict = {}
            for param in params.content:
                param_type =  None
                param_default = param.value if hasattr(param, 'value') else None
                param_dict[param.id] = param_default
                
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
        self.stack.pop()  # 弹出assignment

    #-----------------------------------------
    # 4. 基础值系统
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
        entity.content = ctx.getText()
        
        if self.mode in {"generate_object", "register_template"}:
            entity.value = True if ctx.getText().lower() == "true" else False
            
        self.stack.push(entity)

    def enterInt_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.Integer
        entity.content = ctx.getText()
        
        if self.mode in {"generate_object", "register_template"}:
            entity.value = int(ctx.getText())
            
        self.stack.push(entity)

    def enterFloat_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.Float
        entity.content = ctx.getText()
        
        if self.mode in {"generate_object", "register_template"}:
            entity.value = float(ctx.getText())
            
        self.stack.push(entity)

    def enterString_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.String
        entity.content = ctx.getText()
        
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
        entity.content = ctx.getText()
        
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
        entity.content = ctx.getText()
        
        if self.mode in {"generate_object", "register_template"}:
            entity.value = guid_str
            
        self.stack.push(entity)

    #-----------------------------------------
    # 5. 复合值系统
    #-----------------------------------------
    def enterVector_value(self, ctx):
        """处理向量值"""
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
            
        vector_values = []
        while type(self.stack.top()) != StackMarker:
            vector_values.append(self.stack.pop())
        vector_values.reverse()
        self.stack.pop()
        
        vector = self.stack.top()
        for value in vector_values:
            vector.append(value)
            
        if self.mode in {"generate_object", "register_template"}:
            vector.value = [
                value.value if hasattr(value, 'value') else None 
                for value in vector_values
            ]

    def enterFloat2_value(self, ctx):
        """处理二维向量值的开始"""
        if self.ignore > 0:
            return
        
        entity = Base()
        entity.nodetype = NodeType.Float2
        self.stack.push(entity)

    def exitFloat2_value(self, ctx):
        """处理二维向量值的完成"""
        if self.ignore > 0:
            return
        
        values = []
        for i in range(2):
            value_node = self.stack.pop()
            if not value_node.nodetype in {NodeType.Integer, NodeType.Float}:
                logging.warning(f"Invalid float2 value type: {value_node.nodetype}")
                return
                
            if hasattr(value_node, 'value') and value_node.value is not None:
                val = value_node.value
            else:
                logging.error("Float2 value node has no valid value")
                return
                
            values.insert(0, float(val))
        
        entity = self.stack.top()
        entity.content = values
        if self.mode in {"generate_object", "register_template"}:
            entity.value = tuple(values)

    def enterFloat3_value(self, ctx):
        """处理三维向量值的开始"""
        if self.ignore > 0:
            return
        
        entity = Base()
        entity.nodetype = NodeType.Float3
        self.stack.push(entity)

    def exitFloat3_value(self, ctx):
        """处理三维向量值的完成"""
        if self.ignore > 0:
            return
        
        values = []
        for i in range(3):
            value_node = self.stack.pop()
            if not value_node.nodetype in {NodeType.Integer, NodeType.Float}:
                logging.warning(f"Invalid float3 value type: {value_node.nodetype}")
                return
                
            if hasattr(value_node, 'value') and value_node.value is not None:
                val = value_node.value
            elif hasattr(value_node, 'content') and value_node.content is not None:
                val = value_node.content
            else:
                logging.error("Float3 value node has no valid value or content")
                return
                
            values.insert(0, float(val))
        
        entity = self.stack.top()
        entity.content = values
        if self.mode in {"generate_object", "register_template"}:
            entity.value = tuple(values)

    def enterRgba_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.RGBA
        text = ctx.getText().replace(" ", "").removeprefix("RGBA[").removeprefix("rgba[").removesuffix("]")
        entity.content = ctx.getText()
        
        if self.mode in {"generate_object", "register_template"}:
            entity.value = [int(x) for x in text.split(",")]
            
        self.stack.push(entity)

    def enterMap_value(self, ctx):
        if self.ignore > 0:
            return
        self.stack.push(Map())
        self.stack.push(StackMarker())

    def exitMap_value(self, ctx):
        if self.ignore > 0:
            return
            
        map_values = []
        while type(self.stack.top()) != StackMarker:
            map_values.append(self.stack.pop())
        map_values.reverse()
        self.stack.pop()
        
        _map = self.stack.top()
        if not _map:  # 添加检查
            self._handle_error("No map container found", ctx)
            return
        
        for map_value in map_values:
            if not hasattr(map_value, 'content'):  # 添加成员检查
                self._handle_error("Invalid map value", ctx)
                continue
            if not isinstance(map_value.content, list) or len(map_value.content) != 2:
                self._handle_error("Invalid map pair format", ctx)
                continue
            _map.append(map_value)
            
        if self.mode in {"generate_object", "register_template"}:
            _map.value = {str(value.value[0]): value.value[1] for value in map_values}

    def enterPair_value(self, ctx):
        if self.ignore > 0:
            return
        self.stack.push(Pair())
        self.stack.push(StackMarker())

    def exitPair_value(self, ctx):
        if self.ignore > 0:
            return
            
        pair_values = []
        while type(self.stack.top()) != StackMarker:
            pair_values.append(self.stack.pop())
        pair_values.reverse()
        self.stack.pop()
        
        pair = self.stack.top()
        
        for pair_value in pair_values:
            pair.append(pair_value)
            
        if self.mode in {"generate_object", "register_template"}:
            pair.value = (pair_values[0].value, pair_values[1].value)

    #-----------------------------------------
    # 6. 对象系统
    #-----------------------------------------
    def enterObject_type(self, ctx):
        """处理对象类型"""
        if self.ignore > 0:
            return
        # 只记录类型名称,不创建对象
        pass

    def enterObject(self, ctx):
        """处理对象"""
        if self.ignore > 0:
            return
        
        obj = Object()
        obj.object_type = ctx.getChild(0).getText()  # 获取对象类型名称
        self.stack.push(obj)
        self.stack.push(StackMarker())

    def exitObject(self, ctx):
        """完成对象处理"""
        if self.ignore > 0:
            return

        members = []
        while type(self.stack.top()) != StackMarker:
            member = self.stack.pop()
            if member:  # 检查成员是否存在
                members.append(member)
            
        self.stack.pop()

        obj = self.stack.top()
        
        if not obj:  # 检查对象是否存在
            self._handle_error("No object found", ctx)
            return

        for member in members:
            if hasattr(member, 'is_member') and member.is_member: # 检查成员是否有id属性
                obj.append(member)
            elif hasattr(member, 'id') and not member.is_member:
                if self.mode in {"generate_object", "register_template"}:
                    if self.name_space and self.reference:
                        # 添加到引用字典
                        self.reference.set("~/"+member.id,member.value,self.name_space)

        if self.mode in {"generate_object", "register_template"}:
            class_name = obj.object_type
            kwargs = {val.id: val.value for val in obj.content}
            obj.value = self.instantiate_class(class_name, **kwargs)

        elif self.mode in {"register_object"}:
            class_name, class_attrs = obj.get_class()
            self.register_object(name=class_name, attributes=class_attrs)

    def enterBlock(self, ctx):
        """处理对象成员块"""
        if self.ignore > 0:
            return

    def exitBlock(self, ctx):
        """完成对象成员块处理"""
        if self.ignore > 0:
            return

    #-----------------------------------------
    # 7. 模板系统
    #-----------------------------------------
    def enterTemplate_param(self, ctx):
        """处理模板参数定义"""
        if self.ignore > 0:
            return
            
        assignment = Assignment()
        assignment.is_member = True
        self.stack.push(assignment)

    def exitTemplate_param(self, ctx):
        """完成模板参数处理"""
        if self.ignore > 0:
            return
            
        child_count = ctx.getChildCount()
        
        if child_count == 3:
            value = self.stack.pop()
            assignment = self.stack.top()
            
            assignment.content = value
            if self.mode in {"generate_object", "register_template"}:
                assignment.value = value.value
                if hasattr(assignment, 'type_spec'):
                    assignment.convert_value()
                    
        elif child_count == 1:
            pass

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
        self.stack.pop()
        
        vector = self.stack.top()
        for param in params:
            vector.append(param)

    #-----------------------------------------
    # 8. 修饰符系统
    #-----------------------------------------
    def enterExport_prefix(self, ctx):
        """处理导出前缀修饰符"""
        if self.ignore > 0:
            return
        self.stack.top().is_export = True

    def enterTemplate_prefix(self, ctx):
        if self.ignore > 0:
            return

    def enterPrivate_prefix(self, ctx):
        """处理私有前缀修饰符"""
        if self.ignore > 0:
            return
        self.stack.top().is_private = True

    #-----------------------------------------
    # 9. 引用系统
    #-----------------------------------------
    def enterObj_reference_value(self, ctx):
        """处理引用值"""
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.Reference
        reference_str = ctx.getText()
        entity.content = ctx.getText()  # 保存原始引用字符串
        
        if self.mode in {"generate_object", "register_template"}:
            # 使用_resolve_reference解析引用
            resolved_value = self._resolve_reference(reference_str)
            if resolved_value is not None:
                entity.value = resolved_value
            else:
                entity.value = reference_str
                logging.warning(f"Reference '{reference_str}' not found in reference dictionary")
                
        self.stack.push(entity)

    def exitObj_reference_value(self, ctx):
        """完成引用值的处理"""
        if self.ignore > 0:
            self.ignore -= 1
            return

    def enterReplace_value(self, ctx):
        if self.ignore > 0:
            return
            
        entity = Base()
        entity.nodetype = NodeType.Replacer

        entity.content = ctx.getText()
        if self.mode in {"generate_object", "register_template"}:
            entity.value = "@" + ctx.getText()[1:-1]
            
        self.stack.push(entity)

    def exitReplace_value(self, ctx):
        if self.ignore > 0:
            self.ignore -= 1

    def enterConcatination(self, ctx):
        """处理引用路径的连接"""
        if self.ignore > 0:
            return
        
        if ctx.getChildCount() > 1:
            entity = Base()
            entity.nodetype = NodeType.Reference
            self.stack.push(entity)

    def exitConcatination(self, ctx):
        """完成引用路径的连接"""
        if self.ignore > 0:
            return
        
        if ctx.getChildCount() > 1:
            ref2 = self.stack.pop()
            ref1 = self.stack.pop()
            concat = self.stack.top()
            
            concat.content = f"{ref1.content} | {ref2.content}"
            
            if self.mode in {"generate_object", "register_template"}:
                values = []
                if hasattr(ref1, 'value') and ref1.value is not None:
                    values.append(ref1.value)
                if hasattr(ref2, 'value') and ref2.value is not None:
                    values.append(ref2.value)
                concat.value = values[0] if len(values) == 1 else values

    #-----------------------------------------
    # 10. 表达式系统
    #-----------------------------------------
    def enterArithmetic(self, ctx):
        if self.ignore > 0:
            return
            
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
        
        arithmetic.content = ctx.getText()
        self.stack.push(arithmetic)

    def exitArithmetic(self, ctx):
        if self.ignore > 0:
            return
            
        if ctx.getChildCount() == 1:
            return
            
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "-":
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.content = "-" + op1.content
            if self.mode in {"generate_object", "register_template"}:
                arithmetic.value = -op1.value
            return
            
        elif (ctx.getChildCount() == 3 
              and ctx.getChild(0).getText() == "(" 
              and ctx.getChild(2).getText() == ")"):
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.content = op1.content
            if self.mode in {"generate_object", "register_template"}:
                arithmetic.value = op1.value
            arithmetic.value = op1.value
            return
            
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "+":
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.content = op1.content + "+" + op2.content
            if self.mode in {"generate_object", "register_template"}:
                arithmetic.value = op1.value + op2.value
            return
            
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "-":
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.content = op1.content + "-" + op2.content
            if self.mode in {"generate_object", "register_template"}:
                arithmetic.value = op1.value - op2.value
            return
            
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "*":
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.content = op1.content + "*" + op2.content
            if self.mode in {"generate_object", "register_template"}:
                arithmetic.value = op1.value * op2.value
            return
            
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText().lower() == "div":
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            arithmetic = self.stack.top()
            arithmetic.content = op1.content + "/" + op2.content
            if self.mode in {"generate_object", "register_template"}:
                arithmetic.value = op1.value / op2.value
            return
