from src.extractor.base_class import BaseDescription

class TCapaciteDescriptor(BaseDescription):
    def __init__(self, DescriptorId=None, Name=None, NameToken=None, CumulEffect=None, Declenchement=None, TypeCible=None, TargetTeamFilter=None, InfluenceMapAlliance=None, TargetWoundedFilter=None, AreaShape=None, InfluenceMapType=None, ActionRadiusWithBoundingBox=None, RadiusGRU=None, RangeGRU=None, CastTime=None, Cooldown=None, CheckVisibility=None, AllowReflexDuringCast=None, CanBeCastFromTransport=None, TargetEffect=None, TargetEffectDuration=None, SelfEffectDuration=None, MinVirtualUnits=None, OrderMustSpreadTargets=None, MaxTargetNb=None, MultiplyCost=None, TargetInBuilding=None, TargetInTransport=None, TargetInSelf=None, TargetMySelf=None, FeedbackActivationMask=None, DisplayRangeColor=None, DisplayRangeThickness=None, Price=None, TagsCiblePossible=None, TagsCibleExcluded=None, Conditions=None, SelfEffect=None):
        self.DescriptorId = DescriptorId
        self.Name = Name
        self.NameToken = NameToken
        self.CumulEffect = CumulEffect
        self.Declenchement = Declenchement
        self.TypeCible = TypeCible
        self.TargetTeamFilter = TargetTeamFilter
        self.InfluenceMapAlliance = InfluenceMapAlliance
        self.TargetWoundedFilter = TargetWoundedFilter
        self.AreaShape = AreaShape
        self.InfluenceMapType = InfluenceMapType
        self.ActionRadiusWithBoundingBox = ActionRadiusWithBoundingBox
        self.RadiusGRU = RadiusGRU
        self.RangeGRU = RangeGRU
        self.CastTime = CastTime
        self.Cooldown = Cooldown
        self.CheckVisibility = CheckVisibility
        self.AllowReflexDuringCast = AllowReflexDuringCast
        self.CanBeCastFromTransport = CanBeCastFromTransport
        self.TargetEffect = TargetEffect
        self.TargetEffectDuration = TargetEffectDuration
        self.SelfEffectDuration = SelfEffectDuration
        self.MinVirtualUnits = MinVirtualUnits
        self.OrderMustSpreadTargets = OrderMustSpreadTargets
        self.MaxTargetNb = MaxTargetNb
        self.MultiplyCost = MultiplyCost
        self.TargetInBuilding = TargetInBuilding
        self.TargetInTransport = TargetInTransport
        self.TargetInSelf = TargetInSelf
        self.TargetMySelf = TargetMySelf
        self.FeedbackActivationMask = FeedbackActivationMask
        self.DisplayRangeColor = DisplayRangeColor
        self.DisplayRangeThickness = DisplayRangeThickness
        self.Price = Price
        self.TagsCiblePossible = TagsCiblePossible
        self.TagsCibleExcluded = TagsCibleExcluded
        self.Conditions = Conditions
        self.SelfEffect = SelfEffect


class TEffectsPackDescriptor(BaseDescription):
    def __init__(self, DescriptorId=None, NameForDebug=None, EffectsDescriptors=None):
        self.DescriptorId = DescriptorId
        self.NameForDebug = NameForDebug
        self.EffectsDescriptors = EffectsDescriptors


class TUnitEffectIncreaseWeaponDispersionMaxRangeDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue


class TUnitEffectRaiseTagDescriptor(BaseDescription):
    def __init__(self, TagListToRaise=None):
        self.TagListToRaise = TagListToRaise


class TUnitEffectShowLabelIconDescriptor(BaseDescription):
    def __init__(self, TextureToken=None):
        self.TextureToken = TextureToken


class TUnitEffectIncreaseDamageTakenDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusDamage=None, DamageType=None):
        self.ModifierType = ModifierType
        self.BonusDamage = BonusDamage
        self.DamageType = DamageType


class TStrategicSupplyMalusEffectDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, SupplyMalus=None):
        self.ModifierType = ModifierType
        self.SupplyMalus = SupplyMalus


class TUnitEffectIncreaseInfluenceValueDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, Bonus=None):
        self.ModifierType = ModifierType
        self.Bonus = Bonus


class TUnitEffectIncreaseWeaponPorteeMaxDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None, ModifierValueGRU=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue
        self.ModifierValueGRU = ModifierValueGRU


class TUnitEffectIncreaseWeaponPorteeMaxHADescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None, ModifierValueGRU=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue
        self.ModifierValueGRU = ModifierValueGRU


class TUnitEffectIncreaseWeaponPorteeMaxProjectileDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None, ModifierValueGRU=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue
        self.ModifierValueGRU = ModifierValueGRU


class TUnitEffectIncreaseWeaponPorteeMaxTBADescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None, ModifierValueGRU=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue
        self.ModifierValueGRU = ModifierValueGRU


class TUnitEffectIncreaseDispersionDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusDispersion=None):
        self.ModifierType = ModifierType
        self.BonusDispersion = BonusDispersion


class TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue


class TUnitEffectAlterWeaponTempsEntreDeuxTirsDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue


class TUnitEffectIncreaseChassisRotationSpeedDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusChassisRotationSpeed=None):
        self.ModifierType = ModifierType
        self.BonusChassisRotationSpeed = BonusChassisRotationSpeed


class TUnitEffectIncreaseTurretRotationSpeedDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusTurretRotationSpeed=None):
        self.ModifierType = ModifierType
        self.BonusTurretRotationSpeed = BonusTurretRotationSpeed


class TUnitEffectIncreaseSpeedDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusSpeedBaseInPercent=None):
        self.ModifierType = ModifierType
        self.BonusSpeedBaseInPercent = BonusSpeedBaseInPercent


class TBonusWeaponAimtimeEffectDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue


class TUnitEffectBonusExperienceLevelDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ExperienceLevelModifier=None):
        self.ModifierType = ModifierType
        self.ExperienceLevelModifier = ExperienceLevelModifier


class TUnitEffectIncreaseDangerousnessDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusDangerousness=None):
        self.ModifierType = ModifierType
        self.BonusDangerousness = BonusDangerousness


class TUnitEffectTransportSlotNumberModificationDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, EffectOnTransportSlotNumber=None):
        self.ModifierType = ModifierType
        self.EffectOnTransportSlotNumber = EffectOnTransportSlotNumber


class TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue


class TUnitEffectIncreaseVisionDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusVisionBase=None):
        self.ModifierType = ModifierType
        self.BonusVisionBase = BonusVisionBase


class TUnitEffectIncreaseSpecializedDetectionDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, VisionType=None, BonusValue=None, BonusValueGRU=None):
        self.ModifierType = ModifierType
        self.VisionType = VisionType
        self.BonusValue = BonusValue
        self.BonusValueGRU = BonusValueGRU


class TUnitEffectIncreaseInfluenceValueMinDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, Bonus=None):
        self.ModifierType = ModifierType
        self.Bonus = Bonus


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
    def __init__(self, ModifierType=None, PhysicalDamageValue=None):
        self.ModifierType = ModifierType
        self.PhysicalDamageValue = PhysicalDamageValue


class TUnitEffectIncreaseWeaponPrecisionArretDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue


class TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue


class TUnitEffectRemoveUnitDescriptor(BaseDescription):
    def __init__(self):
        pass


class TKillUnitEffectDescriptor(BaseDescription):
    def __init__(self):
        pass


class TEffectInflictSuppressDamageDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, SuppressDamageValue=None):
        self.ModifierType = ModifierType
        self.SuppressDamageValue = SuppressDamageValue


class TUnitEffectBonusPrecisionWhenTargetedDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusPrecisionWhenTargeted=None):
        self.ModifierType = ModifierType
        self.BonusPrecisionWhenTargeted = BonusPrecisionWhenTargeted


class TUnitEffectIncreaseOpticalStrengthDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusOpticalStrength=None):
        self.ModifierType = ModifierType
        self.BonusOpticalStrength = BonusOpticalStrength


class TUnitEffectIncreaseWeaponPorteeMaxIgnoreSmokeDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusWeaponPorteeMax=None):
        self.ModifierType = ModifierType
        self.BonusWeaponPorteeMax = BonusWeaponPorteeMax


class TResistanceTypeRTTI(BaseDescription):
    def __init__(self, Family=None, Index=None):
        self.Family = Family
        self.Index = Index


class TUnitEffectReplaceArmorDescriptor(BaseDescription):
    def __init__(self, ReplacementBlindage=None, BlindageLocation=None):
        self.ReplacementBlindage = ReplacementBlindage
        self.BlindageLocation = BlindageLocation


class TUnitEffectIncreaseConcealmentBonusDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusConcealmentBonus=None):
        self.ModifierType = ModifierType
        self.BonusConcealmentBonus = BonusConcealmentBonus


class TUnitEffectHealOverTimeDescriptor(BaseDescription):
    def __init__(self, NbUpdatePerSecond=None, HealUnitsPerSecond=None, DamageType=None):
        self.NbUpdatePerSecond = NbUpdatePerSecond
        self.HealUnitsPerSecond = HealUnitsPerSecond
        self.DamageType = DamageType


class TTeamIdentifierForUnitEffect(BaseDescription):
    def __init__(self, TeamType=None, TeamNumber=None):
        self.TeamType = TeamType
        self.TeamNumber = TeamNumber


class TUnitEffectChangeTeamDescriptor(BaseDescription):
    def __init__(self, FutureTeam=None):
        self.FutureTeam = FutureTeam


class TUnitEffectAddCapacityDescriptor(BaseDescription):
    def __init__(self, CapacityToAdd=None):
        self.CapacityToAdd = CapacityToAdd


class TEvacAirplaneEffectDescriptor(BaseDescription):
    def __init__(self):
        pass


class TDamageTypeRTTI(BaseDescription):
    def __init__(self, Family=None, Index=None):
        self.Family = Family
        self.Index = Index


class TDiceHitRollRuleDescriptor(BaseDescription):
    def __init__(self, DescriptorId=None, BaseCriticModifier=None, BaseHitValueModifiers=None, DistanceToTarget=None):
        self.DescriptorId = DescriptorId
        self.BaseCriticModifier = BaseCriticModifier
        self.BaseHitValueModifiers = BaseHitValueModifiers
        self.DistanceToTarget = DistanceToTarget


class TAmmunitionDescriptor(BaseDescription):
    def __init__(self, DescriptorId=None, Name=None, TypeCategoryName=None, Caliber=None, WeaponDescriptionToken=None, TraitsToken=None, WeaponCursorType=None, MinMaxCategory=None, Arme=None, ProjectileType=None, ImpactHappening=None, FxPower=None, TempsEntreDeuxTirs=None, TempsEntreDeuxFx=None, PorteeMaximaleGRU=None, PorteeMinimaleGRU=None, AffecteParNombre=None, AngleDispersion=None, DispersionAtMaxRangeGRU=None, DispersionAtMinRangeGRU=None, DispersionWithoutSorting=None, CorrectedShotAimtimeMultiplier=None, RadiusSplashPhysicalDamagesGRU=None, PhysicalDamages=None, ShowDamageInUI=None, RadiusSplashSuppressDamagesGRU=None, SuppressDamages=None, AllowSuppressDamageWhenNoImpact=None, DisplaySalveAccuracy=None, TirIndirect=None, TirReflexe=None, InterdireTirReflexe=None, MaximalSpeedGRU=None, ShotWithoutPhysics=None, FluidFriction=None, NoiseDissimulationMalus=None, ShotsBeforeMaxNoise=None, TargetOnlyOneUnitInDistrict=None, HitRollRuleDescriptor=None, MaxSuccessiveHitCount=None, TempsDeVisee=None, TempsEntreDeuxSalves=None, TempsEntreDeuxSalves_Min=None, TempsEntreDeuxSalves_Max=None, NbTirParSalves=None, SupplyCost=None, NbSalvosShootOnPosition=None, CanShootOnPosition=None, CanShootWhileMoving=None, NbrProjectilesSimultanes=None, AffichageMunitionParSalve=None, InterfaceWeaponTexture=None, SmokeDescriptor=None, FireDescriptor=None, TargetUnitCenter=None, CanHarmAirplanes=None, IsHarmlessForAllies=None, PiercingWeapon=None, TandemCharge=None, FlightTimeForSpeed=None, DistanceForSpeedGRU=None, DamageTypeEvolutionOverRangeDescriptor=None, PorteeMaximaleTBAGRU=None, FireTriggeringProbability=None, AltitudeAPorteeMinimaleGRU=None, AltitudeAPorteeMaximaleGRU=None, IgnoreInflammabilityConditions=None, IsSubAmmunition=None, ForceHitTopArmor=None, PorteeMinimaleTBAGRU=None, PorteeMinimaleHAGRU=None, PorteeMaximaleHAGRU=None, Guidance=None, CorrectedShotDispersionMultiplier=None, MaxAccelerationGRU=None, IsFireAndForget=None, MissileTimeBetweenCorrections=None, MissileDescriptor=None):
        self.DescriptorId = DescriptorId
        self.Name = Name
        self.TypeCategoryName = TypeCategoryName
        self.Caliber = Caliber
        self.WeaponDescriptionToken = WeaponDescriptionToken
        self.TraitsToken = TraitsToken
        self.WeaponCursorType = WeaponCursorType
        self.MinMaxCategory = MinMaxCategory
        self.Arme = Arme
        self.ProjectileType = ProjectileType
        self.ImpactHappening = ImpactHappening
        self.FxPower = FxPower
        self.TempsEntreDeuxTirs = TempsEntreDeuxTirs
        self.TempsEntreDeuxFx = TempsEntreDeuxFx
        self.PorteeMaximaleGRU = PorteeMaximaleGRU
        self.PorteeMinimaleGRU = PorteeMinimaleGRU
        self.AffecteParNombre = AffecteParNombre
        self.AngleDispersion = AngleDispersion
        self.DispersionAtMaxRangeGRU = DispersionAtMaxRangeGRU
        self.DispersionAtMinRangeGRU = DispersionAtMinRangeGRU
        self.DispersionWithoutSorting = DispersionWithoutSorting
        self.CorrectedShotAimtimeMultiplier = CorrectedShotAimtimeMultiplier
        self.RadiusSplashPhysicalDamagesGRU = RadiusSplashPhysicalDamagesGRU
        self.PhysicalDamages = PhysicalDamages
        self.ShowDamageInUI = ShowDamageInUI
        self.RadiusSplashSuppressDamagesGRU = RadiusSplashSuppressDamagesGRU
        self.SuppressDamages = SuppressDamages
        self.AllowSuppressDamageWhenNoImpact = AllowSuppressDamageWhenNoImpact
        self.DisplaySalveAccuracy = DisplaySalveAccuracy
        self.TirIndirect = TirIndirect
        self.TirReflexe = TirReflexe
        self.InterdireTirReflexe = InterdireTirReflexe
        self.MaximalSpeedGRU = MaximalSpeedGRU
        self.ShotWithoutPhysics = ShotWithoutPhysics
        self.FluidFriction = FluidFriction
        self.NoiseDissimulationMalus = NoiseDissimulationMalus
        self.ShotsBeforeMaxNoise = ShotsBeforeMaxNoise
        self.TargetOnlyOneUnitInDistrict = TargetOnlyOneUnitInDistrict
        self.HitRollRuleDescriptor = HitRollRuleDescriptor
        self.MaxSuccessiveHitCount = MaxSuccessiveHitCount
        self.TempsDeVisee = TempsDeVisee
        self.TempsEntreDeuxSalves = TempsEntreDeuxSalves
        self.TempsEntreDeuxSalves_Min = TempsEntreDeuxSalves_Min
        self.TempsEntreDeuxSalves_Max = TempsEntreDeuxSalves_Max
        self.NbTirParSalves = NbTirParSalves
        self.SupplyCost = SupplyCost
        self.NbSalvosShootOnPosition = NbSalvosShootOnPosition
        self.CanShootOnPosition = CanShootOnPosition
        self.CanShootWhileMoving = CanShootWhileMoving
        self.NbrProjectilesSimultanes = NbrProjectilesSimultanes
        self.AffichageMunitionParSalve = AffichageMunitionParSalve
        self.InterfaceWeaponTexture = InterfaceWeaponTexture
        self.SmokeDescriptor = SmokeDescriptor
        self.FireDescriptor = FireDescriptor
        self.TargetUnitCenter = TargetUnitCenter
        self.CanHarmAirplanes = CanHarmAirplanes
        self.IsHarmlessForAllies = IsHarmlessForAllies
        self.PiercingWeapon = PiercingWeapon
        self.TandemCharge = TandemCharge
        self.FlightTimeForSpeed = FlightTimeForSpeed
        self.DistanceForSpeedGRU = DistanceForSpeedGRU
        self.DamageTypeEvolutionOverRangeDescriptor = DamageTypeEvolutionOverRangeDescriptor
        self.PorteeMaximaleTBAGRU = PorteeMaximaleTBAGRU
        self.FireTriggeringProbability = FireTriggeringProbability
        self.AltitudeAPorteeMinimaleGRU = AltitudeAPorteeMinimaleGRU
        self.AltitudeAPorteeMaximaleGRU = AltitudeAPorteeMaximaleGRU
        self.IgnoreInflammabilityConditions = IgnoreInflammabilityConditions
        self.IsSubAmmunition = IsSubAmmunition
        self.ForceHitTopArmor = ForceHitTopArmor
        self.PorteeMinimaleTBAGRU = PorteeMinimaleTBAGRU
        self.PorteeMinimaleHAGRU = PorteeMinimaleHAGRU
        self.PorteeMaximaleHAGRU = PorteeMaximaleHAGRU
        self.Guidance = Guidance
        self.CorrectedShotDispersionMultiplier = CorrectedShotDispersionMultiplier
        self.MaxAccelerationGRU = MaxAccelerationGRU
        self.IsFireAndForget = IsFireAndForget
        self.MissileTimeBetweenCorrections = MissileTimeBetweenCorrections
        self.MissileDescriptor = MissileDescriptor


class TMountedWeaponDescriptor(BaseDescription):
    def __init__(self, AmmoConsumption_ForInterface=None, Ammunition=None, AnimateOnlyOneSoldier=None, DispersionRadiusOffColor=None, DispersionRadiusOffThickness=None, DispersionRadiusOnColor=None, DispersionRadiusOnThickness=None, EffectTag=None, HandheldEquipmentKey=None, NbWeapons=None, SalvoStockIndex=None, ShowDispersion=None, ShowInInterface=None, WeaponActiveAndCanShootPropertyName=None, WeaponIgnoredPropertyName=None, WeaponShootDataPropertyName=None, TirContinu=None):
        self.AmmoConsumption_ForInterface = AmmoConsumption_ForInterface
        self.Ammunition = Ammunition
        self.AnimateOnlyOneSoldier = AnimateOnlyOneSoldier
        self.DispersionRadiusOffColor = DispersionRadiusOffColor
        self.DispersionRadiusOffThickness = DispersionRadiusOffThickness
        self.DispersionRadiusOnColor = DispersionRadiusOnColor
        self.DispersionRadiusOnThickness = DispersionRadiusOnThickness
        self.EffectTag = EffectTag
        self.HandheldEquipmentKey = HandheldEquipmentKey
        self.NbWeapons = NbWeapons
        self.SalvoStockIndex = SalvoStockIndex
        self.ShowDispersion = ShowDispersion
        self.ShowInInterface = ShowInInterface
        self.WeaponActiveAndCanShootPropertyName = WeaponActiveAndCanShootPropertyName
        self.WeaponIgnoredPropertyName = WeaponIgnoredPropertyName
        self.WeaponShootDataPropertyName = WeaponShootDataPropertyName
        self.TirContinu = TirContinu


class TTurretTwoAxisDescriptor(BaseDescription):
    def __init__(self, AngleRotationBase=None, AngleRotationBasePitch=None, AngleRotationMax=None, AngleRotationMaxPitch=None, AngleRotationMinPitch=None, MountedWeaponDescriptorList=None, OutOfRangeTrackingDuration=None, Tag=None, TurretIdleBehaviourDescriptor=None, VitesseRotation=None, YulBoneOrdinal=None, AimingPriority=None, MasterTurretYulBoneOrdinal=None):
        self.AngleRotationBase = AngleRotationBase
        self.AngleRotationBasePitch = AngleRotationBasePitch
        self.AngleRotationMax = AngleRotationMax
        self.AngleRotationMaxPitch = AngleRotationMaxPitch
        self.AngleRotationMinPitch = AngleRotationMinPitch
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.OutOfRangeTrackingDuration = OutOfRangeTrackingDuration
        self.Tag = Tag
        self.TurretIdleBehaviourDescriptor = TurretIdleBehaviourDescriptor
        self.VitesseRotation = VitesseRotation
        self.YulBoneOrdinal = YulBoneOrdinal
        self.AimingPriority = AimingPriority
        self.MasterTurretYulBoneOrdinal = MasterTurretYulBoneOrdinal


class TWeaponManagerModuleDescriptor(BaseDescription):
    def __init__(self, Salves=None, AlwaysOrientArmorTowardsThreat=None, TurretDescriptorList=None, SalvoIsMainSalvo=None):
        self.Salves = Salves
        self.AlwaysOrientArmorTowardsThreat = AlwaysOrientArmorTowardsThreat
        self.TurretDescriptorList = TurretDescriptorList
        self.SalvoIsMainSalvo = SalvoIsMainSalvo


class TTurretUnitDescriptor(BaseDescription):
    def __init__(self, AngleRotationMax=None, AngleRotationMaxPitch=None, AngleRotationMinPitch=None, MountedWeaponDescriptorList=None, Tag=None, YulBoneOrdinal=None, AimingPriority=None):
        self.AngleRotationMax = AngleRotationMax
        self.AngleRotationMaxPitch = AngleRotationMaxPitch
        self.AngleRotationMinPitch = AngleRotationMinPitch
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.Tag = Tag
        self.YulBoneOrdinal = YulBoneOrdinal
        self.AimingPriority = AimingPriority


class TTurretInfanterieDescriptor(BaseDescription):
    def __init__(self, MountedWeaponDescriptorList=None, YulBoneOrdinal=None):
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.YulBoneOrdinal = YulBoneOrdinal


class TTurretBombardierDescriptor(BaseDescription):
    def __init__(self, FlyingAltitudeGRU=None, FlyingSpeedInKmph=None, MountedWeaponDescriptorList=None, Tag=None, YulBoneOrdinal=None):
        self.FlyingAltitudeGRU = FlyingAltitudeGRU
        self.FlyingSpeedInKmph = FlyingSpeedInKmph
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.Tag = Tag
        self.YulBoneOrdinal = YulBoneOrdinal


class TTypeUnitModuleDescriptor(BaseDescription):
    def __init__(self, Nationalite=None, MotherCountry=None, AcknowUnitType=None, TypeUnitFormation=None):
        self.Nationalite = Nationalite
        self.MotherCountry = MotherCountry
        self.AcknowUnitType = AcknowUnitType
        self.TypeUnitFormation = TypeUnitFormation


class TemplateUnitCriticalModule(BaseDescription):
    def __init__(self, Module=None):
        self.Module = Module


class TTagsModuleDescriptor(BaseDescription):
    def __init__(self, TagSet=None):
        self.TagSet = TagSet


class TExperienceModuleDescriptor(BaseDescription):
    def __init__(self, ExperienceLevelsPackDescriptor=None, CanWinExperience=None, ExperienceGainBySecond=None, ExperienceMultiplierBonusOnKill=None):
        self.ExperienceLevelsPackDescriptor = ExperienceLevelsPackDescriptor
        self.CanWinExperience = CanWinExperience
        self.ExperienceGainBySecond = ExperienceGainBySecond
        self.ExperienceMultiplierBonusOnKill = ExperienceMultiplierBonusOnKill


class TVisibilityModuleDescriptor(BaseDescription):
    def __init__(self, UnitConcealmentBonus=None, VisionUnitType=None):
        self.UnitConcealmentBonus = UnitConcealmentBonus
        self.VisionUnitType = VisionUnitType


class VehicleApparenceModelModuleDescriptor(BaseDescription):
    def __init__(self, Depiction=None, BlackHoleIdentifier=None, GameplayBBoxBoneName=None, ReferenceMesh=None):
        self.Depiction = Depiction
        self.BlackHoleIdentifier = BlackHoleIdentifier
        self.GameplayBBoxBoneName = GameplayBBoxBoneName
        self.ReferenceMesh = ReferenceMesh


class TAutoCoverModuleDescriptor(BaseDescription):
    def __init__(self, AutoCoverRangeGRU=None, OccupationRadiusGRU=None, TerrainListMask=None, TerrainList=None, UseTerrainsForEscape=None):
        self.AutoCoverRangeGRU = AutoCoverRangeGRU
        self.OccupationRadiusGRU = OccupationRadiusGRU
        self.TerrainListMask = TerrainListMask
        self.TerrainList = TerrainList
        self.UseTerrainsForEscape = UseTerrainsForEscape


class TModuleSelector(BaseDescription):
    def __init__(self, Default=None, Selection=None):
        self.Default = Default
        self.Selection = Selection


class TBaseDamageModuleDescriptor(BaseDescription):
    def __init__(self, MaxPhysicalDamages=None, MaxSuppressionDamages=None, MaxStunDamages=None, PhysicalDamageLevelsPack=None, SuppressDamageLevelsPack=None, StunDamageLevelsPack=None):
        self.MaxPhysicalDamages = MaxPhysicalDamages
        self.MaxSuppressionDamages = MaxSuppressionDamages
        self.MaxStunDamages = MaxStunDamages
        self.PhysicalDamageLevelsPack = PhysicalDamageLevelsPack
        self.SuppressDamageLevelsPack = SuppressDamageLevelsPack
        self.StunDamageLevelsPack = StunDamageLevelsPack


class TBlindageProperties(BaseDescription):
    def __init__(self, ResistanceFront=None, ResistanceSides=None, ResistanceRear=None, ResistanceTop=None, ExplosiveReactiveArmor=None):
        self.ResistanceFront = ResistanceFront
        self.ResistanceSides = ResistanceSides
        self.ResistanceRear = ResistanceRear
        self.ResistanceTop = ResistanceTop
        self.ExplosiveReactiveArmor = ExplosiveReactiveArmor


class TDamageModuleDescriptor(BaseDescription):
    def __init__(self, SuppressDamagesRegenRatio=None, StunDamagesRegen=None, BlindageProperties=None, KillWhenDamagesReachMax=None, HitRollECM=None, AutoOrientation=None, UseTopArmorAgainstFire=None):
        self.SuppressDamagesRegenRatio = SuppressDamagesRegenRatio
        self.StunDamagesRegen = StunDamagesRegen
        self.BlindageProperties = BlindageProperties
        self.KillWhenDamagesReachMax = KillWhenDamagesReachMax
        self.HitRollECM = HitRollECM
        self.AutoOrientation = AutoOrientation
        self.UseTopArmorAgainstFire = UseTopArmorAgainstFire


class TDangerousnessModuleDescriptor(BaseDescription):
    def __init__(self, Dangerousness=None):
        self.Dangerousness = Dangerousness


class TRoutModuleDescriptor(BaseDescription):
    def __init__(self, MoralLevel=None):
        self.MoralLevel = MoralLevel


class TGenericMovementModuleDescriptor(BaseDescription):
    def __init__(self, MaxSpeedInKmph=None, PathfindType=None):
        self.MaxSpeedInKmph = MaxSpeedInKmph
        self.PathfindType = PathfindType


class TLandMovementModuleDescriptor(BaseDescription):
    def __init__(self, UnitMovingType=None, SpeedBonusFactorOnRoad=None, MaxAccelerationGRU=None, MaxDecelerationGRU=None, TempsDemiTour=None, StartTime=None, StopTime=None, RotationStartTime=None, RotationStopTime=None, VehicleSizeInMeter=None):
        self.UnitMovingType = UnitMovingType
        self.SpeedBonusFactorOnRoad = SpeedBonusFactorOnRoad
        self.MaxAccelerationGRU = MaxAccelerationGRU
        self.MaxDecelerationGRU = MaxDecelerationGRU
        self.TempsDemiTour = TempsDemiTour
        self.StartTime = StartTime
        self.StopTime = StopTime
        self.RotationStartTime = RotationStartTime
        self.RotationStopTime = RotationStopTime
        self.VehicleSizeInMeter = VehicleSizeInMeter


class TFuelModuleDescriptor(BaseDescription):
    def __init__(self, FuelCapacity=None, FuelMoveDuration=None):
        self.FuelCapacity = FuelCapacity
        self.FuelMoveDuration = FuelMoveDuration


class TScannerConfigurationDescriptor(BaseDescription):
    def __init__(self, OpticsAltitudeConfig=None, PorteeVisionTBAGRU=None, PorteeVisionFOWGRU=None, DetectionTBAGRU=None, PorteeVisionGRU=None, PorteeIdentification=None, OpticalStrength=None, OpticalStrengthAltitude=None, SpecializedDetectionsGRU=None, SpecializedOpticalStrengths=None):
        self.OpticsAltitudeConfig = OpticsAltitudeConfig
        self.PorteeVisionTBAGRU = PorteeVisionTBAGRU
        self.PorteeVisionFOWGRU = PorteeVisionFOWGRU
        self.DetectionTBAGRU = DetectionTBAGRU
        self.PorteeVisionGRU = PorteeVisionGRU
        self.PorteeIdentification = PorteeIdentification
        self.OpticalStrength = OpticalStrength
        self.OpticalStrengthAltitude = OpticalStrengthAltitude
        self.SpecializedDetectionsGRU = SpecializedDetectionsGRU
        self.SpecializedOpticalStrengths = SpecializedOpticalStrengths


class TModernWarfareVisibilityRollRule(BaseDescription):
    def __init__(self, IdentifyBaseProbability=None, TimeBetweenEachIdentifyRoll=None, VisibilityRuleDescriptor=None):
        self.IdentifyBaseProbability = IdentifyBaseProbability
        self.TimeBetweenEachIdentifyRoll = TimeBetweenEachIdentifyRoll
        self.VisibilityRuleDescriptor = VisibilityRuleDescriptor


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
    def __init__(self, DatabaseId=None, GameplayBehavior=None):
        self.DatabaseId = DatabaseId
        self.GameplayBehavior = GameplayBehavior


class TProductionModuleDescriptor(BaseDescription):
    def __init__(self, Factory=None, ProductionTime=None, ProductionRessourcesNeeded=None):
        self.Factory = Factory
        self.ProductionTime = ProductionTime
        self.ProductionRessourcesNeeded = ProductionRessourcesNeeded


class TAutomaticBehaviorModuleDescriptor(BaseDescription):
    def __init__(self, CanAssist=None, AssistRequestBroadcastRadiusGRU=None, DistanceToFleeGRU=None, MaxDistanceForOffensiveReactionGRU=None, MaxDistanceForEngagementGRU=None, SearchedTagsInEngagementTarget=None):
        self.CanAssist = CanAssist
        self.AssistRequestBroadcastRadiusGRU = AssistRequestBroadcastRadiusGRU
        self.DistanceToFleeGRU = DistanceToFleeGRU
        self.MaxDistanceForOffensiveReactionGRU = MaxDistanceForOffensiveReactionGRU
        self.MaxDistanceForEngagementGRU = MaxDistanceForEngagementGRU
        self.SearchedTagsInEngagementTarget = SearchedTagsInEngagementTarget


class TCubeActionModuleDescriptor(BaseDescription):
    def __init__(self, CubeActionDescriptor=None):
        self.CubeActionDescriptor = CubeActionDescriptor


class TMinimapDisplayModuleDescriptor(BaseDescription):
    def __init__(self, Texture=None, FollowUnitOrientation=None):
        self.Texture = Texture
        self.FollowUnitOrientation = FollowUnitOrientation


class TOrderConfigModuleDescriptor(BaseDescription):
    def __init__(self, ValidOrders=None):
        self.ValidOrders = ValidOrders


class TOrderableModuleDescriptor(BaseDescription):
    def __init__(self, UnlockableOrders=None):
        self.UnlockableOrders = UnlockableOrders


class TBUCKToolAlternativeValues_TUIValueTextureNameFromTEugBMutableInteger(BaseDescription):
    def __init__(self, CommandNameTrigger=None, Alterator=None, Values=None):
        self.CommandNameTrigger = CommandNameTrigger
        self.Alterator = Alterator
        self.Values = Values


class TTacticalLabelModuleDescriptor(BaseDescription):
    def __init__(self, MultiSelectionSortingOrder=None, IdentifiedTexture=None, UnidentifiedTexture=None, PositionHeightOffset=None, NbSoldiers=None):
        self.MultiSelectionSortingOrder = MultiSelectionSortingOrder
        self.IdentifiedTexture = IdentifiedTexture
        self.UnidentifiedTexture = UnidentifiedTexture
        self.PositionHeightOffset = PositionHeightOffset
        self.NbSoldiers = NbSoldiers


class TStrategicDataModuleDescriptor(BaseDescription):
    def __init__(self, UnitAttackValue=None, UnitDefenseValue=None, UnitBonusXpPerLevelValue=None):
        self.UnitAttackValue = UnitAttackValue
        self.UnitDefenseValue = UnitDefenseValue
        self.UnitBonusXpPerLevelValue = UnitBonusXpPerLevelValue


class TUnitUIModuleDescriptor(BaseDescription):
    def __init__(self, UnitRole=None, SpecialtiesList=None, NameToken=None, InfoPanelConfigurationToken=None, DisplayRoadSpeedInKmph=None, UpgradeFromUnit=None, GenerateName=None, MenuIconTexture=None, ButtonTexture=None, CountryTexture=None, TypeStrategicCount=None):
        self.UnitRole = UnitRole
        self.SpecialtiesList = SpecialtiesList
        self.NameToken = NameToken
        self.InfoPanelConfigurationToken = InfoPanelConfigurationToken
        self.DisplayRoadSpeedInKmph = DisplayRoadSpeedInKmph
        self.UpgradeFromUnit = UpgradeFromUnit
        self.GenerateName = GenerateName
        self.MenuIconTexture = MenuIconTexture
        self.ButtonTexture = ButtonTexture
        self.CountryTexture = CountryTexture
        self.TypeStrategicCount = TypeStrategicCount


class TUnitUpkeepModuleDescriptor(BaseDescription):
    def __init__(self, UpkeepPercentage=None):
        self.UpkeepPercentage = UpkeepPercentage


class TVisualShootPositionsModuleDescriptor(BaseDescription):
    def __init__(self):
        pass


class TEntityDescriptor(BaseDescription):
    def __init__(self, DescriptorId=None, ClassNameForDebug=None, ModulesDescriptors=None):
        self.DescriptorId = DescriptorId
        self.ClassNameForDebug = ClassNameForDebug
        self.ModulesDescriptors = ModulesDescriptors


class TTransportableModuleDescriptor(BaseDescription):
    def __init__(self, TransportedTexture=None, TransportedSoldier=None, NbSeatsOccupied=None, TimeToLoad=None, IsTowable=None):
        self.TransportedTexture = TransportedTexture
        self.TransportedSoldier = TransportedSoldier
        self.NbSeatsOccupied = NbSeatsOccupied
        self.TimeToLoad = TimeToLoad
        self.IsTowable = IsTowable


class TCapaciteModuleDescriptor(BaseDescription):
    def __init__(self, DefaultSkillList=None):
        self.DefaultSkillList = DefaultSkillList


class TDeploymentShiftModuleDescriptor(BaseDescription):
    def __init__(self, DeploymentShiftGRU=None):
        self.DeploymentShiftGRU = DeploymentShiftGRU


class TTransporterModuleDescriptor(BaseDescription):
    def __init__(self, TransportableTagSet=None, NbSeatsAvailable=None, WreckUnloadPhysicalDamageBonus=None, WreckUnloadSuppressDamageBonus=None, WreckUnloadStunDamageBonus=None, LoadRadiusGRU=None):
        self.TransportableTagSet = TransportableTagSet
        self.NbSeatsAvailable = NbSeatsAvailable
        self.WreckUnloadPhysicalDamageBonus = WreckUnloadPhysicalDamageBonus
        self.WreckUnloadSuppressDamageBonus = WreckUnloadSuppressDamageBonus
        self.WreckUnloadStunDamageBonus = WreckUnloadStunDamageBonus
        self.LoadRadiusGRU = LoadRadiusGRU


class TCommanderModuleDescriptor(BaseDescription):
    def __init__(self):
        pass


class TZoneInfluenceMapModuleDescriptor(BaseDescription):
    def __init__(self, InfluenceStrength=None, MinimumInfluenceStrength=None, StrengthDecayPerSecond=None, PreventsDecayInZone=None, IsEnabledByComportementAuto=None):
        self.InfluenceStrength = InfluenceStrength
        self.MinimumInfluenceStrength = MinimumInfluenceStrength
        self.StrengthDecayPerSecond = StrengthDecayPerSecond
        self.PreventsDecayInZone = PreventsDecayInZone
        self.IsEnabledByComportementAuto = IsEnabledByComportementAuto


class TInfluenceScoutModuleDescriptor(BaseDescription):
    def __init__(self):
        pass


class InfantryApparenceModelModuleDescriptor(BaseDescription):
    def __init__(self, Depiction=None):
        self.Depiction = Depiction


class Descriptor_Unit_MimeticUnit(BaseDescription):
    def __init__(self, DescriptorId=None, MimeticName=None):
        self.DescriptorId = DescriptorId
        self.MimeticName = MimeticName


class TInfantrySquadModuleDescriptor(BaseDescription):
    def __init__(self, NbSoldatInGroupeCombat=None, SquadDataDescriptor=None, InfantryMimeticName=None, WeaponUnitFXKey=None, MimeticDescriptor=None):
        self.NbSoldatInGroupeCombat = NbSoldatInGroupeCombat
        self.SquadDataDescriptor = SquadDataDescriptor
        self.InfantryMimeticName = InfantryMimeticName
        self.WeaponUnitFXKey = WeaponUnitFXKey
        self.MimeticDescriptor = MimeticDescriptor


class TInfantrySquadWeaponAssignmentModuleDescriptor(BaseDescription):
    def __init__(self, InitialSoldiersToTurretIndexMap=None):
        self.InitialSoldiersToTurretIndexMap = InitialSoldiersToTurretIndexMap


class TLinkToDistrictModuleDescriptor(BaseDescription):
    def __init__(self):
        pass


class TSupplyModuleDescriptor(BaseDescription):
    def __init__(self, SupplyDescriptor=None, SupplyCapacity=None, SupplyPriority=None):
        self.SupplyDescriptor = SupplyDescriptor
        self.SupplyCapacity = SupplyCapacity
        self.SupplyPriority = SupplyPriority


class TSellModuleDescriptor(BaseDescription):
    def __init__(self):
        pass


class HelicopterPositionModuleDescriptor(BaseDescription):
    def __init__(self, LowAltitudeFlyingAltitudeGRU=None, NearGroundFlyingAltitudeGRU=None):
        self.LowAltitudeFlyingAltitudeGRU = LowAltitudeFlyingAltitudeGRU
        self.NearGroundFlyingAltitudeGRU = NearGroundFlyingAltitudeGRU


class THelicopterMovementModuleDescriptor(BaseDescription):
    def __init__(self, MaxSpeedInKmph=None, WorldFloorProxy=None, UpwardSpeedInKmph=None, TorqueManoeuvrability=None, CyclicManoeuvrability=None, MaxInclination=None, GFactorLimit=None, RotorArea=None, Mass=None):
        self.MaxSpeedInKmph = MaxSpeedInKmph
        self.WorldFloorProxy = WorldFloorProxy
        self.UpwardSpeedInKmph = UpwardSpeedInKmph
        self.TorqueManoeuvrability = TorqueManoeuvrability
        self.CyclicManoeuvrability = CyclicManoeuvrability
        self.MaxInclination = MaxInclination
        self.GFactorLimit = GFactorLimit
        self.RotorArea = RotorArea
        self.Mass = Mass


class TFlareModuleDescriptor_MW(BaseDescription):
    def __init__(self, ProjectileSpeed=None, DistanceActivationGRU=None, TimeBetweenFlare=None, MinimalTimeBetweenFlare=None, BonusTimeBetweenFlareByProjectile=None):
        self.ProjectileSpeed = ProjectileSpeed
        self.DistanceActivationGRU = DistanceActivationGRU
        self.TimeBetweenFlare = TimeBetweenFlare
        self.MinimalTimeBetweenFlare = MinimalTimeBetweenFlare
        self.BonusTimeBetweenFlareByProjectile = BonusTimeBetweenFlareByProjectile


class AirplanePositionModuleDescriptor(BaseDescription):
    def __init__(self, LowAltitudeFlyingAltitudeGRU=None):
        self.LowAltitudeFlyingAltitudeGRU = LowAltitudeFlyingAltitudeGRU


class AirplaneMovementDescriptor(BaseDescription):
    def __init__(self, AltitudeGRU=None, AltitudeMinGRU=None, SpeedInKmph=None, AgilityRadiusGRU=None, PitchAngle=None, RollAngle=None, RollSpeed=None, EvacAngle=None, EvacToStartingPoint=None, OrderedAttackStrategies=None):
        self.AltitudeGRU = AltitudeGRU
        self.AltitudeMinGRU = AltitudeMinGRU
        self.SpeedInKmph = SpeedInKmph
        self.AgilityRadiusGRU = AgilityRadiusGRU
        self.PitchAngle = PitchAngle
        self.RollAngle = RollAngle
        self.RollSpeed = RollSpeed
        self.EvacAngle = EvacAngle
        self.EvacToStartingPoint = EvacToStartingPoint
        self.OrderedAttackStrategies = OrderedAttackStrategies


class TAirplaneModuleDescriptor(BaseDescription):
    def __init__(self, EvacuationTime=None, TravelDuration=None):
        self.EvacuationTime = EvacuationTime
        self.TravelDuration = TravelDuration


class TDeckDivisionDescriptor(BaseDescription):
    def __init__(self, DescriptorId=None, CfgName=None, DivisionName=None, DivisionPowerClassification=None, DivisionNationalite=None, DivisionTags=None, DescriptionHintTitleToken=None, PackList=None, MaxActivationPoints=None, CostMatrix=None, EmblemTexture=None, PortraitTexture=None, TypeTexture=None, CountryId=None, StrategicLabelColor=None):
        self.DescriptorId = DescriptorId
        self.CfgName = CfgName
        self.DivisionName = DivisionName
        self.DivisionPowerClassification = DivisionPowerClassification
        self.DivisionNationalite = DivisionNationalite
        self.DivisionTags = DivisionTags
        self.DescriptionHintTitleToken = DescriptionHintTitleToken
        self.PackList = PackList
        self.MaxActivationPoints = MaxActivationPoints
        self.CostMatrix = CostMatrix
        self.EmblemTexture = EmblemTexture
        self.PortraitTexture = PortraitTexture
        self.TypeTexture = TypeTexture
        self.CountryId = CountryId
        self.StrategicLabelColor = StrategicLabelColor


class DeckPackDescriptor(BaseDescription):
    def __init__(self, Unit=None):
        self.Unit = Unit


class TDeckUniteRule(BaseDescription):
    def __init__(self, UnitDescriptor=None, AvailableWithoutTransport=None, NumberOfUnitInPack=None, NumberOfUnitInPackXPMultiplier=None, AvailableTransportList=None):
        self.UnitDescriptor = UnitDescriptor
        self.AvailableWithoutTransport = AvailableWithoutTransport
        self.NumberOfUnitInPack = NumberOfUnitInPack
        self.NumberOfUnitInPackXPMultiplier = NumberOfUnitInPackXPMultiplier
        self.AvailableTransportList = AvailableTransportList


class TDeckDivisionRule(BaseDescription):
    def __init__(self, UnitRuleList=None):
        self.UnitRuleList = UnitRuleList


class TDeckDivisionRules(BaseDescription):
    def __init__(self, DivisionRules=None):
        self.DivisionRules = DivisionRules


class TDamageLevelDescriptor(BaseDescription):
    def __init__(self, DescriptorId=None, Value=None, LocalizationToken=None, MoralModifier=None, HitRollModifier=None, TextColor=None, AnimationType=None, EffectsPacks=None, NameForDebug=None, FeedbackOnSelf=None):
        self.DescriptorId = DescriptorId
        self.Value = Value
        self.LocalizationToken = LocalizationToken
        self.MoralModifier = MoralModifier
        self.HitRollModifier = HitRollModifier
        self.TextColor = TextColor
        self.AnimationType = AnimationType
        self.EffectsPacks = EffectsPacks
        self.NameForDebug = NameForDebug
        self.FeedbackOnSelf = FeedbackOnSelf


class TDamageLevelsPackDescriptor(BaseDescription):
    def __init__(self, DescriptorId=None, DamageLevelsDescriptors=None, NameForDebug=None):
        self.DescriptorId = DescriptorId
        self.DamageLevelsDescriptors = DamageLevelsDescriptors
        self.NameForDebug = NameForDebug


class TResistanceTypeFamilyDefinition(BaseDescription):
    def __init__(self, Family=None, MaxIndex=None):
        self.Family = Family
        self.MaxIndex = MaxIndex


class TDamageTypeFamilyDefinition(BaseDescription):
    def __init__(self, Family=None, MaxIndex=None):
        self.Family = Family
        self.MaxIndex = MaxIndex


class TGameplayDamageResistanceContainer(BaseDescription):
    def __init__(self, ResistanceFamilyDefinitionList=None, DamageFamilyDefinitionList=None, Values=None):
        self.ResistanceFamilyDefinitionList = ResistanceFamilyDefinitionList
        self.DamageFamilyDefinitionList = DamageFamilyDefinitionList
        self.Values = Values


class TResistanceFamilyList(BaseDescription):
    def __init__(self, Values=None):
        self.Values = Values


class TDamageFamilyList(BaseDescription):
    def __init__(self, Values=None):
        self.Values = Values


class TStairsDamageTypeEvolutionOverRangeDescriptor(BaseDescription):
    def __init__(self, DistanceGRU=None, AP=None):
        self.DistanceGRU = DistanceGRU
        self.AP = AP

class TGameplayTerrain(BaseDescription):
    def __init__(self, BloqueAmphibie=None, BloqueAtterrissage=None, BloqueInfanterie=None, BloqueVehicule=None, BloqueVision=None, CriticalEffectProbability=None, DebugColor=None, DissimulationModifierGroundAir=None, DissimulationModifierGroundGround=None, HeightInMeters=None, InflammabilityProbability=None, Name=None, SpeedModifierAllTerrainWheel=None, SpeedModifierInfantry=None, SpeedModifierTrack=None, ConcealmentBonus=None, TerrainType=None, WorldLayerActiveMask=None, AuthorizeNearGroundFlying=None, DamageModifierPerFamilyAndResistance=None):
        self.BloqueAmphibie = BloqueAmphibie
        self.BloqueAtterrissage = BloqueAtterrissage
        self.BloqueInfanterie = BloqueInfanterie
        self.BloqueVehicule = BloqueVehicule
        self.BloqueVision = BloqueVision
        self.CriticalEffectProbability = CriticalEffectProbability
        self.DebugColor = DebugColor
        self.DissimulationModifierGroundAir = DissimulationModifierGroundAir
        self.DissimulationModifierGroundGround = DissimulationModifierGroundGround
        self.HeightInMeters = HeightInMeters
        self.InflammabilityProbability = InflammabilityProbability
        self.Name = Name
        self.SpeedModifierAllTerrainWheel = SpeedModifierAllTerrainWheel
        self.SpeedModifierInfantry = SpeedModifierInfantry
        self.SpeedModifierTrack = SpeedModifierTrack
        self.ConcealmentBonus = ConcealmentBonus
        self.TerrainType = TerrainType
        self.WorldLayerActiveMask = WorldLayerActiveMask
        self.AuthorizeNearGroundFlying = AuthorizeNearGroundFlying
        self.DamageModifierPerFamilyAndResistance = DamageModifierPerFamilyAndResistance


###########

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

