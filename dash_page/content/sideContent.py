import dash
from dash import Dash, html, Input, Output, State, dcc
import dash_bootstrap_components as dbc

import pickle
import sys
WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)
from dash_page.util.dataManager import DataManager


class SideContent:
    def __init__(self, app, data_manager: DataManager):
        self.app = app
        self.data_manager = data_manager

        # 组件 ID
        self.querytype_store_id = "querytype"
        self.querykey_store_id = "querykey"
        self.dropdown_menu_querytype_id = "dropdown-menu-querytype-id"
        self.dropdown_menu_querykey_id = "dropdown-menu-querykey-id"

        # 所有字符串选项的统一管理（三级字典）
        self.querytype_options = {
            "dictionary_info": {
                "label": "字典信息",
                "items": {
                    "单位": {
                        "id": "dropdown-menuitem-unit-id",
                        "value": "TEntityDescriptor",
                    },
                    "武器": {
                        "id": "dropdown-menuitem-weapon-id",
                        "value": "TWeaponManagerModuleDescriptor",
                    },
                    "弹药": {
                        "id": "dropdown-menuitem-ammo-id",
                        "value": "TAmmunitionDescriptor",
                    },
                    "特性与光环": {
                        "id": "dropdown-menuitem-traits-id",
                        "value": ["TCapaciteDescriptor", "TEffectsPackDescriptor"],
                    },
                    "暴击效果": {
                        "id": "dropdown-menuitem-crit-effects-id",
                        "value": "TCriticalEffectModuleDescriptor",
                    },
                    "地形": {
                        "id": "dropdown-menuitem-terrain-id",
                        "value": "TGameplayTerrain",
                    },
                    "师与卡组": {
                        "id": "dropdown-menuitem-decks-id",
                        "value": ["TDeckDivisionRule", "TDeckDivisionRules"],
                    },
                },
            },
            "other_info": {
                "label": "其他信息",
                "items": {
                    "特殊机制": {
                        "id": "dropdown-menuitem-mechanics-id",
                        "value": None,
                    },
                },
            },
        }

    def layout(self):
        querytype = dcc.Store(id=self.querytype_store_id)
        querykey = dcc.Store(id=self.querykey_store_id)

        text_descriptor_dropdown_querytype = html.P("请在这里选择想要查看的信息类型。", className="text-body")

        # 动态生成 Dropdown 菜单项
        dropdown_querytype_items = []
        for category, category_details in self.querytype_options.items():
            dropdown_querytype_items.append(dbc.DropdownMenuItem(category_details["label"], header=True))
            dropdown_querytype_items.extend(
                dbc.DropdownMenuItem(option, id=details["id"])
                for option, details in category_details["items"].items()
            )
            dropdown_querytype_items.append(dbc.DropdownMenuItem(divider=True))

        # 移除最后一个多余的分隔符
        if dropdown_querytype_items[-1].divider:
            dropdown_querytype_items.pop()

        dropdown_querytype = dbc.DropdownMenu(
            dropdown_querytype_items,
            label="选择一个你感兴趣的内容",
            class_name="flex",
            id=self.dropdown_menu_querytype_id,
        )

        divider = html.Hr(className="my-4")
        text_descriptor_dropdown_querykey = html.P("请在这里选择具体一项信息。", className="text-body")

        dropdown_querykey = dcc.Dropdown(
            id=self.dropdown_menu_querykey_id,
            placeholder="请先选择一项信息类型",
            className="dbc",
            options=[],
        )

        return dbc.Container(
            [
                querytype,
                querykey,
                text_descriptor_dropdown_querytype,
                dropdown_querytype,
                divider,
                text_descriptor_dropdown_querykey,
                dropdown_querykey,
            ],
            className="mt-4",
        )

    def register_callbacks(self):
        @self.app.callback(
            [
                Output(self.dropdown_menu_querytype_id, "label"),
                Output(self.querytype_store_id, "data"),
                Output(self.dropdown_menu_querykey_id, "options"),
            ],
            [
                Input(details["id"], "n_clicks")
                for category in self.querytype_options.values()
                for details in category["items"].values()
            ],
        )
        def update_dropdown_label_and_options(*clicks):
            ctx = dash.callback_context
            if not ctx.triggered:
                return "选择一个你感兴趣的内容", None, []

            triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

            for category, category_details in self.querytype_options.items():
                for option, details in category_details["items"].items():
                    if details["id"] == triggered_id:
                        label = option
                        value = details["value"]

                        # 更新 querykey 列表
                        querykey_data = self.data_manager.get_data_by_class(value)
                        dropdown_options = [{"label": str(k), "value": str(k)} for k in querykey_data.keys()]
                        return label, value, dropdown_options

            return "选择一个你感兴趣的内容", None, []

        @self.app.callback(
            Output(self.querykey_store_id, "data"),
            Input(self.dropdown_menu_querykey_id, "value"),
        )
        def update_querykey(selected_key):
            return selected_key
