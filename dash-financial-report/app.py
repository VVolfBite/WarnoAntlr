import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from pages import (
    ammunition,
    weapon,
    unit,
    capacityandeffect,
    division,
    terrain,
    critical
)
import pickle
import sys


WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)
import config
from antlr4 import *
from src.parsers.parser_interface import ParserInterface
from src.extractor.extract_class import *
from src.extractor.refined_class import *
with open("global.pkl",'rb') as f:
    global_dict  = pickle.load(f)

# ammo_object = global_dict['Ammo_Canon_AP_105mm_L7A3_Leo1V']
# weapon_object = global_dict['WeaponDescriptor_Su_25_he_SOV']
# unit_object = global_dict['Descriptor_Unit_2K11_KRUG_DDR']
effect_list = [value for key,value in global_dict.items() if isinstance(value,TEffectsPackDescriptor)]
capacity_list = [value for key,value in global_dict.items() if isinstance(value,TCapaciteDescriptor)]

GlobalPackDict = {key:value for key,value in global_dict.items() if isinstance(value,DeckPackDescriptor)}
GlobalDeckDivisionDict = {key:value for key,value in global_dict.items() if isinstance(value,TDeckDivisionDescriptor)}
DivisionRules = [value for key,value in global_dict.items() if isinstance(value,TDeckDivisionRules)][0]

terrain_dict = {key:value for key,value in global_dict.items() if isinstance(value,TGameplayTerrain)}

CriticalEffect_dict = {key:value for key,value in global_dict.items() if isinstance(value,TCriticalEffectModuleDescriptor)}

unite_object = None

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)
app.title = "Warno"
server = app.server

# 侧边栏 目前还没和主页面关联
sidebar = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.H2("Sidebar", style={"textAlign": "center"}),
                                html.H6("Section 1"),
                                html.P("This section contains a dropdown for options."),
                            ],
                            className="twelve columns",
                        ),
                    ],
                    className="row ",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                dcc.Dropdown(
                                    id="dropdown-section-1",
                                    options=[
                                        {"label": "Option 1", "value": "option1"},
                                        {"label": "Option 2", "value": "option2"},
                                    ],
                                    placeholder="Select an option",
                                ),
                                html.H6("Section 2"),
                                html.P("This section provides further information."),
                                dcc.Dropdown(
                                    id="dropdown-section-2",
                                    options=[
                                        {"label": "Option A", "value": "optionA"},
                                        {"label": "Option B", "value": "optionB"},
                                    ],
                                    placeholder="Choose an option",
                                ),
                            ],
                            className="twelve columns",
                        ),
                    ],
                    className="row ",
                ),
            ],
            className="sub_page",
        )
    ],
    className="page",
)

# 整体页面
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            [
                html.Div(
                    [sidebar],
                        style={
                        "margin-right": "20px",
                        "margin-left": "20px",
                        "minWidth": "25%",
                        "maxWidth": "25%",
                    }, 
                ),
                html.Div(
                    id="page-content",
                    style={
                        "margin-left": "20px",
                        "margin-right": "20px",
                        "minWidth": "70%",  # 设置最小宽度为 500px
                        "maxWidth": "70%",
                    },
                ),
            ],
            style={
                "display": "flex", 
            },
        ),
    ]
)


# 主页面逻辑
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    global ammo_object
    if pathname == "/dash-financial-report/price-performance":
        return capacityandeffect.CapacityAndEffectPage(capacity_list,effect_list).AsPage()
    elif pathname == "/dash-financial-report/portfolio-management":
        return capacityandeffect.CapacityAndEffectPage(capacity_list,effect_list).AsPage()
    elif pathname == "/dash-financial-report/fees":
        return capacityandeffect.CapacityAndEffectPage(capacity_list,effect_list).AsPage()
    elif pathname == "/dash-financial-report/distributions":
        return capacityandeffect.CapacityAndEffectPage(capacity_list,effect_list).AsPage()
    elif pathname == "/dash-financial-report/news-and-reviews":
        return capacityandeffect.CapacityAndEffectPage(capacity_list,effect_list).AsPage()
    elif pathname == "/dash-financial-report/full-view":
        return (
            capacityandeffect.CapacityAndEffectPage(capacity_list,effect_list).AsPage()
        )
    else:
        return critical.CriticalPage(CriticalEffect_dict).AsPage()
        # return terrain.TerrainPage(terrain_dict).AsPage()
        # return division.DivisionPage(DivisionRules,GlobalPackDict,GlobalDeckDivisionDict).AsPage()
        # return capacityandeffect.CapacityAndEffectPage(capacity_list,effect_list).AsPage()
        # return unit.UnitComponent(unit_object).AsPage()
        # return weapon.WeaponComponent(weapon_object).AsPage()
        # return ammunition.AmmunitionComponent(ammo_object).AsPage()


if __name__ == "__main__":

    
    with open("global.pkl",'rb') as f:
        global_dict  = pickle.load(f)

    stop = 1

    app.run_server(debug=True)
