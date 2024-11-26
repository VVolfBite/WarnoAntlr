from dash import Dash, html, Input, Output, State, dcc
import dash_bootstrap_components as dbc

# 自定义 HTML 模板，为 body 标签添加 id
app = Dash(
    __name__,
    external_scripts=[
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
    ],
    external_stylesheets=[
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
# 布局设置

offcanvas = html.Div(
    [
        dcc.Store(id="theme-store", data="light"),
        dbc.Button(
            html.I(className="bi bi-code"),
            id="open-offcanvas",
            style={
                "position": "fixed",
                "left": "10px",
                "bottom": "10px",
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
                "bottom": "50px",
                "zIndex": "1050",
            },
            n_clicks=0,
        ),
        dbc.Offcanvas(
            html.P(
                "This is the content of the Offcanvas. "
                "Close it by clicking on the close button, or "
                "the backdrop."
            ),
            id="offcanvas",
            title=html.H1("Title"),
        ),
    ]
)


app.layout = html.Div(offcanvas)


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

if __name__ == "__main__":
    app.run_server(debug=True)
