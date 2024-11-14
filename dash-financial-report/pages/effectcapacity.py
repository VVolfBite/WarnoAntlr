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


class CapacityComponment:
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
        self.TRTagsCiblePossible = Table_Row(
            "需要对目标不具有以下词条",
            show_value(TCapaciteDescriptor.TagsCiblePossible),
        )     
        self.TRTagsCibleExcluded = Table_Row(
            "需要对目标有视野",
            show_value(TCapaciteDescriptor.TagsCibleExcluded),
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
        if isinstance(self.turret, TTurretUnitDescriptor):
            turret_type_table_row = [
                Table_Row("炮台类型", "通用炮台"),
                self.TRAngleRotationMax,
                self.TRAngleRotationMaxPitch,
                self.TRAngleRotationMinPitch,
            ]
        elif isinstance(self.turret, TTurretInfanterieDescriptor):
            turret_type_table_row = [Table_Row("炮台类型", "步兵")]
        elif isinstance(self.turret, TTurretTwoAxisDescriptor):
            turret_type_table_row = [
                Table_Row("炮台类型", "载具(双轴)"),
                self.TRAimingPriority,
                self.TRAngleRotationBase,
                self.TRAngleRotationMax,
                self.TRAngleRotationBasePitch,
                self.TRAngleRotationMaxPitch,
                self.TRAngleRotationMinPitch,
                self.TRVitesseRotation,
                self.TROutOfRangeTrackingDuration,
            ]
        elif isinstance(self.turret, TTurretBombardierDescriptor):
            turret_type_table_row = [
                Table_Row("炮台类型", "飞机(挂载)"),
                self.TRFlyingAltitudeGRU,
                self.TRFlyingSpeedInKmph,
            ]
        turret_table = Content("炮台信息", Table(turret_type_table_row))

        mounted_weapon_name = []
        mounted_weapon_list = []
        for mounted_weapon in self.turret.MountedWeaponDescriptorList:
            mounted_weapon_name.append(
                mounted_weapon.Ammunition.KeyName
                if hasattr(mounted_weapon.Ammunition, "KeyName")
                else str(mounted_weapon.Ammunition)
            )
            mounted_weapon_list.append(
                MountedWeaponComponent(mounted_weapon).DetailComponent()
            )

        mounted_weapon_table = Content(
            "挂载武器信息", Tabs(mounted_weapon_name, mounted_weapon_list)
        )

        col1 = Col(turret_table, className="twelve columns")
        col2 = Col(mounted_weapon_table, className="twelve columns")

        row1 = Row([col1])
        row2 = Row([col2])

        content = Page_Content([row1, row2])
        return content


class MountedWeaponComponent:
    def __init__(self, mounted_weapon: TMountedWeaponDescriptor):
        self.mounted_weapon = mounted_weapon
        self.menu = []
        self.TRAmmoConsumption_ForInterface = Table_Row(
            "UI界面消耗弹药量",
            (
                show_value(self.mounted_weapon.AmmoConsumption_ForInterface)
                if hasattr(self.mounted_weapon, "AmmoConsumption_ForInterface")
                else ""
            ),
        )
        self.TRNbWeapons = Table_Row(
            "武器数量",
            (
                show_value(self.mounted_weapon.NbWeapons)
                if hasattr(self.mounted_weapon, "NbWeapons")
                else ""
            ),
        )
        self.TRSalvoStockIndex = Table_Row(
            "隶属索引号",
            (
                show_value(self.mounted_weapon.SalvoStockIndex)
                if hasattr(self.mounted_weapon, "SalvoStockIndex")
                else ""
            ),
        )

    def DetailComponent(self):
        mounted_weapon_table = Content(
            "挂载武器",
            Table(
                [
                    self.TRSalvoStockIndex,
                    self.TRNbWeapons,
                    self.TRAmmoConsumption_ForInterface,
                ]
            ),
        )
        mounted_weapon_components = Content(
            "挂载武器信息",
            ammunition.AmmunitionComponent(
                self.mounted_weapon.Ammunition
            ).AsComponent(),
        )
        col1 = Col(mounted_weapon_table, className="twelve columns")
        col2 = Col(mounted_weapon_components, className="twelve columns")

        row1 = Row([col1])
        row2 = Row([col2])
        content = Page_Content([row1, row2])
        return content


class WeaponComponent:
    def __init__(self, weapon: TWeaponManagerModuleDescriptor):
        self.weapon_key = weapon.KeyName
        self.weapon = weapon
        self.menu = ["概览"]

        self.TRSalves = Table_Row(
            "弹链数量",
            show_value(self.weapon.Salves) if hasattr(self.weapon, "Salves") else "",
        )
        self.TRSalvoIsMainSalvo = Table_Row(
            "为主武器",
            (
                show_value(self.weapon.SalvoIsMainSalvo)
                if hasattr(self.weapon, "SalvoIsMainSalvo")
                else ""
            ),
        )

    def BriefTable(self):
        page = None
        return page

    def DetailComponent(self):
        turret_name = []
        turret_list = []

        for index, turret_unit in enumerate(self.weapon.TurretDescriptorList):
            tab = ""
            tab += " & ".join(
                (
                    weapon.Ammunition.KeyName
                    if hasattr(weapon.Ammunition, "KeyName")
                    else str(weapon.Ammunition)
                )
                for weapon in turret_unit.MountedWeaponDescriptorList
            )
            turret_name.append(tab)
            turret_list.append(TurretComponment(turret_unit).DetailComponent())

        tabs = Tabs(turret_name, turret_list)
        return tabs

    def AsComponent(self):
        table = Page_Content(
            [
                Row(
                    [
                        Col(
                            TurretComponment(
                                self.weapon.TurretDescriptorList[0]
                            ).DetailComponent(),
                            className="twelve columns",
                        )
                    ]
                )
            ]
        )
        tabs = TurretComponment(self.weapon.TurretDescriptorList[0]).DetailComponent()
        return table

    def AsPage(self):
        tabs = self.DetailComponent()
        header = Header(self.weapon_key)
        page = Page(header, tabs)
        return page
