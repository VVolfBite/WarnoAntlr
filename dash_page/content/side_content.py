from dash import Dash, html, Input, Output, State, dcc
import dash_bootstrap_components as dbc


class SideContent:
    def __init__(self):
        pass

    def layout():
        title = html.H1("Warno")
        text_descriptor = html.P("请在这里选择想要查看的信息。", className="text-body")
        dropdown_querytype = dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem("字典信息", header=True),
                dbc.DropdownMenuItem("单位"),
                dbc.DropdownMenuItem("武器"),
                dbc.DropdownMenuItem("弹药"),
                dbc.DropdownMenuItem("特性与光环"),       
                dbc.DropdownMenuItem("暴击效果"),           
                dbc.DropdownMenuItem("地形"), 
                dbc.DropdownMenuItem("师与卡组"),                               
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("其他信息", header=True),
                dbc.DropdownMenuItem("特殊机制", header=True),
                dbc.DropdownMenuItem(divider=True),
                html.P(
                    "选择一个你感兴趣的内容",
                    className="text-muted px-4 mt-4",
                ),
            ],
            label="选择一个你感兴趣的内容",
        )
