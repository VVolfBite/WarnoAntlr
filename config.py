WORK_DIRECTORY = "D:/WarnoAntlr-main"
RAW_DATA_PATH = WORK_DIRECTORY + "/data/raw/V135139"
EXTRACT_DATA_PATH = WORK_DIRECTORY + "/data/extract/V135139"
PROCESSED_DATA_PATH = WORK_DIRECTORY + "/data/processed/V135139"

CLASS_REGISTER_PATH =  WORK_DIRECTORY + "/src/parsers/register_class"
CLASS_JSON = CLASS_REGISTER_PATH + '/Rclass.json'
CLASS_PY = CLASS_REGISTER_PATH + '/Rclass.py'

PROCESS_FILE_LIST = [    
    "/template_test.ndf",

    # "/GameData/Generated/Gameplay/Gfx/CapaciteList.ndf", # 光环
    # "/GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf", # 效果
    # # "/GameData/Generated/Gameplay/Gfx/ConditionsDescriptor.ndf", # 条件
    # "/GameData/Generated/Gameplay/Gfx/Ammunition.ndf", # 弹药
    # "/GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf", # 导弹
    # "/GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf", # 武器
    # "/GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf", # 单位 
    # "/GameData/Generated/Gameplay/Decks/Divisions.ndf", # 师卡组数
    # "/GameData/Generated/Gameplay/Decks/DivisionPacks.ndf", # 师/卡组包  
    # "/GameData/Generated/Gameplay/Decks/DivisionRules.ndf", # 师卡组经验修正  
    # "/GameData/Generated/Gameplay/Decks/DivisionCostMatrix.ndf", # 师费用矩阵
    # "/GameData/Generated/Gameplay/Gfx/DamageLevels.ndf", # 伤害等级
    # "/GameData/Generated/Gameplay/Gfx/DamageResistance.ndf", # 伤害防御表
    # "/GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyListImpl.ndf", # 伤害防御列表
    # "/GameData/Generated/Gameplay/Gfx/DamageStairTypeEvolutionOverRangeDescriptor.ndf", # 穿深进化表
    # "/GameData/Gameplay/Constantes/Strategic/GDConstantes.ndf",
    # "/GameData/Gameplay/Constantes/Airplane.ndf",
    # "/GameData/Gameplay/Constantes/Deroute.ndf",
    # "/GameData/Gameplay/Constantes/EvaluationMenace.ndf",
    # "/GameData/Gameplay/Constantes/FactoryResources.ndf",
    # "/GameData/Gameplay/Constantes/ActionPointConsumptionGrid.ndf",
    # "/GameData/Gameplay/Constantes/ActionPointConsumptionGridRefs.ndf",
    # "/GameData/Gameplay/Constantes/GDConstantes.ndf", # 全局规则
    # "/GameData/Gameplay/Constantes/HitRollConstants.ndf", # 命中概率修正
    # "/GameData/Gameplay/Constantes/ModificateursJetPourToucher.ndf", # 距离修正曲线
    # "/GameData/Gameplay/Constantes/Ravitaillement.ndf", # 补给规则
    # "/GameData/Gameplay/Constantes/Transport.ndf", # 载具受击
    # "/GameData/Gameplay/Constantes/TransportConstantes.ndf", # 载具基础
    # "/GameData/Gameplay/Constantes/VisionConstantes.ndf", # 视野基础
    # "/GameData/Gameplay/Constantes/WeaponConstantes.ndf", # 武器基础
    # "/GameData/Gameplay/Unit/AirplaneConstantes.ndf", # 飞机基础
    # "/GameData/Gameplay/Unit/DamageModules.ndf", # 伤害基础
    # "/GameData/Gameplay/Constantes/WeaponTypePriorities.ndf", # 优先级
    # "/GameData/Gameplay/Constantes/WreckageConstants.ndf", # 载具受击
    # "/GameData/Gameplay/Terrains/Terrains.ndf", # 地形
    # "/GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Airplane.ndf", # 飞机暴击模型
    # "/GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_GroundUnit.ndf", # 地面暴击模型
    # "/GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Helico.ndf", # 直升机暴击模型
    # "/GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Infanterie.ndf", # 步兵暴击模型
    # "/GameData/Gameplay/Unit/Tactic/Fire.ndf", # 火焰
    # "/GameData/Gameplay/Unit/Tactic/Smoke.ndf", # 烟雾
    # "/GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf", # FOB等建筑
    # "/GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf", # 经验等级包
    # "/GameData/Generated/Gameplay/Gfx/DistrictsDescriptor.ndf", # 街区定义数据
    # "/GameData/Generated/Gameplay/Gfx/FireDescriptor.ndf", # 火
    # "/GameData/Generated/Gameplay/Gfx/SmokeDescriptor.ndf", # 烟雾
    # "/GameData/Generated/Gameplay/Gfx/MissileCarriage.ndf", # 导弹挂载
]