from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pickle
import sys


WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)
from dash_page.tool.component import *

toggle_button = html.Button("Toggle sidebar", id="toggle-button")

side_content = html.Div(id="side-content")

side = OffCanvasSidebar(
    offcanvas_id="myOffcanvas",
    button=toggle_button,
    side_content=side_content,
    side_header="Sidebar",
    position="start",
)
# 创建一个空页面，包含一个折叠侧边栏和按钮
app_layout = Page(page_header=html.Div(), sections=side)  # 空的页面头部
global_theme = "dark"
app = Dash(
    __name__,
    external_scripts=[
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
    ],
    external_stylesheets=[
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
        "https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css",
    ],
)

app.layout = html.Div(app_layout)
# app.layout = html.Div([tool])


if __name__ == "__main__":
    app.run_server(debug=True)
