import pickle
import sys
WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)
import config
from src.extractor.refined_class import *
from dash_page.util.dataManager import DataManager
from dash import dcc, html
import dash_bootstrap_components as dbc

class AmmunitionComponent:
    def __init__(self,app, data_manager: DataManager, ammunition: TAmmunitionDescriptor):
        self.ammunition_key = ammunition.KeyName if hasattr(ammunition, "KeyName") else str(ammunition)
        self.ammunition = ammunition
        self.table_row_list = {
            "brief":
            {
                "基础信息":{
                    
                }
            }
        }

        # 创建一些直接使用变量的内容
        self.TRMinMaxCategory = ammunition.MinMaxCategory if hasattr(ammunition, "MinMaxCategory") else ""
        self.TRTraitsToken = ammunition.TraitsToken if hasattr(ammunition, "TraitsToken") else ""
        self.TRIsSubAmmunition = ammunition.IsSubAmmunition if hasattr(ammunition, "IsSubAmmunition") else ""
        self.TRAffecteParNombre = ammunition.AffecteParNombre if hasattr(ammunition, "AffecteParNombre") else ""

        self.TRArme_Family = ammunition.Arme.Family if hasattr(ammunition, "Arme") else ""
        self.TRArme_Index = ammunition.Arme.Index if hasattr(ammunition, "Arme") else ""
        self.TRPhysicalDamages = ammunition.PhysicalDamages if hasattr(ammunition, "PhysicalDamages") else ""
        self.TRSuppressDamages = ammunition.SuppressDamages if hasattr(ammunition, "SuppressDamages") else ""

        # 其他的行内容
        self.TRPorteeMaximaleGRU = ammunition.PorteeMaximaleGRU if hasattr(ammunition, "PorteeMaximaleGRU") else ""
        self.TRPorteeMinimaleGRU = ammunition.PorteeMinimaleGRU if hasattr(ammunition, "PorteeMinimaleGRU") else ""
        
        self.TRTempsDeVisee = ammunition.TempsDeVisee if hasattr(ammunition, "TempsDeVisee") else ""
        self.TRTempsEntreDeuxSalves = ammunition.TempsEntreDeuxSalves if hasattr(ammunition, "TempsEntreDeuxSalves") else ""

    def BriefTable(self):
        return dbc.Table(
            [
                html.Tr([html.Td("基础"), html.Td(self.TRMinMaxCategory)]),
                html.Tr([html.Td("特性词条"), html.Td(self.TRTraitsToken)]),
                html.Tr([html.Td("描述对象为子武器"), html.Td(self.TRIsSubAmmunition)]),
                html.Tr([html.Td("描述对象因数量属性倍增"), html.Td(self.TRAffecteParNombre)]),
                html.Tr([html.Td("伤害所属族"), html.Td(self.TRArme_Family)]),
                html.Tr([html.Td("伤害索引号"), html.Td(self.TRArme_Index)]),
                html.Tr([html.Td("基底伤害"), html.Td(self.TRPhysicalDamages)]),
                html.Tr([html.Td("压制伤害"), html.Td(self.TRSuppressDamages)]),
                html.Tr([html.Td("对地最大射程"), html.Td(self.TRPorteeMaximaleGRU)]),
                html.Tr([html.Td("对地最小射程"), html.Td(self.TRPorteeMinimaleGRU)]),
                html.Tr([html.Td("瞄准时间"), html.Td(self.TRTempsDeVisee)]),
                html.Tr([html.Td("装填时间"), html.Td(self.TRTempsEntreDeuxSalves)]),
            ],
            bordered=True,
        )

    def DetailComponent(self):
        basic_table = dbc.Card(
            dbc.CardBody([
                html.H4("基础信息", className="card-title"),
                self.BriefTable()
            ])
        )

        # 将不同的部分分配到适当的 Card 组件中
        damage_table = dbc.Card(
            dbc.CardBody([
                html.H4("伤害信息", className="card-title"),
                dbc.Table(
                    [
                        html.Tr([html.Td("伤害所属族"), html.Td(self.TRArme_Family)]),
                        html.Tr([html.Td("伤害索引号"), html.Td(self.TRArme_Index)]),
                        html.Tr([html.Td("基底伤害"), html.Td(self.TRPhysicalDamages)]),
                        html.Tr([html.Td("压制伤害"), html.Td(self.TRSuppressDamages)]),
                    ],
                    bordered=True,
                ),
            ])
        )

        # 其他的表格可以继续按照此方式整理
        range_table = dbc.Card(
            dbc.CardBody([
                html.H4("射程信息", className="card-title"),
                dbc.Table(
                    [
                        html.Tr([html.Td("对地最大射程"), html.Td(self.TRPorteeMaximaleGRU)]),
                        html.Tr([html.Td("对地最小射程"), html.Td(self.TRPorteeMinimaleGRU)]),
                    ],
                    bordered=True,
                ),
            ])
        )

        # 最后你可以继续为每个数据块创建类似的 Card 组件

        # 创建一个列来布局内容
        col1 = dbc.Col([basic_table])
        col2 = dbc.Col([damage_table])
        col3 = dbc.Col([range_table])

        # 将这些列放到一个行里
        row = dbc.Row([col1, col2, col3])

        # 将行内容作为一个更大的页面元素
        content = dbc.Container([row])

        return content

    def AsComponent(self):
        tabs = dcc.Tabs(
            id="tabs",
            value="overview",
            children=[
                dcc.Tab(
                    label="概览",
                    value="overview",
                    children=[self.BriefTable()]
                ),
                dcc.Tab(
                    label="详细",
                    value="detail",
                    children=[self.DetailComponent()]
                ),
            ]
        )
        return tabs

    def AsPage(self):
        header = html.Header(
            html.H1(self.ammunition_key)
        )

        page = html.Div([header, self.AsComponent()])
        return page
