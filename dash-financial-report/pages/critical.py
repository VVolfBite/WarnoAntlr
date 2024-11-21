from ast import List, Pass
from tkinter import PAGES
from dash import dcc
from dash import html
import plotly.graph_objs as go
from pytz import country_timezones
from utils import *
from typing import Counter, Union

import sys

WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)

from src.extractor.refined_class import *


class TCriticalEffectComponment:
    def __init__(self, TCriticalEffect: TCriticalEffect):
        self.TCriticalEffect = TCriticalEffect

        self.TRName = Table_Row("效果名称", show_value(TCriticalEffect.__class__.__name__))
        self.TRRoll = Table_Row("生效区间", show_value(TCriticalEffect.Roll))
        self.TREffectsPack = Table_Row(
            "造成效果", show_value(TCriticalEffect.Descriptor.EffectsPack.KeyName)
        )
        self.TRTimeOut = Table_Row(
            "失效时间", show_value(TCriticalEffect.Descriptor.TimeOut)
        )
        self.TRRepairCost = Table_Row(
            "维修花费", show_value(TCriticalEffect.Descriptor.RepairCost)
        )
        self.TRUnique = Table_Row(
            "不进行叠加", show_value(TCriticalEffect.Descriptor.Unique)
        )

    def DetailComponent(self):
        return [
            self.TRName,
            self.TRRoll,
            self.TREffectsPack,
            self.TRTimeOut,
            self.TRRepairCost,
            self.TRUnique,
        ]


class TCriticalEffectModuleDescriptorComponment:
    def __init__(
        self, TCriticalEffectModuleDescriptor: TCriticalEffectModuleDescriptor
    ):
        self.TCriticalEffectModuleDescriptor = TCriticalEffectModuleDescriptor

        self.TRBounds = Table_Row(
            "随机投掷区间",
            show_value(TCriticalEffectModuleDescriptor.Bounds),
        )
        self.TRTerrainCriticalEffectTimer = Table_Row(
            "触发由地形引起的暴击效果",
            show_value(TCriticalEffectModuleDescriptor.TerrainCriticalEffectTimer),
        )

        self.TREffectsOnFront = Table_Row("直击正面可能造成的暴击效果")
        self.TREffectsOnSides = Table_Row("直击侧面可能造成的暴击效果")
        self.TREffectsOnRear = Table_Row("直击尾面可能造成的暴击效果")
        self.TREffectsOnTop = Table_Row("直击顶面可能造成的暴击效果")

        self.TRPierceEffectsOnFront = Table_Row("击穿正面可能造成的暴击效果")
        self.TRPierceEffectsOnSides = Table_Row("击穿侧面可能造成的暴击效果")
        self.TRPierceEffectsOnRear = Table_Row("击穿尾面可能造成的暴击效果")
        self.TRPierceEffectsOnTop = Table_Row("击穿顶面可能造成的暴击效果")

        self.TRRicochetEffectsOnFront = Table_Row("火箭弹扫射正面可能造成的暴击效果")
        self.TRRicochetEffectsOnSides = Table_Row("火箭弹扫射侧面可能造成的暴击效果")
        self.TRRicochetEffectsOnRear = Table_Row("火箭弹扫射尾面可能造成的暴击效果")
        self.TRRicochetEffectsOnTop = Table_Row("火箭弹扫射顶面可能造成的暴击效果")

    def aggr(self, effect_list: list[TCriticalEffect]):
        if effect_list == None:
            return []
        table_row = []
        for effect in effect_list:
            table_row += TCriticalEffectComponment(effect).DetailComponent()
        return table_row

    def DetailComponent(self):
        critical_effect = (
            [self.TRBounds, self.TRTerrainCriticalEffectTimer]
            + [self.TREffectsOnFront]
            + self.aggr(self.TCriticalEffectModuleDescriptor.EffectsOnFront)
            + [self.TREffectsOnSides]
            + self.aggr(self.TCriticalEffectModuleDescriptor.EffectsOnSides)
            + [self.TREffectsOnRear]
            + self.aggr(self.TCriticalEffectModuleDescriptor.EffectsOnRear)
            + [self.TREffectsOnTop]
            + self.aggr(self.TCriticalEffectModuleDescriptor.EffectsOnTop)
            + [self.TRPierceEffectsOnFront]
            + self.aggr(self.TCriticalEffectModuleDescriptor.EffectsOnFront)
            + [self.TRPierceEffectsOnSides]
            + self.aggr(self.TCriticalEffectModuleDescriptor.EffectsOnSides)
            + [self.TRPierceEffectsOnRear]
            + self.aggr(self.TCriticalEffectModuleDescriptor.EffectsOnRear)
            + [self.TRPierceEffectsOnTop]
            + self.aggr(self.TCriticalEffectModuleDescriptor.EffectsOnTop)
            + [self.TRRicochetEffectsOnFront]
            + self.aggr(self.TCriticalEffectModuleDescriptor.EffectsOnFront)
            + [self.TRRicochetEffectsOnSides]
            + self.aggr(self.TCriticalEffectModuleDescriptor.EffectsOnSides)
            + [self.TRRicochetEffectsOnRear]
            + self.aggr(self.TCriticalEffectModuleDescriptor.EffectsOnRear)
            + [self.TRRicochetEffectsOnTop]
            + self.aggr(self.TCriticalEffectModuleDescriptor.EffectsOnTop)
        )
        return critical_effect


class CriticalPage:
    def __init__(
        self,
        CriticalEffectDict: dict[str:TCriticalEffectModuleDescriptor]
    ):
        self.CriticalEffectDict = CriticalEffectDict

    def DetailComponent(self):
        critical_content_list = []
        for (
            critical_name,
            critical_effect,
        ) in self.CriticalEffectDict.items():
            content = Content(critical_name, Table(TCriticalEffectModuleDescriptorComponment(critical_effect).DetailComponent()))
            critical_content_list.append(content)
        return critical_content_list

    def AsPage(self):
        critical_content_list = self.DetailComponent()
        critical_page_content = Page_Content(
            [
                Row(
                    [
                        Col(critical_content_list[i], className="twelve columns"),
                    ]
                )
                for i in range(0, len(critical_content_list))
            ]
        )
        header = Header("暴击效果")
        page = Page(header, critical_page_content)
        return page
