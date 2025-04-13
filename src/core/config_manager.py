"""配置管理器模块
管理项目配置、路径和批次处理

主要功能:
1. 路径管理 - 项目各类路径的管理
2. 批次管理 - NDF文件批次处理配置
3. 版本管理 - 不同版本数据的管理
"""

import os
from pathlib import Path
import sys
from typing import Dict, List, Tuple, Optional, Union

class ConfigManager:
    """配置管理类"""
    _instance = None
    
    @classmethod
    def get_instance(cls, version: Optional[str] = None) -> 'ConfigManager':
        """获取单例实例
        Args:
            version: 版本号,如果实例不存在则用于初始化,如果实例存在则更新版本
        """
        if cls._instance is None:
            cls._instance = cls(version)
        elif version is not None:
            cls._instance.set_version(version)
        return cls._instance
    
    def __init__(self, version: Optional[str] = None):
        """初始化配置管理器
        Args:
            version: 初始版本号
        """
        # 初始化基础配置
        self._init_paths()
        self._init_files()
        self._init_batches()
        
        # 设置版本(如果提供)
        if version is not None:
            self.set_version(version)
        
    #-------------------------
    # 1. 基础设施
    #-------------------------
    def _init_paths(self):
        """初始化路径配置"""
        # 基础路径
        self.project_root = Path(__file__).parent.parent.parent
        self.data_dir = self.project_root / "data"
        self.output_dir = self.project_root / "output"
        self.src_path = self.project_root / "src"
        
        # 功能路径
        self.parser_path = self.src_path / "parsers"
        self.extractor_path = self.src_path / "extractor"
        
        # Python路径配置
        if str(self.project_root) not in sys.path:
            sys.path.append(str(self.project_root))
            
    def _init_files(self):
        """初始化文件配置"""
        # 类文件
        self.class_file_names = [
            "base_class.py",      # 基础类
            "backup_class.py",    # 备份类
            "refined_class.py",   # 优化类
            "extract_class.py",   # 提取类
            "test_class.py",      # 测试类
        ]
        
        # 版本和处理列表
        self.version = None
        self.process_file_list: List[Tuple[str, str]] = []
        
    def _init_batches(self):
        """初始化批次配置"""
        self.batches = {
            # "constants": self._get_constants_batch(),
            # "effects": self._get_effects_batch(),
            # "unit_consts": self._get_unit_consts_batch(),
            # "weapons": self._get_weapons_batch(),
            "units": self._get_units_batch(),
            "decks": self._get_decks_batch()
        }
        
    #-------------------------
    # 2. 版本管理
    #-------------------------
    def set_version(self, version: str) -> 'ConfigManager':
        """设置版本"""
        version_dir = self.data_dir / version
        if not version_dir.exists():
            raise ValueError(f"Version directory not found: {version}")
        self.version = version
        
        # 创建输出目录
        version_output_dir = self.output_dir / version
        version_output_dir.mkdir(parents=True, exist_ok=True)
        return self
        
    def get_data_dir(self) -> Path:
        """获取数据目录"""
        if not self.version:
            raise ValueError("Version not set")
        return self.data_dir / self.version
        
    #-------------------------
    # 3. 文件管理
    #-------------------------
    def add_file(self, file_path: str, namespace: str = "/") -> None:
        """添加处理文件"""
        self.process_file_list.append((file_path, namespace))
    
    def get_full_path(self, file_path: Union[str, Path]) -> Path:
        """获取完整路径"""
        if not self.version:
            raise ValueError("Version not set")
        return self.data_dir / self.version / file_path
    
    def get_output_path(self, file_name: str) -> Path:
        """获取输出路径"""
        if not self.version:
            raise ValueError("Version not set")
        return self.output_dir / self.version / file_name
        
    #-------------------------
    # 4. 批次管理
    #-------------------------
    def get_batch_files(self, batch_name: str) -> List[Tuple[str, str]]:
        """获取批次文件"""
        if batch_name not in self.batches:
            raise ValueError(f"Unknown batch: {batch_name}")
        return self.batches[batch_name]["files"]
    
    def get_batch_export_file(self, batch_name: str) -> str:
        """获取批次导出文件"""
        if batch_name not in self.batches:
            raise ValueError(f"Unknown batch: {batch_name}")
        return self.batches[batch_name]["export_file"]
    
    def get_batch_names(self) -> List[str]:
        """获取所有批次名称"""
        return list(self.batches.keys())
        
    #-------------------------
    # 5. 批次定义
    #-------------------------

        
    def _get_effects_batch(self) -> Dict:
        """效果批次配置"""
        return {
            "files": [
                ("GameData/Generated/Gameplay/Gfx/ConditionsDescriptor.ndf", "$/GFX/EffectCapacity"),
                ("GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf", "$/GFX/EffectCapacity"),
                ("GameData/Generated/Gameplay/Gfx/CapaciteList.ndf", "$/GFX/EffectCapacity"),
            ],
            "export_file": "effect_class.py"
        }
    
    def _get_constants_batch(self) -> Dict:
        """常量批次配置"""
        return {
            "files": [
                ("GameData/Gameplay/Constantes/Airplane.ndf", "$"),
                ("GameData/Gameplay/Constantes/Deroute.ndf", "$"),
                ("GameData/Gameplay/Constantes/EvaluationMenace.ndf", "$"),
                ("GameData/Gameplay/Constantes/FactoryResources.ndf", "$"),
                ("GameData/Gameplay/Constantes/HitRollConstants.ndf", "$/GFX/Constantes"),
                ("GameData/Gameplay/Constantes/GDConstantes.ndf", "$/GFX/Constantes"),
            ],
            "export_file": "constant_class.py"
        }    
        
    def _get_unit_consts_batch(self) -> Dict:
        """单位常量批次配置"""
        return {
            "files": [
                ("GameData/Gameplay/Unit/CriticalModules/TemplateCriticalEffectModules.ndf", "$/GFX/UnitConstantes"),
                ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_GroundUnit.ndf", "$/GFX/UnitConstantes"),
                ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Airplane.ndf", "$/GFX/UnitConstantes"),
                ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Helico.ndf", "$/GFX/UnitConstantes"),
                ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Infanterie.ndf", "$/GFX/UnitConstantes"),
            ],
            "export_file": "unit_const_class.py"
        }
        
    def _get_weapons_batch(self) -> Dict:
        """武器批次配置"""
        return {
            "files": [
                ("GameData/Generated/Gameplay/Gfx/DamageStairTypeEvolutionOverRangeDescriptor.ndf", "$/GFX/Weapon"),
                ("GameData/Generated/Gameplay/Gfx/FireDescriptor.ndf", "$/GFX/Weapon"),
                ("GameData/Generated/Gameplay/Gfx/SmokeDescriptor.ndf", "$/GFX/Weapon"),    
                ("GameData/Generated/Gameplay/Gfx/Ammunition.ndf", "$/GFX/Weapon"),
                ("GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf", "$/GFX/Weapon"),
                ("GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf", "$/GFX/Weapon"),
                ("GameData/Gameplay/Constantes/Ravitaillement.ndf", "$/GFX/Weapon"),
            ],
            "export_file": "weapon_class.py"
        }
        
    def _get_units_batch(self) -> Dict:
        """单位批次配置"""
        return {
            "files": [
                ("GameData/Generated/Gameplay/Gfx/DamageLevels.ndf", "$/GFX/Unit"),
                ("GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf", "$/GFX/Unit"),                
                ("GameData/Generated/Gameplay/Gfx/DamageResistance.ndf", "$/GFX/Unit"),
                ("GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyListImpl.ndf", "$/GFX/Unit"),                
                ("GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf", "$/GFX/Unit"),
                ("GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf", "$/GFX/Unit"),
                ("GameData/Gameplay/Unit/Tactic/DistrictDescriptor.ndf", "$/GFX/Unit"),
            ],
            "export_file": "unit_class.py"
        }
        
    def _get_decks_batch(self) -> Dict:
        """卡组批次配置"""
        return {
            "files": [
                ("GameData/Generated/Gameplay/Decks/Divisions.ndf", "$/Deck"),
                ("GameData/Generated/Gameplay/Decks/DivisionRules.ndf", "$/Deck"),
                ("GameData/Generated/Gameplay/Decks/DivisionCostMatrix.ndf", "$/Deck"),
            ],
            "export_file": "deck_class.py"
        }