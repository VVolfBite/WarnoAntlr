"""配置管理器模块
管理项目配置、路径和批次处理

主要功能:
1. 版本管理 - 游戏版本和路径配置
2. 批次配置 - NDF文件批次定义
"""

import sys
from pathlib import Path
from typing import Dict, List, Tuple

class ConfigManager:
    """配置管理类"""
    def __init__(self, version: str):
        self.version = version
        self._init_paths()
        
    def _init_paths(self):
        """初始化基础路径"""
        # 基础路径
        self.project_root = Path(__file__).parent.parent.parent
        self.data_dir = self.project_root / "data"
        self.output_dir = self.project_root / "output"
        self.src_path = self.project_root / "src"
        
        # 版本相关路径
        self.version_data_dir = self.data_dir / self.version
        self.version_output_dir = self.output_dir / self.version
        
        # 检查版本目录
        if not self.version_data_dir.exists():
            raise ValueError(f"Version directory not found: {self.version}")
            
        # 创建输出目录
        self.version_output_dir.mkdir(parents=True, exist_ok=True)
        
        # Python路径配置
        if str(self.project_root) not in sys.path:
            sys.path.append(str(self.project_root))
            
        # 提取类相关路径
        self.extractor_path = self.src_path / "extractor"
        self.extract_class_path = self.extractor_path / "extract_class.py"
        
        # 类文件名配置
        self.class_file_names = [
            "extract_class.py",  # 当前使用的提取类文件
            "backup_class.py",   # 备份的提取类文件
            "refined_class.py",  # 精炼的提取类文件
        ]

    @property
    def batches(self) -> Dict[str, Dict]:
        """获取批次配置"""
        return {
            "effects": {
                "files": [
                    ("GameData/Generated/Gameplay/Gfx/ConditionsDescriptor.ndf", "$/GFX/EffectCapacity"),
                    ("GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf", "$/GFX/EffectCapacity"),
                    ("GameData/Generated/Gameplay/Gfx/CapaciteList.ndf", "$/GFX/EffectCapacity"),
                ],
                "output_file": "effect_class.py"
            },
            "unit_consts": {
                "files": [
                    ("GameData/Gameplay/Unit/CriticalModules/TemplateCriticalEffectModules.ndf", "$/GFX/UnitConstantes"),
                    ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_GroundUnit.ndf", "$/GFX/UnitConstantes"),
                    ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Airplane.ndf", "$/GFX/UnitConstantes"),
                    ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Helico.ndf", "$/GFX/UnitConstantes"),
                    ("GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Infanterie.ndf", "$/GFX/UnitConstantes"),
                ],
                "output_file": "unit_const_class.py"
            },
            "weapons": {
                "files": [
                    ("GameData/Generated/Gameplay/Gfx/DamageStairTypeEvolutionOverRangeDescriptor.ndf", "$/GFX/Weapon"),
                    ("GameData/Generated/Gameplay/Gfx/FireDescriptor.ndf", "$/GFX/Weapon"),
                    ("GameData/Generated/Gameplay/Gfx/SmokeDescriptor.ndf", "$/GFX/Weapon"),    
                    ("GameData/Generated/Gameplay/Gfx/Ammunition.ndf", "$/GFX/Weapon"),
                    ("GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf", "$/GFX/Weapon"),
                    ("GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf", "$/GFX/Weapon"),
                    ("GameData/Gameplay/Constantes/Ravitaillement.ndf", "$/GFX/Weapon"),
                ],
                "output_file": "weapon_class.py"
            },
            "units": {
                "files": [
                    ("GameData/Generated/Gameplay/Gfx/DamageLevels.ndf", "$/GFX/Unit"),
                    ("GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf", "$/GFX/Unit"),                
                    ("GameData/Generated/Gameplay/Gfx/DamageResistance.ndf", "$/GFX/Unit"),
                    ("GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyListImpl.ndf", "$/GFX/Unit"),                
                    ("GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf", "$/GFX/Unit"),
                    ("GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf", "$/GFX/Unit"),
                    ("GameData/Gameplay/Unit/Tactic/DistrictDescriptor.ndf", "$/GFX/Unit"),
                ],
                "output_file": "unit_class.py"
            },
            "decks": {
                "files": [
                    ("GameData/Generated/Gameplay/Decks/Divisions.ndf", "$/Deck"),
                    ("GameData/Generated/Gameplay/Decks/DivisionRules.ndf", "$/Deck"),
                    ("GameData/Generated/Gameplay/Decks/DivisionCostMatrix.ndf", "$/Deck"),
                ],
                "output_file": "deck_class.py"
            }
        }

    def get_batch_files(self, batch_name: str) -> List[Tuple[str, str]]:
        """获取批次文件列表"""
        if batch_name not in self.batches:
            raise ValueError(f"Unknown batch: {batch_name}")
        return self.batches[batch_name]["files"]
    
    def get_batch_output_file(self, batch_name: str) -> str:
        """获取批次输出文件名"""
        if batch_name not in self.batches:
            raise ValueError(f"Unknown batch: {batch_name}")
        return self.batches[batch_name]["output_file"]
    
    def get_batch_names(self) -> List[str]:
        """获取所有批次名称"""
        return list(self.batches.keys())