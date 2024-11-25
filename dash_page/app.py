import pickle
import sys
from dash import Dash, html, dcc,Input,Output

import dash_bootstrap_components as dbc
from streamlit import button
WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)
from dash_page.tool.component import *

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

side_content = html.Div(
    children=[
        Dropdown("query_type_dropdown","选择查询的类型",["弹药","武器","单位","特性","机制"]),
        FloatingDropdown(input_id="dropdown1", label="Search and Select", suggestions = ["Option 1", "Option 2", "Option 3"], explanation = "Type to filter options.")

    ]
)

side_bar = OffCanvasSidebar(
    offcanvas_id="sidebar",
    button_class="btn btn-primary",
    side_content=side_content,
    side_header="Sidebar",
    position="start",
)




app_layout = Page(page_header=html.Div(), sections=side_bar)  # 空的页面头部

app.layout = html.Div(app_layout, id= "top_page",**{"data-bs-theme": "dark"})

# CallBack 部分
## 主题切换
@app.callback(
    [Output("top_page", "data-bs-theme"),
     Output("button_theme", "children")],
    Input("button_theme", "n_clicks"),
    prevent_initial_call=True,
)
def toggle_theme(n_clicks):
    if n_clicks % 2 == 0:
        return "light",[html.I(className="bi bi-brightness-high")]
    else:
        return "dark" ,html.I(className="bi bi-moon")


if __name__ == "__main__":
    app.run_server(debug=True)
