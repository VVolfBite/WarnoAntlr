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
        table_row = [
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
            ]
        return table_row

class TEffectsPackDescriptorComponment:
    def __init__(
        self,
        TEffectsPackDescriptor: TEffectsPackDescriptor
    ):
        self.TEffectsPackDescriptor = TEffectsPackDescriptor
        self.KeyName = TEffectsPackDescriptor.KeyName

    def DetailComponent(self):
        effect_table = []
        effect_table.append(Table_Row(self.KeyName))
        for effect in self.TEffectsPackDescriptor.EffectsDescriptors:
            effect_table.append(Table_Row(f""))
            effect_table.append(Table_Row(f"增加效果{effect.__class__.__name__}"))
            if hasattr(effect, 'DamageType'):
                effect_table.append(Table_Row("修正伤害类型",show_value(effect.DamageType)))
            if hasattr(effect, 'ModifierType'):
                effect_table.append(Table_Row("修正方式",show_value(effect.ModifierType)))
            if hasattr(effect, 'ModifierValue'):
                effect_table.append(Table_Row("修正数值",show_value(effect.ModifierValue)))
            if hasattr(effect, 'ExperienceLevelModifier'):
                effect_table.append(Table_Row("修正数值",show_value(effect.ExperienceLevelModifier)))
            if hasattr(effect, 'EffectOnTransportSlotNumber'):
                effect_table.append(Table_Row("修正数值",show_value(effect.EffectOnTransportSlotNumber)))
            if hasattr(effect, 'PhysicalDamageValue'):
                effect_table.append(Table_Row("修正数值",show_value(effect.PhysicalDamageValue)))
            if hasattr(effect, 'SuppressDamageValue'):
                effect_table.append(Table_Row("修正数值",show_value(effect.SuppressDamageValue)))
            if hasattr(effect, 'BonusDamage'):
                effect_table.append(Table_Row("加成数值",show_value(effect.BonusDamage)))
            if hasattr(effect, 'Bonus'):
                effect_table.append(Table_Row("加成数值",show_value(effect.Bonus)))
            if hasattr(effect, 'BonusValue'):
                effect_table.append(Table_Row("加成数值",show_value(effect.BonusValue)))
            if hasattr(effect, 'BonusDispersion'):
                effect_table.append(Table_Row("加成数值",show_value(effect.BonusDispersion)))
            if hasattr(effect, 'BonusChassisRotationSpeed'):
                effect_table.append(Table_Row("加成数值",show_value(effect.BonusChassisRotationSpeed)))
            if hasattr(effect, 'BonusTurretRotationSpeed'):
                effect_table.append(Table_Row("加成数值",show_value(effect.BonusTurretRotationSpeed)))
            if hasattr(effect, 'BonusSpeedBaseInPercent'):
                effect_table.append(Table_Row("加成数值",show_value(effect.BonusSpeedBaseInPercent)))
            if hasattr(effect, 'BonusValueGRUGRU'):
                effect_table.append(Table_Row("加成数值",show_value(effect.BonusValueGRUGRU)))
            if hasattr(effect, 'BonusVisionBase'):
                effect_table.append(Table_Row("加成数值",show_value(effect.BonusVisionBase)))
            if hasattr(effect, 'BonusDangerousness'):
                effect_table.append(Table_Row("加成数值",show_value(effect.BonusDangerousness)))
            if hasattr(effect, 'BonusPrecisionWhenTargeted'):
                effect_table.append(Table_Row("加成数值",show_value(effect.BonusPrecisionWhenTargeted)))
            if hasattr(effect, 'BonusOpticalStrength'):
                effect_table.append(Table_Row("加成数值",show_value(effect.BonusOpticalStrength)))
            if hasattr(effect, 'BonusWeaponPorteeMax'):
                effect_table.append(Table_Row("加成数值",show_value(effect.BonusWeaponPorteeMax)))
            if hasattr(effect, 'BonusConcealmentBonus'):
                effect_table.append(Table_Row("加成数值",show_value(effect.BonusConcealmentBonus)))
            if hasattr(effect, 'SupplyMalus'):
                effect_table.append(Table_Row("惩罚数值",show_value(effect.SupplyMalus)))
            if hasattr(effect, 'TagListToRaise'):
                effect_table.append(Table_Row("为单位增加以下词条",show_value(effect.TagListToRaise)))
            if hasattr(effect, 'TextureToken'):
                effect_table.append(Table_Row("为单位显示以下图标",show_value(effect.TextureToken)))
            if hasattr(effect, 'CapacityToAdd'):
                effect_table.append(Table_Row("为单位增加以下能力",show_value(effect.CapacityToAdd)))
            if hasattr(effect, 'FutureTeam'):
                effect_table.append(Table_Row("为单位变更阵营",show_value(f"{effect.FutureTeam.TeamType}:{effect.FutureTeam.TeamNumber}")))
            if hasattr(effect, 'Selectable'):
                effect_table.append(Table_Row("单位可选",show_value(effect.Selectable)))
            if hasattr(effect, 'UpdateEachTick'):
                effect_table.append(Table_Row("在每个刻度时更新",show_value(effect.UpdateEachTick)))
            if hasattr(effect, 'BlindageLocation'):
                effect_table.append(Table_Row("替换单位以下的护甲", show_value(f"护甲族:{effect.BlindageLocation} 索引值:{effect.ReplacementBlindage.Index}")))
            if hasattr(effect, 'ReplacementBlindage'):
                effect_table.append(Table_Row("替换护甲为", show_value(f"护甲族:{effect.ReplacementBlindage.Family} 索引值:{effect.ReplacementBlindage.Index}")))
            if hasattr(effect, 'HealUnitsPerSecond'):
                effect_table.append(Table_Row("每秒回复量",show_value(effect.HealUnitsPerSecond)))
            if hasattr(effect, 'NbUpdatePerSecond'):
                effect_table.append(Table_Row("每秒更新次数",show_value(effect.NbUpdatePerSecond)))

        
        return effect_table

class CapacityAndEffectPage:
    def __init__(self,capacity_list:list[TCapaciteDescriptor],effect_list:list[TEffectsPackDescriptor]):
        self.capacity_list = capacity_list
        self.effect_list =effect_list
    def DetailComponent(self):
        capacity_content_list = []
        effect_content_list = []
        for capacity in self.capacity_list:
            comp = TCapaciteDescriptorComponment(capacity)
            content = Content(comp.KeyName,Table(comp.DetailComponent()))
            capacity_content_list.append(content)

        for effect in self.effect_list:
            comp = TEffectsPackDescriptorComponment(effect)
            content = Content(comp.KeyName,Table(comp.DetailComponent()))
            effect_content_list.append(content)
        
        capacity_page_content = Page_Content(
            [
                Row([
                    Col(capacity_content_list[i], className="six columns")if i < len(capacity_content_list) else None,
                    Col(capacity_content_list[i + 1], className="six columns") if i + 1 < len(capacity_content_list) else None
                ])
                for i in range(0, len(capacity_content_list), 2)
            ]
        )
    
        effect_page_content = Page_Content(
            [
                Row([
                    Col(effect_content_list[i], className="six columns") if i < len(effect_content_list) else None,
                    Col(effect_content_list[i + 1], className="six columns") if i + 1 < len(effect_content_list) else None,
                ])
                for i in range(0, len(effect_content_list), 2)
            ]
        )

        tab_list = ['光环能力','效果']
        tabs =Tabs(tab_list,[capacity_page_content,effect_page_content])
        return tabs
    def AsPage(self):
        tabs = self.DetailComponent()
        header = Header("光环与效果")
        page = Page(header, tabs)
        return page