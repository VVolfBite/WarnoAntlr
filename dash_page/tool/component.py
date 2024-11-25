from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


def modify_component(component, attr, operation, value=None):

    if not hasattr(component, attr):
        raise AttributeError(f"组件没有名为 '{attr}' 的属性。")

    current_value = getattr(component, attr)

    if operation == "set":
        # 设置属性值
        setattr(component, attr, value)

    elif operation == "add":
        # 如果是字符串类型，可以添加到字符串中
        if isinstance(current_value, str) and isinstance(value, str):
            setattr(component, attr, current_value + value)
        # 如果是列表类型，可以追加元素
        elif isinstance(current_value, list):
            current_value.append(value)
            setattr(component, attr, current_value)

    elif operation == "remove":
        # 如果是字符串类型，删除指定子字符串
        if isinstance(current_value, str) and isinstance(value, str):
            setattr(component, attr, current_value.replace(value, ""))
        # 如果是列表类型，移除指定元素
        elif isinstance(current_value, list) and value in current_value:
            current_value.remove(value)
            setattr(component, attr, current_value)

    elif operation == "clear":
        # 清空属性值
        if isinstance(current_value, list):
            setattr(component, attr, [])
        elif isinstance(current_value, str):
            setattr(component, attr, "")
        else:
            raise ValueError("不支持的清空操作类型。")
    else:
        raise ValueError("无效的操作类型。")


# Structure
def Page(page_header: html.Div, sections: list[html.Div]) -> html.Div:
    return html.Div(className="container", children=[page_header] + sections)


def Section(section_header: html.Div, rows: list[html.Div]) -> html.Div:
    return html.Div(
        className="bs-docs-section",
        children=[
            section_header,
        ]
        + rows,
    )


def Row(cols: list[html.Div]) -> html.Div:
    return html.Div(className="row", children=[col for col in cols])


def Col(components: list[html.Div], width: int = 12) -> html.Div:
    """
    width : int 属于范围 1 - 12
    """
    return html.Div(
        className=f"col-lg-{width}", children=[componment for componment in components]
    )


def Component(comps: list[html.Div]):
    return html.Div(className="bs-component", children=comps)


# Header Header 是直接制作好的 Row-Col-H
def PageHeader(descriptor: str) -> html.Div:
    return html.Div(
        className="page-header", children=[Row([Col([html.H1(descriptor)])])]
    )


def SectionHeader(descriptor: str) -> html.Div:
    return html.Div(
        className="page-header", children=[Row([Col([html.H2(descriptor)])])]
    )


## 因为Component在Col成型之前实现
def ComponentTitle(descriptor: str) -> html.H3:
    return html.H3(children=[descriptor])


# Componment
## Nav
def Navbar(
    descriptor: str,  # 品牌名称，显示在左侧
    nav_item_list: list[html.Li],  # 导航项列表
    content_list: list[html.Div],  # 对应的内容区列表
    theme: str = "bg-body-tertiary",  # 主题样式，默认为 "bg-body-tertiary"
    collapse_id: str = "navbarColor04",  # 折叠区域的 ID
) -> html.Nav:
    """
    WIP
    """
    return html.Nav(
        className=f"navbar navbar-expand-lg {theme}",
        children=[
            html.Div(
                className="container-fluid",
                children=[
                    # 品牌名称部分
                    html.A(descriptor, className="navbar-brand", href="#"),
                    # 折叠区域
                    html.Div(
                        className="navbar-collapse collapse show",
                        id=collapse_id,
                        children=[
                            html.Ul(
                                className="navbar-nav me-auto", children=nav_item_list
                            ),
                        ],
                    ),
                ],
            ),
            # 内容区域部分
            *content_list,  # 展开内容区列表，作为子组件加入到导航栏
        ],
    )


def NavItem(descriptor: str):
    return html.Li(
        className="nav-item",
        children=[
            html.A(
                className="nav-link",
                **{
                    "data-bs-toggle": "tab",
                    "href": f"#",
                    "role": "tab",
                },
                children=descriptor,
            )
        ],
    )


def NavPane(content: html.Div):
    return html.Div(
        className="tab-pane fade", children=[content] ** {"role": "tabpanel"}
    )


def NavTabs(
    nav_item_list: list[html.Li],
    nav_pane_list: list[html.Div],
    style: str = "tabs",
    direction: str = "",
):
    """
    style : str "tabs" 或 "pills"
    direction : str "" 表示横向 或者 "flex-column"表示纵向
    """
    if len(nav_item_list) != len(nav_pane_list):
        raise ValueError("标签数量 和 内容物数量 必须一致！")
    return html.Div(
        className="bs-component",
        children=[
            html.Ul(
                className=f"nav nav-{style} {direction}",
                role="tablist",
                children=nav_item_list,
            ),
            html.Div(
                className="tab-content",
                children=nav_pane_list,
            ),
        ],
    )


## Table
def TableHeaderRow(headers: list):
    return html.Tr(
        children=[html.Th(header, scope="col") for header in headers],
    )


def TableRow(header, datas: list, style: str = "", display_mode="normal"):
    """
    style: str ""默认 "primary"蓝色 "secondary"灰色 "success"绿色 "info"紫色 "warning"橙色 "danger"红色 "light"白色  "dark"暗色
    """

    if display_mode == "normal":
        header_cell = [html.Th(header, scope="row")] if header else []
        data_cells = [html.Td(data) for data in datas]
    if display_mode == "dictionary":
        header_cell = (
            [html.Th(header, scope="row", colSpan=1, style={"width": "50%"})]
            if header
            else []
        )
        data_cells = [
            html.Td(data, colSpan=1, style={"width": "50%"}) for data in datas
        ]

    return (
        html.Tr(className=f"table-{style}", children=header_cell + data_cells)
        if style != ""
        else html.Tr(children=header_cell + data_cells)
    )


def Table(table_header_row: html.Tr = None, table_row_list: list[html.Tr] = None):
    return html.Div(
        className="bs-component",
        children=[
            html.Table(
                className="table table-hover",
                children=[
                    html.Thead(children=[table_header_row] if table_header_row else []),
                    html.Tbody(
                        children=(
                            [row for row in table_row_list] if table_row_list else []
                        )
                    ),
                ],
            )
        ],
    )


## Input
def FloatingInput(input_id: str, label: str, explanation: str = None):
    input_component = html.Div(
        className="form-floating",
        children=[
            dcc.Input(
                type="text",
                className="form-control",
                id=input_id,
                placeholder=label,
            ),
            html.Label(htmlFor=input_id, children=[label]),
        ],
    )

    if explanation:
        input_component.children.append(
            html.Small(
                id=f"{input_id}Help",
                className="form-text text-muted",
                children=[explanation],
            )
        )

    return input_component


def RangeInput(
    input_id: str,
    label: str,
    min_val: int,
    max_val: int,
    step: float = None,
    explanation: str = None,
):
    input_component = html.Div(
        className="mb-3",
        children=[
            html.Label(
                htmlFor=input_id,
                children=[label],
                className="form-label",
            ),
            dcc.Input(
                type="range",
                className="form-range",
                min=min_val,
                max=max_val,
                step=step if step is not None else "",
                id=input_id,
            ),
        ],
    )

    if explanation:
        input_component.children.append(
            html.Small(
                id=f"{input_id}Help",
                className="form-text text-muted",
                children=[explanation],
            )
        )

    return input_component


def SelectInput(input_id: str, label: str, option_list: list, explanation: str = None):
    input_component = html.Div(
        className="mb-3",
        children=[
            html.Label(
                htmlFor=input_id,
                children=[label],
                className="form-label",
            ),
            html.Select(
                className="form-select",
                id=input_id,
                children=[html.Option(option, value=option) for option in option_list],
            ),
        ],
    )

    if explanation:
        input_component.children.append(
            html.Small(
                id=f"{input_id}Help",
                className="form-text text-muted",
                children=[explanation],
            )
        )

    return input_component


def MultiSelectInput(
    input_id: str, label: str, option_list: list, explanation: str = None
):
    input_component = html.Div(
        className="mb-3",
        children=[
            html.Label(
                htmlFor=input_id,
                children=[label],
                className="form-label",
            ),
            html.Select(
                className="form-select",
                id=input_id,
                multiple=True,
                children=[html.Option(option, value=option) for option in option_list],
            ),
        ],
    )

    if explanation:
        input_component.children.append(
            html.Small(
                id=f"{input_id}Help",
                className="form-text text-muted",
                children=[explanation],
            )
        )

    return input_component


def SwitchInput(input_id: str, label: str, value: bool = False):
    return dbc.Switch(
        id=input_id,
        label=label,
        value=value,
        className="form-check form-switch",
        label_class_name="form-check-label",
    )


# collapse


def Accordion(
    headers: list[str], contents: list[html.Div], accordion_id="accordionExample"
) -> html.Div:
    if len(headers) != len(contents):
        raise ValueError("按钮名称列表和内容列表的长度必须一致！")

    accordion_items = []
    for index, (header, content) in enumerate(zip(headers, contents)):
        # 生成唯一 ID
        header_id = f"heading{index}"
        collapse_id = f"collapse{index}"
        expanded = "true" if index == 0 else "false"
        show_class = "show" if index == 0 else ""

        accordion_items.append(
            html.Div(
                className="accordion-item",
                children=[
                    html.H2(
                        className="accordion-header",
                        id=header_id,
                        children=html.Button(
                            header,
                            className=f"accordion-button {'collapsed' if index != 0 else ''}",
                            type="button",
                            **{
                                "data-bs-toggle": "collapse",
                                "data-bs-target": f"#{collapse_id}",
                                "aria-expanded": expanded,
                                "aria-controls": collapse_id,
                            },
                        ),
                    ),
                    html.Div(
                        id=collapse_id,
                        className=f"accordion-collapse collapse {show_class}",
                        **{
                            "aria-labelledby": header_id,
                            "data-bs-parent": f"#{accordion_id}",
                        },
                        children=html.Div(className="accordion-body", children=content),
                    ),
                ],
            )
        )

    return html.Div(
        className="accordion",
        id=accordion_id,
        children=accordion_items,
    )


def Dropdown(button_name: str, options: list[str]):
    return html.Div(
        className="dropdown mt-3",
        children=[
            # Dropdown button
            html.Button(
                button_name,
                className="btn btn-secondary dropdown-toggle",
                type="button",
                id="dropdownMenuButton",
                **{
                    "data-bs-toggle": "dropdown",  # Use double-asterisk for attributes with hyphens
                },
            ),
            # Dropdown menu
            html.Ul(
                className="dropdown-menu",
                **{"aria-labelledby": "dropdownMenuButton"},
                children=[
                    html.Li(html.A(option, className="dropdown-item", href="#"))
                    for option in options  # Create list items dynamically
                ],
            ),
        ],
    )


def OffCanvasSidebar(
    offcanvas_id: str,
    button: html.Button,
    side_content: html.Div,
    side_header: str = "",
    position: str = "start",
):
    """
    position: str  "start" "end" "top" "bottom"
    """
    button_class = (
        button.__getattribute__("className") if hasattr(button, "className") else ""
    )
    button = html.Button(
        children=[html.I(className="bi bi-code")],
        style={
            "position": "fixed",  # 固定位置
            "left": "10px",  # 距离左侧 10px
            "bottom": "10px",  # 距离底部 10px
            "zIndex": "1050",  # 确保按钮显示在其他元素的前面
        },
        className=f"{button_class}",
        **{
            "data-bs-toggle": "offcanvas",
            "data-bs-target": f"#{offcanvas_id}",
            "aria-controls": offcanvas_id,
        },
    )
    side = html.Div(
        className=f"offcanvas offcanvas-{position}",
        id=offcanvas_id,
        tabIndex="-1",
        **{"aria-labelledby": f"{offcanvas_id}Label"},
        children=[
            html.Div(
                className="offcanvas-header",
                children=[
                    html.H5(
                        children=[side_header],
                        className="offcanvas-title",
                        id=f"{offcanvas_id}Label",
                    ),
                    html.Button(
                        className="btn-close text-reset",
                        type="button",
                        **{
                            "data-bs-dismiss": "offcanvas",
                            "aria-label": "Close",
                        },
                    ),
                ],
            ),
            # Offcanvas Body
            html.Div(className="offcanvas-body", children=side_content),
        ],
    )

    return [button, side]


## Small Comp
def Button(label: str, style: str = "primary", size: str = "", outline: bool = False):
    """
    style: str "primary"蓝色 "secondary"灰色 "success"绿色 "info"紫色 "warning"橙色 "danger"红色 "light"白色  "dark"暗色
    size: str "" 普通 "btn-lg" 大 "btn-sm" 小
    outline : bool True 开 False 关
    """
    return dbc.Button(
        label,
        outline=outline,
        color="",
        className=f"btn btn-{style} {size}",
    )


def Text(descriptor: str, style: str = "primary"):
    """
    style: str "body"正常  "body-secondary"正常浅 "primary"蓝色 "secondary"灰色 "success"绿色 "info"紫色 "warning"橙色 "danger"红色 "light"白色  "dark"暗色
    """
    return html.P(className=f"text-{style}", children=[descriptor])


def Alert(descriptor: str, style: str = "secondary", dismissible: bool = False):
    """
    style: str "primary"蓝色 "secondary"灰色 "success"绿色 "info"紫色 "warning"橙色 "danger"红色 "light"白色  "dark"暗色
    dismissible : bool True有关闭按钮 False无关闭按钮
    """
    button = (
        [
            html.Button(
                type="button", className="btn-close", **{"data-bs-dismiss": "alert"}
            )
        ]
        if dismissible
        else []
    )
    return html.Div(
        className=f"alert alert-dismissible alert-{style}",
        children=button + [descriptor],
    )


def Badges(descriptor: str, style="light", coner: str = ""):
    """
    style: str "primary"蓝色 "secondary"灰色 "success"绿色 "info"紫色 "warning"橙色 "danger"红色 "light"白色  "dark"暗色
    coner: str ""方角 "rounded-pill"圆角
    """
    return html.P(className=f"badge bg-{style} {coner}", children=[descriptor])


def ProgressBar(
    current_value: int,  # 当前进度值
    min_value: int = 0,  # 最小值，默认为 0
    max_value: int = 100,  # 最大值，默认为 100
    style: str = "primary",
    striped: bool = False,  # 样式主题，默认为 "progress-bar-striped"
    animed: bool = False,
) -> html.Div:
    """
    style: str "primary"蓝色 "secondary"灰色 "success"绿色 "info"紫色 "warning"橙色 "danger"红色 "light"白色  "dark"暗色
    striped: bool True带条 False 不带条
    striped: bool True动态 False 静态
    """
    striped = "progress-bar-striped" if striped else ""
    animed = "progress-bar-animated" if animed else ""
    current_value = max(min_value, min(current_value, max_value))

    # 计算进度百分比
    percentage = ((current_value - min_value) / (max_value - min_value)) * 100

    return html.Div(
        className="progress",
        children=[
            html.Div(
                className=f"progress-bar bg-{style} {striped} {animed}",
                role="progressbar",
                style={"width": f"{percentage}%"},
                **{
                    "aria-valuenow": current_value,
                    "aria-valuemin": min_value,
                    "aria-valuemax": max_value,
                },
            )
        ],
    )


def TooltipButton(
    descriptor: str,  # Button text displayed to the user
    tooltip_text: str,  # Text displayed in the tooltip
    placement: str = "bottom",  # Tooltip placement, e.g., "top", "bottom", "left", "right"
    style: str = "secondary",  # Button style, defaulting to "btn-secondary"
) -> html.Button:
    """
    style: str "primary"蓝色 "secondary"灰色 "success"绿色 "info"紫色 "warning"橙色 "danger"红色 "light"白色  "dark"暗色
    placement: str "top", "bottom", "left", "right"
    """
    return html.Button(
        descriptor,
        className=f"btn btn-{style}",
        **{
            "type": "button",
            "data-bs-toggle": "tooltip",
            "data-bs-placement": placement,
            "data-bs-original-title": tooltip_text,
        },
    )


def Card(
    header: html.Div,  # 卡片头部内容
    body: html.Div,  # 卡片主体内容
    text_color: str = "white",
    style: str = "dark",
    border: bool = False,
) -> html.Div:
    """
    text_color: str "body"正常  "body-secondary"正常浅 "primary"蓝色 "secondary"灰色 "success"绿色 "info"紫色 "warning"橙色 "danger"红色 "light"白色  "dark"暗色
    style: str ""默认 "primary"蓝色 "secondary"灰色 "success"绿色 "info"紫色 "warning"橙色 "danger"红色 "light"白色  "dark"暗色
    """
    border = "border-" if border else "bg-"
    return html.Div(
        className=f"card text-{text_color} {border}-{style}",
        children=[
            # 卡片头部
            html.Div(
                className="card-header",
                children=header,
            ),
            # 卡片主体
            html.Div(className="card-body", children=body),
        ],
    )
