import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from pages import (
    overview,
    pricePerformance,
    portfolioManagement,
    feesMins,
    distributions,
    newsReviews,
    ammunition,
    weapon,
    unit
)
import pickle
import sys


WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)
import config
from antlr4 import *
from src.parsers.parser_interface import ParserInterface
from src.parsers.register_class.RClass import *
with open("global.pkl",'rb') as f:
    global_dict  = pickle.load(f)
global_dict = ParserInterface.refer_class(global_dict,global_dict)

ammo_object = global_dict['Ammo_Canon_AP_105mm_L7A3_Leo1V']
weapon_object = global_dict['WeaponDescriptor_Su_25_he_SOV']
unit_object = global_dict['Descriptor_Unit_2K11_KRUG_DDR']
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
        return pricePerformance.create_layout(app)
    elif pathname == "/dash-financial-report/portfolio-management":
        return portfolioManagement.create_layout(app)
    elif pathname == "/dash-financial-report/fees":
        return feesMins.create_layout(app)
    elif pathname == "/dash-financial-report/distributions":
        return distributions.create_layout(app)
    elif pathname == "/dash-financial-report/news-and-reviews":
        return newsReviews.create_layout(app)
    elif pathname == "/dash-financial-report/full-view":
        return (
            overview.create_layout(app),
            pricePerformance.create_layout(app),
            portfolioManagement.create_layout(app),
            feesMins.create_layout(app),
            distributions.create_layout(app),
            newsReviews.create_layout(app),
        )
    else:
        return unit.UnitComponent(unit_object).AsPage()
        # return weapon.WeaponComponent(weapon_object).AsPage()
        # return ammunition.AmmunitionComponent(ammo_object).AsPage()


if __name__ == "__main__":

    for file in config.PROCESS_FILE_LIST:
        file = config.RAW_DATA_PATH + file
        # node = ParserInterface.generate_node_object(file)
        # # # ParserInterface.set_class_json(config.CLASS_JSON)
        # # # ParserInterface.generate_class_json_from_ndf_folder(config.RAW_DATA_PATH)
        # # # ParserInterface.generate_class_from_json(config.CLASS_JSON, config.CLASS_PY)
        # # ParserInterface.set_class_py(config.CLASS_PY)
        # # # ParserInterface.register_class(node)
        # value = ParserInterface.value_from_node(node)
        # global_dict.update(value)


    # with open("global.pkl",'wb') as f:
    #     pickle.dump(global_dict, f)
    
    with open("global.pkl",'rb') as f:
        global_dict  = pickle.load(f)
    # global_dict = ParserInterface.refer_class(global_dict,global_dict)

    # with open("global.pkl",'wb') as f:
    #     pickle.dump(global_dict, f)
    
    # with open("global.pkl",'rb') as f:
    #     global_dict  = pickle.load(f)
  
    DamageResistanceParams = global_dict['DamageResistanceParams']

    app.run_server(debug=True)
