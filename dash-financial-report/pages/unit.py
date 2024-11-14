from ast import Mod, Pass
from re import M
from dash import dcc
from dash import html
import plotly.graph_objs as go
from utils import *
from typing import Counter, Union

import sys

WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)

from src.extractor.refined_class import *
from pages import ammunition, weapon


# 基础信息
class TTypeUnitModuleDescriptorComponment:
    def __init__(self, TTypeUnitModuleDescriptor: TTypeUnitModuleDescriptor):
        self.TTypeUnitModuleDescriptor = TTypeUnitModuleDescriptor

        self.TRMotherCountry = Table_Row(
            "所属国家", show_value(TTypeUnitModuleDescriptor.MotherCountry)
        )
        self.TRAcknowUnitType = Table_Row(
            "所属类型", show_value(TTypeUnitModuleDescriptor.AcknowUnitType)
        )


class TTagsModuleDescriptorComponment:
    def __init__(self, TTagsModuleDescriptor: TTagsModuleDescriptor):
        self.TTagsModuleDescriptor = TTagsModuleDescriptor

        self.TRTagSet = Table_Row("单位词条", show_value(TTagsModuleDescriptor.TagSet))


# 伤害信息
class TBaseDamageModuleDescriptorComponment:
    def __init__(self, TBaseDamageModuleDescriptor: TBaseDamageModuleDescriptor):
        self.TBaseDamageModuleDescriptor = TBaseDamageModuleDescriptor

        self.TRMaxPhysicalDamages = Table_Row(
            "单位生命量", show_value(TBaseDamageModuleDescriptor.MaxPhysicalDamages)
        )
        self.TRMaxSuppressionDamages = Table_Row(
            "单位压制量", show_value(TBaseDamageModuleDescriptor.MaxSuppressionDamages)
        )
        self.TRMaxStunDamages = Table_Row(
            "单位震撼量", show_value(TBaseDamageModuleDescriptor.MaxStunDamages)
        )
        self.TRPhysicalDamageLevelsPack = Table_Row(
            "生命损失等级效果包",
            show_value(TBaseDamageModuleDescriptor.PhysicalDamageLevelsPack),
        )
        self.TRSuppressDamageLevelsPack = Table_Row(
            "压制损失等级效果包",
            show_value(TBaseDamageModuleDescriptor.SuppressDamageLevelsPack),
        )
        self.TRStunDamageLevelsPack = Table_Row(
            "压制损失等级效果包",
            show_value(TBaseDamageModuleDescriptor.StunDamageLevelsPack),
        )


class TDamageModuleDescriptorComponment:
    def __init__(self, TDamageModuleDescriptor: TDamageModuleDescriptor):
        self.TDamageModuleDescriptor = TDamageModuleDescriptor

        self.TRMaxPhysicalDamages = Table_Row(
            "压制恢复速率",
            show_value(TDamageModuleDescriptor.SuppressDamagesRegenRatio),
        )
        self.TRStunDamagesRegen = Table_Row(
            "震撼恢复速率", show_value(TDamageModuleDescriptor.StunDamagesRegen)
        )
        self.TRResistanceFront_Family = Table_Row(
            "正面护甲族",
            show_value(
                TDamageModuleDescriptor.BlindageProperties.ResistanceFront.Family
            ),
        )
        self.TRResistanceFront_Index = Table_Row(
            "正面护甲索引值",
            show_value(
                TDamageModuleDescriptor.BlindageProperties.ResistanceFront.Index
            ),
        )
        self.TRResistanceSides_Family = Table_Row(
            "侧面护甲族",
            show_value(
                TDamageModuleDescriptor.BlindageProperties.ResistanceSides.Family
            ),
        )
        self.TRResistanceSides_Index = Table_Row(
            "侧面护甲索引值",
            show_value(
                TDamageModuleDescriptor.BlindageProperties.ResistanceSides.Index
            ),
        )
        self.TRResistanceRear_Family = Table_Row(
            "尾面护甲族",
            show_value(
                TDamageModuleDescriptor.BlindageProperties.ResistanceRear.Family
            ),
        )
        self.TRResistanceRear_Index = Table_Row(
            "尾面护甲索引值",
            show_value(TDamageModuleDescriptor.BlindageProperties.ResistanceRear.Index),
        )
        self.TRResistanceTop_Family = Table_Row(
            "顶面护甲族",
            show_value(TDamageModuleDescriptor.BlindageProperties.ResistanceTop.Family),
        )
        self.TRResistanceTop_Index = Table_Row(
            "顶面护甲索引值",
            show_value(TDamageModuleDescriptor.BlindageProperties.ResistanceTop.Index),
        )
        self.TRExplosiveReactiveArmor = Table_Row(
            "爆炸反应装甲",
            show_value(
                TDamageModuleDescriptor.BlindageProperties.ExplosiveReactiveArmor
            ),
        )
        self.TRHitRollECM = Table_Row(
            "ECM修正", show_value(TDamageModuleDescriptor.HitRollECM)
        )
        self.TRAutoOrientation = Table_Row(
            "自动对敌", show_value(TDamageModuleDescriptor.AutoOrientation)
        )
        self.TRUseTopArmorAgainstFire = Table_Row(
            "使用顶甲计算火焰伤害",
            show_value(TDamageModuleDescriptor.UseTopArmorAgainstFire),
        )


class TemplateUnitCriticalModuleComponment:
    def __init__(self, TemplateUnitCriticalModule: TemplateUnitCriticalModule):
        self.TemplateUnitCriticalModule = TemplateUnitCriticalModule

        self.TRModule = Table_Row(
            "暴击效果模组", show_value(TemplateUnitCriticalModule.Module)
        )


class TRoutModuleDescriptorComponment:
    def __init__(self, TRoutModuleDescriptor: TRoutModuleDescriptor):
        self.TRoutModuleDescriptor = TRoutModuleDescriptor

        self.TRMoralLevel = Table_Row(
            "撤退士气等级", show_value(TRoutModuleDescriptor.MoralLevel)
        )


class TDangerousnessModuleDescriptorComponment:
    def __init__(self, TDangerousnessModuleDescriptor: TDangerousnessModuleDescriptor):
        self.TDangerousnessModuleDescriptor = TDangerousnessModuleDescriptor

        self.TRDangerousness = Table_Row(
            "威胁度", show_value(TDangerousnessModuleDescriptor.Dangerousness)
        )


# 武器信息
class TemplateUnitMissileCarriageComponment:
    def __init__(self, TemplateUnitMissileCarriage: TemplateUnitMissileCarriage):
        self.TemplateUnitMissileCarriage = TemplateUnitMissileCarriage

        self.TRConnoisseur = Table_Row(
            "挂载配置", show_value(TemplateUnitMissileCarriage.Connoisseur)
        )


class TWeaponManagerModuleDescriptorComponment:
    def __init__(self, TWeaponManagerModuleDescriptor: TWeaponManagerModuleDescriptor):
        self.TWeaponManagerModuleDescriptor = TWeaponManagerModuleDescriptor


# 运动信息
class TGenericMovementModuleDescriptorComponment:
    def __init__(
        self, TGenericMovementModuleDescriptor: TGenericMovementModuleDescriptor
    ):
        self.TGenericMovementModuleDescriptor = TGenericMovementModuleDescriptor

        self.TRMaxSpeedInKmph = Table_Row(
            "最大速度", show_value(TGenericMovementModuleDescriptor.MaxSpeedInKmph)
        )
        self.TRPathfindType = Table_Row(
            "寻路类型", show_value(TGenericMovementModuleDescriptor.PathfindType)
        )


class TLandMovementModuleDescriptorComponment:
    def __init__(self, TLandMovementModuleDescriptor: TLandMovementModuleDescriptor):
        self.TLandMovementModuleDescriptor = TLandMovementModuleDescriptor
        self.TRUnitMovingType = Table_Row(
            "移动类型", show_value(TLandMovementModuleDescriptor.UnitMovingType)
        )
        self.TRSpeedBonusFactorOnRoad = Table_Row(
            "路上加成", show_value(TLandMovementModuleDescriptor.SpeedBonusFactorOnRoad)
        )
        self.TRMaxAccelerationGRU = Table_Row(
            "最大加速距离", show_value(TLandMovementModuleDescriptor.MaxAccelerationGRU)
        )
        self.TRMaxDecelerationGRU = Table_Row(
            "最大减速距离", show_value(TLandMovementModuleDescriptor.MaxDecelerationGRU)
        )
        self.TRTempsDemiTour = Table_Row(
            "半圈旋转时间", show_value(TLandMovementModuleDescriptor.TempsDemiTour)
        )

        self.TRStartTime = Table_Row(
            "启动时长", show_value(TLandMovementModuleDescriptor.StartTime)
        )
        self.TRStopTime = Table_Row(
            "停止时间", show_value(TLandMovementModuleDescriptor.StopTime)
        )

        self.TRRotationStartTime = Table_Row(
            "旋转启动时长", show_value(TLandMovementModuleDescriptor.RotationStartTime)
        )
        self.TRRotationStopTime = Table_Row(
            "旋转停止时长", show_value(TLandMovementModuleDescriptor.RotationStopTime)
        )

class THelicopterMovementModuleDescriptorComponment:
    def __init__(
        self, THelicopterMovementModuleDescriptor: THelicopterMovementModuleDescriptor
    ):
        self.THelicopterMovementModuleDescriptor = THelicopterMovementModuleDescriptor
        self.TRMaxSpeedInKmph = Table_Row(
            "最大前进速度",
            show_value(THelicopterMovementModuleDescriptor.MaxSpeedInKmph),
        )
        self.TRUpwardSpeedInKmph = Table_Row(
            "升降速度",
            show_value(THelicopterMovementModuleDescriptor.UpwardSpeedInKmph),
        )
        self.TRTorqueManoeuvrability = Table_Row(
            "扭矩操纵能力",
            show_value(THelicopterMovementModuleDescriptor.TorqueManoeuvrability),
        )
        self.TRCyclicManoeuvrability = Table_Row(
            "循环操纵能力",
            show_value(THelicopterMovementModuleDescriptor.CyclicManoeuvrability),
        )
        self.TRMaxInclination = Table_Row(
            "最大倾斜角", show_value(THelicopterMovementModuleDescriptor.MaxInclination)
        )
        self.TRGFactorLimit = Table_Row(
            "G 力限值", show_value(THelicopterMovementModuleDescriptor.GFactorLimit)
        )
        self.TRRotorArea = Table_Row(
            "旋翼面积", show_value(THelicopterMovementModuleDescriptor.RotorArea)
        )
        self.TRMass = Table_Row(
            "惯性质量", show_value(THelicopterMovementModuleDescriptor.Mass)
        )

class AirplaneMovementDescriptorComponment:
    def __init__(self, AirplaneMovementDescriptor: AirplaneMovementDescriptor):
        self.AirplaneMovementDescriptor = AirplaneMovementDescriptor
        self.TRSpeedInKmph = Table_Row(
            "飞行速度", show_value(AirplaneMovementDescriptor.SpeedInKmph)
        )
        self.TRAltitudeGRU = Table_Row(
            "飞行高度", show_value(AirplaneMovementDescriptor.AltitudeGRU)
        )
        self.TRAltitudeMinGRU = Table_Row(
            "最低飞行高度", show_value(AirplaneMovementDescriptor.AltitudeMinGRU)
        )
        self.TRAltitudeMinGRU = Table_Row(
            "最低飞行高度", show_value(AirplaneMovementDescriptor.AltitudeMinGRU)
        )
        self.TRAgilityRadiusGRU = Table_Row(
            "机动半径", show_value(AirplaneMovementDescriptor.AgilityRadiusGRU)
        )
        self.TRPitchAngle = Table_Row(
            "仰俯角", show_value(AirplaneMovementDescriptor.PitchAngle)
        )
        self.TRRollAngle = Table_Row(
            "翻滚角", show_value(AirplaneMovementDescriptor.RollAngle)
        )
        self.TRRollSpeed = Table_Row(
            "翻滚速度", show_value(AirplaneMovementDescriptor.RollSpeed)
        )
        self.TREvacAngle = Table_Row(
            "撤离角", show_value(AirplaneMovementDescriptor.EvacAngle)
        )
        self.TREvacToStartingPoint = Table_Row(
            "向出发点撤离", show_value(AirplaneMovementDescriptor.EvacToStartingPoint)
        )
        self.TROrderedAttackStrategies = Table_Row(
            "攻击行为", show_value(AirplaneMovementDescriptor.OrderedAttackStrategies)
        )
        pass

class AirplanePositionModuleDescriptorComponment:
    def __init__(
        self, AirplanePositionModuleDescriptor: AirplanePositionModuleDescriptor
    ):
        self.AirplanePositionModuleDescriptor = AirplanePositionModuleDescriptor

        self.TRLowAltitudeFlyingAltitudeGRU = Table_Row(
            "低空飞行高度",
            show_value(AirplanePositionModuleDescriptor.LowAltitudeFlyingAltitudeGRU),
        )    

class HelicopterPositionModuleDescriptorComponment:
    def __init__(
        self, HelicopterPositionModuleDescriptor: HelicopterPositionModuleDescriptor
    ):
        self.HelicopterPositionModuleDescriptor = HelicopterPositionModuleDescriptor

        self.TRNearGroundFlyingAltitudeGRU = Table_Row(
            "贴地飞行高度",
            show_value(HelicopterPositionModuleDescriptor.NearGroundFlyingAltitudeGRU),
        )
        self.TRLowAltitudeFlyingAltitudeGRU = Table_Row(
            "低空飞行高度",
            show_value(HelicopterPositionModuleDescriptor.LowAltitudeFlyingAltitudeGRU),
        )

class TFuelModuleDescriptorComponment:
    def __init__(self, TFuelModuleDescriptor: TFuelModuleDescriptor):
        self.TFuelModuleDescriptor = TFuelModuleDescriptor

        self.TRFuelCapacity = Table_Row(
            "燃料量", show_value(TFuelModuleDescriptor.FuelCapacity)
        )
        self.TRFuelMoveDuration = Table_Row(
            "燃料可用时间", show_value(TFuelModuleDescriptor.FuelMoveDuration)
        )


# 视野信息
class TScannerConfigurationDescriptorComponment:
    def __init__(
        self, TScannerConfigurationDescriptor: TScannerConfigurationDescriptor
    ):
        self.TScannerConfigurationDescriptor = TScannerConfigurationDescriptor

        self.TROpticsAltitudeConfig = Table_Row(
            "视野高度配置",
            show_value(TScannerConfigurationDescriptor.OpticsAltitudeConfig),
        )

        self.TRPorteeVisionFOWGRU = Table_Row(
            "对XXX视距", show_value(TScannerConfigurationDescriptor.PorteeVisionFOWGRU)
        )

        self.TRPorteeVisionGRU = Table_Row(
            "对地视距", show_value(TScannerConfigurationDescriptor.PorteeVisionGRU)
        )
        self.TRPorteeIdentification = Table_Row(
            "对地识别能力XXX",
            show_value(TScannerConfigurationDescriptor.PorteeIdentification),
        )
        self.TROpticalStrength = Table_Row(
            "对地侦测强度", show_value(TScannerConfigurationDescriptor.OpticalStrength)
        )

        self.TRPorteeVisionTBAGRU = Table_Row(
            "直升机对地视距",
            show_value(TScannerConfigurationDescriptor.PorteeVisionTBAGRU),
        )
        self.TRDetectionTBAGRU = Table_Row(
            "侦测直升机距离",
            show_value(TScannerConfigurationDescriptor.DetectionTBAGRU),
        )

        self.TROpticalStrengthAltitude = Table_Row(
            "对空侦测强度",
            show_value(TScannerConfigurationDescriptor.OpticalStrengthAltitude),
        )

        self.TRSpecializedDetectionsGRU = Table_Row(
            "特殊侦测距离",
            show_value(TScannerConfigurationDescriptor.SpecializedDetectionsGRU),
        )
        self.TRSpecializedOpticalStrengths = Table_Row(
            "特殊侦测强度",
            show_value(TScannerConfigurationDescriptor.SpecializedOpticalStrengths),
        )


class TModernWarfareVisibilityRollRuleComponment:
    def __init__(
        self, TModernWarfareVisibilityRollRule: TModernWarfareVisibilityRollRule
    ):
        self.TModernWarfareVisibilityRollRule = TModernWarfareVisibilityRollRule

        self.TRIdentifyBaseProbability = Table_Row(
            "基础识别能力",
            show_value(TModernWarfareVisibilityRollRule.IdentifyBaseProbability),
        )
        self.TRTimeBetweenEachIdentifyRoll = Table_Row(
            "识别时间间隔",
            show_value(TModernWarfareVisibilityRollRule.TimeBetweenEachIdentifyRoll),
        )
        self.TRVisibilityRuleDescriptor = Table_Row(
            "识别规则",
            show_value(TModernWarfareVisibilityRollRule.VisibilityRuleDescriptor),
        )
        self.TRDistanceMultiplierRule = Table_Row("识别距离参数", show_value("Default"))


class TVisibilityModuleDescriptorComponment:
    def __init__(self, TVisibilityModuleDescriptor: TVisibilityModuleDescriptor):
        self.TVisibilityModuleDescriptor = TVisibilityModuleDescriptor

        self.TRUnitConcealmentBonus = Table_Row(
            "单位隐蔽系数", show_value(TVisibilityModuleDescriptor.UnitConcealmentBonus)
        )
        self.TRVisionUnitType = Table_Row(
            "单位隶属视域", show_value(TVisibilityModuleDescriptor.VisionUnitType)
        )


# 部署信息
class TDeploymentShiftModuleDescriptorComponment:
    def __init__(
        self, TDeploymentShiftModuleDescriptor: TDeploymentShiftModuleDescriptor
    ):
        self.TDeploymentShiftModuleDescriptor = TDeploymentShiftModuleDescriptor

        self.TRDeploymentShiftGRU = Table_Row(
            "前置部署量",
            show_value(TDeploymentShiftModuleDescriptor.DeploymentShiftGRU),
        )


class TProductionModuleDescriptorComponment:
    def __init__(self, TProductionModuleDescriptor: TProductionModuleDescriptor):
        self.TProductionModuleDescriptor = TProductionModuleDescriptor

        self.TRFactory = Table_Row(
            "部署所属栏目", show_value(TProductionModuleDescriptor.Factory)
        )
        self.TRProductionTime = Table_Row(
            "部署时间", show_value(TProductionModuleDescriptor.ProductionTime)
        )
        self.TRProductionRessourcesNeeded = Table_Row(
            "部署开销",
            show_value(TProductionModuleDescriptor.ProductionRessourcesNeeded),
        )


class TUnitUpkeepModuleDescriptorComponment:
    def __init__(self, TUnitUpkeepModuleDescriptor: TUnitUpkeepModuleDescriptor):
        self.TUnitUpkeepModuleDescriptor = TUnitUpkeepModuleDescriptor

        self.TRUpkeepPercentage = Table_Row(
            "维持费", show_value(TUnitUpkeepModuleDescriptor.UpkeepPercentage)
        )


class TAirplaneModuleDescriptorComponment:
    def __init__(self, TAirplaneModuleDescriptor: TAirplaneModuleDescriptor):
        self.TAirplaneModuleDescriptor = TAirplaneModuleDescriptor

        self.TRTravelDuration = Table_Row(
            "入场时间", show_value(TAirplaneModuleDescriptor.TravelDuration)
        )
        self.TREvacuationTime = Table_Row(
            "撤离时间", show_value(TAirplaneModuleDescriptor.EvacuationTime)
        )


# 补给信息
class TSupplyModuleDescriptorComponment:
    def __init__(self, TSupplyModuleDescriptor: TSupplyModuleDescriptor):
        self.TSupplyModuleDescriptor = TSupplyModuleDescriptor

        self.TRSupplyCapacity = Table_Row(
            "补给携带量", show_value(TSupplyModuleDescriptor.SupplyCapacity)
        )
        self.TRSupplyPriority = Table_Row(
            "补给优先级", show_value(TSupplyModuleDescriptor.SupplyPriority)
        )


# 运载信息
class TTransporterModuleDescriptorComponment:
    def __init__(self, TTransporterModuleDescriptor: TTransporterModuleDescriptor):
        self.TTransporterModuleDescriptor = TTransporterModuleDescriptor

        self.TRNbSeatsAvailable = Table_Row(
            "可用装载栏位", show_value(TTransporterModuleDescriptor.NbSeatsAvailable)
        )
        self.TRLoadRadiusGRU = Table_Row(
            "装载半径", show_value(TTransporterModuleDescriptor.LoadRadiusGRU)
        )
        self.TRWreckUnloadPhysicalDamageBonus = Table_Row(
            "被毁时承载单位受到的物理伤害加成",
            show_value(TTransporterModuleDescriptor.WreckUnloadPhysicalDamageBonus),
        )
        self.TRWreckUnloadSuppressDamageBonus = Table_Row(
            "被毁时承载单位受到的压制伤害加成",
            show_value(TTransporterModuleDescriptor.WreckUnloadSuppressDamageBonus),
        )
        self.TRWreckUnloadStunDamageBonus = Table_Row(
            "被毁时承载单位受到的震撼伤害加成",
            show_value(TTransporterModuleDescriptor.WreckUnloadStunDamageBonus),
        )


class TTransportableModuleDescriptorComponment:
    def __init__(self, TTransportableModuleDescriptor: TTransportableModuleDescriptor):
        self.TTransportableModuleDescriptor = TTransportableModuleDescriptor

        self.TRTimeToLoad = Table_Row(
            "装载时间", show_value(TTransportableModuleDescriptor.TimeToLoad)
        )
        self.TRNbSeatsOccupied = Table_Row(
            "消耗的装载栏位", show_value(TTransportableModuleDescriptor.NbSeatsOccupied)
        )
        self.TRIsTowable = Table_Row(
            "可架设使用", show_value(TTransportableModuleDescriptor.IsTowable)
        )


# 光环信息
class TCapaciteModuleDescriptorComponment:
    def __init__(self, TCapaciteModuleDescriptor: TCapaciteModuleDescriptor):
        self.TCapaciteModuleDescriptor = TCapaciteModuleDescriptor

        self.TRDefaultSkillList = Table_Row(
            "光环列表", show_value(TCapaciteModuleDescriptor.DefaultSkillList)
        )


# 其他信息
class TAutoCoverModuleDescriptorComponment:
    def __init__(self, TAutoCoverModuleDescriptor: TAutoCoverModuleDescriptor):
        self.TAutoCoverModuleDescriptor = TAutoCoverModuleDescriptor

        self.TRAutoCoverRangeGRU = Table_Row(
            "单位自动寻蔽距离", show_value(TAutoCoverModuleDescriptor.AutoCoverRangeGRU)
        )
        self.TROccupationRadiusGRU = Table_Row(
            "单位占据半径", show_value(TAutoCoverModuleDescriptor.OccupationRadiusGRU)
        )
        self.TRTerrainList = Table_Row(
            "寻蔽地形", show_value(TAutoCoverModuleDescriptor.TerrainList)
        )
        self.TRTerrainListMask = Table_Row(
            "寻蔽屏蔽地形", show_value(TAutoCoverModuleDescriptor.TerrainListMask)
        )
        self.TRUseTerrainsForEscape = Table_Row(
            "使用地形逃脱", show_value(TAutoCoverModuleDescriptor.UseTerrainsForEscape)
        )


class TInfantrySquadModuleDescriptorComponment:
    def __init__(self, TInfantrySquadModuleDescriptor: TInfantrySquadModuleDescriptor):
        self.TInfantrySquadModuleDescriptor = TInfantrySquadModuleDescriptor

        self.TRNbSoldatInGroupeCombat = Table_Row(
            "步兵模型人数",
            show_value(TInfantrySquadModuleDescriptor.NbSoldatInGroupeCombat),
        )


class TZoneInfluenceMapModuleDescriptorComponment:
    def __init__(
        self, TZoneInfluenceMapModuleDescriptor: TZoneInfluenceMapModuleDescriptor
    ):
        self.TZoneInfluenceMapModuleDescriptor = TZoneInfluenceMapModuleDescriptor

        self.TRInfluenceStrength = Table_Row(
            "影响力强度",
            show_value(TZoneInfluenceMapModuleDescriptor.InfluenceStrength),
        )
        self.TRMinimumInfluenceStrength = Table_Row(
            "最小影响力强度",
            show_value(TZoneInfluenceMapModuleDescriptor.MinimumInfluenceStrength),
        )
        self.TRStrengthDecayPerSecond = Table_Row(
            "影响力衰退速度",
            show_value(TZoneInfluenceMapModuleDescriptor.StrengthDecayPerSecond),
        )
        self.TRPreventsDecayInZone = Table_Row(
            "在战区内影响力不在衰退",
            show_value(TZoneInfluenceMapModuleDescriptor.PreventsDecayInZone),
        )


class UnitComponent:
    def __init__(self, unit: TEntityDescriptor):
        self.unit_key = unit.KeyName
        self.unit = unit
        self.menu = ["概览"]

    def BriefTable(self):
        page = None
        return page

    def DetailComponent(self):
        unit_tab_names = []
        unit_tab_contents = []

        base_info_table_rows = []
        damage_info_table_rows = []
        weapon_info_table_rows = []
        movement_info_table_rows = []
        vision_info_table_rows = []
        deploy_info_table_rows = []
        supply_info_table_rows = []
        transport_info_table_rows = []
        capacity_info_table_rows = []
        supply_info_table_rows = []
        other_info_table_rows = []

        for mod in self.unit.ModulesDescriptors:
            if isinstance(mod, TTypeUnitModuleDescriptor):
                comp = TTypeUnitModuleDescriptorComponment(mod)
                base_info_table_rows += [comp.TRMotherCountry, comp.TRAcknowUnitType]
            if isinstance(mod, TTagsModuleDescriptor):
                comp = TTagsModuleDescriptorComponment(mod)
                base_info_table_rows += [comp.TRTagSet]
            if isinstance(mod, TBaseDamageModuleDescriptor):
                comp = TBaseDamageModuleDescriptorComponment(mod)
                damage_info_table_rows += [
                    comp.TRMaxPhysicalDamages,
                    comp.TRMaxSuppressionDamages,
                    comp.TRMaxStunDamages,
                    comp.TRPhysicalDamageLevelsPack,
                    comp.TRSuppressDamageLevelsPack,
                    comp.TRStunDamageLevelsPack,
                ]
            if isinstance(mod, TDamageModuleDescriptor):
                comp = TDamageModuleDescriptorComponment(mod)
                damage_info_table_rows += [
                    comp.TRResistanceFront_Family,
                    comp.TRResistanceFront_Index,
                    comp.TRResistanceSides_Family,
                    comp.TRResistanceSides_Index,
                    comp.TRResistanceRear_Family,
                    comp.TRResistanceRear_Index,
                    comp.TRResistanceTop_Family,
                    comp.TRResistanceTop_Index,
                    comp.TRExplosiveReactiveArmor,
                    comp.TRHitRollECM,
                    comp.TRAutoOrientation,
                    comp.TRUseTopArmorAgainstFire
                ]
            if isinstance(mod,TemplateUnitCriticalModule):
                comp = TemplateUnitCriticalModuleComponment(mod)
                damage_info_table_rows += [
                    comp.TRModule
                ]
            if isinstance(mod,TRoutModuleDescriptor):
                comp = TRoutModuleDescriptorComponment(mod)
                damage_info_table_rows += [
                    comp.TRMoralLevel
                ]
            if isinstance(mod,TDangerousnessModuleDescriptor):
                comp = TDangerousnessModuleDescriptorComponment(mod)
                damage_info_table_rows += [
                    comp.TRDangerousness
                ]
            if isinstance(mod,TModuleSelector) and isinstance(mod.Default,TWeaponManagerModuleDescriptor):
                comp = weapon.WeaponComponent(mod.Default).AsComponent()
                unit_tab_names.append("武器信息")
                unit_tab_contents.append(comp)
            if isinstance(mod,TModuleSelector) and isinstance(mod.Default,TGenericMovementModuleDescriptor):
                comp = TGenericMovementModuleDescriptorComponment(mod.Default)
                movement_info_table_rows += [
                    comp.TRPathfindType,
                    comp.TRMaxSpeedInKmph
                ]
            if isinstance(mod,TModuleSelector) and isinstance(mod.Default,TLandMovementModuleDescriptor):
                comp = TLandMovementModuleDescriptorComponment(mod.Default)
                movement_info_table_rows += [
                    comp.TRUnitMovingType,
                    comp.TRSpeedBonusFactorOnRoad,
                    comp.TRTempsDemiTour,
                    comp.TRMaxAccelerationGRU,
                    comp.TRMaxDecelerationGRU,
                    comp.TRStartTime,
                    comp.TRStopTime,
                    comp.TRRotationStartTime,
                    comp.TRRotationStopTime,
                ]
            if isinstance(mod,TModuleSelector) and isinstance(mod.Default,THelicopterMovementModuleDescriptor):
                comp = THelicopterMovementModuleDescriptorComponment(mod.Default)
                movement_info_table_rows += [
                    comp.TRMaxSpeedInKmph,
                    comp.TRUpwardSpeedInKmph,                    
                    comp.TRMass,
                    comp.TRRotorArea,
                    comp.TRMaxInclination,
                    comp.TRTorqueManoeuvrability,
                    comp.TRCyclicManoeuvrability,
                    comp.TRGFactorLimit,
                ]
            if isinstance(mod,HelicopterPositionModuleDescriptor):
                comp = HelicopterPositionModuleDescriptorComponment(mod)
                movement_info_table_rows += [
                    comp.TRLowAltitudeFlyingAltitudeGRU,
                    comp.TRNearGroundFlyingAltitudeGRU,
                ]
            if isinstance(mod,AirplaneMovementDescriptor):
                comp = AirplaneMovementDescriptorComponment(mod)
                movement_info_table_rows += [
                    comp.TRSpeedInKmph,
                    comp.TRAgilityRadiusGRU,
                    comp.TRAltitudeGRU,
                    comp.TRAltitudeMinGRU,
                    comp.TREvacToStartingPoint,
                    comp.TREvacAngle,
                    comp.TROrderedAttackStrategies,
                    comp.TRRollSpeed,
                    comp.TRRollAngle,
                    comp.TRPitchAngle,
                ]
            if isinstance(mod,AirplanePositionModuleDescriptor):
                comp = AirplanePositionModuleDescriptorComponment(mod)
                movement_info_table_rows += [
                    comp.TRLowAltitudeFlyingAltitudeGRU
                ]
            if isinstance(mod,TModuleSelector) and isinstance(mod.Default,AirplaneMovementDescriptor):
                comp = AirplaneMovementDescriptorComponment(mod.Default)
                movement_info_table_rows += [
                    comp.TRSpeedInKmph,
                    comp.TRAgilityRadiusGRU,
                    comp.TRAltitudeGRU,
                    comp.TRAltitudeMinGRU,
                    comp.TREvacToStartingPoint,
                    comp.TREvacAngle,
                    comp.TROrderedAttackStrategies,
                    comp.TRRollSpeed,
                    comp.TRRollAngle,
                    comp.TRPitchAngle,
                ]   
            if isinstance(mod,TFuelModuleDescriptor):
                comp = TFuelModuleDescriptorComponment(mod)
                movement_info_table_rows += [
                    comp.TRFuelMoveDuration,
                    comp.TRFuelCapacity,
                ]
            if isinstance(mod, TReverseScannerWithIdentificationDescriptor):
                comp = TModernWarfareVisibilityRollRuleComponment(mod.VisibilityRollRule)
                vision_info_table_rows += [
                    comp.TRIdentifyBaseProbability,
                    comp.TRTimeBetweenEachIdentifyRoll,
                    comp.TRVisibilityRuleDescriptor,
                ]
            if isinstance(mod,TScannerConfigurationDescriptor):
                comp = TScannerConfigurationDescriptorComponment(mod)
                vision_info_table_rows += [
                    comp.TROpticsAltitudeConfig,                  
                    comp.TRPorteeVisionGRU,
                    comp.TRPorteeVisionTBAGRU,
                    comp.TRPorteeVisionFOWGRU,                
                    comp.TROpticalStrength,
                    comp.TROpticalStrengthAltitude,
                    comp.TRDetectionTBAGRU,
                    comp.TRPorteeIdentification,
                    comp.TRSpecializedDetectionsGRU,
                    comp.TRSpecializedOpticalStrengths
                ]
            if isinstance(mod, TVisibilityModuleDescriptor):
                comp = TVisibilityModuleDescriptorComponment(mod)
                vision_info_table_rows += [
                    comp.TRUnitConcealmentBonus,
                    comp.TRVisionUnitType,
                ]
            if isinstance(mod, TSupplyModuleDescriptor):
                comp = TSupplyModuleDescriptorComponment(mod)
                supply_info_table_rows += [
                    comp.TRSupplyCapacity,
                    comp.TRSupplyPriority
                ]
            if isinstance(mod, TSupplyModuleDescriptor):
                comp = TSupplyModuleDescriptorComponment(mod)
                supply_info_table_rows += [
                    comp.TRSupplyCapacity,
                    comp.TRSupplyPriority
                ]                     
            if isinstance(mod,TAirplaneModuleDescriptor):
                comp = TAirplaneModuleDescriptorComponment(mod)
                deploy_info_table_rows += [
                    comp.TRTravelDuration,
                    comp.TREvacuationTime,
                ]                
            if isinstance(mod,TDeploymentShiftModuleDescriptor):
                comp = TDeploymentShiftModuleDescriptorComponment(mod)
                deploy_info_table_rows += [
                    comp.TRDeploymentShiftGRU
                ]          
            if isinstance(mod,TProductionModuleDescriptor):
                comp = TProductionModuleDescriptorComponment (mod)
                deploy_info_table_rows += [
                    comp.TRFactory,
                    comp.TRProductionTime,
                    comp.TRProductionRessourcesNeeded,
                ]               
            if isinstance(mod,TUnitUpkeepModuleDescriptor):
                comp = TUnitUpkeepModuleDescriptorComponment(mod)
                deploy_info_table_rows += [
                    comp.TRUpkeepPercentage
                ]     
            if isinstance(mod,TTransporterModuleDescriptor):
                comp = TTransporterModuleDescriptorComponment(mod)
                transport_info_table_rows += [
                    comp.TRNbSeatsAvailable,
                    comp.TRLoadRadiusGRU,
                    comp.TRWreckUnloadPhysicalDamageBonus,
                    comp.TRWreckUnloadSuppressDamageBonus,
                    comp.TRWreckUnloadStunDamageBonus,
                ]     
            if isinstance(mod,TTransportableModuleDescriptor):
                comp = TTransportableModuleDescriptorComponment(mod)
                transport_info_table_rows += [
                    comp.TRNbSeatsOccupied,
                    comp.TRTimeToLoad,
                    comp.TRIsTowable,
                ]
            if isinstance(mod,TModuleSelector) and isinstance(mod.Default,TCapaciteModuleDescriptor):
                comp = TCapaciteModuleDescriptorComponment(mod)
                transport_info_table_rows += [
                    comp.TRDefaultSkillList
                ]        
            if isinstance(mod,TAutoCoverModuleDescriptor):
                comp = TAutoCoverModuleDescriptorComponment(mod)
                other_info_table_rows += [
                    comp.TRAutoCoverRangeGRU,
                    comp.TROccupationRadiusGRU,
                    comp.TRTerrainList,
                    comp.TRTerrainListMask,
                    comp.TRUseTerrainsForEscape,
                ]  
            if isinstance(mod,TZoneInfluenceMapModuleDescriptor):
                comp = TZoneInfluenceMapModuleDescriptorComponment(mod)
                other_info_table_rows += [
                    comp.TRInfluenceStrength,
                    comp.TRMinimumInfluenceStrength,
                    comp.TRStrengthDecayPerSecond,
                    comp.TRPreventsDecayInZone,
                ]  
                        
        if base_info_table_rows != []:
            unit_tab_names.append("基础信息")
            unit_tab_contents.append(
                Page_Content(
                    [
                        Row(
                            [
                                Col(
                                    Content("基础信息", Table(base_info_table_rows)),
                                    className="twelve columns",
                                )
                            ]
                        )
                    ]
                )
            )
        if damage_info_table_rows != []:
            unit_tab_names.append("伤害信息")
            unit_tab_contents.append(
                Page_Content(
                    [
                        Row(
                            [
                                Col(
                                    Content("伤害信息", Table(damage_info_table_rows)),
                                    className="twelve columns",
                                )
                            ]
                        )
                    ]
                )
            )
        if movement_info_table_rows != []:
            unit_tab_names.append("运动信息")
            unit_tab_contents.append(
                Page_Content(
                    [
                        Row(
                            [
                                Col(
                                    Content("运动信息", Table(movement_info_table_rows)),
                                    className="twelve columns",
                                )
                            ]
                        )
                    ]
                )
            )
        if vision_info_table_rows != []:
            unit_tab_names.append("视野信息")
            unit_tab_contents.append(
                Page_Content(
                    [
                        Row(
                            [
                                Col(
                                    Content("视野信息", Table(vision_info_table_rows)),
                                    className="twelve columns",
                                )
                            ]
                        )
                    ]
                )
            )
        if supply_info_table_rows != []:
            unit_tab_names.append("补给信息")
            unit_tab_contents.append(
                Page_Content(
                    [
                        Row(
                            [
                                Col(
                                    Content("补给信息", Table(supply_info_table_rows)),
                                    className="twelve columns",
                                )
                            ]
                        )
                    ]
                )
            )
        if deploy_info_table_rows != []:
            unit_tab_names.append("部署信息")
            unit_tab_contents.append(
                Page_Content(
                    [
                        Row(
                            [
                                Col(
                                    Content("部署信息", Table(deploy_info_table_rows)),
                                    className="twelve columns",
                                )
                            ]
                        )
                    ]
                )
            )
        if transport_info_table_rows != []:
            unit_tab_names.append("运载信息")
            unit_tab_contents.append(
                Page_Content(
                    [
                        Row(
                            [
                                Col(
                                    Content("运载信息", Table(transport_info_table_rows)),
                                    className="twelve columns",
                                )
                            ]
                        )
                    ]
                )
            )
        if capacity_info_table_rows != []:
            unit_tab_names.append("光环信息")
            unit_tab_contents.append(
                Page_Content(
                    [
                        Row(
                            [
                                Col(
                                    Content("光环信息", Table(capacity_info_table_rows)),
                                    className="twelve columns",
                                )
                            ]
                        )
                    ]
                )
            )
        if other_info_table_rows != []:
            unit_tab_names.append("其他信息")
            unit_tab_contents.append(
                Page_Content(
                    [
                        Row(
                            [
                                Col(
                                    Content("其他信息", Table(other_info_table_rows)),
                                    className="twelve columns",
                                )
                            ]
                        )
                    ]
                )
            )
    
   

        tabs = Tabs(unit_tab_names, unit_tab_contents)
        return tabs

    def AsPage(self):
        tabs = self.DetailComponent()
        header = Header(self.unit_key)
        page = Page(header, tabs)
        return page
