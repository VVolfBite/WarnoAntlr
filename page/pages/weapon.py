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
from pages import ammunition


class TurretComponment:
    def __init__(
        self,
        turret: Union[
            TTurretUnitDescriptor,
            TTurretInfanterieDescriptor,
            TTurretTwoAxisDescriptor,
            TTurretBombardierDescriptor,
        ],
    ):
        self.turret = turret

        self.TRAimingPriority = Table_Row(
            "瞄准优先级",
            (
                show_value(turret.AimingPriority)
                if hasattr(turret, "AimingPriority")
                else ""
            ),
        )
        self.TROutOfRangeTrackingDuration = Table_Row(
            "超出射程的追敌时间",
            (
                show_value(turret.OutOfRangeTrackingDuration)
                if hasattr(turret, "OutOfRangeTrackingDuration")
                else ""
            ),
        )

        self.TRVitesseRotation = Table_Row(
            "炮台旋转速度",
            (
                show_value(turret.VitesseRotation)
                if hasattr(turret, "VitesseRotation")
                else ""
            ),
        )
        self.TRAngleRotationBase = Table_Row(
            "炮台旋转角度",
            (
                show_value(turret.AngleRotationBase)
                if hasattr(turret, "AngleRotationBase")
                else ""
            ),
        )
        self.TRAngleRotationMax = Table_Row(
            "炮台最大旋转角度",
            (
                show_value(turret.AngleRotationMax)
                if hasattr(turret, "AngleRotationMax")
                else ""
            ),
        )
        self.TRAngleRotationBasePitch = Table_Row(
            "炮台仰俯角度",
            (
                show_value(turret.AngleRotationBasePitch)
                if hasattr(turret, "AngleRotationBasePitch")
                else ""
            ),
        )
        self.TRAngleRotationMaxPitch = Table_Row(
            "炮台最大仰俯角度",
            (
                show_value(turret.AngleRotationMaxPitch)
                if hasattr(turret, "AngleRotationMaxPitch")
                else ""
            ),
        )
        self.TRAngleRotationMinPitch = Table_Row(
            "炮台最小仰俯角度",
            (
                show_value(turret.AngleRotationMinPitch)
                if hasattr(turret, "AngleRotationMinPitch")
                else ""
            ),
        )

        self.TRFlyingAltitudeGRU = Table_Row(
            "投弹高度",
            (
                show_value(turret.FlyingAltitudeGRU)
                if hasattr(turret, "FlyingAltitudeGRU")
                else ""
            ),
        )
        self.TRFlyingSpeedInKmph = Table_Row(
            "投弹速度",
            (
                show_value(turret.FlyingSpeedInKmph)
                if hasattr(turret, "FlyingSpeedInKmph")
                else ""
            ),
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
