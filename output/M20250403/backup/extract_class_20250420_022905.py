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
    def __init__(self, EffectsFromTerrain=None, PackEffetCritique=None):
        self.EffectsFromTerrain = EffectsFromTerrain
        self.PackEffetCritique = PackEffetCritique


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


class TStairsDamageTypeEvolutionOverRangeDescriptor(BaseDescription):
    def __init__(self, AP=None, DistanceGRU=None):
        self.AP = AP
        self.DistanceGRU = DistanceGRU


class Template_DescriptorFire_Depiction(BaseDescription):
    def __init__(self, Density=None, FX=None, Radius=None):
        self.Density = Density
        self.FX = FX
        self.Radius = Radius


class TApparenceModuleDescriptor(BaseDescription):
    def __init__(self, DefaultVisibility=None, Depiction=None, ReferenceMesh=None):
        self.DefaultVisibility = DefaultVisibility
        self.Depiction = Depiction
        self.ReferenceMesh = ReferenceMesh


class TFireModuleDescriptor(BaseDescription):
    def __init__(self, SmokeDescriptor=None, OverridenSpreadDescriptor=None, IgniteDistricts=None, TimeBetweenBurns=None, AmmunitionForBurn=None, RadiusGRU=None, IsNewFireProbability=None, SpreadProbability=None, TimeBeforeSpreadAttempt=None, TimeBeforeSpreading=None, TimeToLive=None):
        self.SmokeDescriptor = SmokeDescriptor
        self.OverridenSpreadDescriptor = OverridenSpreadDescriptor
        self.IgniteDistricts = IgniteDistricts
        self.TimeBetweenBurns = TimeBetweenBurns
        self.AmmunitionForBurn = AmmunitionForBurn
        self.RadiusGRU = RadiusGRU
        self.IsNewFireProbability = IsNewFireProbability
        self.SpreadProbability = SpreadProbability
        self.TimeBeforeSpreadAttempt = TimeBeforeSpreadAttempt
        self.TimeBeforeSpreading = TimeBeforeSpreading
        self.TimeToLive = TimeToLive


class TEntityDescriptor(BaseDescription):
    def __init__(self, ModulesDescriptors=None, DescriptorId=None, ClassNameForDebug=None, CadavreDescriptor=None, World=None):
        self.ModulesDescriptors = ModulesDescriptors
        self.DescriptorId = DescriptorId
        self.ClassNameForDebug = ClassNameForDebug
        self.CadavreDescriptor = CadavreDescriptor
        self.World = World


class Template_DescriptorSmoke_Depiction(BaseDescription):
    def __init__(self, Density=None, Height=None, Radius=None):
        self.Density = Density
        self.Height = Height
        self.Radius = Radius


class TSmokeModuleDescriptor(BaseDescription):
    def __init__(self, Terrain=None, RadiusGRU=None, TimeToLive=None, AltitudeGRU=None):
        self.Terrain = Terrain
        self.RadiusGRU = RadiusGRU
        self.TimeToLive = TimeToLive
        self.AltitudeGRU = AltitudeGRU


class TDamageTypeRTTI(BaseDescription):
    def __init__(self, Index=None, Family=None):
        self.Index = Index
        self.Family = Family


class TDiceHitRollRuleDescriptor(BaseDescription):
    def __init__(self, BaseHitValueModifiers=None, BaseCriticModifier=None, DescriptorId=None, DistanceToTarget=None):
        self.BaseHitValueModifiers = BaseHitValueModifiers
        self.BaseCriticModifier = BaseCriticModifier
        self.DescriptorId = DescriptorId
        self.DistanceToTarget = DistanceToTarget


class TAmmunitionDescriptor(BaseDescription):
    def __init__(self, MissileDescriptor=None, MissileTimeBetweenCorrections=None, DamageTypeEvolutionOverRangeDescriptor=None, TandemCharge=None, PiercingWeapon=None, IsHarmlessForAllies=None, CanHarmAirplanes=None, TargetUnitCenter=None, FireDescriptor=None, SmokeDescriptor=None, InterfaceWeaponTexture=None, AffichageMunitionParSalve=None, NbrProjectilesSimultanes=None, CanShootWhileMoving=None, CanShootOnPosition=None, SupplyCost=None, NbTirParSalves=None, TimeBetweenTwoSalvos_Max=None, TimeBetweenTwoSalvos_Min=None, TimeBetweenTwoSalvos=None, TempsDeVisee=None, HitRollRuleDescriptor=None, TargetOnlyOneUnitInDistrict=None, IsFireAndForget=None, ShotsBeforeMaxNoise=None, NoiseDissimulationMalus=None, FluidFriction=None, ShotWithoutPhysics=None, MaxAccelerationGRU=None, MaximalSpeedGRU=None, InterdireTirReflexe=None, TirReflexe=None, TirIndirect=None, DisplaySalveAccuracy=None, AllowSuppressDamageWhenNoImpact=None, SuppressDamages=None, RadiusSplashSuppressDamagesGRU=None, ShowDamageInUI=None, PhysicalDamages=None, RadiusSplashPhysicalDamagesGRU=None, CorrectedShotAimtimeMultiplier=None, DispersionWithoutSorting=None, AngleDispersion=None, PorteeMaximaleHAGRU=None, TimeBetweenTwoFx=None, TimeBetweenTwoShots=None, FxPower=None, ImpactHappening=None, ProjectileType=None, Arme=None, MinMaxCategory=None, WeaponCursorType=None, TraitsToken=None, WeaponDescriptionToken=None, Caliber=None, TypeCategoryName=None, Name=None, DescriptorId=None, PorteeMaximaleTBAGRU=None, DispersionAtMinRangeGRU=None, DispersionAtMaxRangeGRU=None, PorteeMinimaleGRU=None, PorteeMaximaleGRU=None, MaxSuccessiveHitCount=None, Guidance=None, ForceHitTopArmor=None, NbSalvosShootOnPosition=None, PorteeMinimaleTBAGRU=None, DistanceForSpeedGRU=None, FlightTimeForSpeed=None, AffecteParNombre=None, FireTriggeringProbability=None, IgnoreInflammabilityConditions=None, AltitudeAPorteeMaximaleGRU=None, AltitudeAPorteeMinimaleGRU=None, IsSubAmmunition=None, PorteeMinimaleHAGRU=None, CorrectedShotDispersionMultiplier=None):
        self.MissileDescriptor = MissileDescriptor
        self.MissileTimeBetweenCorrections = MissileTimeBetweenCorrections
        self.DamageTypeEvolutionOverRangeDescriptor = DamageTypeEvolutionOverRangeDescriptor
        self.TandemCharge = TandemCharge
        self.PiercingWeapon = PiercingWeapon
        self.IsHarmlessForAllies = IsHarmlessForAllies
        self.CanHarmAirplanes = CanHarmAirplanes
        self.TargetUnitCenter = TargetUnitCenter
        self.FireDescriptor = FireDescriptor
        self.SmokeDescriptor = SmokeDescriptor
        self.InterfaceWeaponTexture = InterfaceWeaponTexture
        self.AffichageMunitionParSalve = AffichageMunitionParSalve
        self.NbrProjectilesSimultanes = NbrProjectilesSimultanes
        self.CanShootWhileMoving = CanShootWhileMoving
        self.CanShootOnPosition = CanShootOnPosition
        self.SupplyCost = SupplyCost
        self.NbTirParSalves = NbTirParSalves
        self.TimeBetweenTwoSalvos_Max = TimeBetweenTwoSalvos_Max
        self.TimeBetweenTwoSalvos_Min = TimeBetweenTwoSalvos_Min
        self.TimeBetweenTwoSalvos = TimeBetweenTwoSalvos
        self.TempsDeVisee = TempsDeVisee
        self.HitRollRuleDescriptor = HitRollRuleDescriptor
        self.TargetOnlyOneUnitInDistrict = TargetOnlyOneUnitInDistrict
        self.IsFireAndForget = IsFireAndForget
        self.ShotsBeforeMaxNoise = ShotsBeforeMaxNoise
        self.NoiseDissimulationMalus = NoiseDissimulationMalus
        self.FluidFriction = FluidFriction
        self.ShotWithoutPhysics = ShotWithoutPhysics
        self.MaxAccelerationGRU = MaxAccelerationGRU
        self.MaximalSpeedGRU = MaximalSpeedGRU
        self.InterdireTirReflexe = InterdireTirReflexe
        self.TirReflexe = TirReflexe
        self.TirIndirect = TirIndirect
        self.DisplaySalveAccuracy = DisplaySalveAccuracy
        self.AllowSuppressDamageWhenNoImpact = AllowSuppressDamageWhenNoImpact
        self.SuppressDamages = SuppressDamages
        self.RadiusSplashSuppressDamagesGRU = RadiusSplashSuppressDamagesGRU
        self.ShowDamageInUI = ShowDamageInUI
        self.PhysicalDamages = PhysicalDamages
        self.RadiusSplashPhysicalDamagesGRU = RadiusSplashPhysicalDamagesGRU
        self.CorrectedShotAimtimeMultiplier = CorrectedShotAimtimeMultiplier
        self.DispersionWithoutSorting = DispersionWithoutSorting
        self.AngleDispersion = AngleDispersion
        self.PorteeMaximaleHAGRU = PorteeMaximaleHAGRU
        self.TimeBetweenTwoFx = TimeBetweenTwoFx
        self.TimeBetweenTwoShots = TimeBetweenTwoShots
        self.FxPower = FxPower
        self.ImpactHappening = ImpactHappening
        self.ProjectileType = ProjectileType
        self.Arme = Arme
        self.MinMaxCategory = MinMaxCategory
        self.WeaponCursorType = WeaponCursorType
        self.TraitsToken = TraitsToken
        self.WeaponDescriptionToken = WeaponDescriptionToken
        self.Caliber = Caliber
        self.TypeCategoryName = TypeCategoryName
        self.Name = Name
        self.DescriptorId = DescriptorId
        self.PorteeMaximaleTBAGRU = PorteeMaximaleTBAGRU
        self.DispersionAtMinRangeGRU = DispersionAtMinRangeGRU
        self.DispersionAtMaxRangeGRU = DispersionAtMaxRangeGRU
        self.PorteeMinimaleGRU = PorteeMinimaleGRU
        self.PorteeMaximaleGRU = PorteeMaximaleGRU
        self.MaxSuccessiveHitCount = MaxSuccessiveHitCount
        self.Guidance = Guidance
        self.ForceHitTopArmor = ForceHitTopArmor
        self.NbSalvosShootOnPosition = NbSalvosShootOnPosition
        self.PorteeMinimaleTBAGRU = PorteeMinimaleTBAGRU
        self.DistanceForSpeedGRU = DistanceForSpeedGRU
        self.FlightTimeForSpeed = FlightTimeForSpeed
        self.AffecteParNombre = AffecteParNombre
        self.FireTriggeringProbability = FireTriggeringProbability
        self.IgnoreInflammabilityConditions = IgnoreInflammabilityConditions
        self.AltitudeAPorteeMaximaleGRU = AltitudeAPorteeMaximaleGRU
        self.AltitudeAPorteeMinimaleGRU = AltitudeAPorteeMinimaleGRU
        self.IsSubAmmunition = IsSubAmmunition
        self.PorteeMinimaleHAGRU = PorteeMinimaleHAGRU
        self.CorrectedShotDispersionMultiplier = CorrectedShotDispersionMultiplier


class TMountedWeaponDescriptor(BaseDescription):
    def __init__(self, WeaponShootDataPropertyName=None, WeaponIgnoredPropertyName=None, WeaponActiveAndCanShootPropertyName=None, TirContinu=None, ShowInInterface=None, ShowDispersion=None, SalvoStockIndex=None, NbWeapons=None, HandheldEquipmentKey=None, EffectTag=None, DispersionRadiusOnThickness=None, DispersionRadiusOnColor=None, DispersionRadiusOffThickness=None, DispersionRadiusOffColor=None, AnimateOnlyOneSoldier=None, Ammunition=None):
        self.WeaponShootDataPropertyName = WeaponShootDataPropertyName
        self.WeaponIgnoredPropertyName = WeaponIgnoredPropertyName
        self.WeaponActiveAndCanShootPropertyName = WeaponActiveAndCanShootPropertyName
        self.TirContinu = TirContinu
        self.ShowInInterface = ShowInInterface
        self.ShowDispersion = ShowDispersion
        self.SalvoStockIndex = SalvoStockIndex
        self.NbWeapons = NbWeapons
        self.HandheldEquipmentKey = HandheldEquipmentKey
        self.EffectTag = EffectTag
        self.DispersionRadiusOnThickness = DispersionRadiusOnThickness
        self.DispersionRadiusOnColor = DispersionRadiusOnColor
        self.DispersionRadiusOffThickness = DispersionRadiusOffThickness
        self.DispersionRadiusOffColor = DispersionRadiusOffColor
        self.AnimateOnlyOneSoldier = AnimateOnlyOneSoldier
        self.Ammunition = Ammunition


class TTurretTwoAxisDescriptor(BaseDescription):
    def __init__(self, YulBoneOrdinal=None, VitesseRotation=None, Tag=None, MountedWeaponDescriptorList=None, AngleRotationMinPitch=None, AngleRotationMaxPitch=None, AngleRotationMax=None, AngleRotationBasePitch=None, AngleRotationBase=None, TurretIdleBehaviourDescriptor=None, OutOfRangeTrackingDuration=None, MasterTurretYulBoneOrdinal=None, AimingPriority=None):
        self.YulBoneOrdinal = YulBoneOrdinal
        self.VitesseRotation = VitesseRotation
        self.Tag = Tag
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.AngleRotationMinPitch = AngleRotationMinPitch
        self.AngleRotationMaxPitch = AngleRotationMaxPitch
        self.AngleRotationMax = AngleRotationMax
        self.AngleRotationBasePitch = AngleRotationBasePitch
        self.AngleRotationBase = AngleRotationBase
        self.TurretIdleBehaviourDescriptor = TurretIdleBehaviourDescriptor
        self.OutOfRangeTrackingDuration = OutOfRangeTrackingDuration
        self.MasterTurretYulBoneOrdinal = MasterTurretYulBoneOrdinal
        self.AimingPriority = AimingPriority


class TWeaponManagerModuleDescriptor(BaseDescription):
    def __init__(self, TurretDescriptorList=None, AlwaysOrientArmorTowardsThreat=None, SalvoIsMainSalvo=None, Salves=None):
        self.TurretDescriptorList = TurretDescriptorList
        self.AlwaysOrientArmorTowardsThreat = AlwaysOrientArmorTowardsThreat
        self.SalvoIsMainSalvo = SalvoIsMainSalvo
        self.Salves = Salves


class TTurretUnitDescriptor(BaseDescription):
    def __init__(self, YulBoneOrdinal=None, Tag=None, MountedWeaponDescriptorList=None, AngleRotationMinPitch=None, AngleRotationMaxPitch=None, AngleRotationMax=None, AimingPriority=None):
        self.YulBoneOrdinal = YulBoneOrdinal
        self.Tag = Tag
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.AngleRotationMinPitch = AngleRotationMinPitch
        self.AngleRotationMaxPitch = AngleRotationMaxPitch
        self.AngleRotationMax = AngleRotationMax
        self.AimingPriority = AimingPriority


class TTurretInfanterieDescriptor(BaseDescription):
    def __init__(self, YulBoneOrdinal=None, MountedWeaponDescriptorList=None):
        self.YulBoneOrdinal = YulBoneOrdinal
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList


class TTurretBombardierDescriptor(BaseDescription):
    def __init__(self, YulBoneOrdinal=None, Tag=None, MountedWeaponDescriptorList=None, FlyingSpeedInKmph=None, FlyingAltitudeGRU=None):
        self.YulBoneOrdinal = YulBoneOrdinal
        self.Tag = Tag
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.FlyingSpeedInKmph = FlyingSpeedInKmph
        self.FlyingAltitudeGRU = FlyingAltitudeGRU


class TSupplyDescriptor(BaseDescription):
    def __init__(self, FeedbackDrawer=None, CriticsSupplyCostBySecond=None, CriticsSupplyBySecond=None, AmmunitionSupplyBySecond=None, SupplySupplyCostBySecond=None, SupplySupplyBySecond=None, HealthSupplyCostBySecond=None, HealthSupplyBySecond=None, FuelSupplyCostBySecond=None, FuelSupplyBySecond=None, DefaultSupplyRangeGRU=None):
        self.FeedbackDrawer = FeedbackDrawer
        self.CriticsSupplyCostBySecond = CriticsSupplyCostBySecond
        self.CriticsSupplyBySecond = CriticsSupplyBySecond
        self.AmmunitionSupplyBySecond = AmmunitionSupplyBySecond
        self.SupplySupplyCostBySecond = SupplySupplyCostBySecond
        self.SupplySupplyBySecond = SupplySupplyBySecond
        self.HealthSupplyCostBySecond = HealthSupplyCostBySecond
        self.HealthSupplyBySecond = HealthSupplyBySecond
        self.FuelSupplyCostBySecond = FuelSupplyCostBySecond
        self.FuelSupplyBySecond = FuelSupplyBySecond
        self.DefaultSupplyRangeGRU = DefaultSupplyRangeGRU


class TSupplyFeedbackDrawer(BaseDescription):
    def __init__(self, FeedbackFadeOutTime=None, FeedbackScreenResilienceDuration=None, LineThickness=None, ZOffset=None, LineColor=None):
        self.FeedbackFadeOutTime = FeedbackFadeOutTime
        self.FeedbackScreenResilienceDuration = FeedbackScreenResilienceDuration
        self.LineThickness = LineThickness
        self.ZOffset = ZOffset
        self.LineColor = LineColor


class TDamageLevelDescriptor(BaseDescription):
    def __init__(self, NameForDebug=None, EffectsPacks=None, AnimationType=None, TextColor=None, HitRollModifier=None, MoralModifier=None, LocalizationToken=None, Value=None, DescriptorId=None, FeedbackOnSelf=None):
        self.NameForDebug = NameForDebug
        self.EffectsPacks = EffectsPacks
        self.AnimationType = AnimationType
        self.TextColor = TextColor
        self.HitRollModifier = HitRollModifier
        self.MoralModifier = MoralModifier
        self.LocalizationToken = LocalizationToken
        self.Value = Value
        self.DescriptorId = DescriptorId
        self.FeedbackOnSelf = FeedbackOnSelf


class TDamageLevelsPackDescriptor(BaseDescription):
    def __init__(self, NameForDebug=None, DamageLevelsDescriptors=None, DescriptorId=None):
        self.NameForDebug = NameForDebug
        self.DamageLevelsDescriptors = DamageLevelsDescriptors
        self.DescriptorId = DescriptorId


class TExperienceLevelDescriptor(BaseDescription):
    def __init__(self, NameForDebug=None, HintBodyToken=None, HintTitleToken=None, ThresholdPriceMultiplier=None, ThresholdAdditionalValue=None, LocalizationToken=None, DescriptorId=None, LevelEffectsPacks=None):
        self.NameForDebug = NameForDebug
        self.HintBodyToken = HintBodyToken
        self.HintTitleToken = HintTitleToken
        self.ThresholdPriceMultiplier = ThresholdPriceMultiplier
        self.ThresholdAdditionalValue = ThresholdAdditionalValue
        self.LocalizationToken = LocalizationToken
        self.DescriptorId = DescriptorId
        self.LevelEffectsPacks = LevelEffectsPacks


class TExperienceLevelsPackDescriptor(BaseDescription):
    def __init__(self, NameForDebug=None, ExperienceLevelsDescriptors=None, DescriptorId=None):
        self.NameForDebug = NameForDebug
        self.ExperienceLevelsDescriptors = ExperienceLevelsDescriptors
        self.DescriptorId = DescriptorId


class TResistanceTypeFamilyDefinition(BaseDescription):
    def __init__(self, MaxIndex=None, Family=None):
        self.MaxIndex = MaxIndex
        self.Family = Family


class TDamageTypeFamilyDefinition(BaseDescription):
    def __init__(self, MaxIndex=None, Family=None):
        self.MaxIndex = MaxIndex
        self.Family = Family


class TGameplayDamageResistanceContainer(BaseDescription):
    def __init__(self, Values=None, DamageFamilyDefinitionList=None, ResistanceFamilyDefinitionList=None):
        self.Values = Values
        self.DamageFamilyDefinitionList = DamageFamilyDefinitionList
        self.ResistanceFamilyDefinitionList = ResistanceFamilyDefinitionList


class TResistanceFamilyList(BaseDescription):
    def __init__(self, Values=None):
        self.Values = Values


class TDamageFamilyList(BaseDescription):
    def __init__(self, Values=None):
        self.Values = Values


class TTypeUnitModuleDescriptor(BaseDescription):
    def __init__(self, Coalition=None, MotherCountry=None, TypeUnitFormation=None, AcknowUnitType=None):
        self.Coalition = Coalition
        self.MotherCountry = MotherCountry
        self.TypeUnitFormation = TypeUnitFormation
        self.AcknowUnitType = AcknowUnitType


class TemplateUnitCriticalModule(BaseDescription):
    def __init__(self, Module=None):
        self.Module = Module


class TTagsModuleDescriptor(BaseDescription):
    def __init__(self, TagSet=None):
        self.TagSet = TagSet


class TExperienceModuleDescriptor(BaseDescription):
    def __init__(self, ExperienceMultiplierBonusOnKill=None, ExperienceLevelsPackDescriptor=None):
        self.ExperienceMultiplierBonusOnKill = ExperienceMultiplierBonusOnKill
        self.ExperienceLevelsPackDescriptor = ExperienceLevelsPackDescriptor


class TVisibilityModuleDescriptor(BaseDescription):
    def __init__(self, UnitConcealmentBonus=None):
        self.UnitConcealmentBonus = UnitConcealmentBonus


class VehicleApparenceModuleDescriptor(BaseDescription):
    def __init__(self, ReferenceMesh=None, GameplayBBoxBoneName=None, BlackHoleIdentifier=None, Depiction=None):
        self.ReferenceMesh = ReferenceMesh
        self.GameplayBBoxBoneName = GameplayBBoxBoneName
        self.BlackHoleIdentifier = BlackHoleIdentifier
        self.Depiction = Depiction


class TAutoCoverModuleDescriptor(BaseDescription):
    def __init__(self, UseTerrainsForEscape=None, TerrainList=None, TerrainListMask=None, OccupationRadiusGRU=None, AutoCoverRangeGRU=None):
        self.UseTerrainsForEscape = UseTerrainsForEscape
        self.TerrainList = TerrainList
        self.TerrainListMask = TerrainListMask
        self.OccupationRadiusGRU = OccupationRadiusGRU
        self.AutoCoverRangeGRU = AutoCoverRangeGRU


class TModuleSelector(BaseDescription):
    def __init__(self, Condition=None, Default=None):
        self.Condition = Condition
        self.Default = Default


class TBaseDamageModuleDescriptor(BaseDescription):
    def __init__(self, MaxStunDamages=None, MaxSuppressionDamages=None, MaxPhysicalDamages=None, StunDamageLevelsPack=None, SuppressDamageLevelsPack=None, PhysicalDamageLevelsPack=None):
        self.MaxStunDamages = MaxStunDamages
        self.MaxSuppressionDamages = MaxSuppressionDamages
        self.MaxPhysicalDamages = MaxPhysicalDamages
        self.StunDamageLevelsPack = StunDamageLevelsPack
        self.SuppressDamageLevelsPack = SuppressDamageLevelsPack
        self.PhysicalDamageLevelsPack = PhysicalDamageLevelsPack


class TBlindageProperties(BaseDescription):
    def __init__(self, ExplosiveReactiveArmor=None, ResistanceTop=None, ResistanceRear=None, ResistanceSides=None, ResistanceFront=None):
        self.ExplosiveReactiveArmor = ExplosiveReactiveArmor
        self.ResistanceTop = ResistanceTop
        self.ResistanceRear = ResistanceRear
        self.ResistanceSides = ResistanceSides
        self.ResistanceFront = ResistanceFront


class TDamageModuleDescriptor(BaseDescription):
    def __init__(self, UseTopArmorAgainstFire=None, AutoOrientation=None, HitRollECM=None, KillWhenDamagesReachMax=None, BlindageProperties=None, StunDamagesRegen=None, SuppressDamagesRegenRatio=None):
        self.UseTopArmorAgainstFire = UseTopArmorAgainstFire
        self.AutoOrientation = AutoOrientation
        self.HitRollECM = HitRollECM
        self.KillWhenDamagesReachMax = KillWhenDamagesReachMax
        self.BlindageProperties = BlindageProperties
        self.StunDamagesRegen = StunDamagesRegen
        self.SuppressDamagesRegenRatio = SuppressDamagesRegenRatio


class TDangerousnessModuleDescriptor(BaseDescription):
    def __init__(self, Dangerousness=None):
        self.Dangerousness = Dangerousness


class TRoutModuleDescriptor(BaseDescription):
    def __init__(self, MoralLevel=None):
        self.MoralLevel = MoralLevel


class TGenericMovementModuleDescriptor(BaseDescription):
    def __init__(self, PathfindType=None, MaxSpeedInKmph=None):
        self.PathfindType = PathfindType
        self.MaxSpeedInKmph = MaxSpeedInKmph


class TLandMovementModuleDescriptor(BaseDescription):
    def __init__(self, RotationStopTime=None, RotationStartTime=None, StopTime=None, StartTime=None, TempsDemiTour=None, MaxDecelerationGRU=None, MaxAccelerationGRU=None, SpeedBonusFactorOnRoad=None, UnitMovingType=None, VehicleSizeInMeter=None):
        self.RotationStopTime = RotationStopTime
        self.RotationStartTime = RotationStartTime
        self.StopTime = StopTime
        self.StartTime = StartTime
        self.TempsDemiTour = TempsDemiTour
        self.MaxDecelerationGRU = MaxDecelerationGRU
        self.MaxAccelerationGRU = MaxAccelerationGRU
        self.SpeedBonusFactorOnRoad = SpeedBonusFactorOnRoad
        self.UnitMovingType = UnitMovingType
        self.VehicleSizeInMeter = VehicleSizeInMeter


class TFuelModuleDescriptor(BaseDescription):
    def __init__(self, FuelMoveDuration=None, FuelCapacity=None):
        self.FuelMoveDuration = FuelMoveDuration
        self.FuelCapacity = FuelCapacity


class TScannerConfigurationDescriptor(BaseDescription):
    def __init__(self, OpticalStrengths=None, VisionRangesGRU=None):
        self.OpticalStrengths = OpticalStrengths
        self.VisionRangesGRU = VisionRangesGRU


class TModernWarfareVisibilityRollRule(BaseDescription):
    def __init__(self, VisibilityRuleDescriptor=None, TimeBetweenEachIdentifyRoll=None, IdentifyBaseProbability=None):
        self.VisibilityRuleDescriptor = VisibilityRuleDescriptor
        self.TimeBetweenEachIdentifyRoll = TimeBetweenEachIdentifyRoll
        self.IdentifyBaseProbability = IdentifyBaseProbability


class TReverseScannerWithIdentificationDescriptor(BaseDescription):
    def __init__(self, VisibilityRollRule=None):
        self.VisibilityRollRule = VisibilityRollRule


class TemplateUnitMissileCarriage(BaseDescription):
    def __init__(self, Connoisseur=None):
        self.Connoisseur = Connoisseur


class TCadavreGeneratorModuleDescriptor(BaseDescription):
    def __init__(self, CadavreDescriptor=None):
        self.CadavreDescriptor = CadavreDescriptor


class TIAStratModuleDescriptor(BaseDescription):
    def __init__(self, GameplayBehavior=None, DatabaseId=None):
        self.GameplayBehavior = GameplayBehavior
        self.DatabaseId = DatabaseId


class TProductionModuleDescriptor(BaseDescription):
    def __init__(self, ProductionRessourcesNeeded=None, ProductionTime=None, Factory=None):
        self.ProductionRessourcesNeeded = ProductionRessourcesNeeded
        self.ProductionTime = ProductionTime
        self.Factory = Factory


class TAutomaticBehaviorModuleDescriptor(BaseDescription):
    def __init__(self, SearchedTagsInEngagementTarget=None, MaxDistanceForEngagementGRU=None, MaxDistanceForOffensiveReactionGRU=None, DistanceToFleeGRU=None, AssistRequestBroadcastRadiusGRU=None, CanAssist=None):
        self.SearchedTagsInEngagementTarget = SearchedTagsInEngagementTarget
        self.MaxDistanceForEngagementGRU = MaxDistanceForEngagementGRU
        self.MaxDistanceForOffensiveReactionGRU = MaxDistanceForOffensiveReactionGRU
        self.DistanceToFleeGRU = DistanceToFleeGRU
        self.AssistRequestBroadcastRadiusGRU = AssistRequestBroadcastRadiusGRU
        self.CanAssist = CanAssist


class TCubeActionModuleDescriptor(BaseDescription):
    def __init__(self, CubeActionDescriptor=None):
        self.CubeActionDescriptor = CubeActionDescriptor


class TMinimapDisplayModuleDescriptor(BaseDescription):
    def __init__(self, FollowUnitOrientation=None, Texture=None):
        self.FollowUnitOrientation = FollowUnitOrientation
        self.Texture = Texture


class TOrderConfigModuleDescriptor(BaseDescription):
    def __init__(self, ValidOrders=None):
        self.ValidOrders = ValidOrders


class TOrderableModuleDescriptor(BaseDescription):
    def __init__(self, UnlockableOrders=None):
        self.UnlockableOrders = UnlockableOrders


class TBUCKToolAlternativeValues_TUIValueTextureNameFromTEugBMutableInteger(BaseDescription):
    def __init__(self, Values=None, Alterator=None, CommandNameTrigger=None):
        self.Values = Values
        self.Alterator = Alterator
        self.CommandNameTrigger = CommandNameTrigger


class TTacticalLabelModuleDescriptor(BaseDescription):
    def __init__(self, PositionHeightOffset=None, UnidentifiedTexture=None, IdentifiedTexture=None, MultiSelectionSortingOrder=None):
        self.PositionHeightOffset = PositionHeightOffset
        self.UnidentifiedTexture = UnidentifiedTexture
        self.IdentifiedTexture = IdentifiedTexture
        self.MultiSelectionSortingOrder = MultiSelectionSortingOrder


class TStrategicDataModuleDescriptor(BaseDescription):
    def __init__(self, UnitBonusXpPerLevelValue=None, UnitDefenseValue=None, UnitAttackValue=None):
        self.UnitBonusXpPerLevelValue = UnitBonusXpPerLevelValue
        self.UnitDefenseValue = UnitDefenseValue
        self.UnitAttackValue = UnitAttackValue


class TUnitUIModuleDescriptor(BaseDescription):
    def __init__(self, TypeStrategicCount=None, CountryTexture=None, ButtonTexture=None, MenuIconTexture=None, GenerateName=None, InfoPanelConfigurationToken=None, NameToken=None, PriceCategory=None, UnitRole=None, SpecialtiesList=None, UpgradeFromUnit=None, DisplayRoadSpeedInKmph=None):
        self.TypeStrategicCount = TypeStrategicCount
        self.CountryTexture = CountryTexture
        self.ButtonTexture = ButtonTexture
        self.MenuIconTexture = MenuIconTexture
        self.GenerateName = GenerateName
        self.InfoPanelConfigurationToken = InfoPanelConfigurationToken
        self.NameToken = NameToken
        self.PriceCategory = PriceCategory
        self.UnitRole = UnitRole
        self.SpecialtiesList = SpecialtiesList
        self.UpgradeFromUnit = UpgradeFromUnit
        self.DisplayRoadSpeedInKmph = DisplayRoadSpeedInKmph


class TShowRoomEquivalenceModuleDescriptor(BaseDescription):
    def __init__(self, ShowRoomDescriptor=None):
        self.ShowRoomDescriptor = ShowRoomDescriptor


class TUnitUpkeepModuleDescriptor(BaseDescription):
    def __init__(self, UpkeepPercentage=None):
        self.UpkeepPercentage = UpkeepPercentage


class TVisualShootPositionsModuleDescriptor(BaseDescription):
    def __init__(self):
        pass


class TCapaciteModuleDescriptor(BaseDescription):
    def __init__(self, DefaultSkillList=None):
        self.DefaultSkillList = DefaultSkillList


class TTransportableModuleDescriptor(BaseDescription):
    def __init__(self, IsTowable=None, TimeToLoad=None, NbSeatsOccupied=None, TransportedSoldier=None, TransportedTexture=None):
        self.IsTowable = IsTowable
        self.TimeToLoad = TimeToLoad
        self.NbSeatsOccupied = NbSeatsOccupied
        self.TransportedSoldier = TransportedSoldier
        self.TransportedTexture = TransportedTexture


class TDeploymentShiftModuleDescriptor(BaseDescription):
    def __init__(self, DeploymentShiftGRU=None):
        self.DeploymentShiftGRU = DeploymentShiftGRU


class TSupplyModuleDescriptor(BaseDescription):
    def __init__(self, SupplyPriority=None, SupplyCapacity=None, SupplyDescriptor=None):
        self.SupplyPriority = SupplyPriority
        self.SupplyCapacity = SupplyCapacity
        self.SupplyDescriptor = SupplyDescriptor


class TSellModuleDescriptor(BaseDescription):
    def __init__(self):
        pass


class TTransporterModuleDescriptor(BaseDescription):
    def __init__(self, LoadRadiusGRU=None, WreckUnloadStunDamageBonus=None, WreckUnloadSuppressDamageBonus=None, WreckUnloadPhysicalDamageBonus=None, NbSeatsAvailable=None, TransportableTagSet=None):
        self.LoadRadiusGRU = LoadRadiusGRU
        self.WreckUnloadStunDamageBonus = WreckUnloadStunDamageBonus
        self.WreckUnloadSuppressDamageBonus = WreckUnloadSuppressDamageBonus
        self.WreckUnloadPhysicalDamageBonus = WreckUnloadPhysicalDamageBonus
        self.NbSeatsAvailable = NbSeatsAvailable
        self.TransportableTagSet = TransportableTagSet


class TCommanderModuleDescriptor(BaseDescription):
    def __init__(self):
        pass


class TZoneInfluenceMapModuleDescriptor(BaseDescription):
    def __init__(self, IsEnabledByComportementAuto=None, PreventsDecayInZone=None, StrengthDecayPerSecond=None, MinimumInfluenceStrength=None, InfluenceStrength=None):
        self.IsEnabledByComportementAuto = IsEnabledByComportementAuto
        self.PreventsDecayInZone = PreventsDecayInZone
        self.StrengthDecayPerSecond = StrengthDecayPerSecond
        self.MinimumInfluenceStrength = MinimumInfluenceStrength
        self.InfluenceStrength = InfluenceStrength


class TInfluenceScoutModuleDescriptor(BaseDescription):
    def __init__(self):
        pass


class InfantryApparenceModuleDescriptor(BaseDescription):
    def __init__(self, Depiction=None):
        self.Depiction = Depiction


class Descriptor_Unit_MimeticUnit(BaseDescription):
    def __init__(self, MimeticName=None, DescriptorId=None):
        self.MimeticName = MimeticName
        self.DescriptorId = DescriptorId


class TInfantrySquadModuleDescriptor(BaseDescription):
    def __init__(self, MimeticDescriptor=None, WeaponUnitFXKey=None, InfantryMimeticName=None, SquadDataDescriptor=None, NbSoldatInGroupeCombat=None):
        self.MimeticDescriptor = MimeticDescriptor
        self.WeaponUnitFXKey = WeaponUnitFXKey
        self.InfantryMimeticName = InfantryMimeticName
        self.SquadDataDescriptor = SquadDataDescriptor
        self.NbSoldatInGroupeCombat = NbSoldatInGroupeCombat


class TInfantrySquadWeaponAssignmentModuleDescriptor(BaseDescription):
    def __init__(self):
        pass


class TLinkToDistrictModuleDescriptor(BaseDescription):
    def __init__(self):
        pass


class HelicopterPositionModuleDescriptor(BaseDescription):
    def __init__(self, NearGroundFlyingAltitudeGRU=None, LowAltitudeFlyingAltitudeGRU=None):
        self.NearGroundFlyingAltitudeGRU = NearGroundFlyingAltitudeGRU
        self.LowAltitudeFlyingAltitudeGRU = LowAltitudeFlyingAltitudeGRU


class THelicopterMovementModuleDescriptor(BaseDescription):
    def __init__(self, Mass=None, RotorArea=None, GFactorLimit=None, MaxInclination=None, CyclicManoeuvrability=None, TorqueManoeuvrability=None, UpwardSpeedInKmph=None, WorldFloorProxy=None, MaxSpeedInKmph=None):
        self.Mass = Mass
        self.RotorArea = RotorArea
        self.GFactorLimit = GFactorLimit
        self.MaxInclination = MaxInclination
        self.CyclicManoeuvrability = CyclicManoeuvrability
        self.TorqueManoeuvrability = TorqueManoeuvrability
        self.UpwardSpeedInKmph = UpwardSpeedInKmph
        self.WorldFloorProxy = WorldFloorProxy
        self.MaxSpeedInKmph = MaxSpeedInKmph


class TFlareModuleDescriptor_MW(BaseDescription):
    def __init__(self, BonusTimeBetweenFlareByProjectile=None, MinimalTimeBetweenFlare=None, TimeBetweenFlare=None, DistanceActivationGRU=None, ProjectileSpeed=None):
        self.BonusTimeBetweenFlareByProjectile = BonusTimeBetweenFlareByProjectile
        self.MinimalTimeBetweenFlare = MinimalTimeBetweenFlare
        self.TimeBetweenFlare = TimeBetweenFlare
        self.DistanceActivationGRU = DistanceActivationGRU
        self.ProjectileSpeed = ProjectileSpeed


class AirplanePositionModuleDescriptor(BaseDescription):
    def __init__(self, LowAltitudeFlyingAltitudeGRU=None):
        self.LowAltitudeFlyingAltitudeGRU = LowAltitudeFlyingAltitudeGRU


class AirplaneMovementDescriptor(BaseDescription):
    def __init__(self, OrderedAttackStrategies=None, EvacToStartingPoint=None, EvacAngle=None, RollSpeed=None, RollAngle=None, PitchAngle=None, AgilityRadiusGRU=None, SpeedInKmph=None, AltitudeMinGRU=None, AltitudeGRU=None):
        self.OrderedAttackStrategies = OrderedAttackStrategies
        self.EvacToStartingPoint = EvacToStartingPoint
        self.EvacAngle = EvacAngle
        self.RollSpeed = RollSpeed
        self.RollAngle = RollAngle
        self.PitchAngle = PitchAngle
        self.AgilityRadiusGRU = AgilityRadiusGRU
        self.SpeedInKmph = SpeedInKmph
        self.AltitudeMinGRU = AltitudeMinGRU
        self.AltitudeGRU = AltitudeGRU


class TAirplaneModuleDescriptor(BaseDescription):
    def __init__(self, TravelDuration=None, EvacuationTime=None):
        self.TravelDuration = TravelDuration
        self.EvacuationTime = EvacuationTime


class BuildingApparenceModuleDescriptor(BaseDescription):
    def __init__(self, SymbolName=None, BlackHoleIdentifier=None):
        self.SymbolName = SymbolName
        self.BlackHoleIdentifier = BlackHoleIdentifier


class BuildingCadavreModuleDescriptor(BaseDescription):
    def __init__(self, ModuleDescriptorsToSteal=None, CadavreDuration=None):
        self.ModuleDescriptorsToSteal = ModuleDescriptorsToSteal
        self.CadavreDuration = CadavreDuration


class TDistrictUnitsContainerModuleDescriptor(BaseDescription):
    def __init__(self, AllowedTagSet=None, NbSlots=None):
        self.AllowedTagSet = AllowedTagSet
        self.NbSlots = NbSlots


class TDynamicTerrainModuleDescriptor(BaseDescription):
    def __init__(self, TerrainToApplyOnDeath=None, TerrainToApplyOnInit=None):
        self.TerrainToApplyOnDeath = TerrainToApplyOnDeath
        self.TerrainToApplyOnInit = TerrainToApplyOnInit


class TShootingPointsModuleDescriptor(BaseDescription):
    def __init__(self):
        pass


class DistrictDescriptor(BaseDescription):
    def __init__(self, KillWhenDamagesReachMax=None, MaxPhysicalDamages=None, NbSlots=None, ClassNameForDebug=None, CadavreDescriptorId=None, DescriptorId=None):
        self.KillWhenDamagesReachMax = KillWhenDamagesReachMax
        self.MaxPhysicalDamages = MaxPhysicalDamages
        self.NbSlots = NbSlots
        self.ClassNameForDebug = ClassNameForDebug
        self.CadavreDescriptorId = CadavreDescriptorId
        self.DescriptorId = DescriptorId


class TDeckDivisionDescriptor(BaseDescription):
    def __init__(self, CountryId=None, TypeTexture=None, PortraitTexture=None, EmblemTexture=None, CostMatrix=None, DivisionRule=None, MaxActivationPoints=None, DescriptionHintTitleToken=None, DivisionTags=None, DivisionCoalition=None, DivisionPowerClassification=None, InterfaceOrder=None, DivisionName=None, CfgName=None, DescriptorId=None, StrategicLabelColor=None):
        self.CountryId = CountryId
        self.TypeTexture = TypeTexture
        self.PortraitTexture = PortraitTexture
        self.EmblemTexture = EmblemTexture
        self.CostMatrix = CostMatrix
        self.DivisionRule = DivisionRule
        self.MaxActivationPoints = MaxActivationPoints
        self.DescriptionHintTitleToken = DescriptionHintTitleToken
        self.DivisionTags = DivisionTags
        self.DivisionCoalition = DivisionCoalition
        self.DivisionPowerClassification = DivisionPowerClassification
        self.InterfaceOrder = InterfaceOrder
        self.DivisionName = DivisionName
        self.CfgName = CfgName
        self.DescriptorId = DescriptorId
        self.StrategicLabelColor = StrategicLabelColor


class TDeckUniteRule(BaseDescription):
    def __init__(self, NumberOfUnitInPackXPMultiplier=None, NumberOfUnitInPack=None, MaxPackNumber=None, AvailableWithoutTransport=None, UnitDescriptor=None, AvailableTransportList=None):
        self.NumberOfUnitInPackXPMultiplier = NumberOfUnitInPackXPMultiplier
        self.NumberOfUnitInPack = NumberOfUnitInPack
        self.MaxPackNumber = MaxPackNumber
        self.AvailableWithoutTransport = AvailableWithoutTransport
        self.UnitDescriptor = UnitDescriptor
        self.AvailableTransportList = AvailableTransportList


class TDeckDivisionRule(BaseDescription):
    def __init__(self, UnitRuleList=None):
        self.UnitRuleList = UnitRuleList


class CriticalEffect_TransmissionDamaged(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="~/CriticalEffect_TransmissionDamaged_Desc", Roll=Roll)
        self.Roll = Roll


class CriticalEffect_Bounce(TCriticalEffect):
    def __init__(self, Roll=None):
        super().__init__(Descriptor="~/CriticalEffect_Bounce_Desc", Roll=Roll)
        self.Roll = Roll
