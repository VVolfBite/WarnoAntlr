from ast import List, Pass
from tkinter import PAGES
from dash import dcc
from dash import html
import plotly.graph_objs as go
from pytz import country_timezones
from utils import *
from typing import Counter, Union

import sys

WORK_DIRECTORY = "D:/WarnoAntlr-main/"
sys.path.append(WORK_DIRECTORY)

from src.extractor.refined_class import *

                
class TGameplayTerrainComponment:
    def __init__(
        self,
        TGameplayTerrain: TGameplayTerrain
    ):
        self.TGameplayTerrain = TGameplayTerrain
        self.KeyName = TGameplayTerrain.KeyName

        self.TRBloqueAmphibie = Table_Row(
            "两栖单位无法通行",
            show_value(TGameplayTerrain.BloqueAmphibie),
        )
        self.TRBloqueAtterrissage = Table_Row(
            "直升机单位无法降落",
            show_value(TGameplayTerrain.BloqueAtterrissage),
        )
        self.TRBloqueInfanterie = Table_Row(
            "步兵单位无法通行",
            show_value(TGameplayTerrain.BloqueInfanterie),
        )
        self.TRBloqueVehicule = Table_Row(
            "载具单位无法通行",
            show_value(TGameplayTerrain.BloqueVehicule),
        )
        self.TRBloqueVision = Table_Row(
            "阻挡视野",
            show_value(TGameplayTerrain.BloqueVision),
        )
        self.TRCriticalEffectProbability = Table_Row(
            "暴击效果触发概率",
            show_value(TGameplayTerrain.CriticalEffectProbability),
        )
        self.TRDissimulationModifierGroundAir = Table_Row(
            "地面单位对空的伪装加成",
            show_value(TGameplayTerrain.DissimulationModifierGroundAir),
        )
        self.TRDissimulationModifierGroundGround  = Table_Row(
            "地面单位对地的伪装加成",
            show_value(TGameplayTerrain.DissimulationModifierGroundGround),
        )
        self.TRHeightInMeters  = Table_Row(
            "地形高度",
            show_value(TGameplayTerrain.HeightInMeters),
        )
        self.TRInflammabilityProbability  = Table_Row(
            "地形可燃概率",
            show_value(TGameplayTerrain.InflammabilityProbability),
        )        
        self.TRSpeedModifierAllTerrainWheel  = Table_Row(
            "轮式单位的速度修正",
            show_value(TGameplayTerrain.SpeedModifierAllTerrainWheel),
        )
        self.TRSpeedModifierInfantry  = Table_Row(
            "步兵单位的速度修正",
            show_value(TGameplayTerrain.SpeedModifierInfantry),
        )
        self.TRSpeedModifierTrack  = Table_Row(
            "履带单位的速度修正",
            show_value(TGameplayTerrain.SpeedModifierTrack),
        )
        self.TRConcealmentBonus  = Table_Row(
            "给予其上单位的隐蔽加成",
            show_value(TGameplayTerrain.ConcealmentBonus),
        )
        self.TRAuthorizeNearGroundFlying  = Table_Row(
            "允许直升机近地飞行",
            show_value(TGameplayTerrain.AuthorizeNearGroundFlying),
        )
        self.TRTerrainType  = Table_Row(
            "地形类型",
            show_value(TGameplayTerrain.TerrainType),
        )
        self.TRDamageModifierPerFamilyAndResistance = Table_Row(
            "伤害修正",
            show_value(TGameplayTerrain.DamageModifierPerFamilyAndResistance),
        )
     
    def DetailComponent(self):
        table_row = [
                self.TRBloqueAmphibie,
                self.TRBloqueAtterrissage,
                self.TRBloqueInfanterie,
                self.TRBloqueVehicule,
                self.TRBloqueVision,
                self.TRSpeedModifierInfantry,
                self.TRSpeedModifierTrack,
                self.TRSpeedModifierAllTerrainWheel,
                self.TRConcealmentBonus,
                self.TRDissimulationModifierGroundAir,
                self.TRDissimulationModifierGroundGround,
                self.TRCriticalEffectProbability,
                self.TRInflammabilityProbability,
                self.TRAuthorizeNearGroundFlying,
                self.TRTerrainType,
                self.TRHeightInMeters,
                self.TRDamageModifierPerFamilyAndResistance
            ]
        return table_row

class TerrainPage:
    def __init__(self,TGameplayTerrainDict: dict[str:TGameplayTerrain]):
        self.TGameplayTerrainDict = TGameplayTerrainDict


    def DetailComponent(self):
        terrain_content_list = []
        for terrain_name,terrain in self.TGameplayTerrainDict.items():
            comp = TGameplayTerrainComponment(terrain)
            content = Content(terrain_name,Table(comp.DetailComponent()))
            terrain_content_list.append(content)
        return terrain_content_list
    
    def AsPage(self):
        terrain_content_list = self.DetailComponent()
        terrain_content_page = Page_Content(
            [
                Row([
                    Col(terrain_content_list[i], className="twelve columns"),
                ])
                for i in range(0, len(terrain_content_list))
            ]
        )
        header = Header("地形")
        page = Page(header, terrain_content_page)
        return page