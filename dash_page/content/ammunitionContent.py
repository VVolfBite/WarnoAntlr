import pickle
import sys
WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)
from dash import dcc, html
import dash_bootstrap_components as dbc

from src.extractor.refined_class import *
from dash_page.util.dataProcess import DataManager,DataFormatter,Suffix





class AmmunitionComponent:
    def __init__(self,app, data_manager: DataManager, ammunition: TAmmunitionDescriptor):
        self.ammunition_key = ammunition.KeyName if hasattr(ammunition, "KeyName") else str(ammunition)
        self.ammunition = ammunition
        base_hit_values = {
            k: v
            for d in ammunition.HitRollRuleDescriptor.BaseHitValueModifiers
            for k, v in d.items()
        }
        self.table_row_data = [
            DataFormatter(key="MinMaxCategory", value=ammunition.MinMaxCategory, suffix=None),
            DataFormatter(key="TraitsToken", value=ammunition.TraitsToken, suffix=None),
            DataFormatter(key="IsSubAmmunition", value=ammunition.IsSubAmmunition, suffix=None, caption="此词条注明指明其是否仅为一份弹药量的伤害，比如航弹。"),
            DataFormatter(key="AffecteParNombre", value=ammunition.AffecteParNombre, suffix=None, caption="此词条注明弹药效果是否会因持有人数倍增，比如枪械弹药。"),
            DataFormatter(key="Arme.Family", value=ammunition.Arme.Family, suffix=None),
            DataFormatter(key="Arme.Index", value=ammunition.Arme.Index, suffix=None),
            DataFormatter(key="PhysicalDamages", value=ammunition.PhysicalDamages, suffix=None),
            DataFormatter(key="RadiusSplashPhysicalDamagesGRU", value=ammunition.RadiusSplashPhysicalDamagesGRU, suffix=None),
            DataFormatter(key="SuppressDamages", value=ammunition.SuppressDamages, suffix=None),
            DataFormatter(key="RadiusSplashSuppressDamagesGRU", value=ammunition.RadiusSplashSuppressDamagesGRU, suffix=None),
            DataFormatter(key="AllowSuppressDamageWhenNoImpact", value=ammunition.AllowSuppressDamageWhenNoImpact, suffix=None),
            DataFormatter(key="ForceHitTopArmor", value=ammunition.ForceHitTopArmor, suffix=None),
            DataFormatter(key="TargetOnlyOneUnitInDistrict", value=ammunition.TargetOnlyOneUnitInDistrict, suffix=None),
            DataFormatter(key="PorteeMaximaleGRU", value=ammunition.PorteeMaximaleGRU, suffix=None),
            DataFormatter(key="PorteeMaximaleTBAGRU", value=ammunition.PorteeMaximaleTBAGRU, suffix=None),
            DataFormatter(key="PorteeMaximaleHAGRU", value=ammunition.PorteeMaximaleHAGRU, suffix=None),
            DataFormatter(key="PorteeMinimaleGRU", value=ammunition.PorteeMinimaleGRU, suffix=None),
            DataFormatter(key="PorteeMinimaleTBAGRU", value=ammunition.PorteeMinimaleTBAGRU, suffix=None),
            DataFormatter(key="PorteeMinimaleHAGRU", value=ammunition.PorteeMinimaleHAGRU, suffix=None),
            DataFormatter(key="Base", value=base_hit_values.get("Base", "N/A"), suffix=None),
            DataFormatter(key="Idling", value=base_hit_values.get("Idling", "N/A"), suffix=None),
            DataFormatter(key="Moving", value=base_hit_values.get("Moving", "N/A"), suffix=None),
            DataFormatter(key="Targeted", value=base_hit_values.get("Targeted", "N/A"), suffix=None),
            DataFormatter(key="BaseCriticModifier", value=ammunition.HitRollRuleDescriptor.BaseCriticModifier, suffix=None),
            DataFormatter(key="DistanceToTarget", value=ammunition.HitRollRuleDescriptor.DistanceToTarget, suffix=None),
            DataFormatter(key="MaxSuccessiveHitCount", value=ammunition.MaxSuccessiveHitCount, suffix=None),
            DataFormatter(key="CanShootWhileMoving", value=ammunition.CanShootWhileMoving, suffix=None),
            DataFormatter(key="DispersionAtMaxRangeGRU", value=ammunition.DispersionAtMaxRangeGRU, suffix=None),
            DataFormatter(key="DispersionAtMinRangeGRU", value=ammunition.DispersionAtMinRangeGRU, suffix=None),
            DataFormatter(key="CorrectedShotDispersionMultiplier", value=ammunition.CorrectedShotDispersionMultiplier, suffix=None),
            DataFormatter(key="DispersionWithoutSorting", value=ammunition.DispersionWithoutSorting, suffix=None),
            DataFormatter(key="AngleDispersion", value=ammunition.AngleDispersion, suffix=None),
            DataFormatter(key="TempsDeVisee", value=ammunition.TempsDeVisee, suffix=None),
            DataFormatter(key="TempsEntreDeuxSalves", value=ammunition.TempsEntreDeuxSalves, suffix=None),
            DataFormatter(key="TempsEntreDeuxTirs", value=ammunition.TempsEntreDeuxTirs, suffix=None),
            DataFormatter(key="NbTirParSalves", value=ammunition.NbTirParSalves, suffix=None),
            DataFormatter(key="CorrectedShotAimtimeMultiplier", value=ammunition.CorrectedShotAimtimeMultiplier, suffix=None),
            DataFormatter(key="TempsEntreDeuxSalves_Min", value=ammunition.TempsEntreDeuxSalves_Min, suffix=None),
            DataFormatter(key="TempsEntreDeuxSalves_Max", value=ammunition.TempsEntreDeuxSalves_Max, suffix=None),
            DataFormatter(key="CanShootOnPosition", value=ammunition.CanShootOnPosition, suffix=None),
            DataFormatter(key="NbSalvosShootOnPosition", value=ammunition.NbSalvosShootOnPosition, suffix=None),
            DataFormatter(key="TirIndirect", value=ammunition.TirIndirect, suffix=None),
            DataFormatter(key="TirReflexe", value=ammunition.TirReflexe, suffix=None),
            DataFormatter(key="InterdireTirReflexe", value=ammunition.TirReflexe, suffix=None),
            DataFormatter(key="TargetUnitCenter", value=ammunition.TargetUnitCenter, suffix=None),
            DataFormatter(key="PiercingWeapon", value=ammunition.PiercingWeapon, suffix=None),
            DataFormatter(key="IsHarmlessForAllies", value=ammunition.IsHarmlessForAllies, suffix=None),
            DataFormatter(key="CanHarmAirplanes", value=ammunition.CanHarmAirplanes, suffix=None),
            DataFormatter(key="Guidance", value=ammunition.Guidance, suffix=None),
            DataFormatter(key="IsFireAndForget", value=ammunition.IsFireAndForget, suffix=None),
            DataFormatter(key="MissileDescriptor", value=ammunition.MissileDescriptor, suffix=None),
            DataFormatter(key="TandemCharge", value=ammunition.TandemCharge, suffix=None),
            DataFormatter(key="MissileTimeBetweenCorrections", value=ammunition.MissileTimeBetweenCorrections, suffix=None),
            DataFormatter(key="SupplyCost", value=ammunition.SupplyCost, suffix=None),
            DataFormatter(key="SmokeDescriptor", value=ammunition.SmokeDescriptor, suffix=None),
            DataFormatter(key="FireDescriptor", value=ammunition.FireDescriptor, suffix=None),
            DataFormatter(key="FireTriggeringProbability", value=ammunition.FireTriggeringProbability, suffix=None),
            DataFormatter(key="IgnoreInflammabilityConditions", value=ammunition.IgnoreInflammabilityConditions, suffix=None),
        ]

    def BriefTable(self):
        return dbc.Table(
            [
                html.Tr([html.Td("基础"), html.Td(self.TRMinMaxCategory)]),
                html.Tr([html.Td("特性词条"), html.Td(self.TRTraitsToken)]),
                html.Tr([html.Td("描述对象为子武器"), html.Td(self.TRIsSubAmmunition)]),
                html.Tr([html.Td("描述对象因数量属性倍增"), html.Td(self.TRAffecteParNombre)]),
                html.Tr([html.Td("伤害所属族"), html.Td(self.TRArme_Family)]),
                html.Tr([html.Td("伤害索引号"), html.Td(self.TRArme_Index)]),
                html.Tr([html.Td("基底伤害"), html.Td(self.TRPhysicalDamages)]),
                html.Tr([html.Td("压制伤害"), html.Td(self.TRSuppressDamages)]),
                html.Tr([html.Td("对地最大射程"), html.Td(self.TRPorteeMaximaleGRU)]),
                html.Tr([html.Td("对地最小射程"), html.Td(self.TRPorteeMinimaleGRU)]),
                html.Tr([html.Td("瞄准时间"), html.Td(self.TRTempsDeVisee)]),
                html.Tr([html.Td("装填时间"), html.Td(self.TRTempsEntreDeuxSalves)]),
            ],
            bordered=True,
        )

    def DetailComponent(self):
        basic_table = dbc.Card(
            dbc.CardBody([
                html.H4("基础信息", className="card-title"),
                self.BriefTable()
            ])
        )

        # 将不同的部分分配到适当的 Card 组件中
        damage_table = dbc.Card(
            dbc.CardBody([
                html.H4("伤害信息", className="card-title"),
                dbc.Table(
                    [
                        html.Tr([html.Td("伤害所属族"), html.Td(self.TRArme_Family)]),
                        html.Tr([html.Td("伤害索引号"), html.Td(self.TRArme_Index)]),
                        html.Tr([html.Td("基底伤害"), html.Td(self.TRPhysicalDamages)]),
                        html.Tr([html.Td("压制伤害"), html.Td(self.TRSuppressDamages)]),
                    ],
                    bordered=True,
                ),
            ])
        )

        # 其他的表格可以继续按照此方式整理
        range_table = dbc.Card(
            dbc.CardBody([
                html.H4("射程信息", className="card-title"),
                dbc.Table(
                    [
                        html.Tr([html.Td("对地最大射程"), html.Td(self.TRPorteeMaximaleGRU)]),
                        html.Tr([html.Td("对地最小射程"), html.Td(self.TRPorteeMinimaleGRU)]),
                    ],
                    bordered=True,
                ),
            ])
        )

        # 最后你可以继续为每个数据块创建类似的 Card 组件

        # 创建一个列来布局内容
        col1 = dbc.Col([basic_table])
        col2 = dbc.Col([damage_table])
        col3 = dbc.Col([range_table])

        # 将这些列放到一个行里
        row = dbc.Row([col1, col2, col3])

        # 将行内容作为一个更大的页面元素
        content = dbc.Container([row])

        return content

    def AsComponent(self):
        tabs = dcc.Tabs(
            id="tabs",
            value="overview",
            children=[
                dcc.Tab(
                    label="概览",
                    value="overview",
                    children=[self.BriefTable()]
                ),
                dcc.Tab(
                    label="详细",
                    value="detail",
                    children=[self.DetailComponent()]
                ),
            ]
        )
        return tabs

    def AsPage(self):
        header = html.Header(
            html.H1(self.ammunition_key)
        )

        page = html.Div([header, self.AsComponent()])
        return page

