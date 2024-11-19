import pickle
from pydoc import classname
from dash import html
from dash import dcc

import sys

WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)
import config
from antlr4 import *



def show_value(value, default_view=None):
    if value is None:
        return (
            "否"
            if default_view == "bool"
            else "不可用" if default_view == "int" else "无"
        )
    elif isinstance(value, bool):
        return "是" if value else "否"
    elif isinstance(value, (int, float)):
        return "默认" if value == -1 or value == -1.0 else str(value)
    elif isinstance(value, (list, tuple)):
        return f"[ {' , '.join(repr(item) for item in value)} ]"
    return str(value)

def Page(header: html.Div, tabs: html.Div):
    return html.Div([header,tabs], className="page")

def Header(title: str):
    page_header = html.Div(
        [
            html.Div(
                [],
                className="row",
                style={"height": "20px"},  # 根据需要调整高度
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5(title)],  # 使用传入的 title 参数
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/dash-financial-report/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return html.Div([page_header, html.Br([])])

def Tabs(label_list:list[str], tab_content:list[html.Div]):
    return html.Div(
        [
            dcc.Tabs(
                [
                    dcc.Tab(label=label, children=[content])
                    for label, content in zip(label_list, tab_content)
                ],
                className="tabs",  
            )
        ],
        className="pagetwo"
    )

def Page_Content(rows: list[html.Div]):
    return html.Div(rows, className="sub_page")

def Row(cols: list[html.Div]):
    return html.Div(cols, className="row")

def Col(contents: list[html.Div], className="six columns"):
    return html.Div(contents, className=className)

def Content(sub_header: str, component:html):
    return [html.H6([sub_header], className="subtitle padded"), component]

def Table(table_rows: list[html.Tr]):
    return html.Table(table_rows)

def Table_Row(key:str, value:str=None, caption:str=None):
    if value is None:
        return html.Tr([html.Th(key,colSpan=2,style={"font-weight": "bold","width": "100%","text-align": "center",},)])
    key_cell = html.Td(
        [
            html.Div([key]),
            (
                html.Div(caption, style={"font-size": "small", "color": "gray"})
                if caption
                else None
            ),
        ],
        style={"width": "50%", "font-weight": "bold"},
    )
    value_cell = html.Td([value], style={"width": "50%"})

    return html.Tr([key_cell, value_cell])

def make_dash_table(df):
    pass
