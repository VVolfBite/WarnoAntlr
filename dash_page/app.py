from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
global_theme = "dark"
app = Dash(__name__)


# Nav
def Navbar(nav_item_list: list[html.Li], theme="bg-body-tertiary", global_theme="dark"):
    return html.Div(
        className="bs-component",
        **{"data-bs-theme": global_theme},
        children=[
            html.Nav(
                className=f"navbar navbar-expand-lg {theme}",  # 使用 f-string 拼接
                children=[
                    html.Div(
                        className="container-fluid",
                        children=[
                            html.Div(
                                className="collapse navbar-collapse",
                                children=[
                                    html.Ul(
                                        className="navbar-nav me-auto",
                                        children=nav_item_list,
                                    )
                                ],
                            )
                        ],
                    )
                ],
            )
        ],
    )

def NavItem(descriptor: str, href: str = "#", active: bool = False):
    # 根据 active 状态添加 'active' 类
    class_name = "nav-item"
    if active:
        class_name += " active"

    return html.Li(
        className=class_name,
        children=[html.A(className="nav-link", href=href, children=[descriptor])],
    )

# Table
def Table(TableHeader: html.Tr = None, TableRowList: list[html.Tr] = None):
    return html.Div(
        className="bs-component",
        children=[
            html.Table(
                className="table table-hover",
                children=[
                    html.Thead(children=[TableHeader] if TableHeader else []),
                    html.Tbody(
                        children=[row for row in TableRowList] if TableRowList else []
                    ),
                ],
            )
        ],
    )

def TableHeaderRow(headers: list, theme="table-dark"):
    return html.Tr(
        className=theme,
        children=[html.Th(header, scope="col") for header in headers],
    )

def TableRow(header, data: list, theme="table-dark", display_mode="normal"):
    if not header:
        return html.Tr(
            className=theme, children=[html.Td(data_item) for data_item in data]
        )
    if display_mode == "normal":
        return html.Tr(
            className=theme,
            children=[html.Th(header, scope="row")]
            + [html.Td(data_item) for data_item in data],
        )

    elif display_mode == "dictionary":
        header_cell = html.Th(header, scope="row", colSpan=1, style={"width": "50%"})
        data_cells = [
            html.Td(data_item, colSpan=1, style={"width": "50%"}) for data_item in data
        ]
        return html.Tr(className=theme, children=[header_cell] + data_cells)

# Header
def PageHeader(descriptor: str):
    return html.Div(className="page-header", children=[html.H1(descriptor)])

def ContentHeader(descriptor: str):
    return html.H2(descriptor)

def SectionHeader(descriptor: str):
    return html.H3(descriptor)

def ComponentTitle(descriptor:str):
    return html.Label(className="form-label", children=[descriptor])
# Text
def Text(descriptor: str, theme = ".text-body"):
    return html.P(className=theme, children=[descriptor])

# Input
def FloatingInput(id: str, label: str, explanation: str = None):
    input_component = html.Div(
        className="form-floating mb-3",
        children=[
            dcc.Input(
                type="text",  # 普通的输入类型
                className="form-control",
                id=id,
                placeholder=label,  # 设置占位符为label
            ),
            html.Label(
                htmlFor=id,
                children=[label]  # 漂浮显示的文字
            ),
        ]
    )

    if explanation:
        input_component.children.append(
            html.Small(
                id=f"{id}Help",  # 关联帮助信息的id
                className="form-text text-muted",
                children=[explanation]  # 显示解释文本
            )
        )

    return input_component

def RangeInput(id: str, label: str, min: int, max: int, step: float = None, explanation: str = None):
    input_component = html.Div(
        className="mb-3",
        children=[
            html.Label(
                htmlFor=id,
                children=[label],  # 传入的label
                className="form-label",  # 表单控件的标签样式
            ),
            dcc.Input(
                type="range",
                className="form-range",
                min=min,
                max=max,
                step=step if step is not None else "",  # 如果step是None，则移除step
                id=id,
            ),
        ],
    )

    if explanation:
        input_component.children.append(
            html.Small(
                id=f"{id}Help",  # 关联帮助信息的id
                className="form-text text-muted",
                children=[explanation]  # 显示解释文本
            )
        )

    return input_component

def SelectInput(id: str, label: str, option_list: list, explanation: str = None):
    input_component = html.Div(
        className="mb-3",
        children=[
            html.Label(
                htmlFor=id,
                children=[label],  # 必填的label
                className="form-label",
            ),
            html.Select(
                className="form-select",
                id=id,
                children=[
                    html.Option(option, value=option) for option in option_list  # 遍历 options 列表生成 <option> 标签
                ]
            ),
        ]
    )

    if explanation:
        input_component.children.append(
            html.Small(
                id=f"{id}Help",  # 关联帮助信息的id
                className="form-text text-muted",
                children=[explanation]  # 显示解释文本
            )
        )

    return input_component

def MultiSelectInput(id: str, label: str, option_list: list, explanation: str = None):
    input_component = html.Div(
        className="mb-3",
        children=[
            html.Label(
                htmlFor=id,
                children=[label],  # 必填的label
                className="form-label",
            ),
            html.Select(
                className="form-select",
                id=id,
                multiple=True,  # 启用多选
                children=[
                    html.Option(option, value=option) for option in option_list
                ]
            ),
        ]
    )

    if explanation:
        input_component.children.append(
            html.Small(
                id=f"{id}Help",  # 关联帮助信息的id
                className="form-text text-muted",
                children=[explanation]  # 显示解释文本
            )
        )

    return input_component

# def CheckboxInput(id: str, label: str):
#     # 创建一个带有复选框和标签的组件
#     input_component = html.Div(
#         className="form-check form-switch",  # Switch样式
#         children=[
#             dbc.Checkbox(
#                 className="form-check-input",  # 表单复选框的样式
#                 id=id,
#                 label= label
#             ),
#         ]
#     )


#     return input_component

def SwitchInput(id: str, label: str, value: bool = False):
    # 创建 Switch 控件
    input_component = dbc.Switch(
                id=id,  # Switch 控件的 ID
                label=label,  # Switch 的标签 form-check-label
                value=value,  # 默认值
                className="form-check form-switch",  # 用于 Switch 的 Bootstrap 样式
                label_class_name= "form-check-label"
            )

    return input_component

# --------------------------------------------- Nav Test
# navitem_list = [
#     NavItem(123, href="https://bootswatch.com/cosmo/#", active=True),
#     NavItem(456, href="https://bootswatch.com/cosmo/#")
# ]

# navbar = Navbar(navitem_list)

# --------------------------------------------- Table Test
# header1 = ["A", "B", "C"]
# rows1 = [("T", 1, 3), ("B", 2, 4), ("C", 9, 0)]

# TableRowList1 = [
#     TableRow(header=row[0], data=row[1:], display_mode="normal") for row in rows1
# ]

# table1 = Table(TableHeaderRow(header=header1), TableRowList=TableRowList1)

# header2 = ["Key", "Value"]
# rows2 = [("A", [1,2]), ("B", 2), ("C", 3)]

# TableRowList2 = [
#     TableRow(header=row[0], data=row[1:], display_mode="dictionary") for row in rows2
# ]

# table2 = Table(TableHeaderRow(header=header2), TableRowList=TableRowList2)


# --------------------------------------------- Header Test
# page_header = PageHeader(123)

# --------------------------------------------- Text Test
# text = Text(123)

# --------------------------------------------- Input Test
title = ComponentTitle("Sui bian")
floating_input = FloatingInput("test", "输入信息",explanation="随便写点")
range_input = RangeInput("123","456",min = "3",max = "5",step = "0.1", explanation="随便啦")
select_input = SelectInput("sel","sel", ["1","2","3"])
mutilselect_input = MultiSelectInput("sel","sel", ["1","2","3"])
switch_input = SwitchInput("13","23")
# --------------------------------------------- Select Test

app.layout = html.Div([switch_input])


if __name__ == "__main__":
    app.run_server(debug=True)
