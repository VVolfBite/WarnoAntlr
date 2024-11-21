from itertools import takewhile
from src.extractor.base_class import BaseDescription


# 引入类
class TDiceHitRollRuleDescriptor(BaseDescription):
    def __init__(
        self,
        DescriptorId=None,
        BaseCriticModifier=None,
        BaseHitValueModifiers=None,
        DistanceToTarget=None,
    ):
        self.DescriptorId = DescriptorId
        self.BaseCriticModifier = BaseCriticModifier
        self.BaseHitValueModifiers = BaseHitValueModifiers
        self.DistanceToTarget = DistanceToTarget

    def __repr__(self):
        return (
            f"<TDiceHitRollRuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "DescriptorId",
                        "BaseCriticModifier",
                        "BaseHitValueModifiers",
                        "DistanceToTarget",
                    ]
                ]
            )
            + ">"
        )


# 通用
class TModernWarfareTunableConstante(BaseDescription):
    def __init__(
        self,
        FrontSideAngleInDeg=None,
        TempsSansTirNiDamagePourPasserHorsCombat=None,
        TagStunned=None,
        TandemModifierType=None,
        LinkToCommonConstantes=None,
        SpreadDistanceUnitGRU=None,
        RearSideAngleInDeg=None,
        IgnoreTirPenetrantSiAucunBlindage=None,
        RefreshBestPlaceEveryNbSeconds=None,
        SplashCollisionPlanes=None,
        NbSalveDesignatedShot=None,
        MargePourLesTestsDeSortieDeDistrictLBU=None,
        MoteurHelicos_TempsDemarrage=None,
        TagUberstress=None,
        ArtilleryDispersionTargetNotVisible=None,
        DensitePointsRecherchePosition=None,
        MultiplicateurConsommationUnitesArretees=None,
        FuirDistrictEnFeu=None,
        MergeAllWeaponOnSameTurretInUI=None,
        TransformerAttackEnMoveSiPasDArmeAdaptee=None,
        AdditionalSuppressDamagePerLostPhysicalDamage=None,
        ShootingAdjustmentAngleMax=None,
        TempsSansStressPourRegen=None,
        TagNonRadarTargetable=None,
        RegenStressParSeconde=None,
        FacteurMinTempsViseeReel=None,
        MoteurHelicos_TempsArret=None,
        DurationForLeavingDistrict=None,
        TandemModifierValue=None,
        DistanceToAddToEnnemiDetectionForOtherWeaponGRU=None,
        ClustersDimensionMaxGRU=None,
        PorteeMinArmeEstConsidereCommeArtillerieGRU=None,
        SplashSurTirRate=None,
        SplashRatioDistance=None,
        DistanceMinFleeFireGRU=None,
        DistanceRelaunchMouvementForMoveAndAttackGRU=None,
        DistanceInfanterieEnnemiDetectionGRU=None,
        DistanceToAddToEnnemiDetectionForAAWeaponGRU=None,
        TagAllowedForMissileRoE=None,
        RelativeBonusMoneyByIADifficulty=None,
        DistanceFriendlyFireGRU=None,
        RatioSupplyAmmoAndFuel=None,
        DistanceToAddToEnnemiDetectionForAntiProjectileWeaponGRU=None,
        SpreadDistanceGroupGRU=None,
        DureeDeRevelationApresAttaque=None,
        SplashRatioDamage=None,
    ):
        self.FrontSideAngleInDeg = FrontSideAngleInDeg
        self.TempsSansTirNiDamagePourPasserHorsCombat = (
            TempsSansTirNiDamagePourPasserHorsCombat
        )
        self.TagStunned = TagStunned
        self.TandemModifierType = TandemModifierType
        self.LinkToCommonConstantes = LinkToCommonConstantes
        self.SpreadDistanceUnitGRU = SpreadDistanceUnitGRU
        self.RearSideAngleInDeg = RearSideAngleInDeg
        self.IgnoreTirPenetrantSiAucunBlindage = IgnoreTirPenetrantSiAucunBlindage
        self.RefreshBestPlaceEveryNbSeconds = RefreshBestPlaceEveryNbSeconds
        self.SplashCollisionPlanes = SplashCollisionPlanes
        self.NbSalveDesignatedShot = NbSalveDesignatedShot
        self.MargePourLesTestsDeSortieDeDistrictLBU = (
            MargePourLesTestsDeSortieDeDistrictLBU
        )
        self.MoteurHelicos_TempsDemarrage = MoteurHelicos_TempsDemarrage
        self.TagUberstress = TagUberstress
        self.ArtilleryDispersionTargetNotVisible = ArtilleryDispersionTargetNotVisible
        self.DensitePointsRecherchePosition = DensitePointsRecherchePosition
        self.MultiplicateurConsommationUnitesArretees = (
            MultiplicateurConsommationUnitesArretees
        )
        self.FuirDistrictEnFeu = FuirDistrictEnFeu
        self.MergeAllWeaponOnSameTurretInUI = MergeAllWeaponOnSameTurretInUI
        self.TransformerAttackEnMoveSiPasDArmeAdaptee = (
            TransformerAttackEnMoveSiPasDArmeAdaptee
        )
        self.AdditionalSuppressDamagePerLostPhysicalDamage = (
            AdditionalSuppressDamagePerLostPhysicalDamage
        )
        self.ShootingAdjustmentAngleMax = ShootingAdjustmentAngleMax
        self.TempsSansStressPourRegen = TempsSansStressPourRegen
        self.TagNonRadarTargetable = TagNonRadarTargetable
        self.RegenStressParSeconde = RegenStressParSeconde
        self.FacteurMinTempsViseeReel = FacteurMinTempsViseeReel
        self.MoteurHelicos_TempsArret = MoteurHelicos_TempsArret
        self.DurationForLeavingDistrict = DurationForLeavingDistrict
        self.TandemModifierValue = TandemModifierValue
        self.DistanceToAddToEnnemiDetectionForOtherWeaponGRU = (
            DistanceToAddToEnnemiDetectionForOtherWeaponGRU
        )
        self.ClustersDimensionMaxGRU = ClustersDimensionMaxGRU
        self.PorteeMinArmeEstConsidereCommeArtillerieGRU = (
            PorteeMinArmeEstConsidereCommeArtillerieGRU
        )
        self.SplashSurTirRate = SplashSurTirRate
        self.SplashRatioDistance = SplashRatioDistance
        self.DistanceMinFleeFireGRU = DistanceMinFleeFireGRU
        self.DistanceRelaunchMouvementForMoveAndAttackGRU = (
            DistanceRelaunchMouvementForMoveAndAttackGRU
        )
        self.DistanceInfanterieEnnemiDetectionGRU = DistanceInfanterieEnnemiDetectionGRU
        self.DistanceToAddToEnnemiDetectionForAAWeaponGRU = (
            DistanceToAddToEnnemiDetectionForAAWeaponGRU
        )
        self.TagAllowedForMissileRoE = TagAllowedForMissileRoE
        self.RelativeBonusMoneyByIADifficulty = RelativeBonusMoneyByIADifficulty
        self.DistanceFriendlyFireGRU = DistanceFriendlyFireGRU
        self.RatioSupplyAmmoAndFuel = RatioSupplyAmmoAndFuel
        self.DistanceToAddToEnnemiDetectionForAntiProjectileWeaponGRU = (
            DistanceToAddToEnnemiDetectionForAntiProjectileWeaponGRU
        )
        self.SpreadDistanceGroupGRU = SpreadDistanceGroupGRU
        self.DureeDeRevelationApresAttaque = DureeDeRevelationApresAttaque
        self.SplashRatioDamage = SplashRatioDamage

    def __repr__(self):
        return (
            f"<TModernWarfareTunableConstante "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "FrontSideAngleInDeg",
                        "TempsSansTirNiDamagePourPasserHorsCombat",
                        "TagStunned",
                        "TandemModifierType",
                        "LinkToCommonConstantes",
                        "SpreadDistanceUnitGRU",
                        "RearSideAngleInDeg",
                        "IgnoreTirPenetrantSiAucunBlindage",
                        "RefreshBestPlaceEveryNbSeconds",
                        "SplashCollisionPlanes",
                        "NbSalveDesignatedShot",
                        "MargePourLesTestsDeSortieDeDistrictLBU",
                        "MoteurHelicos_TempsDemarrage",
                        "TagUberstress",
                        "ArtilleryDispersionTargetNotVisible",
                        "DensitePointsRecherchePosition",
                        "MultiplicateurConsommationUnitesArretees",
                        "FuirDistrictEnFeu",
                        "MergeAllWeaponOnSameTurretInUI",
                        "TransformerAttackEnMoveSiPasDArmeAdaptee",
                        "AdditionalSuppressDamagePerLostPhysicalDamage",
                        "ShootingAdjustmentAngleMax",
                        "TempsSansStressPourRegen",
                        "TagNonRadarTargetable",
                        "RegenStressParSeconde",
                        "FacteurMinTempsViseeReel",
                        "MoteurHelicos_TempsArret",
                        "DurationForLeavingDistrict",
                        "TandemModifierValue",
                        "DistanceToAddToEnnemiDetectionForOtherWeaponGRU",
                        "ClustersDimensionMaxGRU",
                        "PorteeMinArmeEstConsidereCommeArtillerieGRU",
                        "SplashSurTirRate",
                        "SplashRatioDistance",
                        "DistanceMinFleeFireGRU",
                        "DistanceRelaunchMouvementForMoveAndAttackGRU",
                        "DistanceInfanterieEnnemiDetectionGRU",
                        "DistanceToAddToEnnemiDetectionForAAWeaponGRU",
                        "TagAllowedForMissileRoE",
                        "RelativeBonusMoneyByIADifficulty",
                        "DistanceFriendlyFireGRU",
                        "RatioSupplyAmmoAndFuel",
                        "DistanceToAddToEnnemiDetectionForAntiProjectileWeaponGRU",
                        "SpreadDistanceGroupGRU",
                        "DureeDeRevelationApresAttaque",
                        "SplashRatioDamage",
                    ]
                ]
            )
            + ">"
        )

    def splash_damage_percent_by_radius_ratio(self, radius_ratio):
        if self.SplashSurTirRate == False:
            return 0

        current_damage = 1.0
        current_distance = 0
        next_distance = 0
        reduction_amount = 0

        for dmg_reduction, dist_threshold in zip(
            self.SplashRatioDamage, self.SplashRatioDistance
        ):
            current_distance = next_distance
            next_distance = current_distance + dist_threshold

            if current_distance <= radius_ratio <= next_distance:
                return current_damage - reduction_amount * (
                    radius_ratio - current_distance
                ) / (next_distance - current_distance)
            else:
                current_damage -= reduction_amount
                reduction_amount = dmg_reduction

        return 0


class TModernWarfareVisibilityRollRule(BaseDescription):
    def __init__(
        self,
        VisibilityRuleDescriptor=None,
        TimeBetweenEachIdentifyRoll=None,
        IdentifyBaseProbability=None,
        DistanceMultiplierRule=None,
    ):
        self.VisibilityRuleDescriptor = VisibilityRuleDescriptor
        self.TimeBetweenEachIdentifyRoll = TimeBetweenEachIdentifyRoll
        self.IdentifyBaseProbability = IdentifyBaseProbability
        self.DistanceMultiplierRule = DistanceMultiplierRule

    def __repr__(self):
        return (
            f"<TModernWarfareVisibilityRollRule "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "VisibilityRuleDescriptor",
                        "TimeBetweenEachIdentifyRoll",
                        "IdentifyBaseProbability",
                        "DistanceMultiplierRule",
                    ]
                ]
            )
            + ">"
        )


class TModernWarfareVisibilityRollRule(BaseDescription):
    def __init__(
        self,
        VisibilityRuleDescriptor=None,
        TimeBetweenEachIdentifyRoll=None,
        IdentifyBaseProbability=None,
        DistanceMultiplierRule=None,
    ):
        self.VisibilityRuleDescriptor = VisibilityRuleDescriptor
        self.TimeBetweenEachIdentifyRoll = TimeBetweenEachIdentifyRoll
        self.IdentifyBaseProbability = IdentifyBaseProbability
        self.DistanceMultiplierRule = DistanceMultiplierRule

    def __repr__(self):
        return (
            f"<TModernWarfareVisibilityRollRule "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "VisibilityRuleDescriptor",
                        "TimeBetweenEachIdentifyRoll",
                        "IdentifyBaseProbability",
                        "DistanceMultiplierRule",
                    ]
                ]
            )
            + ">"
        )


# 准度
class TRollParameters(BaseDescription):
    def __init__(
        self,
        PiercingThresholdBias=None,
        InterpolateRangeTable=None,
        MinimalHitChanceWithECM=None,
        DicesNumberFaces=None,
        RangeModifiersTable=None,
        DistanceToleranceGRU=None,
        SuccessiveHitModifiersTable=None,
    ):
        self.PiercingThresholdBias = PiercingThresholdBias
        self.InterpolateRangeTable = InterpolateRangeTable
        self.MinimalHitChanceWithECM = MinimalHitChanceWithECM
        self.DicesNumberFaces = DicesNumberFaces
        self.RangeModifiersTable = RangeModifiersTable
        self.DistanceToleranceGRU = DistanceToleranceGRU
        self.SuccessiveHitModifiersTable = SuccessiveHitModifiersTable

    def __repr__(self):
        return (
            f"<TRollParameters "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "PiercingThresholdBias",
                        "InterpolateRangeTable",
                        "MinimalHitChanceWithECM",
                        "DicesNumberFaces",
                        "RangeModifiersTable",
                        "DistanceToleranceGRU",
                        "SuccessiveHitModifiersTable",
                    ]
                ]
            )
            + ">"
        )

    def modification_factor_of_accuracy_by_distance_radius(self, distance_radius):

        range_modifiers_list = [
            [key, value]
            for item in self.RangeModifiersTable
            for key, value in item.items()
        ]
        range_modifiers_list.sort(key=lambda x: x[0])

        for i in range(1, len(range_modifiers_list)):
            lower_bound, lower_value = range_modifiers_list[i - 1]
            upper_bound, upper_value = range_modifiers_list[i]

            if lower_bound <= distance_radius <= upper_bound:
                ratio = (distance_radius - lower_bound) / (upper_bound - lower_bound)
                interpolated_value = lower_value + ratio * (upper_value - lower_value)
                return 1 + interpolated_value

        return 1

    def bonus_of_accuracy_by_successive_hit(self, successive_hit):
        successive_hit_modifiers_list = [
            [key, value]
            for item in self.SuccessiveHitModifiersTable
            for key, value in item.items()
        ]
        successive_hit_modifiers_list = sorted(
            successive_hit_modifiers_list, key=lambda x: x[0]
        )
        for mod in successive_hit_modifiers_list:
            if successive_hit == mod[0]:
                return mod[1]
        # 如果超出范围，返回最后一个值
        return 0


# 伤害防御类
class TStairsDamageTypeEvolutionOverRangeDescriptor(BaseDescription):
    def __init__(self, AP=None, DistanceGRU=None):
        self.AP = AP
        self.DistanceGRU = DistanceGRU

    def __repr__(self):
        return (
            f"<TStairsDamageTypeEvolutionOverRangeDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["AP", "DistanceGRU"]]
            )
            + ">"
        )

    def ap_increase_by_distance(self, distance):
        return int(distance * self.AP / self.DistanceGRU)


class TDamageTypeRTTI(BaseDescription):
    def __init__(self, Index=None, Family=None):
        self.Index = Index
        self.Family = Family

    def __repr__(self):
        return (
            f"<TDamageTypeRTTI "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["Index", "Family"]]
            )
            + ">"
        )


class TResistanceTypeRTTI(BaseDescription):
    def __init__(self, Family=None, Index=None):
        self.Family = Family
        self.Index = Index

    def __repr__(self):
        return (
            f"<TResistanceTypeRTTI "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["Family", "Index"]]
            )
            + ">"
        )


class TDamageTypeFamilyDefinition(BaseDescription):
    def __init__(self, Family=None, MaxIndex=None):
        self.Family = Family
        self.MaxIndex = MaxIndex

    def __repr__(self):
        return (
            f"<TDamageTypeFamilyDefinition "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["Family", "MaxIndex"]]
            )
            + ">"
        )

    def is_valid(self, damage_rtti: TDamageTypeRTTI):
        return (
            damage_rtti.Family == self.Family
            and 0 <= damage_rtti.Index <= self.MaxIndex
        )


class TResistanceTypeFamilyDefinition(BaseDescription):
    def __init__(self, Family=None, MaxIndex=None):
        self.Family = Family
        self.MaxIndex = MaxIndex

    def __repr__(self):
        return (
            f"<TResistanceTypeFamilyDefinition "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["Family", "MaxIndex"]]
            )
            + ">"
        )

    def is_valid(self, resistance_rtti: TResistanceTypeRTTI):
        return (
            resistance_rtti.Family == self.Family
            and 0 <= resistance_rtti.Index <= self.MaxIndex
        )


class TGameplayDamageResistanceContainer(BaseDescription):
    def __init__(
        self,
        ResistanceFamilyDefinitionList=None,
        DamageFamilyDefinitionList=None,
        Values=None,
    ):
        self.ResistanceFamilyDefinitionList = ResistanceFamilyDefinitionList
        self.DamageFamilyDefinitionList = DamageFamilyDefinitionList
        self.Values = Values

    def __repr__(self):
        return (
            f"<TGameplayDamageResistanceContainer "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "ResistanceFamilyDefinitionList",
                        "DamageFamilyDefinitionList",
                        "Values",
                    ]
                ]
            )
            + ">"
        )

    def is_valid(
        self,
        damage_type_rtti: TDamageTypeRTTI,
        resistance_type_rtti: TResistanceTypeRTTI,
    ):
        damage_valid = (
            True
            if damage_valid is not None
            else any(
                d.is_valid(damage_type_rtti) for d in self.DamageFamilyDefinitionList
            )
        )
        resistance_valid = (
            True
            if resistance_valid is not None
            else any(
                r.is_valid(resistance_type_rtti)
                for r in self.ResistanceFamilyDefinitionList
            )
        )
        return damage_valid and resistance_valid

    def modification_factor(
        self,
        damage_type_rtti: TDamageTypeRTTI,
        resistance_type_rtti: TResistanceTypeRTTI,
    ):
        if not self.is_valid(damage_type_rtti, resistance_type_rtti):
            raise ValueError("Invalid Damage or Resistance Index")

        # 伤害类型的偏移量和索引
        damage_offset = sum(
            dfd.MaxIndex
            for dfd in takewhile(
                lambda dfd: dfd.Family != damage_type_rtti.Family,
                self.DamageFamilyDefinitionList,
            )
        )

        damage_index = damage_type_rtti.Index - 1 + damage_offset

        # 抵抗类型的偏移量和索引
        resistance_offset = sum(
            rfd.MaxIndex
            for rfd in takewhile(
                lambda rfd: rfd.Family != resistance_type_rtti.Family,
                self.ResistanceFamilyDefinitionList,
            )
        )

        resistance_index = resistance_type_rtti.Index - 1 + resistance_offset

        return self.Values[damage_index][resistance_index]

    def modification_factor_of_damage(self, damage_type_rtti: TDamageTypeRTTI):
        if not self.is_valid(damage_type_rtti, None):
            raise ValueError("Invalid Damage or Resistance Index")
        # 伤害类型的偏移量和索引
        damage_offset = sum(
            dfd.MaxIndex
            for dfd in takewhile(
                lambda dfd: dfd.Family != damage_type_rtti.Family,
                self.DamageFamilyDefinitionList,
            )
        )

        damage_index = damage_type_rtti.Index - 1 + damage_offset
        return self.Values[damage_index]

    def modification_factor_of_damage(self, resistance_type_rtti: TResistanceTypeRTTI):
        if not self.is_valid(resistance_type_rtti, None):
            raise ValueError("Invalid Damage or Resistance Index")
        # 抵抗类型的偏移量和索引
        resistance_offset = sum(
            rfd.MaxIndex
            for rfd in takewhile(
                lambda rfd: rfd.Family != resistance_type_rtti.Family,
                self.ResistanceFamilyDefinitionList,
            )
        )

        resistance_index = resistance_type_rtti.Index - 1 + resistance_offset

        return [row[resistance_index] for row in self.Values]


# Ammunition类
class TAmmunitionDescriptor(BaseDescription):
    def __init__(
        self,
        IsSubAmmunition=None,
        TargetOnlyOneUnitInDistrict=None,
        WeaponForceNote=None,
        ImpactHappening=None,
        FireDescriptor=None,
        PiercingWeapon=None,
        IsHarmlessForAllies=None,
        TirIndirect=None,
        InterdireTirReflexe=None,
        AllowSuppressDamageWhenNoImpact=None,
        CorrectedShotAimtimeMultiplier=None,
        IgnoreInflammabilityConditions=None,
        TempsEntreDeuxFx=None,
        PorteeMinimaleHAGRU=None,
        TypeCategoryName=None,
        CorrectedShotDispersionMultiplier=None,
        SupplyCost=None,
        FluidFriction=None,
        DispersionAtMaxRangeGRU=None,
        DamageTypeEvolutionOverRangeDescriptor=None,
        MissileDescriptor=None,
        WeaponDescriptionToken=None,
        FireTriggeringProbability=None,
        Guidance=None,
        TempsEntreDeuxSalves_Min=None,
        ProjectileType=None,
        PorteeMinimaleGRU=None,
        CanHarmAirplanes=None,
        AngleDispersion=None,
        Caliber=None,
        TirReflexe=None,
        MaximalSpeedGRU=None,
        PhysicalDamages=None,
        AltitudeAPorteeMaximaleGRU=None,
        TempsDeVisee=None,
        RadiusSplashPhysicalDamagesGRU=None,
        MaxAccelerationGRU=None,
        AffecteParNombre=None,
        FlightTimeForSpeed=None,
        MaxSuccessiveHitCount=None,
        TempsEntreDeuxSalves=None,
        SuppressDamages=None,
        MissileTimeBetweenCorrections=None,
        CanShootWhileMoving=None,
        NoiseDissimulationMalus=None,
        IsFireAndForget=None,
        InterfaceWeaponTexture=None,
        FxPower=None,
        TandemCharge=None,
        TempsEntreDeuxTirs=None,
        Name=None,
        ShotWithoutPhysics=None,
        DescriptorId=None,
        ShowDamageInUI=None,
        DispersionWithoutSorting=None,
        MinMaxCategory=None,
        PorteeMaximaleHAGRU=None,
        AffichageMunitionParSalve=None,
        ForceHitTopArmor=None,
        TraitsToken=None,
        DisplaySalveAccuracy=None,
        RadiusSplashSuppressDamagesGRU=None,
        DispersionAtMinRangeGRU=None,
        HitRollRuleDescriptor=None,
        NbTirParSalves=None,
        TempsEntreDeuxSalves_Max=None,
        AltitudeAPorteeMinimaleGRU=None,
        Arme=None,
        ShotsBeforeMaxNoise=None,
        PorteeMaximaleGRU=None,
        WeaponCursorType=None,
        PorteeMaximaleTBAGRU=None,
        PorteeMinimaleTBAGRU=None,
        NbSalvosShootOnPosition=None,
        TargetUnitCenter=None,
        CanShootOnPosition=None,
        NbrProjectilesSimultanes=None,
        DistanceForSpeedGRU=None,
        SmokeDescriptor=None,
    ):
        self.IsSubAmmunition = IsSubAmmunition
        self.TargetOnlyOneUnitInDistrict = TargetOnlyOneUnitInDistrict
        self.WeaponForceNote = WeaponForceNote
        self.ImpactHappening = ImpactHappening
        self.FireDescriptor = FireDescriptor
        self.PiercingWeapon = PiercingWeapon
        self.IsHarmlessForAllies = IsHarmlessForAllies
        self.TirIndirect = TirIndirect
        self.InterdireTirReflexe = InterdireTirReflexe
        self.AllowSuppressDamageWhenNoImpact = AllowSuppressDamageWhenNoImpact
        self.CorrectedShotAimtimeMultiplier = CorrectedShotAimtimeMultiplier
        self.IgnoreInflammabilityConditions = IgnoreInflammabilityConditions
        self.TempsEntreDeuxFx = TempsEntreDeuxFx
        self.PorteeMinimaleHAGRU = PorteeMinimaleHAGRU
        self.TypeCategoryName = TypeCategoryName
        self.CorrectedShotDispersionMultiplier = CorrectedShotDispersionMultiplier
        self.SupplyCost = SupplyCost
        self.FluidFriction = FluidFriction
        self.DispersionAtMaxRangeGRU = DispersionAtMaxRangeGRU
        self.DamageTypeEvolutionOverRangeDescriptor = (
            DamageTypeEvolutionOverRangeDescriptor
        )
        self.MissileDescriptor = MissileDescriptor
        self.WeaponDescriptionToken = WeaponDescriptionToken
        self.FireTriggeringProbability = FireTriggeringProbability
        self.Guidance = Guidance
        self.TempsEntreDeuxSalves_Min = TempsEntreDeuxSalves_Min
        self.ProjectileType = ProjectileType
        self.PorteeMinimaleGRU = PorteeMinimaleGRU
        self.CanHarmAirplanes = CanHarmAirplanes
        self.AngleDispersion = AngleDispersion
        self.Caliber = Caliber
        self.TirReflexe = TirReflexe
        self.MaximalSpeedGRU = MaximalSpeedGRU
        self.PhysicalDamages = PhysicalDamages
        self.AltitudeAPorteeMaximaleGRU = AltitudeAPorteeMaximaleGRU
        self.TempsDeVisee = TempsDeVisee
        self.RadiusSplashPhysicalDamagesGRU = RadiusSplashPhysicalDamagesGRU
        self.MaxAccelerationGRU = MaxAccelerationGRU
        self.AffecteParNombre = AffecteParNombre
        self.FlightTimeForSpeed = FlightTimeForSpeed
        self.MaxSuccessiveHitCount = MaxSuccessiveHitCount
        self.TempsEntreDeuxSalves = TempsEntreDeuxSalves
        self.SuppressDamages = SuppressDamages
        self.MissileTimeBetweenCorrections = MissileTimeBetweenCorrections
        self.CanShootWhileMoving = CanShootWhileMoving
        self.NoiseDissimulationMalus = NoiseDissimulationMalus
        self.IsFireAndForget = IsFireAndForget
        self.InterfaceWeaponTexture = InterfaceWeaponTexture
        self.FxPower = FxPower
        self.TandemCharge = TandemCharge
        self.TempsEntreDeuxTirs = TempsEntreDeuxTirs
        self.Name = Name
        self.ShotWithoutPhysics = ShotWithoutPhysics
        self.DescriptorId = DescriptorId
        self.ShowDamageInUI = ShowDamageInUI
        self.DispersionWithoutSorting = DispersionWithoutSorting
        self.MinMaxCategory = MinMaxCategory
        self.PorteeMaximaleHAGRU = PorteeMaximaleHAGRU
        self.AffichageMunitionParSalve = AffichageMunitionParSalve
        self.ForceHitTopArmor = ForceHitTopArmor
        self.TraitsToken = TraitsToken
        self.DisplaySalveAccuracy = DisplaySalveAccuracy
        self.RadiusSplashSuppressDamagesGRU = RadiusSplashSuppressDamagesGRU
        self.DispersionAtMinRangeGRU = DispersionAtMinRangeGRU
        self.HitRollRuleDescriptor = HitRollRuleDescriptor
        self.NbTirParSalves = NbTirParSalves
        self.TempsEntreDeuxSalves_Max = TempsEntreDeuxSalves_Max
        self.AltitudeAPorteeMinimaleGRU = AltitudeAPorteeMinimaleGRU
        self.Arme = Arme
        self.ShotsBeforeMaxNoise = ShotsBeforeMaxNoise
        self.PorteeMaximaleGRU = PorteeMaximaleGRU
        self.WeaponCursorType = WeaponCursorType
        self.PorteeMaximaleTBAGRU = PorteeMaximaleTBAGRU
        self.PorteeMinimaleTBAGRU = PorteeMinimaleTBAGRU
        self.NbSalvosShootOnPosition = NbSalvosShootOnPosition
        self.TargetUnitCenter = TargetUnitCenter
        self.CanShootOnPosition = CanShootOnPosition
        self.NbrProjectilesSimultanes = NbrProjectilesSimultanes
        self.DistanceForSpeedGRU = DistanceForSpeedGRU
        self.SmokeDescriptor = SmokeDescriptor

    def __repr__(self):
        return (
            f"<TAmmunitionDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "IsSubAmmunition",
                        "TargetOnlyOneUnitInDistrict",
                        "WeaponForceNote",
                        "ImpactHappening",
                        "FireDescriptor",
                        "PiercingWeapon",
                        "IsHarmlessForAllies",
                        "TirIndirect",
                        "InterdireTirReflexe",
                        "AllowSuppressDamageWhenNoImpact",
                        "CorrectedShotAimtimeMultiplier",
                        "IgnoreInflammabilityConditions",
                        "TempsEntreDeuxFx",
                        "PorteeMinimaleHAGRU",
                        "TypeCategoryName",
                        "CorrectedShotDispersionMultiplier",
                        "SupplyCost",
                        "FluidFriction",
                        "DispersionAtMaxRangeGRU",
                        "DamageTypeEvolutionOverRangeDescriptor",
                        "MissileDescriptor",
                        "WeaponDescriptionToken",
                        "FireTriggeringProbability",
                        "Guidance",
                        "TempsEntreDeuxSalves_Min",
                        "ProjectileType",
                        "PorteeMinimaleGRU",
                        "CanHarmAirplanes",
                        "AngleDispersion",
                        "Caliber",
                        "TirReflexe",
                        "MaximalSpeedGRU",
                        "PhysicalDamages",
                        "AltitudeAPorteeMaximaleGRU",
                        "TempsDeVisee",
                        "RadiusSplashPhysicalDamagesGRU",
                        "MaxAccelerationGRU",
                        "AffecteParNombre",
                        "FlightTimeForSpeed",
                        "MaxSuccessiveHitCount",
                        "TempsEntreDeuxSalves",
                        "SuppressDamages",
                        "MissileTimeBetweenCorrections",
                        "CanShootWhileMoving",
                        "NoiseDissimulationMalus",
                        "IsFireAndForget",
                        "InterfaceWeaponTexture",
                        "FxPower",
                        "TandemCharge",
                        "TempsEntreDeuxTirs",
                        "Name",
                        "ShotWithoutPhysics",
                        "DescriptorId",
                        "ShowDamageInUI",
                        "DispersionWithoutSorting",
                        "MinMaxCategory",
                        "PorteeMaximaleHAGRU",
                        "AffichageMunitionParSalve",
                        "ForceHitTopArmor",
                        "TraitsToken",
                        "DisplaySalveAccuracy",
                        "RadiusSplashSuppressDamagesGRU",
                        "DispersionAtMinRangeGRU",
                        "HitRollRuleDescriptor",
                        "NbTirParSalves",
                        "TempsEntreDeuxSalves_Max",
                        "AltitudeAPorteeMinimaleGRU",
                        "Arme",
                        "ShotsBeforeMaxNoise",
                        "PorteeMaximaleGRU",
                        "WeaponCursorType",
                        "PorteeMaximaleTBAGRU",
                        "PorteeMinimaleTBAGRU",
                        "NbSalvosShootOnPosition",
                        "TargetUnitCenter",
                        "CanShootOnPosition",
                        "NbrProjectilesSimultanes",
                        "DistanceForSpeedGRU",
                        "SmokeDescriptor",
                    ]
                ]
            )
            + ">"
        )

    def modification_factor_of_damage(self, gdrcD: TGameplayDamageResistanceContainer):
        return gdrcD.modification_factor_of_damage(self.Arme)

    def ap_increase_by_distance(self, distance):
        return self.DamageTypeEvolutionOverRangeDescriptor.ap_increase_by_distance(
            distance
        )

    def splash_physic_damage_percent_by_radius_ratio(
        self, mwtcD: TModernWarfareTunableConstante, distance
    ):
        return self.PhysicalDamages * mwtcD.splash_damage_percent_by_radius_ratio(
            distance / self.RadiusSplashPhysicalDamagesGRU
        )

    def splash_suppress_damage_percent_by_radius_ratio(
        self, mwtcD: TModernWarfareTunableConstante, distance
    ):
        if self.AllowSuppressDamageWhenNoImpact == False:
            return 0
        else:
            return self.SuppressDamages * mwtcD.splash_damage_percent_by_radius_ratio(
                distance / self.RadiusSplashSuppressDamagesGRU
            )

    def modification_factor_of_accuracy_by_distance_radius(
        self, rpD: TRollParameters, distance_radius
    ):
        if self.HitRollRuleDescriptor.DistanceToTarget == False:
            return 1
        else:
            return rpD.modification_factor_of_accuracy_by_distance_radius(
                distance_radius=distance_radius
            )

    def bonus_of_accuracy_by_successive_hit(self, rpD: TRollParameters, successive_hit):
        if self.MaxSuccessiveHitCount == None:
            return 0

        successive_hit = (
            successive_hit
            if successive_hit <= self.MaxSuccessiveHitCount
            else self.MaxSuccessiveHitCount
        )
        return rpD.bonus_of_accuracy_by_successive_hit(successive_hit=successive_hit)

    def modification_factor_of_dispersion(self, distance):
        return (distance - self.PorteeMinimaleGRU) * (
            self.DispersionAtMaxRangeGRU - self.DispersionAtMinRangeGRU
        ) / (
            self.PorteeMaximaleGRU - self.PorteeMinimaleGRU
        ) + self.DispersionAtMinRangeGRU

    def time_to_finish_a_salve(self):
        return (
            self.TempsDeVisee * self.CorrectedShotAimtimeMultiplier
            + self.TempsEntreDeuxTirs * (self.NbTirParSalves - 1)
        )


# 炮台
class TMountedWeaponDescriptor(BaseDescription):
    def __init__(
        self,
        AnimateOnlyOneSoldier=None,
        SalvoStockIndex=None,
        WeaponActiveAndCanShootPropertyName=None,
        EffectTag=None,
        WeaponShootDataPropertyName=None,
        DispersionRadiusOnThickness=None,
        NbWeapons=None,
        DispersionRadiusOffColor=None,
        DispersionRadiusOnColor=None,
        Ammunition=None,
        DispersionRadiusOffThickness=None,
        ShowInInterface=None,
        HandheldEquipmentKey=None,
        WeaponIgnoredPropertyName=None,
        AmmoConsumption_ForInterface=None,
        TirContinu=None,
        ShowDispersion=None,
    ):
        self.AnimateOnlyOneSoldier = AnimateOnlyOneSoldier
        self.SalvoStockIndex = SalvoStockIndex
        self.WeaponActiveAndCanShootPropertyName = WeaponActiveAndCanShootPropertyName
        self.EffectTag = EffectTag
        self.WeaponShootDataPropertyName = WeaponShootDataPropertyName
        self.DispersionRadiusOnThickness = DispersionRadiusOnThickness
        self.NbWeapons = NbWeapons
        self.DispersionRadiusOffColor = DispersionRadiusOffColor
        self.DispersionRadiusOnColor = DispersionRadiusOnColor
        self.Ammunition = Ammunition
        self.DispersionRadiusOffThickness = DispersionRadiusOffThickness
        self.ShowInInterface = ShowInInterface
        self.HandheldEquipmentKey = HandheldEquipmentKey
        self.WeaponIgnoredPropertyName = WeaponIgnoredPropertyName
        self.AmmoConsumption_ForInterface = AmmoConsumption_ForInterface
        self.TirContinu = TirContinu
        self.ShowDispersion = ShowDispersion

    def __repr__(self):
        return (
            f"<TMountedWeaponDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "AnimateOnlyOneSoldier",
                        "SalvoStockIndex",
                        "WeaponActiveAndCanShootPropertyName",
                        "EffectTag",
                        "WeaponShootDataPropertyName",
                        "DispersionRadiusOnThickness",
                        "NbWeapons",
                        "DispersionRadiusOffColor",
                        "DispersionRadiusOnColor",
                        "Ammunition",
                        "DispersionRadiusOffThickness",
                        "ShowInInterface",
                        "HandheldEquipmentKey",
                        "WeaponIgnoredPropertyName",
                        "AmmoConsumption_ForInterface",
                        "TirContinu",
                        "ShowDispersion",
                    ]
                ]
            )
            + ">"
        )


class TTurretUnitDescriptor(BaseDescription):
    def __init__(
        self,
        Tag=None,
        AngleRotationMinPitch=None,
        AimingPriority=None,
        MountedWeaponDescriptorList=None,
        AngleRotationMax=None,
        YulBoneOrdinal=None,
        AngleRotationMaxPitch=None,
    ):
        self.Tag = Tag
        self.AngleRotationMinPitch = AngleRotationMinPitch
        self.AimingPriority = AimingPriority
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.AngleRotationMax = AngleRotationMax
        self.YulBoneOrdinal = YulBoneOrdinal
        self.AngleRotationMaxPitch = AngleRotationMaxPitch

    def __repr__(self):
        return (
            f"<TTurretUnitDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "Tag",
                        "AngleRotationMinPitch",
                        "AimingPriority",
                        "MountedWeaponDescriptorList",
                        "AngleRotationMax",
                        "YulBoneOrdinal",
                        "AngleRotationMaxPitch",
                    ]
                ]
            )
            + ">"
        )


class TTurretTwoAxisDescriptor(BaseDescription):
    def __init__(
        self,
        Tag=None,
        VitesseRotation=None,
        TurretIdleBehaviourDescriptor=None,
        YulBoneOrdinal=None,
        AngleRotationMaxPitch=None,
        AngleRotationMinPitch=None,
        AimingPriority=None,
        AngleRotationBase=None,
        AngleRotationBasePitch=None,
        MountedWeaponDescriptorList=None,
        AngleRotationMax=None,
        MasterTurretYulBoneOrdinal=None,
        OutOfRangeTrackingDuration=None,
    ):
        self.Tag = Tag
        self.VitesseRotation = VitesseRotation
        self.TurretIdleBehaviourDescriptor = TurretIdleBehaviourDescriptor
        self.YulBoneOrdinal = YulBoneOrdinal
        self.AngleRotationMaxPitch = AngleRotationMaxPitch
        self.AngleRotationMinPitch = AngleRotationMinPitch
        self.AimingPriority = AimingPriority
        self.AngleRotationBase = AngleRotationBase
        self.AngleRotationBasePitch = AngleRotationBasePitch
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.AngleRotationMax = AngleRotationMax
        self.MasterTurretYulBoneOrdinal = MasterTurretYulBoneOrdinal
        self.OutOfRangeTrackingDuration = OutOfRangeTrackingDuration

    def __repr__(self):
        return (
            f"<TTurretTwoAxisDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "Tag",
                        "VitesseRotation",
                        "TurretIdleBehaviourDescriptor",
                        "YulBoneOrdinal",
                        "AngleRotationMaxPitch",
                        "AngleRotationMinPitch",
                        "AimingPriority",
                        "AngleRotationBase",
                        "AngleRotationBasePitch",
                        "MountedWeaponDescriptorList",
                        "AngleRotationMax",
                        "MasterTurretYulBoneOrdinal",
                        "OutOfRangeTrackingDuration",
                    ]
                ]
            )
            + ">"
        )


class TTurretInfanterieDescriptor(BaseDescription):
    def __init__(self, YulBoneOrdinal=None, MountedWeaponDescriptorList=None):
        self.YulBoneOrdinal = YulBoneOrdinal
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList

    def __repr__(self):
        return (
            f"<TTurretInfanterieDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["YulBoneOrdinal", "MountedWeaponDescriptorList"]
                ]
            )
            + ">"
        )


class TTurretBombardierDescriptor(BaseDescription):
    def __init__(
        self,
        Tag=None,
        MountedWeaponDescriptorList=None,
        FlyingAltitudeGRU=None,
        FlyingSpeedInKmph=None,
        YulBoneOrdinal=None,
    ):
        self.Tag = Tag
        self.MountedWeaponDescriptorList = MountedWeaponDescriptorList
        self.FlyingAltitudeGRU = FlyingAltitudeGRU
        self.FlyingSpeedInKmph = FlyingSpeedInKmph
        self.YulBoneOrdinal = YulBoneOrdinal

    def __repr__(self):
        return (
            f"<TTurretBombardierDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "Tag",
                        "MountedWeaponDescriptorList",
                        "FlyingAltitudeGRU",
                        "FlyingSpeedInKmph",
                        "YulBoneOrdinal",
                    ]
                ]
            )
            + ">"
        )


# Weapon类
class TWeaponManagerModuleDescriptor(BaseDescription):
    def __init__(
        self,
        SalvoIsMainSalvo=None,
        TurretDescriptorList=None,
        Salves=None,
        AlwaysOrientArmorTowardsThreat=None,
    ):
        self.SalvoIsMainSalvo = SalvoIsMainSalvo
        self.TurretDescriptorList = TurretDescriptorList
        self.Salves = Salves
        self.AlwaysOrientArmorTowardsThreat = AlwaysOrientArmorTowardsThreat

    def __repr__(self):
        return (
            f"<TWeaponManagerModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "SalvoIsMainSalvo",
                        "TurretDescriptorList",
                        "Salves",
                        "AlwaysOrientArmorTowardsThreat",
                    ]
                ]
            )
            + ">"
        )


# Missile类


class TMissileCarriageWeaponInfo(BaseDescription):
    def __init__(
        self,
        Count=None,
        MissileType=None,
        WeaponIndex=None,
        MountingType=None,
        MeshDescriptor=None,
    ):
        self.Count = Count
        self.MissileType = MissileType
        self.WeaponIndex = WeaponIndex
        self.MountingType = MountingType
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return (
            f"<TMissileCarriageWeaponInfo "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "Count",
                        "MissileType",
                        "WeaponIndex",
                        "MountingType",
                        "MeshDescriptor",
                    ]
                ]
            )
            + ">"
        )


class TMissileCarriageSubDepictionGenerator(BaseDescription):
    def __init__(
        self,
        Pylons=None,
        ReferenceMesh=None,
        Missiles=None,
        MissileCarriageConnoisseur=None,
    ):
        self.Pylons = Pylons
        self.ReferenceMesh = ReferenceMesh
        self.Missiles = Missiles
        self.MissileCarriageConnoisseur = MissileCarriageConnoisseur

    def __repr__(self):
        return (
            f"<TMissileCarriageSubDepictionGenerator "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "Pylons",
                        "ReferenceMesh",
                        "Missiles",
                        "MissileCarriageConnoisseur",
                    ]
                ]
            )
            + ">"
        )


class TMissileCarriageSubDepictionMissileInfo(BaseDescription):
    def __init__(self, WeaponIndex=None, MissileIndex=None, Depiction=None):
        self.WeaponIndex = WeaponIndex
        self.MissileIndex = MissileIndex
        self.Depiction = Depiction

    def __repr__(self):
        return (
            f"<TMissileCarriageSubDepictionMissileInfo "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["WeaponIndex", "MissileIndex", "Depiction"]
                ]
            )
            + ">"
        )


# 单位模组类


class TModuleSelector(BaseDescription):
    def __init__(self, Selection=None, Default=None):
        self.Selection = Selection
        self.Default = Default

    def __repr__(self):
        return (
            f"<TModuleSelector "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["Selection", "Default"]]
            )
            + ">"
        )


class TUnitUIModuleDescriptor(BaseDescription):
    def __init__(
        self,
        SpecialtiesList=None,
        DisplayRoadSpeedInKmph=None,
        UpgradeFromUnit=None,
        UnitRole=None,
        NameToken=None,
        CountryTexture=None,
        GenerateName=None,
        ButtonTexture=None,
        TypeStrategicCount=None,
        InfoPanelConfigurationToken=None,
        MenuIconTexture=None,
    ):
        self.SpecialtiesList = SpecialtiesList
        self.DisplayRoadSpeedInKmph = DisplayRoadSpeedInKmph
        self.UpgradeFromUnit = UpgradeFromUnit
        self.UnitRole = UnitRole
        self.NameToken = NameToken
        self.CountryTexture = CountryTexture
        self.GenerateName = GenerateName
        self.ButtonTexture = ButtonTexture
        self.TypeStrategicCount = TypeStrategicCount
        self.InfoPanelConfigurationToken = InfoPanelConfigurationToken
        self.MenuIconTexture = MenuIconTexture

    def __repr__(self):
        return (
            f"<TUnitUIModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "SpecialtiesList",
                        "DisplayRoadSpeedInKmph",
                        "UpgradeFromUnit",
                        "UnitRole",
                        "NameToken",
                        "CountryTexture",
                        "GenerateName",
                        "ButtonTexture",
                        "TypeStrategicCount",
                        "InfoPanelConfigurationToken",
                        "MenuIconTexture",
                    ]
                ]
            )
            + ">"
        )


class TTypeUnitModuleDescriptor(BaseDescription):
    def __init__(
        self,
        Nationalite=None,
        TypeUnitFormation=None,
        MotherCountry=None,
        AcknowUnitType=None,
    ):
        self.Nationalite = Nationalite
        self.TypeUnitFormation = TypeUnitFormation
        self.MotherCountry = MotherCountry
        self.AcknowUnitType = AcknowUnitType

    def __repr__(self):
        return (
            f"<TTypeUnitModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "Nationalite",
                        "TypeUnitFormation",
                        "MotherCountry",
                        "AcknowUnitType",
                    ]
                ]
            )
            + ">"
        )


class TTagsModuleDescriptor(BaseDescription):
    def __init__(self, TagSet=None):
        self.TagSet = TagSet

    def __repr__(self):
        return (
            f"<TTagsModuleDescriptor "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["TagSet"]])
            + ">"
        )


class TBlindageProperties(BaseDescription):
    def __init__(
        self,
        ResistanceFront=None,
        ResistanceRear=None,
        ResistanceTop=None,
        ExplosiveReactiveArmor=None,
        ResistanceSides=None,
    ):
        self.ResistanceFront = ResistanceFront
        self.ResistanceRear = ResistanceRear
        self.ResistanceTop = ResistanceTop
        self.ExplosiveReactiveArmor = ExplosiveReactiveArmor
        self.ResistanceSides = ResistanceSides

    def __repr__(self):
        return (
            f"<TBlindageProperties "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "ResistanceFront",
                        "ResistanceRear",
                        "ResistanceTop",
                        "ExplosiveReactiveArmor",
                        "ResistanceSides",
                    ]
                ]
            )
            + ">"
        )


class TBaseDamageModuleDescriptor(BaseDescription):
    def __init__(
        self,
        SuppressDamageLevelsPack=None,
        MaxPhysicalDamages=None,
        StunDamageLevelsPack=None,
        MaxStunDamages=None,
        PhysicalDamageLevelsPack=None,
        MaxSuppressionDamages=None,
    ):
        self.SuppressDamageLevelsPack = SuppressDamageLevelsPack
        self.MaxPhysicalDamages = MaxPhysicalDamages
        self.StunDamageLevelsPack = StunDamageLevelsPack
        self.MaxStunDamages = MaxStunDamages
        self.PhysicalDamageLevelsPack = PhysicalDamageLevelsPack
        self.MaxSuppressionDamages = MaxSuppressionDamages

    def __repr__(self):
        return (
            f"<TBaseDamageModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "SuppressDamageLevelsPack",
                        "MaxPhysicalDamages",
                        "StunDamageLevelsPack",
                        "MaxStunDamages",
                        "PhysicalDamageLevelsPack",
                        "MaxSuppressionDamages",
                    ]
                ]
            )
            + ">"
        )


class TDamageModuleDescriptor(BaseDescription):
    def __init__(
        self,
        SuppressDamagesRegenRatio=None,
        HitRollECM=None,
        KillWhenDamagesReachMax=None,
        UseTopArmorAgainstFire=None,
        StunDamagesRegen=None,
        BlindageProperties=None,
        AutoOrientation=None,
    ):
        self.SuppressDamagesRegenRatio = SuppressDamagesRegenRatio
        self.HitRollECM = HitRollECM
        self.KillWhenDamagesReachMax = KillWhenDamagesReachMax
        self.UseTopArmorAgainstFire = UseTopArmorAgainstFire
        self.StunDamagesRegen = StunDamagesRegen
        self.BlindageProperties = BlindageProperties
        self.AutoOrientation = AutoOrientation

    def __repr__(self):
        return (
            f"<TDamageModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "SuppressDamagesRegenRatio",
                        "HitRollECM",
                        "KillWhenDamagesReachMax",
                        "UseTopArmorAgainstFire",
                        "StunDamagesRegen",
                        "BlindageProperties",
                        "AutoOrientation",
                    ]
                ]
            )
            + ">"
        )


class TRoutModuleDescriptor(BaseDescription):
    def __init__(self, MoralLevel=None):
        self.MoralLevel = MoralLevel

    def __repr__(self):
        return (
            f"<TRoutModuleDescriptor "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["MoralLevel"]])
            + ">"
        )


class TDangerousnessModuleDescriptor(BaseDescription):
    def __init__(self, Dangerousness=None):
        self.Dangerousness = Dangerousness

    def __repr__(self):
        return (
            f"<TDangerousnessModuleDescriptor "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Dangerousness"]])
            + ">"
        )


class TemplateUnitCriticalModule(BaseDescription):
    def __init__(self, Module=None):
        self.Module = Module

    def __repr__(self):
        return (
            f"<TemplateUnitCriticalModule "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Module"]])
            + ">"
        )


class TemplateUnitMissileCarriage(BaseDescription):
    def __init__(self, Connoisseur=None):
        self.Connoisseur = Connoisseur

    def __repr__(self):
        return (
            f"<TemplateUnitMissileCarriage "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Connoisseur"]])
            + ">"
        )


class TExperienceModuleDescriptor(BaseDescription):
    def __init__(
        self,
        ExperienceGainBySecond=None,
        ExperienceLevelsPackDescriptor=None,
        CanWinExperience=None,
        ExperienceMultiplierBonusOnKill=None,
    ):
        self.ExperienceGainBySecond = ExperienceGainBySecond
        self.ExperienceLevelsPackDescriptor = ExperienceLevelsPackDescriptor
        self.CanWinExperience = CanWinExperience
        self.ExperienceMultiplierBonusOnKill = ExperienceMultiplierBonusOnKill

    def __repr__(self):
        return (
            f"<TExperienceModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "ExperienceGainBySecond",
                        "ExperienceLevelsPackDescriptor",
                        "CanWinExperience",
                        "ExperienceMultiplierBonusOnKill",
                    ]
                ]
            )
            + ">"
        )


class TVisibilityModuleDescriptor(BaseDescription):
    def __init__(self, UnitConcealmentBonus=None, VisionUnitType=None):
        self.UnitConcealmentBonus = UnitConcealmentBonus
        self.VisionUnitType = VisionUnitType

    def __repr__(self):
        return (
            f"<TVisibilityModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["UnitConcealmentBonus", "VisionUnitType"]
                ]
            )
            + ">"
        )


class TAutoCoverModuleDescriptor(BaseDescription):
    def __init__(
        self,
        TerrainList=None,
        OccupationRadiusGRU=None,
        AutoCoverRangeGRU=None,
        TerrainListMask=None,
        UseTerrainsForEscape=None,
    ):
        self.TerrainList = TerrainList
        self.OccupationRadiusGRU = OccupationRadiusGRU
        self.AutoCoverRangeGRU = AutoCoverRangeGRU
        self.TerrainListMask = TerrainListMask
        self.UseTerrainsForEscape = UseTerrainsForEscape

    def __repr__(self):
        return (
            f"<TAutoCoverModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "TerrainList",
                        "OccupationRadiusGRU",
                        "AutoCoverRangeGRU",
                        "TerrainListMask",
                        "UseTerrainsForEscape",
                    ]
                ]
            )
            + ">"
        )


class TGenericMovementModuleDescriptor(BaseDescription):
    def __init__(self, PathfindType=None, MaxSpeedInKmph=None):
        self.PathfindType = PathfindType
        self.MaxSpeedInKmph = MaxSpeedInKmph

    def __repr__(self):
        return (
            f"<TGenericMovementModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["PathfindType", "MaxSpeedInKmph"]
                ]
            )
            + ">"
        )


class TLandMovementModuleDescriptor(BaseDescription):
    def __init__(
        self,
        StartTime=None,
        RotationStopTime=None,
        MaxDecelerationGRU=None,
        StopTime=None,
        RotationStartTime=None,
        SpeedBonusFactorOnRoad=None,
        UnitMovingType=None,
        MaxAccelerationGRU=None,
        TempsDemiTour=None,
        VehicleSizeInMeter=None,
    ):
        self.StartTime = StartTime
        self.RotationStopTime = RotationStopTime
        self.MaxDecelerationGRU = MaxDecelerationGRU
        self.StopTime = StopTime
        self.RotationStartTime = RotationStartTime
        self.SpeedBonusFactorOnRoad = SpeedBonusFactorOnRoad
        self.UnitMovingType = UnitMovingType
        self.MaxAccelerationGRU = MaxAccelerationGRU
        self.TempsDemiTour = TempsDemiTour
        self.VehicleSizeInMeter = VehicleSizeInMeter

    def __repr__(self):
        return (
            f"<TLandMovementModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "StartTime",
                        "RotationStopTime",
                        "MaxDecelerationGRU",
                        "StopTime",
                        "RotationStartTime",
                        "SpeedBonusFactorOnRoad",
                        "UnitMovingType",
                        "MaxAccelerationGRU",
                        "TempsDemiTour",
                        "VehicleSizeInMeter",
                    ]
                ]
            )
            + ">"
        )


class THelicopterMovementModuleDescriptor(BaseDescription):
    def __init__(
        self,
        CyclicManoeuvrability=None,
        TorqueManoeuvrability=None,
        MaxSpeedInKmph=None,
        Mass=None,
        RotorArea=None,
        WorldFloorProxy=None,
        UpwardSpeedInKmph=None,
        MaxInclination=None,
        GFactorLimit=None,
    ):
        self.CyclicManoeuvrability = CyclicManoeuvrability
        self.TorqueManoeuvrability = TorqueManoeuvrability
        self.MaxSpeedInKmph = MaxSpeedInKmph
        self.Mass = Mass
        self.RotorArea = RotorArea
        self.WorldFloorProxy = WorldFloorProxy
        self.UpwardSpeedInKmph = UpwardSpeedInKmph
        self.MaxInclination = MaxInclination
        self.GFactorLimit = GFactorLimit

    def __repr__(self):
        return (
            f"<THelicopterMovementModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "CyclicManoeuvrability",
                        "TorqueManoeuvrability",
                        "MaxSpeedInKmph",
                        "Mass",
                        "RotorArea",
                        "WorldFloorProxy",
                        "UpwardSpeedInKmph",
                        "MaxInclination",
                        "GFactorLimit",
                    ]
                ]
            )
            + ">"
        )


class AirplaneMovementDescriptor(BaseDescription):
    def __init__(
        self,
        OrderedAttackStrategies=None,
        RollAngle=None,
        EvacToStartingPoint=None,
        PitchAngle=None,
        SpeedInKmph=None,
        AgilityRadiusGRU=None,
        RollSpeed=None,
        EvacAngle=None,
        AltitudeMinGRU=None,
        AltitudeGRU=None,
    ):
        self.OrderedAttackStrategies = OrderedAttackStrategies
        self.RollAngle = RollAngle
        self.EvacToStartingPoint = EvacToStartingPoint
        self.PitchAngle = PitchAngle
        self.SpeedInKmph = SpeedInKmph
        self.AgilityRadiusGRU = AgilityRadiusGRU
        self.RollSpeed = RollSpeed
        self.EvacAngle = EvacAngle
        self.AltitudeMinGRU = AltitudeMinGRU
        self.AltitudeGRU = AltitudeGRU

    def __repr__(self):
        return (
            f"<AirplaneMovementDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "OrderedAttackStrategies",
                        "RollAngle",
                        "EvacToStartingPoint",
                        "PitchAngle",
                        "SpeedInKmph",
                        "AgilityRadiusGRU",
                        "RollSpeed",
                        "EvacAngle",
                        "AltitudeMinGRU",
                        "AltitudeGRU",
                    ]
                ]
            )
            + ">"
        )


class HelicopterPositionModuleDescriptor(BaseDescription):
    def __init__(
        self, LowAltitudeFlyingAltitudeGRU=None, NearGroundFlyingAltitudeGRU=None
    ):
        self.LowAltitudeFlyingAltitudeGRU = LowAltitudeFlyingAltitudeGRU
        self.NearGroundFlyingAltitudeGRU = NearGroundFlyingAltitudeGRU

    def __repr__(self):
        return (
            f"<HelicopterPositionModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "LowAltitudeFlyingAltitudeGRU",
                        "NearGroundFlyingAltitudeGRU",
                    ]
                ]
            )
            + ">"
        )


class AirplanePositionModuleDescriptor(BaseDescription):
    def __init__(self, LowAltitudeFlyingAltitudeGRU=None):
        self.LowAltitudeFlyingAltitudeGRU = LowAltitudeFlyingAltitudeGRU

    def __repr__(self):
        return (
            f"<AirplanePositionModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["LowAltitudeFlyingAltitudeGRU"]
                ]
            )
            + ">"
        )


class TFuelModuleDescriptor(BaseDescription):
    def __init__(self, FuelMoveDuration=None, FuelCapacity=None):
        self.FuelMoveDuration = FuelMoveDuration
        self.FuelCapacity = FuelCapacity

    def __repr__(self):
        return (
            f"<TFuelModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["FuelMoveDuration", "FuelCapacity"]
                ]
            )
            + ">"
        )


class TScannerConfigurationDescriptor(BaseDescription):
    def __init__(
        self,
        PorteeVisionGRU=None,
        PorteeVisionFOWGRU=None,
        OpticalStrengthAltitude=None,
        OpticalStrength=None,
        PorteeVisionTBAGRU=None,
        OpticsAltitudeConfig=None,
        SpecializedOpticalStrengths=None,
        SpecializedDetectionsGRU=None,
        PorteeIdentification=None,
        DetectionTBAGRU=None,
    ):
        self.PorteeVisionGRU = PorteeVisionGRU
        self.PorteeVisionFOWGRU = PorteeVisionFOWGRU
        self.OpticalStrengthAltitude = OpticalStrengthAltitude
        self.OpticalStrength = OpticalStrength
        self.PorteeVisionTBAGRU = PorteeVisionTBAGRU
        self.OpticsAltitudeConfig = OpticsAltitudeConfig
        self.SpecializedOpticalStrengths = SpecializedOpticalStrengths
        self.SpecializedDetectionsGRU = SpecializedDetectionsGRU
        self.PorteeIdentification = PorteeIdentification
        self.DetectionTBAGRU = DetectionTBAGRU

    def __repr__(self):
        return (
            f"<TScannerConfigurationDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "PorteeVisionGRU",
                        "PorteeVisionFOWGRU",
                        "OpticalStrengthAltitude",
                        "OpticalStrength",
                        "PorteeVisionTBAGRU",
                        "OpticsAltitudeConfig",
                        "SpecializedOpticalStrengths",
                        "SpecializedDetectionsGRU",
                        "PorteeIdentification",
                        "DetectionTBAGRU",
                    ]
                ]
            )
            + ">"
        )


class TReverseScannerWithIdentificationDescriptor(BaseDescription):
    def __init__(self, VisibilityRollRule=None):
        self.VisibilityRollRule = VisibilityRollRule

    def __repr__(self):
        return (
            f"<TReverseScannerWithIdentificationDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["VisibilityRollRule"]]
            )
            + ">"
        )


class TAirplaneModuleDescriptor(BaseDescription):
    def __init__(self, EvacuationTime=None, TravelDuration=None):
        self.EvacuationTime = EvacuationTime
        self.TravelDuration = TravelDuration

    def __repr__(self):
        return (
            f"<TAirplaneModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["EvacuationTime", "TravelDuration"]
                ]
            )
            + ">"
        )


class TSupplyModuleDescriptor(BaseDescription):
    def __init__(self, SupplyCapacity=None, SupplyDescriptor=None, SupplyPriority=None):
        self.SupplyCapacity = SupplyCapacity
        self.SupplyDescriptor = SupplyDescriptor
        self.SupplyPriority = SupplyPriority

    def __repr__(self):
        return (
            f"<TSupplyModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["SupplyCapacity", "SupplyDescriptor", "SupplyPriority"]
                ]
            )
            + ">"
        )


class TDeploymentShiftModuleDescriptor(BaseDescription):
    def __init__(self, DeploymentShiftGRU=None):
        self.DeploymentShiftGRU = DeploymentShiftGRU

    def __repr__(self):
        return (
            f"<TDeploymentShiftModuleDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["DeploymentShiftGRU"]]
            )
            + ">"
        )


class TUnitUpkeepModuleDescriptor(BaseDescription):
    def __init__(self, UpkeepPercentage=None):
        self.UpkeepPercentage = UpkeepPercentage

    def __repr__(self):
        return (
            f"<TUnitUpkeepModuleDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["UpkeepPercentage"]]
            )
            + ">"
        )


class TProductionModuleDescriptor(BaseDescription):
    def __init__(
        self, ProductionRessourcesNeeded=None, Factory=None, ProductionTime=None
    ):
        self.ProductionRessourcesNeeded = ProductionRessourcesNeeded
        self.Factory = Factory
        self.ProductionTime = ProductionTime

    def __repr__(self):
        return (
            f"<TProductionModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "ProductionRessourcesNeeded",
                        "Factory",
                        "ProductionTime",
                    ]
                ]
            )
            + ">"
        )


class TTransportableModuleDescriptor(BaseDescription):
    def __init__(
        self,
        TimeToLoad=None,
        NbSeatsOccupied=None,
        IsTowable=None,
        TransportedTexture=None,
        TransportedSoldier=None,
    ):
        self.TimeToLoad = TimeToLoad
        self.NbSeatsOccupied = NbSeatsOccupied
        self.IsTowable = IsTowable
        self.TransportedTexture = TransportedTexture
        self.TransportedSoldier = TransportedSoldier

    def __repr__(self):
        return (
            f"<TTransportableModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "TimeToLoad",
                        "NbSeatsOccupied",
                        "IsTowable",
                        "TransportedTexture",
                        "TransportedSoldier",
                    ]
                ]
            )
            + ">"
        )


class TTransporterModuleDescriptor(BaseDescription):
    def __init__(
        self,
        WreckUnloadPhysicalDamageBonus=None,
        TransportableTagSet=None,
        NbSeatsAvailable=None,
        WreckUnloadStunDamageBonus=None,
        LoadRadiusGRU=None,
        WreckUnloadSuppressDamageBonus=None,
    ):
        self.WreckUnloadPhysicalDamageBonus = WreckUnloadPhysicalDamageBonus
        self.TransportableTagSet = TransportableTagSet
        self.NbSeatsAvailable = NbSeatsAvailable
        self.WreckUnloadStunDamageBonus = WreckUnloadStunDamageBonus
        self.LoadRadiusGRU = LoadRadiusGRU
        self.WreckUnloadSuppressDamageBonus = WreckUnloadSuppressDamageBonus

    def __repr__(self):
        return (
            f"<TTransporterModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "WreckUnloadPhysicalDamageBonus",
                        "TransportableTagSet",
                        "NbSeatsAvailable",
                        "WreckUnloadStunDamageBonus",
                        "LoadRadiusGRU",
                        "WreckUnloadSuppressDamageBonus",
                    ]
                ]
            )
            + ">"
        )


class TInfantrySquadModuleDescriptor(BaseDescription):
    def __init__(
        self,
        WeaponUnitFXKey=None,
        MimeticDescriptor=None,
        NbSoldatInGroupeCombat=None,
        SquadDataDescriptor=None,
        InfantryMimeticName=None,
    ):
        self.WeaponUnitFXKey = WeaponUnitFXKey
        self.MimeticDescriptor = MimeticDescriptor
        self.NbSoldatInGroupeCombat = NbSoldatInGroupeCombat
        self.SquadDataDescriptor = SquadDataDescriptor
        self.InfantryMimeticName = InfantryMimeticName

    def __repr__(self):
        return (
            f"<TInfantrySquadModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "WeaponUnitFXKey",
                        "MimeticDescriptor",
                        "NbSoldatInGroupeCombat",
                        "SquadDataDescriptor",
                        "InfantryMimeticName",
                    ]
                ]
            )
            + ">"
        )


class TZoneInfluenceMapModuleDescriptor(BaseDescription):
    def __init__(
        self,
        StrengthDecayPerSecond=None,
        MinimumInfluenceStrength=None,
        InfluenceStrength=None,
        PreventsDecayInZone=None,
        IsEnabledByComportementAuto=None,
    ):
        self.StrengthDecayPerSecond = StrengthDecayPerSecond
        self.MinimumInfluenceStrength = MinimumInfluenceStrength
        self.InfluenceStrength = InfluenceStrength
        self.PreventsDecayInZone = PreventsDecayInZone
        self.IsEnabledByComportementAuto = IsEnabledByComportementAuto

    def __repr__(self):
        return (
            f"<TZoneInfluenceMapModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "StrengthDecayPerSecond",
                        "MinimumInfluenceStrength",
                        "InfluenceStrength",
                        "PreventsDecayInZone",
                        "IsEnabledByComportementAuto",
                    ]
                ]
            )
            + ">"
        )


# 单位类
class TEntityDescriptor(BaseDescription):
    def __init__(
        self,
        World=None,
        DescriptorId=None,
        ModulesDescriptors=None,
        ClassNameForDebug=None,
    ):
        self.World = World
        self.DescriptorId = DescriptorId
        self.ModulesDescriptors = ModulesDescriptors
        self.ClassNameForDebug = ClassNameForDebug

    def __repr__(self):
        return (
            f"<TEntityDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "World",
                        "DescriptorId",
                        "ModulesDescriptors",
                        "ClassNameForDebug",
                    ]
                ]
            )
            + ">"
        )


# 光环与效果


class TCapaciteDescriptor(BaseDescription):
    def __init__(
        self,
        TargetInBuilding=None,
        SelfEffect=None,
        RangeGRU=None,
        MaxTargetNb=None,
        TargetTeamFilter=None,
        NameToken=None,
        DisplayRangeColor=None,
        TargetEffectDuration=None,
        TargetMySelf=None,
        CanBeCastFromTransport=None,
        TargetWoundedFilter=None,
        Name=None,
        DescriptorId=None,
        AreaShape=None,
        DisplayRangeThickness=None,
        TargetEffect=None,
        Cooldown=None,
        InfluenceMapAlliance=None,
        CheckVisibility=None,
        Price=None,
        InfluenceMapType=None,
        Declenchement=None,
        TargetInTransport=None,
        OrderMustSpreadTargets=None,
        ActionRadiusWithBoundingBox=None,
        FeedbackActivationMask=None,
        SelfEffectDuration=None,
        CumulEffect=None,
        MultiplyCost=None,
        TagsCibleExcluded=None,
        AllowReflexDuringCast=None,
        TagsCiblePossible=None,
        MinVirtualUnits=None,
        TypeCible=None,
        RadiusGRU=None,
        Conditions=None,
        CastTime=None,
        TargetInSelf=None,
    ):
        self.TargetInBuilding = TargetInBuilding
        self.SelfEffect = SelfEffect
        self.RangeGRU = RangeGRU
        self.MaxTargetNb = MaxTargetNb
        self.TargetTeamFilter = TargetTeamFilter
        self.NameToken = NameToken
        self.DisplayRangeColor = DisplayRangeColor
        self.TargetEffectDuration = TargetEffectDuration
        self.TargetMySelf = TargetMySelf
        self.CanBeCastFromTransport = CanBeCastFromTransport
        self.TargetWoundedFilter = TargetWoundedFilter
        self.Name = Name
        self.DescriptorId = DescriptorId
        self.AreaShape = AreaShape
        self.DisplayRangeThickness = DisplayRangeThickness
        self.TargetEffect = TargetEffect
        self.Cooldown = Cooldown
        self.InfluenceMapAlliance = InfluenceMapAlliance
        self.CheckVisibility = CheckVisibility
        self.Price = Price
        self.InfluenceMapType = InfluenceMapType
        self.Declenchement = Declenchement
        self.TargetInTransport = TargetInTransport
        self.OrderMustSpreadTargets = OrderMustSpreadTargets
        self.ActionRadiusWithBoundingBox = ActionRadiusWithBoundingBox
        self.FeedbackActivationMask = FeedbackActivationMask
        self.SelfEffectDuration = SelfEffectDuration
        self.CumulEffect = CumulEffect
        self.MultiplyCost = MultiplyCost
        self.TagsCibleExcluded = TagsCibleExcluded
        self.AllowReflexDuringCast = AllowReflexDuringCast
        self.TagsCiblePossible = TagsCiblePossible
        self.MinVirtualUnits = MinVirtualUnits
        self.TypeCible = TypeCible
        self.RadiusGRU = RadiusGRU
        self.Conditions = Conditions
        self.CastTime = CastTime
        self.TargetInSelf = TargetInSelf

    def __repr__(self):
        return (
            f"<TCapaciteDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "TargetInBuilding",
                        "SelfEffect",
                        "RangeGRU",
                        "MaxTargetNb",
                        "TargetTeamFilter",
                        "NameToken",
                        "DisplayRangeColor",
                        "TargetEffectDuration",
                        "TargetMySelf",
                        "CanBeCastFromTransport",
                        "TargetWoundedFilter",
                        "Name",
                        "DescriptorId",
                        "AreaShape",
                        "DisplayRangeThickness",
                        "TargetEffect",
                        "Cooldown",
                        "InfluenceMapAlliance",
                        "CheckVisibility",
                        "Price",
                        "InfluenceMapType",
                        "Declenchement",
                        "TargetInTransport",
                        "OrderMustSpreadTargets",
                        "ActionRadiusWithBoundingBox",
                        "FeedbackActivationMask",
                        "SelfEffectDuration",
                        "CumulEffect",
                        "MultiplyCost",
                        "TagsCibleExcluded",
                        "AllowReflexDuringCast",
                        "TagsCiblePossible",
                        "MinVirtualUnits",
                        "TypeCible",
                        "RadiusGRU",
                        "Conditions",
                        "CastTime",
                        "TargetInSelf",
                    ]
                ]
            )
            + ">"
        )


class TEffectsPackDescriptor(BaseDescription):
    def __init__(self, DescriptorId=None, EffectsDescriptors=None, NameForDebug=None):
        self.DescriptorId = DescriptorId
        self.EffectsDescriptors = EffectsDescriptors
        self.NameForDebug = NameForDebug

    def __repr__(self):
        return (
            f"<TEffectsPackDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["DescriptorId", "EffectsDescriptors", "NameForDebug"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseWeaponDispersionMaxRangeDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseWeaponDispersionMaxRangeDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "ModifierValue"]
                ]
            )
            + ">"
        )


class TUnitEffectRaiseTagDescriptor(BaseDescription):
    def __init__(self, TagListToRaise=None):
        self.TagListToRaise = TagListToRaise

    def __repr__(self):
        return (
            f"<TUnitEffectRaiseTagDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["TagListToRaise"]]
            )
            + ">"
        )


class TUnitEffectShowLabelIconDescriptor(BaseDescription):
    def __init__(self, TextureToken=None):
        self.TextureToken = TextureToken

    def __repr__(self):
        return (
            f"<TUnitEffectShowLabelIconDescriptor "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["TextureToken"]])
            + ">"
        )


class TUnitEffectIncreaseDamageTakenDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, DamageType=None, BonusDamage=None):
        self.ModifierType = ModifierType
        self.DamageType = DamageType
        self.BonusDamage = BonusDamage

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseDamageTakenDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "DamageType", "BonusDamage"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseInfluenceValueDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, Bonus=None):
        self.ModifierType = ModifierType
        self.Bonus = Bonus

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseInfluenceValueDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["ModifierType", "Bonus"]]
            )
            + ">"
        )


class TUnitEffectIncreaseWeaponPorteeMaxDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None, ModifierValueGRU=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue
        self.ModifierValueGRU = ModifierValueGRU

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseWeaponPorteeMaxDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "ModifierValue", "ModifierValueGRU"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseWeaponPorteeMaxHADescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None, ModifierValueGRU=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue
        self.ModifierValueGRU = ModifierValueGRU

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseWeaponPorteeMaxHADescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "ModifierValue", "ModifierValueGRU"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseWeaponPorteeMaxProjectileDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None, ModifierValueGRU=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue
        self.ModifierValueGRU = ModifierValueGRU

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseWeaponPorteeMaxProjectileDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "ModifierValue", "ModifierValueGRU"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseWeaponPorteeMaxTBADescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None, ModifierValueGRU=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue
        self.ModifierValueGRU = ModifierValueGRU

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseWeaponPorteeMaxTBADescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "ModifierValue", "ModifierValueGRU"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseDispersionDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusDispersion=None):
        self.ModifierType = ModifierType
        self.BonusDispersion = BonusDispersion

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseDispersionDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "BonusDispersion"]
                ]
            )
            + ">"
        )


class TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return (
            f"<TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "ModifierValue"]
                ]
            )
            + ">"
        )


class TUnitEffectAlterWeaponTempsEntreDeuxTirsDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return (
            f"<TUnitEffectAlterWeaponTempsEntreDeuxTirsDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "ModifierValue"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseChassisRotationSpeedDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusChassisRotationSpeed=None):
        self.ModifierType = ModifierType
        self.BonusChassisRotationSpeed = BonusChassisRotationSpeed

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseChassisRotationSpeedDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "BonusChassisRotationSpeed"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseTurretRotationSpeedDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusTurretRotationSpeed=None):
        self.ModifierType = ModifierType
        self.BonusTurretRotationSpeed = BonusTurretRotationSpeed

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseTurretRotationSpeedDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "BonusTurretRotationSpeed"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseSpeedDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusSpeedBaseInPercent=None):
        self.ModifierType = ModifierType
        self.BonusSpeedBaseInPercent = BonusSpeedBaseInPercent

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseSpeedDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "BonusSpeedBaseInPercent"]
                ]
            )
            + ">"
        )


class TUnitEffectBonusExperienceLevelDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ExperienceLevelModifier=None):
        self.ModifierType = ModifierType
        self.ExperienceLevelModifier = ExperienceLevelModifier

    def __repr__(self):
        return (
            f"<TUnitEffectBonusExperienceLevelDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "ExperienceLevelModifier"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseDangerousnessDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusDangerousness=None):
        self.ModifierType = ModifierType
        self.BonusDangerousness = BonusDangerousness

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseDangerousnessDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "BonusDangerousness"]
                ]
            )
            + ">"
        )


class TUnitEffectTransportSlotNumberModificationDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, EffectOnTransportSlotNumber=None):
        self.ModifierType = ModifierType
        self.EffectOnTransportSlotNumber = EffectOnTransportSlotNumber

    def __repr__(self):
        return (
            f"<TUnitEffectTransportSlotNumberModificationDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "EffectOnTransportSlotNumber"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "ModifierValue"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseVisionDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusVisionBase=None):
        self.ModifierType = ModifierType
        self.BonusVisionBase = BonusVisionBase

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseVisionDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "BonusVisionBase"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseSpecializedDetectionDescriptor(BaseDescription):
    def __init__(
        self, BonusValueGRU=None, ModifierType=None, BonusValue=None, VisionType=None
    ):
        self.BonusValueGRU = BonusValueGRU
        self.ModifierType = ModifierType
        self.BonusValue = BonusValue
        self.VisionType = VisionType

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseSpecializedDetectionDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "BonusValueGRU",
                        "ModifierType",
                        "BonusValue",
                        "VisionType",
                    ]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseInfluenceValueMinDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, Bonus=None):
        self.ModifierType = ModifierType
        self.Bonus = Bonus

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseInfluenceValueMinDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["ModifierType", "Bonus"]]
            )
            + ">"
        )


class TUnitEffectSetSelectableDescriptor(BaseDescription):
    def __init__(self, Selectable=None):
        self.Selectable = Selectable

    def __repr__(self):
        return (
            f"<TUnitEffectSetSelectableDescriptor "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Selectable"]])
            + ">"
        )


class TUnitEffectStopWithInertiaEffectDescriptor(BaseDescription):
    def __init__(self, UpdateEachTick=None):
        self.UpdateEachTick = UpdateEachTick

    def __repr__(self):
        return (
            f"<TUnitEffectStopWithInertiaEffectDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["UpdateEachTick"]]
            )
            + ">"
        )


class TUnitEffectIncreaseWeaponPrecisionArretDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseWeaponPrecisionArretDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "ModifierValue"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "ModifierValue"]
                ]
            )
            + ">"
        )


class TUnitEffectRemoveUnitDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TUnitEffectRemoveUnitDescriptor>"


class TUnitEffectBonusPrecisionWhenTargetedDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusPrecisionWhenTargeted=None):
        self.ModifierType = ModifierType
        self.BonusPrecisionWhenTargeted = BonusPrecisionWhenTargeted

    def __repr__(self):
        return (
            f"<TUnitEffectBonusPrecisionWhenTargetedDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "BonusPrecisionWhenTargeted"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseOpticalStrengthDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusOpticalStrength=None):
        self.ModifierType = ModifierType
        self.BonusOpticalStrength = BonusOpticalStrength

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseOpticalStrengthDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "BonusOpticalStrength"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseWeaponPorteeMaxIgnoreSmokeDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusWeaponPorteeMax=None):
        self.ModifierType = ModifierType
        self.BonusWeaponPorteeMax = BonusWeaponPorteeMax

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseWeaponPorteeMaxIgnoreSmokeDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "BonusWeaponPorteeMax"]
                ]
            )
            + ">"
        )


class TUnitEffectReplaceArmorDescriptor(BaseDescription):
    def __init__(self, ReplacementBlindage=None, BlindageLocation=None):
        self.ReplacementBlindage = ReplacementBlindage
        self.BlindageLocation = BlindageLocation

    def __repr__(self):
        return (
            f"<TUnitEffectReplaceArmorDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ReplacementBlindage", "BlindageLocation"]
                ]
            )
            + ">"
        )


class TUnitEffectIncreaseConcealmentBonusDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, BonusConcealmentBonus=None):
        self.ModifierType = ModifierType
        self.BonusConcealmentBonus = BonusConcealmentBonus

    def __repr__(self):
        return (
            f"<TUnitEffectIncreaseConcealmentBonusDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "BonusConcealmentBonus"]
                ]
            )
            + ">"
        )


class TUnitEffectHealOverTimeDescriptor(BaseDescription):
    def __init__(
        self, NbUpdatePerSecond=None, DamageType=None, HealUnitsPerSecond=None
    ):
        self.NbUpdatePerSecond = NbUpdatePerSecond
        self.DamageType = DamageType
        self.HealUnitsPerSecond = HealUnitsPerSecond

    def __repr__(self):
        return (
            f"<TUnitEffectHealOverTimeDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "NbUpdatePerSecond",
                        "DamageType",
                        "HealUnitsPerSecond",
                    ]
                ]
            )
            + ">"
        )


class TUnitEffectChangeTeamDescriptor(BaseDescription):
    def __init__(self, FutureTeam=None):
        self.FutureTeam = FutureTeam

    def __repr__(self):
        return (
            f"<TUnitEffectChangeTeamDescriptor "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["FutureTeam"]])
            + ">"
        )


class TUnitEffectAddCapacityDescriptor(BaseDescription):
    def __init__(self, CapacityToAdd=None):
        self.CapacityToAdd = CapacityToAdd

    def __repr__(self):
        return (
            f"<TUnitEffectAddCapacityDescriptor "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["CapacityToAdd"]])
            + ">"
        )


class TStrategicSupplyMalusEffectDescriptor(BaseDescription):
    def __init__(self, SupplyMalus=None, ModifierType=None):
        self.SupplyMalus = SupplyMalus
        self.ModifierType = ModifierType

    def __repr__(self):
        return (
            f"<TStrategicSupplyMalusEffectDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["SupplyMalus", "ModifierType"]
                ]
            )
            + ">"
        )


class TBonusWeaponAimtimeEffectDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, ModifierValue=None):
        self.ModifierType = ModifierType
        self.ModifierValue = ModifierValue

    def __repr__(self):
        return (
            f"<TBonusWeaponAimtimeEffectDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "ModifierValue"]
                ]
            )
            + ">"
        )


class TDerouteUnitEffectDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TDerouteUnitEffectDescriptor>"


class TEffectInflictSuppressDamageDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, SuppressDamageValue=None):
        self.ModifierType = ModifierType
        self.SuppressDamageValue = SuppressDamageValue

    def __repr__(self):
        return (
            f"<TEffectInflictSuppressDamageDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "SuppressDamageValue"]
                ]
            )
            + ">"
        )


class TKillUnitEffectDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TKillUnitEffectDescriptor>"


# 师与卡组配置

class DeckPackDescriptor(BaseDescription):
    def __init__(self, Transport=None, Unit=None, Xp=None):
        self.Transport = Transport
        self.Unit = Unit
        self.Xp = Xp

    def __repr__(self):
        return (
            f"<DeckPackDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["Transport", "Unit", "Xp"]
                ]
            )
            + ">"
        )
    


class TDeckDivisionRules(BaseDescription):
    def __init__(self, DivisionRules=None):
        self.DivisionRules = DivisionRules

    def __repr__(self):
        return (
            f"<TDeckDivisionRules "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["DivisionRules"]])
            + ">"
        )


class TDeckDivisionRule(BaseDescription):
    def __init__(self, UnitRuleList=None):
        self.UnitRuleList = UnitRuleList

    def __repr__(self):
        return (
            f"<TDeckDivisionRule "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["UnitRuleList"]])
            + ">"
        )


class TDeckUniteRule(BaseDescription):
    def __init__(
        self,
        UnitDescriptor=None,
        NumberOfUnitInPack=None,
        NumberOfUnitInPackXPMultiplier=None,
        AvailableTransportList=None,
        AvailableWithoutTransport=None,
    ):
        self.UnitDescriptor = UnitDescriptor
        self.NumberOfUnitInPack = NumberOfUnitInPack
        self.NumberOfUnitInPackXPMultiplier = NumberOfUnitInPackXPMultiplier
        self.AvailableTransportList = AvailableTransportList
        self.AvailableWithoutTransport = AvailableWithoutTransport

    def __repr__(self):
        return (
            f"<TDeckUniteRule "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "UnitDescriptor",
                        "NumberOfUnitInPack",
                        "NumberOfUnitInPackXPMultiplier",
                        "AvailableTransportList",
                        "AvailableWithoutTransport",
                    ]
                ]
            )
            + ">"
        )


class TDeckDivisionDescriptor(BaseDescription):
    def __init__(
        self,
        DivisionNationalite=None,
        DivisionTags=None,
        DivisionPowerClassification=None,
        MaxActivationPoints=None,
        DescriptionHintTitleToken=None,
        DescriptorId=None,
        DivisionName=None,
        EmblemTexture=None,
        PackList=None,
        CountryId=None,
        PortraitTexture=None,
        StrategicLabelColor=None,
        TypeTexture=None,
        CostMatrix=None,
        CfgName=None,
    ):
        self.DivisionNationalite = DivisionNationalite
        self.DivisionTags = DivisionTags
        self.DivisionPowerClassification = DivisionPowerClassification
        self.MaxActivationPoints = MaxActivationPoints
        self.DescriptionHintTitleToken = DescriptionHintTitleToken
        self.DescriptorId = DescriptorId
        self.DivisionName = DivisionName
        self.EmblemTexture = EmblemTexture
        self.PackList = PackList
        self.CountryId = CountryId
        self.PortraitTexture = PortraitTexture
        self.StrategicLabelColor = StrategicLabelColor
        self.TypeTexture = TypeTexture
        self.CostMatrix = CostMatrix
        self.CfgName = CfgName

    def __repr__(self):
        return (
            f"<TDeckDivisionDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "DivisionNationalite",
                        "DivisionTags",
                        "DivisionPowerClassification",
                        "MaxActivationPoints",
                        "DescriptionHintTitleToken",
                        "DescriptorId",
                        "DivisionName",
                        "EmblemTexture",
                        "PackList",
                        "CountryId",
                        "PortraitTexture",
                        "StrategicLabelColor",
                        "TypeTexture",
                        "CostMatrix",
                        "CfgName",
                    ]
                ]
            )
            + ">"
        )

## 地形


class TGameplayTerrain(BaseDescription):
    def __init__(
        self,
        WorldLayerActiveMask=None,
        BloqueInfanterie=None,
        HeightInMeters=None,
        ConcealmentBonus=None,
        BloqueAmphibie=None,
        Name=None,
        BloqueAtterrissage=None,
        DissimulationModifierGroundAir=None,
        SpeedModifierTrack=None,
        SpeedModifierAllTerrainWheel=None,
        AuthorizeNearGroundFlying=None,
        DissimulationModifierGroundGround=None,
        TerrainType=None,
        DamageModifierPerFamilyAndResistance=None,
        BloqueVehicule=None,
        CriticalEffectProbability=None,
        DebugColor=None,
        InflammabilityProbability=None,
        BloqueVision=None,
        SpeedModifierInfantry=None,
    ):
        self.WorldLayerActiveMask = WorldLayerActiveMask
        self.BloqueInfanterie = BloqueInfanterie
        self.HeightInMeters = HeightInMeters
        self.ConcealmentBonus = ConcealmentBonus
        self.BloqueAmphibie = BloqueAmphibie
        self.Name = Name
        self.BloqueAtterrissage = BloqueAtterrissage
        self.DissimulationModifierGroundAir = DissimulationModifierGroundAir
        self.SpeedModifierTrack = SpeedModifierTrack
        self.SpeedModifierAllTerrainWheel = SpeedModifierAllTerrainWheel
        self.AuthorizeNearGroundFlying = AuthorizeNearGroundFlying
        self.DissimulationModifierGroundGround = DissimulationModifierGroundGround
        self.TerrainType = TerrainType
        self.DamageModifierPerFamilyAndResistance = DamageModifierPerFamilyAndResistance
        self.BloqueVehicule = BloqueVehicule
        self.CriticalEffectProbability = CriticalEffectProbability
        self.DebugColor = DebugColor
        self.InflammabilityProbability = InflammabilityProbability
        self.BloqueVision = BloqueVision
        self.SpeedModifierInfantry = SpeedModifierInfantry

    def __repr__(self):
        return (
            f"<TGameplayTerrain "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "WorldLayerActiveMask",
                        "BloqueInfanterie",
                        "HeightInMeters",
                        "ConcealmentBonus",
                        "BloqueAmphibie",
                        "Name",
                        "BloqueAtterrissage",
                        "DissimulationModifierGroundAir",
                        "SpeedModifierTrack",
                        "SpeedModifierAllTerrainWheel",
                        "AuthorizeNearGroundFlying",
                        "DissimulationModifierGroundGround",
                        "TerrainType",
                        "DamageModifierPerFamilyAndResistance",
                        "BloqueVehicule",
                        "CriticalEffectProbability",
                        "DebugColor",
                        "InflammabilityProbability",
                        "BloqueVision",
                        "SpeedModifierInfantry",
                    ]
                ]
            )
            + ">"
        )

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