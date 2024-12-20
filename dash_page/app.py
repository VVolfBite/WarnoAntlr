from dash import Dash, html, Input, Output, State, dcc
import dash_bootstrap_components as dbc
import pickle
import sys
import os

# 获取当前脚本的绝对路径
current_directory = os.path.abspath(__file__)

# 获取前两级目录
WORK_DIRECTORY = os.path.dirname(os.path.dirname(current_directory))


# 将工作目录添加到 sys.path
sys.path.append(WORK_DIRECTORY)

import config
from dash_page.util import dataProcess
from dash_page.content import sideContent

# 自定义 HTML 模板，为 body 标签添加 id
app = Dash(
    __name__,
    external_scripts=[
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
    ],
    external_stylesheets=[
        "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.2.4/dbc.min.css",
        "https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css",
    ],
    index_string="""
                <!DOCTYPE html>
                <html lang="en">
                    <head>
                        {%metas%}
                        <title>{%title%}</title>
                        {%favicon%}
                        {%css%}
                    </head>
                    <body id="body" data-bs-theme="light">
                        {%app_entry%}
                        <footer>
                            {%config%}
                            {%scripts%}
                            {%renderer%}
                        </footer>
                    </body>
                </html>
                """,
)
# 将主题挂载在body下,防止临时生成的页面没有挂载在layout下
app.clientside_callback(
    """
    function(theme) {
        const body = document.getElementById("body");
        if (body) {
            body.setAttribute("data-bs-theme", theme);
        }
        return null; // 返回值不影响
    }
    """,
    Input("theme-store", "data"),
)

data_manager = dataProcess.DataManager("./dash_page/util/global.pkl")
# 布局设置
side_content = sideContent.SideContent(app, data_manager)
side_content.register_callbacks()
side_bar = html.Div(
    [
        dcc.Store(id="theme-store", data="light"),
        dbc.Button(
            html.I(className="bi bi-code"),
            id="open-offcanvas",
            style={
                "position": "fixed",
                "left": "10px",
                "bottom": "100px",
                "zIndex": "1050",
            },
            n_clicks=0,
        ),
        dbc.Button(
            html.I(className="bi bi-brightness-high"),
            id="change-theme",
            style={
                "position": "fixed",
                "left": "10px",
                "bottom": "60px",
                "zIndex": "1050",
            },
            n_clicks=0,
        ),
        dbc.Offcanvas(
            side_content.layout(),
            id="offcanvas",
            title=html.H1("Warno"),
        ),
    ]
)


# 回调函数：切换主题状态
@app.callback(
    Output("theme-store", "data"),
    Output("change-theme", "children"),
    Input("change-theme", "n_clicks"),
    State("theme-store", "data"),
)
def toggle_theme(n1, current_theme):
    if n1 and current_theme == "dark":
        return "light", html.I(className="bi bi-brightness-high")
    if n1 and current_theme == "light":
        return "dark", html.I(className="bi bi-moon")
    return current_theme, html.I(
        className="bi bi-brightness-high" if current_theme == "light" else "bi bi-moon"
    )


# 回调函数：开关侧边栏
@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


main_content = [
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
    html.H1(12321312),
]
main_page = html.Div(
    [
        dbc.NavbarSimple(
            children=[],
            brand="Warno",
            brand_href="#",
            color="primary",
            dark=True,
            fixed="top",
            sticky=True,
        ),
        html.Div(
            children=main_content,
            className="container mt-6 mb-6",
            id="main-content",  # 根据导航栏高度调整

        ),  # Wrap main_content in a Div if needed
        dbc.NavbarSimple(
            children=[],
            brand="Footer",
            brand_href="#",
            color="secondary",
            dark=True,
            fixed="bottom",
            sticky=True,
        ),
    ],
    className="container",
)
@app.callback(
    Output("main-content", "children"),
    Input(side_content.querytype_store_id, "data"), [Input(side_content.querykey_store_id, "data")],
    prevent_initial_call=True,
)
def update_main_content(type_data, key_data):
    if type_data :
        return [html.H1(type_data)]

app.layout = html.Div([side_bar, main_page])


if __name__ == "__main__":
    app.run_server(debug=True)
