from dash import dcc
from dash import html
import plotly.graph_objs as go
from utils import *

import sys

WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)
from src.extractor.refined_class import *

class AmmunitionComponent:
    def __init__(self, ammunition: TAmmunitionDescriptor):
        self.ammunition_key = ammunition.KeyName if hasattr(ammunition, "KeyName") else str(ammunition)
        self.ammunition = ammunition
        self.menu = ["概览", "详细"]

        self.TRMinMaxCategory = Table_Row(
            "所属类型",
            show_value(ammunition.MinMaxCategory) if hasattr(self.ammunition, "MinMaxCategory") else "",
            caption="该类别其实是用来划分最大最小等级范围的（即游戏中蓝色等级，绿色等级，红色等级）",
        )
        self.TRTraitsToken = Table_Row(
            "特性词条", show_value(ammunition.TraitsToken, default_view="list") if hasattr(self.ammunition, "TraitsToken") else "",
        )
        self.TRIsSubAmmunition = Table_Row(
            "描述对象为子武器",
            show_value(ammunition.IsSubAmmunition, default_view="bool") if hasattr(self.ammunition, "TraitsToken") else "",
            caption="此词条注明指明其是否仅为一份弹药量的伤害，比如航弹。",
        )
        self.TRAffecteParNombre = Table_Row(
            "描述对象因数量属性倍增",
            show_value(ammunition.AffecteParNombre, default_view="bool"),
            caption="此词条注明弹药效果是否会因持有人数倍增，比如枪械弹药。",
        )

        self.TRArme_Family = Table_Row("伤害所属族", show_value(ammunition.Arme.Family))
        self.TRArme_Index = Table_Row("伤害索引号", show_value(ammunition.Arme.Index))
        self.TRPhysicalDamages = Table_Row(
            "基底伤害", show_value(ammunition.PhysicalDamages)
        )
        self.TRRadiusSplashPhysicalDamagesGRU = Table_Row(
            "基底伤害溅射半径", show_value(ammunition.RadiusSplashPhysicalDamagesGRU)
        )
        self.TRSuppressDamages = Table_Row(
            "压制伤害", show_value(ammunition.SuppressDamages)
        )
        self.TRRadiusSplashSuppressDamagesGRU = Table_Row(
            "压制伤害溅射半径", show_value(ammunition.RadiusSplashSuppressDamagesGRU)
        )
        self.TRAllowSuppressDamageWhenNoImpact = Table_Row(
            "允许未命中造成压制",
            show_value(ammunition.AllowSuppressDamageWhenNoImpact, default_view="bool"),
        )
        self.TRForceHitTopArmor = Table_Row(
            "强制攻顶", show_value(ammunition.ForceHitTopArmor, default_view="bool")
        )
        self.TRTargetOnlyOneUnitInDistrict = Table_Row(
            "仅针对城区中的单一单位",
            show_value(ammunition.TargetOnlyOneUnitInDistrict, default_view="bool"),
        )

        self.TRPorteeMaximaleGRU = Table_Row(
            "对地最大射程", show_value(ammunition.PorteeMaximaleGRU)
        )
        self.TRPorteeMaximaleTBAGRU = Table_Row(
            "对直升机最大射程", show_value(ammunition.PorteeMaximaleTBAGRU)
        )
        self.TRPorteeMaximaleHAGRU = Table_Row(
            "对空最大射程", show_value(ammunition.PorteeMaximaleHAGRU)
        )
        self.TRPorteeMinimaleGRU = Table_Row(
            "对地最小射程", show_value(ammunition.PorteeMinimaleGRU)
        )
        self.TRPorteeMinimaleTBAGRU = Table_Row(
            "对直升机最小射程", show_value(ammunition.PorteeMinimaleTBAGRU)
        )
        self.TRPorteeMinimaleHAGRU = Table_Row(
            "对空最小射程", show_value(ammunition.PorteeMinimaleHAGRU)
        )

        base_hit_values = {
            k: v
            for d in ammunition.HitRollRuleDescriptor.BaseHitValueModifiers
            for k, v in d.items()
        }
        self.TRBase = Table_Row(
            "基础准度", show_value(base_hit_values.get("Base", "N/A"))
        )
        self.TRIdling = Table_Row(
            "静止准度", show_value(base_hit_values.get("Idling", "N/A"))
        )
        self.TRMoving = Table_Row(
            "移动准度", show_value(base_hit_values.get("Moving", "N/A"))
        )
        self.TRTargeted = Table_Row(
            "被瞄准度", show_value(base_hit_values.get("Targeted", "N/A"))
        )
        self.TRBaseCriticModifier = Table_Row(
            "基础暴击效果概率",
            show_value(ammunition.HitRollRuleDescriptor.BaseCriticModifier),
        )
        self.TRDistanceToTarget = Table_Row(
            "准度随距离修正",
            show_value(
                ammunition.HitRollRuleDescriptor.DistanceToTarget, default_view="bool"
            ),
        )
        self.TRMaxSuccessiveHitCount = Table_Row(
            "最大连射长度", show_value(ammunition.MaxSuccessiveHitCount)
        )
        self.TRCanShootWhileMoving = Table_Row(
            "允许移动攻击",
            show_value(ammunition.CanShootWhileMoving, default_view="bool"),
        )

        self.TRDispersionAtMaxRangeGRU = Table_Row(
            "最大射程下散布", show_value(ammunition.DispersionAtMaxRangeGRU)
        )
        self.TRDispersionAtMinRangeGRU = Table_Row(
            "最小射程下散布", show_value(ammunition.DispersionAtMinRangeGRU)
        )
        self.TRCorrectedShotDispersionMultiplier = Table_Row(
            "校正散布修正", show_value(ammunition.CorrectedShotDispersionMultiplier)
        )
        self.TRDispersionWithoutSorting = Table_Row(
            "乱序射击",
            show_value(ammunition.DispersionWithoutSorting, default_view="bool"),
        )
        self.TRAngleDispersion = Table_Row(
            "散布角度", show_value(ammunition.AngleDispersion)
        )

        self.TRTempsDeVisee = Table_Row("瞄准时间", show_value(ammunition.TempsDeVisee))
        self.TRTempsEntreDeuxSalves = Table_Row(
            "装填时间", show_value(ammunition.TempsEntreDeuxSalves)
        )
        self.TRTempsEntreDeuxTirs = Table_Row(
            "射击间隔", show_value(ammunition.TempsEntreDeuxTirs)
        )
        self.TRNbTirParSalves = Table_Row(
            "装填前发射次数", show_value(ammunition.NbTirParSalves)
        )
        self.TRCorrectedShotAimtimeMultiplier = Table_Row(
            "校正射击瞄准时间修正",
            show_value(ammunition.CorrectedShotAimtimeMultiplier),
        )
        self.TRTempsEntreDeuxSalves_Min = Table_Row(
            "最小射击间隔", show_value(ammunition.TempsEntreDeuxSalves_Min)
        )
        self.TRTempsEntreDeuxSalves_Max = Table_Row(
            "最大射击间隔", show_value(ammunition.TempsEntreDeuxSalves_Max)
        )

        self.TRCanShootOnPosition = Table_Row(
            "允许强制攻击",
            show_value(ammunition.CanShootOnPosition, default_view="bool"),
        )
        self.TRNbSalvosShootOnPosition = Table_Row(
            "强制攻击装填次数", show_value(ammunition.NbSalvosShootOnPosition)
        )
        self.TRTirIndirect = Table_Row(
            "仅能直射", show_value(ammunition.TirIndirect, default_view="bool")
        )
        self.TRTirReflexe = Table_Row(
            "无法追踪目标", show_value(ammunition.TirReflexe, default_view="bool")
        )
        self.TRInterdireTirReflexe = Table_Row(
            "允许追踪目标", show_value(ammunition.TirReflexe, default_view="bool")
        )
        self.TRTargetUnitCenter = Table_Row(
            "瞄准目标中心", show_value(ammunition.TargetUnitCenter, default_view="bool")
        )
        self.TRPiercingWeapon = Table_Row(
            "为穿甲武器", show_value(ammunition.PiercingWeapon, default_view="bool")
        )
        self.TRIsHarmlessForAllies = Table_Row(
            "无友军伤害", show_value(ammunition.IsHarmlessForAllies)
        )
        self.TRCanHarmAirplanes = Table_Row(
            "可对飞机造成伤害", show_value(ammunition.CanHarmAirplanes)
        )

        self.TRGuidance = Table_Row("引导方式", show_value(ammunition.Guidance))
        self.TRIsFireAndForget = Table_Row(
            "射后不理", show_value(ammunition.IsFireAndForget)
        )
        self.TRMissileDescriptor = Table_Row(
            "挂载导弹", show_value(ammunition.MissileDescriptor)
        )
        self.TRTandemCharge = Table_Row("串联弹头", show_value(ammunition.TandemCharge))
        self.TRMissileTimeBetweenCorrections = Table_Row(
            "导弹射击时间修正", show_value(ammunition.MissileTimeBetweenCorrections)
        )

        self.TRSupplyCost = Table_Row("补给消耗", show_value(ammunition.SupplyCost))
        self.TRSmokeDescriptor = Table_Row(
            "烟雾类型", show_value(ammunition.SmokeDescriptor)
        )
        self.TRFireDescriptor = Table_Row(
            "火焰类型", show_value(ammunition.FireDescriptor)
        )
        self.TRFireTriggeringProbability = Table_Row(
            "引火概率", show_value(ammunition.FireTriggeringProbability)
        )
        self.TRIgnoreInflammabilityConditions = Table_Row(
            "忽视不可引火条件",
            show_value(ammunition.IgnoreInflammabilityConditions, default_view="bool"),
        )

    def BriefTable(self):
        return Table(
            [
                Table_Row("基础"),
                self.TRMinMaxCategory,
                self.TRTraitsToken,
                Table_Row("伤害"),
                self.TRArme_Family,
                self.TRArme_Index,
                self.TRPhysicalDamages,
                self.TRSuppressDamages,
                Table_Row("射程"),
                self.TRPorteeMaximaleGRU,
                self.TRPorteeMaximaleTBAGRU,
                self.TRPorteeMaximaleHAGRU,
                self.TRPorteeMinimaleGRU,
                self.TRPorteeMinimaleTBAGRU,
                self.TRPorteeMinimaleHAGRU,
                Table_Row("准度"),
                self.TRIdling,
                self.TRMoving,
                Table_Row("时间"),
                self.TRTempsDeVisee,
                self.TRTempsEntreDeuxSalves,
                self.TRNbTirParSalves,
                Table_Row("补给"),
                self.TRSupplyCost,
            ]
        )

    def DetailComponent(self):
        basic_table = Content(
            "基础信息",
            Table(
                [
                    self.TRMinMaxCategory,
                    self.TRTraitsToken,
                    self.TRIsSubAmmunition,
                    self.TRAffecteParNombre,
                ]
            ),
        )
        damage_table = Content(
            "伤害信息",
            Table(
                [
                    self.TRArme_Family,
                    self.TRArme_Index,
                    self.TRPhysicalDamages,
                    self.TRSuppressDamages,
                    self.TRRadiusSplashPhysicalDamagesGRU,
                    self.TRRadiusSplashSuppressDamagesGRU,
                    self.TRAllowSuppressDamageWhenNoImpact,
                    self.TRForceHitTopArmor,
                    self.TRTargetOnlyOneUnitInDistrict,
                ]
            ),
        )
        range_table = Content(
            "射程信息",
            Table(
                [
                    self.TRPorteeMaximaleGRU,
                    self.TRPorteeMaximaleTBAGRU,
                    self.TRPorteeMaximaleHAGRU,
                    self.TRPorteeMinimaleGRU,
                    self.TRPorteeMinimaleTBAGRU,
                    self.TRPorteeMinimaleHAGRU,
                ]
            ),
        )
        accuracy_table = Content(
            "准度信息",
            Table(
                [
                    self.TRBase,
                    self.TRIdling,
                    self.TRMoving,
                    self.TRTargeted,
                    self.TRBaseCriticModifier,
                    self.TRDistanceToTarget,
                    self.TRMaxSuccessiveHitCount,
                    self.TRCanShootWhileMoving,
                ]
            ),
        )
        dispersion_table = Content(
            "散布信息",
            Table(
                [
                    self.TRDispersionAtMaxRangeGRU,
                    self.TRDispersionAtMinRangeGRU,
                    self.TRCorrectedShotDispersionMultiplier,
                    self.TRDispersionWithoutSorting,
                    self.TRAngleDispersion,
                ]
            ),
        )
        time_table = Content(
            "时间信息",
            Table(
                [
                    self.TRTempsDeVisee,
                    self.TRTempsEntreDeuxSalves,
                    self.TRTempsEntreDeuxTirs,
                    self.TRNbTirParSalves,
                    self.TRCorrectedShotAimtimeMultiplier,
                    self.TRTempsEntreDeuxSalves_Min,
                    self.TRTempsEntreDeuxSalves_Max,
                ]
            ),
        )
        target_table = Content(
            "目标选择信息",
            Table(
                [
                    self.TRPiercingWeapon,
                    self.TRIsHarmlessForAllies,
                    self.TRCanHarmAirplanes,
                    self.TRCanShootOnPosition,
                    self.TRNbSalvosShootOnPosition,
                    self.TRTirIndirect,
                    self.TRTargetUnitCenter,
                    self.TRTirReflexe,
                    self.TRInterdireTirReflexe,
                ]
            ),
        )
        missle_table = Content(
            "导弹信息",
            Table(
                [
                    self.TRGuidance,
                    self.TRIsFireAndForget,
                    self.TRMissileDescriptor,
                    self.TRTandemCharge,
                    self.TRMissileTimeBetweenCorrections,
                ]
            ),
        )
        other_table = Content(
            "其他信息",
            Table(
                [
                    self.TRSupplyCost,
                    self.TRSmokeDescriptor,
                    self.TRFireDescriptor,
                    self.TRFireTriggeringProbability,
                    self.TRIgnoreInflammabilityConditions,
                ]
            ),
        )

        col1_1 = Col(basic_table)
        col1_2 = Col(damage_table)

        col2_1 = Col(range_table)
        col2_2 = Col(accuracy_table)

        col3_1 = Col(dispersion_table)
        col3_2 = Col(time_table)

        col4_1 = Col(target_table)
        col4_2 = Col(missle_table)

        col5_1 = Col(other_table)

        row1 = Row([col1_1, col1_2])
        row2 = Row([col2_1, col2_2])
        row3 = Row([col3_1, col3_2])
        row4 = Row([col4_1, col4_2])
        row5 = Row([col5_1])

        content = Page_Content([row1, row2, row3, row4, row5])
        return content

    def AsComponent(self):
        table = Page_Content(
            [
                Row(
                    [
                        Col(
                            Content("数据信息", self.BriefTable()),
                            className="twelve columns",
                        )
                    ]
                )
            ]
        )
        component = self.DetailComponent()
        tabs = Tabs(self.menu, [table, component])
        return tabs
         
    def AsPage(self):
        tabs = self.AsComponent()
        header = Header(self.ammunition_key)
        page = Page(header, tabs)
        return page
