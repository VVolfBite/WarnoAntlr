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
    def __init__(self, DescriptorId=None, Name=None, TypeCategoryName=None, Caliber=None, WeaponDescriptionToken=None, TraitsToken=None, WeaponCursorType=None, MinMaxCategory=None, Arme=None, ProjectileType=None, ImpactHappening=None, FxPower=None, TempsEntreDeuxTirs=None, TempsEntreDeuxFx=None, PorteeMaximaleHAGRU=None, AngleDispersion=None, DispersionWithoutSorting=None, CorrectedShotAimtimeMultiplier=None, RadiusSplashPhysicalDamagesGRU=None, PhysicalDamages=None, ShowDamageInUI=None, RadiusSplashSuppressDamagesGRU=None, SuppressDamages=None, AllowSuppressDamageWhenNoImpact=None, DisplaySalveAccuracy=None, TirIndirect=None, TirReflexe=None, InterdireTirReflexe=None, MaximalSpeedGRU=None, MaxAccelerationGRU=None, ShotWithoutPhysics=None, FluidFriction=None, NoiseDissimulationMalus=None, ShotsBeforeMaxNoise=None, IsFireAndForget=None, TargetOnlyOneUnitInDistrict=None, HitRollRuleDescriptor=None, TempsDeVisee=None, TempsEntreDeuxSalves=None, TempsEntreDeuxSalves_Min=None, TempsEntreDeuxSalves_Max=None, NbTirParSalves=None, SupplyCost=None, CanShootOnPosition=None, CanShootWhileMoving=None, NbrProjectilesSimultanes=None, AffichageMunitionParSalve=None, InterfaceWeaponTexture=None, SmokeDescriptor=None, FireDescriptor=None, TargetUnitCenter=None, CanHarmAirplanes=None, IsHarmlessForAllies=None, PiercingWeapon=None, TandemCharge=None, DamageTypeEvolutionOverRangeDescriptor=None, MissileTimeBetweenCorrections=None, MissileDescriptor=None, PorteeMaximaleTBAGRU=None, PorteeMaximaleGRU=None, PorteeMinimaleGRU=None, DispersionAtMaxRangeGRU=None, DispersionAtMinRangeGRU=None, MaxSuccessiveHitCount=None, Guidance=None, ForceHitTopArmor=None, NbSalvosShootOnPosition=None, PorteeMinimaleTBAGRU=None):
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
        self.PorteeMaximaleHAGRU = PorteeMaximaleHAGRU
        self.AngleDispersion = AngleDispersion
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
        self.MaxAccelerationGRU = MaxAccelerationGRU
        self.ShotWithoutPhysics = ShotWithoutPhysics
        self.FluidFriction = FluidFriction
        self.NoiseDissimulationMalus = NoiseDissimulationMalus
        self.ShotsBeforeMaxNoise = ShotsBeforeMaxNoise
        self.IsFireAndForget = IsFireAndForget
        self.TargetOnlyOneUnitInDistrict = TargetOnlyOneUnitInDistrict
        self.HitRollRuleDescriptor = HitRollRuleDescriptor
        self.TempsDeVisee = TempsDeVisee
        self.TempsEntreDeuxSalves = TempsEntreDeuxSalves
        self.TempsEntreDeuxSalves_Min = TempsEntreDeuxSalves_Min
        self.TempsEntreDeuxSalves_Max = TempsEntreDeuxSalves_Max
        self.NbTirParSalves = NbTirParSalves
        self.SupplyCost = SupplyCost
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
        self.DamageTypeEvolutionOverRangeDescriptor = DamageTypeEvolutionOverRangeDescriptor
        self.MissileTimeBetweenCorrections = MissileTimeBetweenCorrections
        self.MissileDescriptor = MissileDescriptor
        self.PorteeMaximaleTBAGRU = PorteeMaximaleTBAGRU
        self.PorteeMaximaleGRU = PorteeMaximaleGRU
        self.PorteeMinimaleGRU = PorteeMinimaleGRU
        self.DispersionAtMaxRangeGRU = DispersionAtMaxRangeGRU
        self.DispersionAtMinRangeGRU = DispersionAtMinRangeGRU
        self.MaxSuccessiveHitCount = MaxSuccessiveHitCount
        self.Guidance = Guidance
        self.ForceHitTopArmor = ForceHitTopArmor
        self.NbSalvosShootOnPosition = NbSalvosShootOnPosition
        self.PorteeMinimaleTBAGRU = PorteeMinimaleTBAGRU
