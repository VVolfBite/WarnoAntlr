from src.extractor.base_class import BaseDescription

class TConditionTagRaisedInUnit(BaseDescription):
    def __init__(self, Amount=None, Tag=None, DescriptorId=None):
        self.Amount = Amount
        self.Tag = Tag
        self.DescriptorId = DescriptorId


class TConditionTagNotRaisedInUnit(BaseDescription):
    def __init__(self, Amount=None, Tag=None, DescriptorId=None):
        self.Amount = Amount
        self.Tag = Tag
        self.DescriptorId = DescriptorId


class TConditionNotInMovement(BaseDescription):
    def __init__(self, DescriptorId=None):
        self.DescriptorId = DescriptorId


class TEffectsPackDescriptor(BaseDescription):
    def __init__(self, EffectsDescriptors=None, NameForDebug=None, DescriptorId=None):
        self.EffectsDescriptors = EffectsDescriptors
        self.NameForDebug = NameForDebug
        self.DescriptorId = DescriptorId


class TUnitEffectIncreaseWeaponDispersionMaxRangeDescriptor(BaseDescription):
    def __init__(self, ModifierValue=None, ModifierType=None):
        self.ModifierValue = ModifierValue
        self.ModifierType = ModifierType


class TUnitEffectRaiseTagDescriptor(BaseDescription):
    def __init__(self, TagListToRaise=None):
        self.TagListToRaise = TagListToRaise


class TUnitEffectShowLabelIconDescriptor(BaseDescription):
    def __init__(self, TextureToken=None):
        self.TextureToken = TextureToken


class TUnitEffectIncreaseDamageTakenDescriptor(BaseDescription):
    def __init__(self, DamageType=None, BonusDamage=None, ModifierType=None):
        self.DamageType = DamageType
        self.BonusDamage = BonusDamage
        self.ModifierType = ModifierType


class TStrategicSupplyMalusEffectDescriptor(BaseDescription):
    def __init__(self, SupplyMalus=None, ModifierType=None):
        self.SupplyMalus = SupplyMalus
        self.ModifierType = ModifierType


class TUnitEffectIncreaseInfluenceValueDescriptor(BaseDescription):
    def __init__(self, Bonus=None, ModifierType=None):
        self.Bonus = Bonus
        self.ModifierType = ModifierType


class TUnitEffectIncreaseWeaponPorteeMaxDescriptor(BaseDescription):
    def __init__(self, ModifierValue=None, ModifierType=None, ModifierValueGRU=None):
        self.ModifierValue = ModifierValue
        self.ModifierType = ModifierType
        self.ModifierValueGRU = ModifierValueGRU


class TUnitEffectIncreaseWeaponPorteeMaxHADescriptor(BaseDescription):
    def __init__(self, ModifierValue=None, ModifierType=None, ModifierValueGRU=None):
        self.ModifierValue = ModifierValue
        self.ModifierType = ModifierType
        self.ModifierValueGRU = ModifierValueGRU


class TUnitEffectIncreaseWeaponPorteeMaxProjectileDescriptor(BaseDescription):
    def __init__(self, ModifierValue=None, ModifierType=None, ModifierValueGRU=None):
        self.ModifierValue = ModifierValue
        self.ModifierType = ModifierType
        self.ModifierValueGRU = ModifierValueGRU


class TUnitEffectIncreaseWeaponPorteeMaxTBADescriptor(BaseDescription):
    def __init__(self, ModifierValue=None, ModifierType=None, ModifierValueGRU=None):
        self.ModifierValue = ModifierValue
        self.ModifierType = ModifierType
        self.ModifierValueGRU = ModifierValueGRU


class TUnitEffectIncreaseDispersionDescriptor(BaseDescription):
    def __init__(self, BonusDispersion=None, ModifierType=None):
        self.BonusDispersion = BonusDispersion
        self.ModifierType = ModifierType


class TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor(BaseDescription):
    def __init__(self, ModifierValue=None, ModifierType=None):
        self.ModifierValue = ModifierValue
        self.ModifierType = ModifierType


class TUnitEffectAlterWeaponTempsEntreDeuxTirsDescriptor(BaseDescription):
    def __init__(self, ModifierValue=None, ModifierType=None):
        self.ModifierValue = ModifierValue
        self.ModifierType = ModifierType


class TUnitEffectIncreaseChassisRotationSpeedDescriptor(BaseDescription):
    def __init__(self, BonusChassisRotationSpeed=None, ModifierType=None):
        self.BonusChassisRotationSpeed = BonusChassisRotationSpeed
        self.ModifierType = ModifierType


class TUnitEffectIncreaseTurretRotationSpeedDescriptor(BaseDescription):
    def __init__(self, BonusTurretRotationSpeed=None, ModifierType=None):
        self.BonusTurretRotationSpeed = BonusTurretRotationSpeed
        self.ModifierType = ModifierType


class TUnitEffectIncreaseSpeedDescriptor(BaseDescription):
    def __init__(self, BonusSpeedBaseInPercent=None, ModifierType=None):
        self.BonusSpeedBaseInPercent = BonusSpeedBaseInPercent
        self.ModifierType = ModifierType


class TBonusWeaponAimtimeEffectDescriptor(BaseDescription):
    def __init__(self, ModifierValue=None, ModifierType=None):
        self.ModifierValue = ModifierValue
        self.ModifierType = ModifierType


class TUnitEffectBonusExperienceLevelDescriptor(BaseDescription):
    def __init__(self, ExperienceLevelModifier=None, ModifierType=None):
        self.ExperienceLevelModifier = ExperienceLevelModifier
        self.ModifierType = ModifierType


class TUnitEffectIncreaseDangerousnessDescriptor(BaseDescription):
    def __init__(self, BonusDangerousness=None, ModifierType=None):
        self.BonusDangerousness = BonusDangerousness
        self.ModifierType = ModifierType


class TUnitEffectTransportSlotNumberModificationDescriptor(BaseDescription):
    def __init__(self, EffectOnTransportSlotNumber=None, ModifierType=None):
        self.EffectOnTransportSlotNumber = EffectOnTransportSlotNumber
        self.ModifierType = ModifierType


class TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor(BaseDescription):
    def __init__(self, ModifierValue=None, ModifierType=None):
        self.ModifierValue = ModifierValue
        self.ModifierType = ModifierType


class TUnitEffectIncreaseVisionDescriptor(BaseDescription):
    def __init__(self, BonusVisionBase=None, ModifierType=None):
        self.BonusVisionBase = BonusVisionBase
        self.ModifierType = ModifierType


class TUnitEffectIncreaseSpecializedDetectionDescriptor(BaseDescription):
    def __init__(self, BonusValueGRU=None, VisionType=None, ModifierType=None):
        self.BonusValueGRU = BonusValueGRU
        self.VisionType = VisionType
        self.ModifierType = ModifierType


class TUnitEffectIncreaseInfluenceValueMinDescriptor(BaseDescription):
    def __init__(self, Bonus=None, ModifierType=None):
        self.Bonus = Bonus
        self.ModifierType = ModifierType


class TUnitEffectSetSelectableDescriptor(BaseDescription):
    def __init__(self, Selectable=None):
        self.Selectable = Selectable


class TUnitEffectStopWithInertiaEffectDescriptor(BaseDescription):
    def __init__(self, UpdateEachTick=None):
        self.UpdateEachTick = UpdateEachTick


class TDerouteUnitEffectDescriptor(BaseDescription):
    def __init__(self):
        pass


class TEffectInflictPhysicalDamageDescriptor(BaseDescription):
    def __init__(self, PhysicalDamageValue=None, ModifierType=None):
        self.PhysicalDamageValue = PhysicalDamageValue
        self.ModifierType = ModifierType


class TUnitEffectIncreaseWeaponPrecisionArretDescriptor(BaseDescription):
    def __init__(self, ModifierValue=None, ModifierType=None):
        self.ModifierValue = ModifierValue
        self.ModifierType = ModifierType


class TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor(BaseDescription):
    def __init__(self, ModifierValue=None, ModifierType=None):
        self.ModifierValue = ModifierValue
        self.ModifierType = ModifierType


class TUnitEffectRemoveUnitDescriptor(BaseDescription):
    def __init__(self):
        pass


class TKillUnitEffectDescriptor(BaseDescription):
    def __init__(self):
        pass


class TEffectInflictSuppressDamageDescriptor(BaseDescription):
    def __init__(self, SuppressDamageValue=None, ModifierType=None):
        self.SuppressDamageValue = SuppressDamageValue
        self.ModifierType = ModifierType


class TUnitEffectBonusPrecisionWhenTargetedDescriptor(BaseDescription):
    def __init__(self, BonusPrecisionWhenTargeted=None, ModifierType=None):
        self.BonusPrecisionWhenTargeted = BonusPrecisionWhenTargeted
        self.ModifierType = ModifierType


class TUnitEffectIncreaseOpticalStrengthDescriptor(BaseDescription):
    def __init__(self, BonusOpticalStrength=None, ModifierType=None):
        self.BonusOpticalStrength = BonusOpticalStrength
        self.ModifierType = ModifierType


class TUnitEffectIncreaseWeaponPorteeMaxIgnoreSmokeDescriptor(BaseDescription):
    def __init__(self, BonusWeaponPorteeMax=None, ModifierType=None):
        self.BonusWeaponPorteeMax = BonusWeaponPorteeMax
        self.ModifierType = ModifierType


class TResistanceTypeRTTI(BaseDescription):
    def __init__(self, Index=None, Family=None):
        self.Index = Index
        self.Family = Family


class TUnitEffectReplaceArmorDescriptor(BaseDescription):
    def __init__(self, BlindageLocation=None, ReplacementBlindage=None):
        self.BlindageLocation = BlindageLocation
        self.ReplacementBlindage = ReplacementBlindage


class TUnitEffectIncreaseConcealmentBonusDescriptor(BaseDescription):
    def __init__(self, BonusConcealmentBonus=None, ModifierType=None):
        self.BonusConcealmentBonus = BonusConcealmentBonus
        self.ModifierType = ModifierType


class TUnitEffectHealOverTimeDescriptor(BaseDescription):
    def __init__(self, DamageType=None, HealUnitsPerSecond=None, NbUpdatePerSecond=None):
        self.DamageType = DamageType
        self.HealUnitsPerSecond = HealUnitsPerSecond
        self.NbUpdatePerSecond = NbUpdatePerSecond


class TTeamIdentifierForUnitEffect(BaseDescription):
    def __init__(self, TeamNumber=None, TeamType=None):
        self.TeamNumber = TeamNumber
        self.TeamType = TeamType


class TUnitEffectChangeTeamDescriptor(BaseDescription):
    def __init__(self, FutureTeam=None):
        self.FutureTeam = FutureTeam


class TUnitEffectAddCapacityDescriptor(BaseDescription):
    def __init__(self, CapacityToAdd=None):
        self.CapacityToAdd = CapacityToAdd


class TUnitEffectBonusHitRollECMDescriptor(BaseDescription):
    def __init__(self, BonusHitRollECM=None, ModifierType=None):
        self.BonusHitRollECM = BonusHitRollECM
        self.ModifierType = ModifierType


class TEvacAirplaneEffectDescriptor(BaseDescription):
    def __init__(self):
        pass


class TCapaciteDescriptor(BaseDescription):
    def __init__(self, Conditions=None, TagsCibleExcluded=None, TagsCiblePossible=None, DisplayRangeThickness=None, DisplayRangeColor=None, FeedbackActivationMask=None, TargetMySelf=None, TargetInSelf=None, TargetInTransport=None, TargetInBuilding=None, MaxTargetNb=None, SelfEffectDuration=None, TargetEffectDuration=None, TargetEffect=None, CanBeCastFromTransport=None, CheckVisibility=None, Cooldown=None, CastTime=None, RangeGRU=None, InfluenceMapAlliance=None, TargetTeamFilter=None, Declenchement=None, CumulEffect=None, NameToken=None, Name=None, DescriptorId=None, SelfEffect=None):
        self.Conditions = Conditions
        self.TagsCibleExcluded = TagsCibleExcluded
        self.TagsCiblePossible = TagsCiblePossible
        self.DisplayRangeThickness = DisplayRangeThickness
        self.DisplayRangeColor = DisplayRangeColor
        self.FeedbackActivationMask = FeedbackActivationMask
        self.TargetMySelf = TargetMySelf
        self.TargetInSelf = TargetInSelf
        self.TargetInTransport = TargetInTransport
        self.TargetInBuilding = TargetInBuilding
        self.MaxTargetNb = MaxTargetNb
        self.SelfEffectDuration = SelfEffectDuration
        self.TargetEffectDuration = TargetEffectDuration
        self.TargetEffect = TargetEffect
        self.CanBeCastFromTransport = CanBeCastFromTransport
        self.CheckVisibility = CheckVisibility
        self.Cooldown = Cooldown
        self.CastTime = CastTime
        self.RangeGRU = RangeGRU
        self.InfluenceMapAlliance = InfluenceMapAlliance
        self.TargetTeamFilter = TargetTeamFilter
        self.Declenchement = Declenchement
        self.CumulEffect = CumulEffect
        self.NameToken = NameToken
        self.Name = Name
        self.DescriptorId = DescriptorId
        self.SelfEffect = SelfEffect


class TCriticalEffectDescriptor(BaseDescription):
    def __init__(self, DisplayOnDeath=None, Unique=None, RepairCost=None, TimeOut=None, EffectsPack=None, HappeningKey=None, Token=None):
        self.DisplayOnDeath = DisplayOnDeath
        self.Unique = Unique
        self.RepairCost = RepairCost
        self.TimeOut = TimeOut
        self.EffectsPack = EffectsPack
        self.HappeningKey = HappeningKey
        self.Token = Token


class TCriticalEffect(BaseDescription):
    def __init__(self, Descriptor=None, Roll=None):
        self.Descriptor = Descriptor
        self.Roll = Roll


class CriticalEffect_Incendiary(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class CriticalEffect_EngineDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class CriticalEffect_EngineDestroyed(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class CriticalEffect_AmmoExplosion(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class CriticalEffect_FuelExplosion(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class CriticalEffect_CompReset(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class CriticalEffect_BailedOut(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class CriticalEffect_ArmourCracked(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class CriticalEffect_Spalling(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class CriticalEffect_TracksBroken(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class CriticalEffect_TurretStuck(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class HelicoCriticalEffect_HUD(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class HelicoCriticalEffect_CrewInjured(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class HelicoCriticalEffect_MainRotorDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class HelicoCriticalEffect_Turbine_Engine_Failure(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class HelicoCriticalEffect_turbineOnFire(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class HelicoCriticalEffect_FuelTankOnFire(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class HelicoCriticalEffect_FuelTankLeaking(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class HelicoCriticalEffect_WeaponsJammed(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class HelicoCriticalEffect_Hydraulic_Fluid_Fire(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class HelicoCriticalEffect_TailRotorDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class TemplateCriticalEffectModule_GroundUnit(BaseDescription):
    def __init__(self, PackEffetCritique=None, EffectsFromTerrain=None):
        self.PackEffetCritique = PackEffetCritique
        self.EffectsFromTerrain = EffectsFromTerrain


class TCriticalEffectModuleDescriptor(BaseDescription):
    def __init__(self, TerrainCriticalEffectTimer=None, Bounds=None, RicochetEffectsOnTop=None, RicochetEffectsOnRear=None, RicochetEffectsOnSides=None, RicochetEffectsOnFront=None, PierceEffectsOnTop=None, PierceEffectsOnRear=None, PierceEffectsOnSides=None, PierceEffectsOnFront=None, EffectsOnTop=None, EffectsOnRear=None, EffectsOnSides=None, EffectsOnFront=None, EffectsFromTerrain=None):
        self.TerrainCriticalEffectTimer = TerrainCriticalEffectTimer
        self.Bounds = Bounds
        self.RicochetEffectsOnTop = RicochetEffectsOnTop
        self.RicochetEffectsOnRear = RicochetEffectsOnRear
        self.RicochetEffectsOnSides = RicochetEffectsOnSides
        self.RicochetEffectsOnFront = RicochetEffectsOnFront
        self.PierceEffectsOnTop = PierceEffectsOnTop
        self.PierceEffectsOnRear = PierceEffectsOnRear
        self.PierceEffectsOnSides = PierceEffectsOnSides
        self.PierceEffectsOnFront = PierceEffectsOnFront
        self.EffectsOnTop = EffectsOnTop
        self.EffectsOnRear = EffectsOnRear
        self.EffectsOnSides = EffectsOnSides
        self.EffectsOnFront = EffectsOnFront
        self.EffectsFromTerrain = EffectsFromTerrain


class AirplaneCriticalEffect_WingsDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_EngineOnFire(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_PropellerDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_EngineDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_FloatCarburatorFailure(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_OilLeak(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_EngineOverheating(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_EngineStalling(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_ElevatorDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_FuelTankLeaking(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_RadiatorDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_RadiatorOverheating(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_PilotInjured(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_PilotPanicked(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_PilotUnconscious(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_WeaponsJammed(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_AileronDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_TailDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_FuelTankOnFire(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll


class AirplaneCriticalEffect_RudderDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll
