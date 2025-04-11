import os
from pathlib import Path
import sys
from typing import Dict, List, Tuple, Optional, Union

class ConfigManager:
    """配置管理类"""
    _instance = None
    
    @classmethod
    def get_instance(cls) -> 'ConfigManager':
        """获取单例实例"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        """初始化配置管理器"""
        # 基础路径配置
        self.project_root = Path(__file__).parent.parent.parent
        self.data_dir = self.project_root / "data"
        self.output_dir = self.project_root / "output"
        self.src_path = self.project_root / "src"
        
        # 添加到 Python 路径
        if str(self.project_root) not in sys.path:
            sys.path.append(str(self.project_root))
        
        # 文件路径配置
        self.parser_path = self.src_path / "parsers"
        self.extractor_path = self.src_path / "extractor"  # 添加提取器路径
        
        # 类文件配置
        self.class_file_names = [
            "base_class.py",      # 基础类
            "backup_class.py",    # 备份类
            "refined_class.py",   # 优化类
            "extract_class.py",   # 提取类
            "test_class.py",      # 测试类
        ]
        
        # 版本路径
        self.version = None  # 默认版本
        
        # 文件配置
        self.process_file_list: List[Tuple[str, str]] = []
        
        # 批次配置
        self.batches = {
            # "test": {
            #     "files": [
            #         ("test.ndf", "/test")
            #     ],
            #     "export_file": "test_class.py"
            # },
            "constants": {
                "files": [
                    ("GameData/Gameplay/Constantes/Airplane.ndf", "$"),
                    ("GameData/Gameplay/Constantes/Deroute.ndf", "$"),
                    ("GameData/Gameplay/Constantes/EvaluationMenace.ndf", "$"),
                    ("GameData/Gameplay/Constantes/FactoryResources.ndf", "$"),
                    ("GameData/Gameplay/Constantes/GDConstantes.ndf", "$/GFX/Constantes"),
                    ("GameData/Gameplay/Constantes/HitRollConstants.ndf", "$/GFX/Constantes"),
                ],
                "export_file": "constant_class.py"
            },
            "effects": {
                "files": [
                    ("GameData/Generated/Gameplay/Gfx/CapaciteList.ndf", "$/GFX/EffectCapacity"),
                    ("GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf", "$/GFX/EffectCapacity"),
                    ("GameData/Generated/Gameplay/Gfx/ConditionsDescriptor.ndf", "$/GFX/EffectCapacity"),
                ],
                "export_file": "effect_class.py"
            },
            "unit_consts": {
                "files": [
                    ("GameData/Gameplay/Unit/CriticalModules/TemplateCriticalEffectModules.ndf", "$/GFX/UnitConstantes"),
                    ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Airplane.ndf", "$/GFX/UnitConstantes"),
                    ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_GroundUnit.ndf", "$/GFX/UnitConstantes"),
                    ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Helico.ndf", "$/GFX/UnitConstantes"),
                    ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Infanterie.ndf", "$/GFX/UnitConstantes"),
                ],
                "export_file": "unit_const_class.py"
            },
            "weapons": {
                "files": [
                    ("GameData/Generated/Gameplay/Gfx/Ammunition.ndf", "$/GFX/Weapon"),  # 弹药
                    ("GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf", "$/GFX/Weapon"),  # 导弹
                    ("GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf", "$/GFX/Weapon"),  # 武器
                    ("GameData/Generated/Gameplay/Gfx/DamageStairTypeEvolutionOverRangeDescriptor.ndf", "$/GFX/Weapon"),  # 穿透
                    ("GameData/Generated/Gameplay/Gfx/FireDescriptor.ndf", "$/GFX/Weapon"),  # 火
                    ("GameData/Generated/Gameplay/Gfx/SmokeDescriptor.ndf", "$/GFX/Weapon"),  # 烟雾
                    ("GameData/Gameplay/Constantes/Ravitaillement.ndf", "$/GFX/Weapon"),  # 补给规则
                ],
                "export_file": "weapon_class.py"
            },
            "units": {
                "files": [
                    ("GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf", "$/GFX/Unit"),  # 单位
                    ("GameData/Generated/Gameplay/Gfx/DamageLevels.ndf", "$/GFX/Unit"),  # 伤害等级
                    ("GameData/Generated/Gameplay/Gfx/DamageResistance.ndf", "$/GFX/Unit"),  # 防御
                    ("GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyListImpl.ndf", "$/GFX/Unit"),  # 家族
                    ("GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf", "$/GFX/Unit"),  # FOB等建筑
                    ("GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf", "$/GFX/Unit"),  # 经验等级
                    ("GameData/Gameplay/Unit/Tactic/DistrictDescriptor.ndf", "$/GFX/Unit"),  # 街区定义
                ],
                "export_file": "unit_class.py"
            },
            "decks": {
                "files": [
                    ("GameData/Generated/Gameplay/Decks/Divisions.ndf", "$/Deck"),  # 师卡组
                    ("GameData/Generated/Gameplay/Decks/DivisionRules.ndf", "$/Deck"),  # 师规则
                    ("GameData/Generated/Gameplay/Decks/DivisionCostMatrix.ndf", "$/Deck"),  # 费用
                ],
                "export_file": "deck_class.py"
            }
        }
    
    def set_version(self, version: str):
        """设置版本并创建相应目录"""
        version_dir = self.data_dir / version
        if not version_dir.exists():
            raise ValueError(f"Version directory not found: {version}")
        self.version = version
        # 创建版本对应的输出目录
        version_output_dir = self.output_dir / version
        version_output_dir.mkdir(parents=True, exist_ok=True)
        return self

    def get_data_dir(self) -> Path:
        """获取当前版本的数据目录"""
        if not self.version:
            raise ValueError("Version not set")
        return self.data_dir / self.version

    def add_file(self, file_path: str, namespace: str = "/") -> None:
        """添加要处理的文件
        
        Args:
            file_path: 相对于data目录的文件路径
            namespace: 命名空间
        """
        self.process_file_list.append((file_path, namespace))
    
    def get_full_path(self, file_path: Union[str, Path]) -> Path:
        """获取数据文件的完整路径"""
        if not self.version:
            raise ValueError("Version not set")
        return self.data_dir / self.version / file_path
    
    def get_output_path(self, file_name: str) -> Path:
        """获取输出文件的完整路径"""
        if not self.version:
            raise ValueError("Version not set")
        return self.output_dir / self.version / file_name

    def get_batch_files(self, batch_name: str) -> List[Tuple[str, str]]:
        """获取指定批次的文件列表"""
        if batch_name not in self.batches:
            raise ValueError(f"Unknown batch: {batch_name}")
        return self.batches[batch_name]["files"]
    
    def get_batch_export_file(self, batch_name: str) -> str:
        """获取指定批次的导出文件名"""
        if batch_name not in self.batches:
            raise ValueError(f"Unknown batch: {batch_name}")
        return self.batches[batch_name]["export_file"]
    
    def get_batch_names(self) -> List[str]:
        """获取所有批次名称"""
        return list(self.batches.keys())