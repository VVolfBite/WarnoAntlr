from ast import Pass
from tkinter import PAGES
from dash import dcc
from dash import html
import plotly.graph_objs as go
from utils import *
from typing import Counter, Union

import sys

WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)

from src.extractor.refined_class import *


class TCapaciteDescriptorComponment:
    def __init__(
        self,
        TCapaciteDescriptor: TCapaciteDescriptor
    ):
        self.TCapaciteDescriptor = TCapaciteDescriptor
        self.KeyName = TCapaciteDescriptor.KeyName

        self.TRCumulEffect = Table_Row(
            "叠加规则",
            show_value(TCapaciteDescriptor.CumulEffect),
        )
        self.TRDeclenchement = Table_Row(
            "触发规则",
            show_value(TCapaciteDescriptor.Declenchement),
        )

        self.TRTypeCible = Table_Row(
            "作用类型",
            show_value(TCapaciteDescriptor.TypeCible),
        )
        self.TRTargetTeamFilter = Table_Row(
            "目标分队要求",
            show_value(TCapaciteDescriptor.TargetTeamFilter),
        )           
        self.TRTargetWoundedFilter = Table_Row(
            "目标损伤要求",
            show_value(TCapaciteDescriptor.TargetWoundedFilter),
        )          
        self.TRTargetInBuilding = Table_Row(
            "目标可以在建筑内",
            show_value(TCapaciteDescriptor.TargetInBuilding),
        )    
        self.TRTargetInTransport = Table_Row(
            "目标可以在载具内",
            show_value(TCapaciteDescriptor.TargetInTransport),
        )   
        self.TRTargetInSelf = Table_Row(
            "目标可以承载在自己内",
            show_value(TCapaciteDescriptor.TargetInSelf),
        )
        self.TRTargetMySelf = Table_Row(
            "目标可以为自己",
            show_value(TCapaciteDescriptor.TargetMySelf),
        )   

        self.TRInfluenceMapType = Table_Row(
            "影响区域类型",
            show_value(TCapaciteDescriptor.InfluenceMapAlliance),
        )          
        self.TRInfluenceMapAlliance = Table_Row(
            "影响区域下的联盟",
            show_value(TCapaciteDescriptor.InfluenceMapAlliance),
        ) 
    


        self.TRAreaShape = Table_Row(
            "能力区域形状",
            show_value(TCapaciteDescriptor.AreaShape),
        )
        self.TRRadiusGRU = Table_Row(
            "能力半径",
            show_value(TCapaciteDescriptor.RadiusGRU),
        )   
        self.TRRangeGRU = Table_Row(
            "能力释放半径",
            show_value(TCapaciteDescriptor.RangeGRU),
        )
        self.TRCastTime = Table_Row(
            "能力释放时间",
            show_value(TCapaciteDescriptor.CastTime),
        )   
        self.TRCooldown = Table_Row(
            "能力冷却时间",
            show_value(TCapaciteDescriptor.Cooldown),
        )   
        self.TRConditions = Table_Row(
            "能力释放条件",
            show_value(TCapaciteDescriptor.Conditions),
        ) 

        self.TRTagsCiblePossible = Table_Row(
            "需要对目标具有以下词条",
            show_value(TCapaciteDescriptor.TagsCiblePossible),
        )         
        self.TRTagsCibleExcluded = Table_Row(
            "需要对目标不具有以下词条",
            show_value(TCapaciteDescriptor.TagsCibleExcluded),
        )     
        self.TRCheckVisibility = Table_Row(
            "需要对目标有视野",
            show_value(TCapaciteDescriptor.CheckVisibility),
        ) 
        self.TRAllowReflexDuringCast = Table_Row(
            "在释放能力时对单位锁定",
            show_value(TCapaciteDescriptor.AllowReflexDuringCast),
        )
        self.TRCanBeCastFromTransport = Table_Row(
            "可以在载具内释放能力",
            show_value(TCapaciteDescriptor.CanBeCastFromTransport),
        )
        self.TRTargetEffect = Table_Row(
            "对目标附加效果",
            show_value(TCapaciteDescriptor.TargetEffect),
        )
        self.TRTargetEffectDuration = Table_Row(
            "对目标附加效果时长",
            show_value(TCapaciteDescriptor.TargetEffectDuration),
        )    
        self.TRSelfEffectDuration  = Table_Row(
            "对自己附加效果时长",
            show_value(TCapaciteDescriptor.SelfEffectDuration ),
        )   
        self.TRMinVirtualUnits  = Table_Row(
            "最少目标量",
            show_value(TCapaciteDescriptor.MinVirtualUnits ),
        ) 
        self.TRMaxTargetNb  = Table_Row(
            "最大目标量",
            show_value(TCapaciteDescriptor.MaxTargetNb ),
        )
        self.TRMultiplyCost  = Table_Row(
            "多次释放",
            show_value(TCapaciteDescriptor.MultiplyCost ),
        )

        self.TROrderMustSpreadTargets  = Table_Row(
            "仅在收到指令后释放能力",
            show_value(TCapaciteDescriptor.OrderMustSpreadTargets ),
        ) 
        
    def DetailComponent(self):
        capacity_table = Content(
            f"{self.KeyName}",
            Table([
                "释放效果",
                self.TRTargetEffect,
                self.TRTargetEffectDuration,
                self.TRSelfEffectDuration,
                "目标选择",
                self.TRTypeCible,
                self.TRTargetTeamFilter,
                self.TRTargetWoundedFilter,
                self.TRTargetInBuilding,
                self.TRTargetInTransport,
                self.TRTargetInSelf,
                self.TRTargetMySelf,
                self.TRTagsCiblePossible,
                self.TRTagsCibleExcluded,
                self.TRConditions,
                "释放范围与时间",
                self.TRAreaShape,
                self.TRRadiusGRU,
                self.TRRangeGRU,
                self.TRCastTime,
                self.TRCooldown,
                "释放规则",
                self.TRCheckVisibility,
                self.TRCumulEffect,
                self.TRDeclenchement,
                self.TRInfluenceMapType,
                self.TRInfluenceMapAlliance,
                self.TRMinVirtualUnits,
                self.TRMaxTargetNb,
                self.TRCanBeCastFromTransport,
                self.TRAllowReflexDuringCast,
                self.TROrderMustSpreadTargets,
            ])
        )
        return capacity_table

class TEffectsPackDescriptorComponment:
    def __init__(
        self,
        TEffectsPackDescriptor: TEffectsPackDescriptor
    ):
        self.TEffectsPackDescriptor = TEffectsPackDescriptor
        self.KeyName = TEffectsPackDescriptor.KeyName

    def DetailComponent(self):
        effect_table = []
        for effect in self.TEffectsPackDescriptor.EffectsDescriptors:
            effect_table.append(Table_Row(effect.__class__.__name__))
            effect_table.append(Table_Row("效果说明",effect.__class__.__name__))
            if hasattr(effect, 'DamageType'):
                Table_Row("修正伤害类型",effect.DamageType)
            if hasattr(effect, 'ModifierType'):
                Table_Row("修正方式",effect.ModifierType)
            if hasattr(effect, 'ModifierValue'):
                Table_Row("修正数值",effect.ModifierValue)
            if hasattr(effect, 'ExperienceLevelModifier'):
                Table_Row("修正数值",effect.ExperienceLevelModifier)
            if hasattr(effect, 'EffectOnTransportSlotNumber'):
                Table_Row("修正数值",effect.EffectOnTransportSlotNumber)   


            if hasattr(effect, 'BonusDamage'):
                Table_Row("加成数值",effect.BonusDamage)
            if hasattr(effect, 'Bonus'):
                Table_Row("加成数值",effect.Bonus)
            if hasattr(effect, 'BonusDispersion'):
                Table_Row("加成数值",effect.BonusDispersion)
            if hasattr(effect, 'BonusChassisRotationSpeed'):
                Table_Row("加成数值",effect.BonusChassisRotationSpeed)
            if hasattr(effect, 'BonusTurretRotationSpeed'):
                Table_Row("加成数值",effect.BonusTurretRotationSpeed)
            if hasattr(effect, 'BonusSpeedBaseInPercent'):
                Table_Row("加成数值",effect.BonusSpeedBaseInPercent)
            if hasattr(effect, 'BonusValueGRUGRU'):
                Table_Row("加成数值",effect.BonusValueGRUGRU)

            if hasattr(effect, 'BonusDangerousness'):
                Table_Row("加成数值",effect.BonusDangerousness)
            if hasattr(effect, 'SupplyMalus'):
                Table_Row("惩罚数值",effect.SupplyMalus)

            if hasattr(effect, 'TagListToRaise'):
                Table_Row("为单位增加以下词条",effect.TagListToRaise)
            if hasattr(effect, 'TextureToken'):
                Table_Row("为单位显示以下图标",effect.TextureToken)
            if hasattr(effect, 'CapacityToAdd'):
                Table_Row("为单位增加以下能力",effect.CapacityToAdd)
            if hasattr(effect, 'FutureTeam'):
                Table_Row("为单位变更阵营",f"{effect.FutureTeam.TeamType}:{effect.Future.TeamNumber}")   
                     