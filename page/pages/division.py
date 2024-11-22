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



class UnitRuleListComponment:
    def __init__(
        self,
        UnitRuleList: list[TDeckUniteRule],
        PackList : dict,
        GlobalPackDict: dict
    ):
        self.UnitRuleList = UnitRuleList
        self.PackList = PackList
        self.GlobalPackDict = GlobalPackDict

    def DetailComponent(self):
        unit_rule_table = []
        for unit_pack,pack_num in self.PackList.items():
            for deck_unite_rule in self.UnitRuleList:
                if deck_unite_rule.UnitDescriptor != self.GlobalPackDict[unit_pack].Unit:
                    continue
                pack_unit = deck_unite_rule.UnitDescriptor
                pack_num = pack_num
                pack_available_without_transport = deck_unite_rule.AvailableWithoutTransport
                pack_available_transport_list = deck_unite_rule.AvailableTransportList
                pack_number_of_unit_in_pack = deck_unite_rule.NumberOfUnitInPack
                pack_number_of_unit_in_pack_XP_multiplier = deck_unite_rule.NumberOfUnitInPackXPMultiplier
                
                unit_rule_table.append(Table_Row(show_value(str(pack_unit))))
                unit_rule_table.append(Table_Row("卡组单位名",show_value(str(pack_unit))))
                unit_rule_table.append(Table_Row("卡组数量",show_value(str(pack_num))))
                unit_rule_table.append(Table_Row("卡组单位无配套载具",show_value(pack_available_without_transport)))
                unit_rule_table.append(Table_Row("卡组单位可用载具列表",show_value(pack_available_transport_list)))
                unit_rule_table.append(Table_Row("卡组单位数量修正",show_value(pack_number_of_unit_in_pack_XP_multiplier)))
        return unit_rule_table
                
class TDeckDivisionDescriptorComponment:
    def __init__(
        self,
        TDeckDivisionDescriptor: TDeckDivisionDescriptor
    ):
        self.TDeckDivisionDescriptor = TDeckDivisionDescriptor
        self.KeyName = TDeckDivisionDescriptor.KeyName
        self.TRCfgName = Table_Row(
            "师名称",
            show_value(TDeckDivisionDescriptor.CfgName),
        )
        self.TRMaxActivationPoints = Table_Row(
            "最大行动点数",
            show_value(TDeckDivisionDescriptor.MaxActivationPoints),
        )
        self.TRCostMatrix = Table_Row(
            "行动点数矩阵",
            show_value(TDeckDivisionDescriptor.CostMatrix),
        )
        self.TRDivisionTags = Table_Row(
            "师词条",
            show_value(TDeckDivisionDescriptor.DivisionTags),
        )

    def DetailComponent(self):
        table_row = [
                self.TRCfgName,
                self.TRMaxActivationPoints,
                self.TRCostMatrix,
                self.TRDivisionTags,
            ]
        self.TDeckDivisionDescriptor.PackList
        return table_row

class DivisionPage:
    def __init__(self,TDeckDivisionRules: TDeckDivisionRules,GlobalPackDict: dict[str:int], GlobalDeckDivision:dict[str:TDeckDivisionRule]):
        self.TDeckDivisionRules = TDeckDivisionRules
        self.GlobalDeckDivision = GlobalDeckDivision
        self.GlobalPackDict = GlobalPackDict

    def DetailComponent(self):
        division_content_list = []
        for division_deck,division_rule in self.TDeckDivisionRules.DivisionRules.items():
            table_rows = []
            deck = self.GlobalDeckDivision[division_deck]
            comp1 = TDeckDivisionDescriptorComponment(deck)
            table_rows += comp1.DetailComponent()
            comp2 = UnitRuleListComponment(division_rule.UnitRuleList,deck.PackList,self.GlobalPackDict)
            table_rows += comp2.DetailComponent()
            content = Content(comp1.TRCfgName,Table(table_rows))
            division_content_list.append(content)
        return division_content_list
    
    def AsPage(self):
        division_content_list = self.DetailComponent()
        division_page_content = Page_Content(
            [
                Row([
                    Col(division_content_list[i], className="twelve columns"),
                ])
                for i in range(0, len(division_content_list))
            ]
        )
        header = Header("师卡组")
        page = Page(header, division_page_content)
        return page