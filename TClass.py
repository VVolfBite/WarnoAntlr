class TCriticalEffectDescriptor(BaseDescription):
    def __init__(self, Token=None, HappeningKey=None, EffectsPack=None, TimeOut=None, RepairCost=None, Unique=None, DisplayOnDeath=None):
        self.Token = Token
        self.HappeningKey = HappeningKey
        self.EffectsPack = EffectsPack
        self.TimeOut = TimeOut
        self.RepairCost = RepairCost
        self.Unique = Unique
        self.DisplayOnDeath = DisplayOnDeath


class TCriticalEffect(BaseDescription):
    def __init__(self, Roll=None, Descriptor=None):
        self.Roll = Roll
        self.Descriptor = Descriptor


class CriticalEffect_Incendiary(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="CriticalEffect_Incendiary_Desc", Roll=Roll)
        self.Roll = Roll


class CriticalEffect_EngineDamaged(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="CriticalEffect_EngineDamaged_Desc", Roll=Roll)
        self.Roll = Roll


class CriticalEffect_EngineDestroyed(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="CriticalEffect_EngineDestroyed_Desc", Roll=Roll)
        self.Roll = Roll


class CriticalEffect_AmmoExplosion(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="CriticalEffect_AmmoExplosion_Desc", Roll=Roll)
        self.Roll = Roll


class CriticalEffect_FuelExplosion(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="CriticalEffect_FuelExplosion_Desc", Roll=Roll)
        self.Roll = Roll


class CriticalEffect_CompReset(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="CriticalEffect_CompReset_Desc", Roll=Roll)
        self.Roll = Roll


class CriticalEffect_BailedOut(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="CriticalEffect_BailedOut_Desc", Roll=Roll)
        self.Roll = Roll


class CriticalEffect_ArmourCracked(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="CriticalEffect_ArmourCracked_Desc", Roll=Roll)
        self.Roll = Roll


class CriticalEffect_Spalling(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="CriticalEffect_Spalling_Desc", Roll=Roll)
        self.Roll = Roll


class CriticalEffect_TracksBroken(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="CriticalEffect_TracksBroken_Desc", Roll=Roll)
        self.Roll = Roll


class CriticalEffect_TurretStuck(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="CriticalEffect_TurretStuck_Desc", Roll=Roll)
        self.Roll = Roll


class HelicoCriticalEffect_HUD(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="HelicoCriticalEffect_HUD_Desc", Roll=Roll)
        self.Roll = Roll


class HelicoCriticalEffect_CrewInjured(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="HelicoCriticalEffect_CrewInjured_Desc", Roll=Roll)
        self.Roll = Roll


class HelicoCriticalEffect_MainRotorDamaged(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="HelicoCriticalEffect_MainRotorDamaged_Desc", Roll=Roll)
        self.Roll = Roll


class HelicoCriticalEffect_Turbine_Engine_Failure(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="HelicoCriticalEffect_Turbine_Engine_Failure_Desc", Roll=Roll)
        self.Roll = Roll


class HelicoCriticalEffect_turbineOnFire(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="HelicoCriticalEffect_turbineOnFire_Desc", Roll=Roll)
        self.Roll = Roll


class HelicoCriticalEffect_FuelTankOnFire(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="HelicoCriticalEffect_FuelTankOnFire_Desc", Roll=Roll)
        self.Roll = Roll


class HelicoCriticalEffect_FuelTankLeaking(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="HelicoCriticalEffect_FuelTankLeaking_Desc", Roll=Roll)
        self.Roll = Roll


class HelicoCriticalEffect_WeaponsJammed(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="HelicoCriticalEffect_WeaponsJammed_Desc", Roll=Roll)
        self.Roll = Roll


class HelicoCriticalEffect_Hydraulic_Fluid_Fire(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="HelicoCriticalEffect_Hydraulic_Fluid_Fire_Desc", Roll=Roll)
        self.Roll = Roll


class HelicoCriticalEffect_TailRotorDamaged(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="HelicoCriticalEffect_TailRotorDamaged_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_WingsDamaged(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_WingsDamaged_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_EngineOnFire(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_EngineOnFire_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_PropellerDamaged(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_PropellerDamaged_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_EngineDamaged(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_EngineDamaged_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_FloatCarburatorFailure(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_FloatCarburatorFailure_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_OilLeak(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_OilLeak_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_EngineOverheating(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_EngineOverheating_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_EngineStalling(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_EngineStalling_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_ElevatorDamaged(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_ElevatorDamaged_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_FuelTankLeaking(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_FuelTankLeaking_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_RadiatorDamaged(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_RadiatorDamaged_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_RadiatorOverheating(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_RadiatorOverheating_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_PilotInjured(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_PilotInjured_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_PilotPanicked(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_PilotPanicked_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_PilotUnconscious(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_PilotUnconscious_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_WeaponsJammed(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_WeaponsJammed_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_AileronDamaged(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_AileronDamaged_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_TailDamaged(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_TailDamaged_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_FuelTankOnFire(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_FuelTankOnFire_Desc", Roll=Roll)
        self.Roll = Roll


class AirplaneCriticalEffect_RudderDamaged(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="AirplaneCriticalEffect_RudderDamaged_Desc", Roll=Roll)
        self.Roll = Roll


class TCriticalEffectModuleDescriptor(BaseDescription):
    def __init__(self, Bounds=None, TerrainCriticalEffectTimer=None, EffectsOnFront=None, EffectsOnSides=None, EffectsOnRear=None, EffectsFromTerrain=None, EffectsOnTop=None, PierceEffectsOnFront=None, PierceEffectsOnSides=None, PierceEffectsOnRear=None, PierceEffectsOnTop=None, RicochetEffectsOnFront=None, RicochetEffectsOnSides=None, RicochetEffectsOnRear=None, RicochetEffectsOnTop=None):
        self.Bounds = Bounds
        self.TerrainCriticalEffectTimer = TerrainCriticalEffectTimer
        self.EffectsOnFront = EffectsOnFront
        self.EffectsOnSides = EffectsOnSides
        self.EffectsOnRear = EffectsOnRear
        self.EffectsFromTerrain = EffectsFromTerrain
        self.EffectsOnTop = EffectsOnTop
        self.PierceEffectsOnFront = PierceEffectsOnFront
        self.PierceEffectsOnSides = PierceEffectsOnSides
        self.PierceEffectsOnRear = PierceEffectsOnRear
        self.PierceEffectsOnTop = PierceEffectsOnTop
        self.RicochetEffectsOnFront = RicochetEffectsOnFront
        self.RicochetEffectsOnSides = RicochetEffectsOnSides
        self.RicochetEffectsOnRear = RicochetEffectsOnRear
        self.RicochetEffectsOnTop = RicochetEffectsOnTop


class TemplateCriticalEffectModule_GroundUnit(TCriticalEffectModuleDescriptor):
    def __init__(self, PackEffetCritique="PackEffetCritique_VehiculeStandard", EffectsFromTerrain=[]):
        super().__init__(Bounds={1: 200}, EffectsFromTerrain=EffectsFromTerrain, EffectsOnFront=PackEffetCritique, EffectsOnRear=PackEffetCritique, EffectsOnSides=PackEffetCritique, EffectsOnTop=PackEffetCritique, PierceEffectsOnFront=PackEffetCritique, PierceEffectsOnRear=PackEffetCritique, PierceEffectsOnSides=PackEffetCritique, PierceEffectsOnTop=[], RicochetEffectsOnFront=[], RicochetEffectsOnRear=[], RicochetEffectsOnSides=[], RicochetEffectsOnTop=[], TerrainCriticalEffectTimer=1)
        self.PackEffetCritique = PackEffetCritique
        self.EffectsFromTerrain = EffectsFromTerrain


class CriticalEffect_TransmissionDamaged(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="CriticalEffect_TransmissionDamaged_Desc", Roll=Roll)
        self.Roll = Roll


class CriticalEffect_Bounce(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="CriticalEffect_Bounce_Desc", Roll=Roll)
        self.Roll = Roll
