import dill
import antlr4
from antlr4 import *
from src.extractor.base_class import BaseDescription
from src.parsers.parser.NdfGrammarLexer import NdfGrammarLexer
from src.parsers.parser.NdfGrammarParser import NdfGrammarParser
from src.parsers.syntax_tree.actions import semantic_actions_generator
from src.parsers.syntax_tree.nodes.syntax_node_assignment import *
from src.parsers.syntax_tree.nodes.syntax_node_collection import *
from typing import List, Tuple, Dict, Any, Union, Optional
from src.config.config_manager import ConfigManager
from src.extractor.backup_class import *
from src.extractor.base_class import *
from src.extractor.refined_class import *
from src.extractor.extract_class import *
from src.extractor.test_class import *  # 最后导入test_class

#=============================================
# 2. 统一管理器类
#=============================================
class Manager:
    """统一管理器类
    
    提供功能:
    - 注册对象(register_object)
    - 注册模板(register_template) 
    - 生成对象(generate)
    - 导出类(export)
    - 路径解析(resolve_path)
    - 文件读写(save/load)
    """
    def __init__(
        self, 
        file_list: List[Tuple[str, str]], 
        register_file: str = "register.pkl",
        generate_file: str = "global.pkl",
        log_file: str = "log.txt",
        export_file: str = "TClass.py"
    ):
        # 获取配置实例
        self.config = ConfigManager().get_instance()
        self.file_list = file_list
        self.register_dict = {}
        self.dict = {}
        # 使用config处理文件路径
        self.register_file = self.config.get_output_path(register_file)
        self.generate_file = self.config.get_output_path(generate_file)
        self.log_file = self.config.get_output_path(log_file)
        self.export_file = self.config.get_output_path(export_file)

    def save(self, mode: str = "generate"):
        """保存到文件，使用dill处理复杂对象序列化"""
        try:
            if mode == "register":
                with open(self.register_file, "wb") as f:
                    dill.dump(self.register_dict, f)
            else:
                with open(self.generate_file, "wb") as f:
                    dill.dump(self.dict, f)
        except Exception as e:
            self.log(f"Error saving to file: {str(e)}")
            raise

    def load(self, mode: str = "generate"):
        """从文件加载，使用dill处理复杂对象反序列化"""
        try:
            if mode == "register":
                with open(self.register_file, "rb") as f:
                    self.register_dict = dill.load(f)
            else:
                with open(self.generate_file, "rb") as f:
                    self.dict = dill.load(f)
        except Exception as e:
            self.log(f"Error loading from file: {str(e)}")
            raise

    def log(self, message: str):
        """写入日志"""
        with open(self.log_file, "a") as f:
            f.write(message + "\n")

    def merge(self, dict1: dict, dict2: dict) -> dict:
        """合并字典"""
        for key, value in dict2.items():
            if key in dict1:
                if isinstance(dict1[key], dict) and isinstance(value, dict):
                    dict1[key] = self.merge(dict1[key], value)
                elif dict1[key] is None:
                    dict1[key] = value
            else:
                dict1[key] = value
        return dict1

    def extract(self, file_name: str, name_space: str, reference: Any, mode: str = "generate_object") -> Dict:
        """解析NDF文件"""
        try:
            input_stream = antlr4.InputStream(str(FileStream(file_name, encoding="utf8")))
            lexer = NdfGrammarLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = NdfGrammarParser(stream)
            tree = parser.ndf_file()
            
            listener = semantic_actions_generator.Generator(
                parser, 
                name_space=name_space,
                reference=reference,
                mode=mode
            )
            
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            
            return (listener.generator if mode == "generate_object" 
                    else listener.register)
                    
        except FileNotFoundError:
            self.log(f"Error: File not found: {file_name}")
            raise
        except Exception as e:
            self.log(f"Error parsing file {file_name}: {str(e)}")
            raise

    def check_file_exist(self) -> Dict[str, bool]:
        """检查文件是否存在"""
        file_status = {}
        for file, _ in self.file_list:
            file_path = self.config.get_full_path(file)
            exists = file_path.exists()
            if not exists:
                self.log(f"Warning: File not found: {file_path}")
            file_status[file] = exists
        return file_status

    def _resolve_path(self, path: Union[str, List[str]], namespace: Optional[str]) -> str:
        """解析路径"""
        if isinstance(path, list):
            path = '/' + '/'.join(str(p) for p in path)
        elif not isinstance(path, str):
            raise TypeError("路径必须是字符串或列表")

        path = path.strip()
        if path.startswith("$/"):
            return path[2:].strip('/')
        if path.startswith("~/"):
            if not namespace or not namespace.startswith('/'):
                raise ValueError(f"Namespace '{namespace}' 必须以 '/' 开头")
            return f"{namespace.rstrip('/')}/{path[2:].strip('/')}"
        return path.strip('/')

    def get(self, path: Union[str, List[str]], namespace: Optional[str] = None) -> Any:
        """获取值"""
        try:
            full_path = self._resolve_path(path, namespace)
            keys = full_path.strip('/').split('/')
            current = self.dict

            for key in keys:
                if isinstance(current, dict) and key in current:
                    current = current[key]
                elif hasattr(current, key):
                    current = getattr(current, key)
                else:
                    self.log(f"Warning: Path '{path}' not found in namespace '{namespace}'")
                    return full_path.lstrip("$~/")
            return current
        except Exception as e:
            self.log(f"Error accessing path '{path}': {str(e)}")
            return None

    def set(self, path: str, value: Any, namespace: Optional[str] = None):
        """设置值"""
        full_path = self._resolve_path(path, namespace)
        keys = full_path.strip('/').split('/')
        current = self.dict

        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]
        current[keys[-1]] = value

    def set_batch(self, data_dict: dict, current_namespace: str):
        """批量设置值"""
        if not isinstance(data_dict, dict):
            raise TypeError("data_dict 必须是一个字典")
        for key, value in data_dict.items():
            self.set(key, value, namespace=current_namespace)

    def register(self, reference: Optional[Any] = None):
        """执行完整注册流程"""
        self.register_object(reference)
        self.export()
        self.register_template(reference)
        self.export()
    
    def register_template(self, reference: Optional[Any] = None):
        """注册模板"""
        for file, name_space in self.file_list:
            file_path = self.config.get_full_path(file)
            template = self.extract(
                str(file_path),
                name_space=name_space,
                reference=reference,
                mode="register_template"
            )
            self.register_dict = self.merge(self.register_dict, template)

    def register_object(self, reference: Optional[Any] = None):
        """注册对象"""
        for file, name_space in self.file_list:
            file_path = self.config.get_full_path(file)
            object = self.extract(
                str(file_path),
                name_space=name_space,
                reference=reference,
                mode="register_object"
            )
            self.register_dict = self.merge(self.register_dict, object)

    def generate(self, reference: Optional[Any] = None):
        """生成对象
        
        处理每个文件时:
        1. 解析文件生成对象
        2. 立即将对象添加到命名空间
        3. 更新引用信息
        """
        for file, name_space in self.file_list:
            file_path = self.config.get_full_path(file)
            # 解析当前文件
            object_dict = self.extract(
                str(file_path),
                name_space=name_space,
                reference=reference or self,
                mode="generate_object"
            )
            
            # 立即添加到命名空间
            self.set_batch(object_dict, name_space)
            
            # 记录日志
            self.log(f"Generated objects from {file} in namespace {name_space}")
            self.log(f"Objects: {list(object_dict.keys())}")

    def export(self):
        """导出类定义"""
        def format_value(value):
            """格式化任意值为字符串表示
            
            处理以下类型:
            1. BaseDescription对象 -> 调用reverse()
            2. 列表/元组 -> 递归处理每个元素
            3. 字典 -> 递归处理每个值
            4. 字符串 -> 添加引号
            5. 其他类型 -> 直接str()转换
            """
            if isinstance(value, BaseDescription):
                return value.reverse()
            elif isinstance(value, (list, tuple)):
                items = [format_value(item) for item in value]
                return f"[{', '.join(items)}]"
            elif isinstance(value, dict):
                items = [f'"{k}": {format_value(v)}' for k, v in value.items()]
                return f"{{{', '.join(items)}}}"
            elif isinstance(value, str):
                return f'"{value}"'
            else:
                return str(value)

        def format_param_default(key, value, is_base_only):
            """格式化参数默认值"""
            if is_base_only:
                return f"{key}=None"
                
            if isinstance(value, dict) and 'default' in value:
                default = value['default']
                if isinstance(default, str):
                    return f'{key}="{default}"'
                return f"{key}={default if default is not None else 'None'}"
            elif isinstance(value, str):
                if value.startswith('@'):
                    return f"{key}={value.lstrip('@')}"
                return f'{key}="{value}"'
            else:
                return f"{key}={format_value(value)}"
        # 生成导入语句
        imports = "from src.extractor.base_class import BaseDescription\n\n"
        # 主要导出逻辑
        class_definitions = []
        for class_name, data in self.register_dict.items():
            # 获取类信息
            attributes = data.get("attributes", {})
            base = data.get("base") or {}
            base_name = base.get("name", "BaseDescription")
            base_attributes = base.get("attributes", {})
            
            # 生成类定义
            class_definition = f"class {class_name}({base_name}):\n"
            
            # 判断是否仅继承BaseDescription
            is_base_only = base_name == "BaseDescription"
            
            # 生成当前类参数
            current_params = ", ".join(
                format_param_default(key, value, is_base_only)
                for key, value in attributes.items()
            )
            
            # 生成父类参数
            if not is_base_only:
                super_params = ", ".join(
                    format_param_default(key, value, False)
                    for key, value in base_attributes.items()
                )
            
            # 生成__init__方法
            if current_params:
                class_definition += f"    def __init__(self, {current_params}):\n"
                if not is_base_only:
                    class_definition += f"        super().__init__({super_params})\n"
                for key in attributes.keys():
                    class_definition += f"        self.{key} = {key}\n"
            else:
                class_definition += f"    def __init__(self, {current_params}):\n"
                for key in attributes.keys():
                    class_definition += f"        self.{key} = {key}\n"

            class_definitions.append(class_definition)

        # 写入文件
        complete_class_definitions = imports + "\n\n".join(class_definitions)
        with open(self.export_file, "w") as f:
            f.write(complete_class_definitions)
        print(f"Classes successfully written to {self.export_file}")

#=============================================
# 3. 主函数
#=============================================
def setup_files(config: ConfigManager):
    """设置要处理的文件和命名空间"""
    # 1. 测试文件
    config.add_file("M20250403/test.ndf", "/")
    
    # 2. 游戏系统数据
    game_system_files = [
        # ("GameData/Generated/Gameplay/Gfx/CapaciteList.ndf", "/gameplay/gfx/aura"),  # 光环
        # ("GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf", "/gameplay/gfx/effect"),  # 效果
        # ("GameData/Generated/Gameplay/Gfx/ConditionsDescriptor.ndf", "/gameplay/gfx/condition"),  # 条件
        # ("GameData/Generated/Gameplay/Gfx/Ammunition.ndf", "/gameplay/gfx/ammo"),  # 弹药
        # ("GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf", "/gameplay/gfx/missile"),  # 导弹
        # ("GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf", "/gameplay/gfx/weapon"),  # 武器
        # ("GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf", "/gameplay/gfx/unit"),  # 单位
    ]
    
    # 3. 战斗编制数据
    division_files = [
        # ("GameData/Generated/Gameplay/Decks/Divisions.ndf", "/gameplay/division/deck"),  # 师卡组
        # ("GameData/Generated/Gameplay/Decks/DivisionRules.ndf", "/gameplay/division/rule"),  # 师规则
        # ("GameData/Generated/Gameplay/Decks/DivisionCostMatrix.ndf", "/gameplay/division/cost"),  # 费用
    ]
    
    # 4. 伤害系统数据
    damage_files = [
        # ("GameData/Generated/Gameplay/Gfx/DamageLevels.ndf", "/gameplay/damage/level"),  # 伤害等级
        # ("GameData/Generated/Gameplay/Gfx/DamageResistance.ndf", "/gameplay/damage/resistance"),  # 防御
        # ("GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyListImpl.ndf", "/gameplay/damage/family"),  # 家族
        # ("GameData/Generated/Gameplay/Gfx/DamageStairTypeEvolutionOverRangeDescriptor.ndf", "/gameplay/damage/penetration"),  # 穿透
    ]
    
    # 5. 地形系统数据
    # config.add_file("M20250403/GameData/Gameplay/Terrains/Terrains.ndf", "/gameplay/terrain")
    
    # 6. 暴击系统数据
    critical_files = [
        # ("GameData/Gameplay/Unit/CriticalModules/TemplateCriticalEffectModules.ndf", "/gameplay/critical/template"),
        # ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Airplane.ndf", "/gameplay/critical/air"),
        # ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_GroundUnit.ndf", "/gameplay/critical/ground"),
        # ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Helico.ndf", "/gameplay/critical/helicopter"),
        # ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Infanterie.ndf", "/gameplay/critical/infantry"),
    ]
    
    # 7. 游戏常量数据
    constant_files = [
        # ("GameData/Gameplay/Constantes/Strategic/GDConstantes.ndf", "/gameplay/const/strategic"),
        # ("GameData/Gameplay/Constantes/Airplane.ndf", "/gameplay/const/air"),
        # ("GameData/Gameplay/Constantes/Deroute.ndf", "/gameplay/const/rout"),
        # ("GameData/Gameplay/Constantes/EvaluationMenace.ndf", "/gameplay/const/threat"),
        # ("GameData/Gameplay/Constantes/FactoryResources.ndf", "/gameplay/const/resource"),
        # ("GameData/Gameplay/Constantes/ActionPointConsumptionGrid.ndf", "/gameplay/const/ap/grid"),
        # ("GameData/Gameplay/Constantes/ActionPointConsumptionGridRefs.ndf", "/gameplay/const/ap/ref"),
        # ("GameData/Gameplay/Constantes/GDConstantes.ndf", "/gameplay/const/global"),
        # ("GameData/Gameplay/Constantes/HitRollConstants.ndf", "/gameplay/const/hitroll"),
        # ("GameData/Gameplay/Constantes/Ravitaillement.ndf", "/gameplay/const/supply"),
        # ("GameData/Gameplay/Constantes/Transport.ndf", "/gameplay/const/transport/hit"),
        # ("GameData/Gameplay/Constantes/TransportConstantes.ndf", "/gameplay/const/transport/base"),
        # ("GameData/Gameplay/Constantes/VisionConstantes.ndf", "/gameplay/const/vision"),
        # ("GameData/Gameplay/Constantes/WeaponConstantes.ndf", "/gameplay/const/weapon"),
        # ("GameData/Gameplay/Unit/AirplaneConstantes.ndf", "/gameplay/const/aircraft"),
        # ("GameData/Gameplay/Unit/DamageModules.ndf", "/gameplay/const/damage"),
        # ("GameData/Gameplay/Constantes/WeaponTypePriorities.ndf", "/gameplay/const/priority"),
        # ("GameData/Gameplay/Constantes/WreckageConstants.ndf", "/gameplay/const/wreck"),
    ]
    
    # 8. 其他系统数据
    other_files = [
        # ("GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf", "/gameplay/gfx/building"),
        # ("GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf", "/gameplay/gfx/experience"),
        # ("GameData/Gameplay/Unit/Tactic/DistrictDescriptor.ndf", "/gameplay/district"),
        # ("GameData/Generated/Gameplay/Gfx/FireDescriptor.ndf", "/gameplay/gfx/fire"),
        # ("GameData/Generated/Gameplay/Gfx/SmokeDescriptor.ndf", "/gameplay/gfx/smoke"),
        # ("GameData/Generated/Gameplay/Gfx/MissileCarriage.ndf", "/gameplay/gfx/carriage"),
    ]
    
    # 批量添加文件和命名空间
    for file_list in [game_system_files, division_files, damage_files, 
                      critical_files, constant_files, other_files]:
        for file, namespace in file_list:
            config.add_file(f"M20250403/{file}", namespace)

def main():
    """主函数"""
    # 获取配置实例
    config = ConfigManager().get_instance()
    
    # # 打印当前Python路径
    # print("Python路径:", sys.path)
    
    # # 打印已加载模块
    # print("已加载模块:")
    # for name, module in sys.modules.items():
    #     if 'test_class' in name:
    #         print(f"- {name}: {module}")
            
    # # 尝试显式导入test_class
    # try:
    #     from src.extractor.test_class import TChildTemplate
    #     print("成功导入 TChildTemplate")
    # except ImportError as e:
    #     print("导入失败:", str(e))
        
    
    # 设置文件和命名空间
    setup_files(config)
    
    # 创建管理器
    manager = Manager(
        file_list=config.process_file_list,
        # 无需指定完整路径,Manager会自动处理
        register_file="register.pkl",
        generate_file="global.pkl",
        log_file="log.txt",
        export_file="TClass.py"
    )
    
    # 执行处理流程
    manager.check_file_exist()
    manager.register(reference=manager)
    manager.save(mode="register")
    manager.generate(reference=manager)
    manager.save(mode="generate")
    manager.dict = {}
    manager.load(mode="generate")
    x = 1
    print(x)

if __name__ == "__main__":
    main()