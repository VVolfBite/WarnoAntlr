from src.extractor.base_class import BaseDescription

class TAirplaneConstantesModernWarfareDescriptor(BaseDescription):
    def __init__(self, BackLandingGearMeshNodeName=None, FrontLandingGearMeshNodeName=None, UtiliserArmesPendantEvac=None, EvacWinchesterToutesLesArmesPrincipales=None, TempsEntreDeuxDecollagesEnSecondes=None, EvacuationAltitudeGRU=None):
        self.BackLandingGearMeshNodeName = BackLandingGearMeshNodeName
        self.FrontLandingGearMeshNodeName = FrontLandingGearMeshNodeName
        self.UtiliserArmesPendantEvac = UtiliserArmesPendantEvac
        self.EvacWinchesterToutesLesArmesPrincipales = EvacWinchesterToutesLesArmesPrincipales
        self.TempsEntreDeuxDecollagesEnSecondes = TempsEntreDeuxDecollagesEnSecondes
        self.EvacuationAltitudeGRU = EvacuationAltitudeGRU


class TRoutConstants(BaseDescription):
    def __init__(self, SortieSeuilSuppression=None, ProtectionContreLaSuppressionEnDeroute=None, EffetAppliqueSuppression=None, EffetConditionSuppression=None, TempsEntreDeuxTestsMoralSeuilSuppression=None, LanceTestMoralSeuilSuppression=None, TempsEntreDeuxTestsMoralPertePV=None, LanceTestMoralPertePV=None, TestMoralSeuil=None, TestMoralNombreFacesDes=None, TestMoralNombreDes=None):
        self.SortieSeuilSuppression = SortieSeuilSuppression
        self.ProtectionContreLaSuppressionEnDeroute = ProtectionContreLaSuppressionEnDeroute
        self.EffetAppliqueSuppression = EffetAppliqueSuppression
        self.EffetConditionSuppression = EffetConditionSuppression
        self.TempsEntreDeuxTestsMoralSeuilSuppression = TempsEntreDeuxTestsMoralSeuilSuppression
        self.LanceTestMoralSeuilSuppression = LanceTestMoralSeuilSuppression
        self.TempsEntreDeuxTestsMoralPertePV = TempsEntreDeuxTestsMoralPertePV
        self.LanceTestMoralPertePV = LanceTestMoralPertePV
        self.TestMoralSeuil = TestMoralSeuil
        self.TestMoralNombreFacesDes = TestMoralNombreFacesDes
        self.TestMoralNombreDes = TestMoralNombreDes


class TEvaluationMenaceConstantesDescriptor(BaseDescription):
    def __init__(self, ConsidererLesMenacesEnMouvementCommeDirectes=None, DureeDeMemoireDeLaMenaceEnSecondes=None, EscapeRadiusGRU=None, CercleMenaceGRU=None):
        self.ConsidererLesMenacesEnMouvementCommeDirectes = ConsidererLesMenacesEnMouvementCommeDirectes
        self.DureeDeMemoireDeLaMenaceEnSecondes = DureeDeMemoireDeLaMenaceEnSecondes
        self.EscapeRadiusGRU = EscapeRadiusGRU
        self.CercleMenaceGRU = CercleMenaceGRU


class TSpecificFactoryDescription(BaseDescription):
    def __init__(self, FactoryHintExtended=None, FactoryHintBody=None, FactoryHintTitle=None, FactoryName=None):
        self.FactoryHintExtended = FactoryHintExtended
        self.FactoryHintBody = FactoryHintBody
        self.FactoryHintTitle = FactoryHintTitle
        self.FactoryName = FactoryName


class TSpecificFactoryResources(BaseDescription):
    def __init__(self, FactoryDescriptions=None, FactoryDisplayOrder=None):
        self.FactoryDescriptions = FactoryDescriptions
        self.FactoryDisplayOrder = FactoryDisplayOrder


class TBaseClass(BaseDescription):
    def __init__(self, None=None):
        self.None = None


class TGhostColors(BaseDescription):
    def __init__(self, GhostBlends=None, GhostAlphas=None, GhostColor=None):
        self.GhostBlends = GhostBlends
        self.GhostAlphas = GhostAlphas
        self.GhostColor = GhostColor


class TTunableConstante(BaseDescription):
    def __init__(self, ConsidereUniteConcealmentSurTerrainAvecDissimulation=None, RelativeScanningPositionGRU=None, MultiplicateurBonusDissimulationParDistanceGRU=None, OutmapShootPositionYaw=None, OutmapShootPositionRelativeAltitude=None, OutmapShootPositionPitch=None, WithdrawalDuration=None, DeploymentDuration=None, AllowMultipleBuildingSelection=None, AllowMixedSelection=None, AllowGhostCrossUnitSelection=None, CooldownBeforeKillInSeconds=None, ResaleDistanceGRU=None, ResalePriceRatio=None, TagDecrochage=None, DecalageDepuisLeCentreDansCouloirGRU=None, ToleranceLargeurRoutePourMouvementsRapidesShiftes=None, LargeurRouteGRU=None, ForcerMarcheAvantPourAttaquer=None, DistancePourDeclencherMarcheArriereGRU=None, AngleArrierePourMarcheArriereEnDegre=None, TempsAutoriseHorsMondePourMissileSansCible=None, DefaultTimeLimitInMinutes=None, TimeLimitTable=None, DefaultGhostColors=None, ShowroomMinSoldiersPerLine=None, ShowroomNumberOfLines=None, ShowroomOffsetBetweenSoldiers=None, ShowroomOffsetBetweenLines=None, LandingPositionTimePredictionInSeconds=None, DistanceMaxSmallMovementsInMeters=None, MaxTerrainAngleForLanding=None, DistanceCoherenceGRU=None, TacticVictoryLevelConstantes=None, DureeRetraitControleZone=None, DureeDeploiementControleZone=None, MinimumNumberOfUnitToStayInGameWithoutCmdOrProductionInDestructionMode=None, SuddenDeathTime=None, DefaultAIDifficultyForPlayerReplacement=None, BaseAttackingAllianceNum=None, Persistance_Bruit=None, CanUseAlliedAllianceCorridors=None, CommanderRadiusEffectByLevelGRU=None, CommanderEffect=None, StunEffectDuration=None, LaunchDeathAmmoOutmap=None, PerteDeSuppressParPointDeVieEntierPerdu=None, EfficiencyShotSearchDistanceTolerance=None, PorteeRadioArtillerieGRU=None, TagRadioJammed=None, TagRadioArtillerie=None, ReductionDegatsSuppressDansVehicule=None, Color_OutmapDispersionAreaOutline=None, Color_OutmapDispersionAreaFill=None, Color_ObserverDebugOutline=None, Color_ObserverDebugFill=None, UnitPositionVerticalOffsetFromRoofGRU=None, CadavreOffsetMin=None, CadavreOffsetMax=None, AltitudeVolGRU=None, TireursIgnoreesPourLaFuite=None, RatioPuissancePourRetaliation=None, AutoSmokeQuandRatioPvInferieurA=None, TempsEnSecondesEntreDeuxSmokeAutomatiques=None, TagBloquantLeMoveAndAttack=None, MaxPullDistanceForAirplaneGRU=None, MaxPullDistanceGRU=None, AutoCover_TagEmpechantLAutocover=None, AutoCover_DistanceMaxEntreLesChecksDeTerrainsGRU=None, FumigeneTimeout=None, FumigeneMaxCount=None, FumigeneAlphaGhost=None, EliminationWarningsDuration=None):
        self.ConsidereUniteConcealmentSurTerrainAvecDissimulation = ConsidereUniteConcealmentSurTerrainAvecDissimulation
        self.RelativeScanningPositionGRU = RelativeScanningPositionGRU
        self.MultiplicateurBonusDissimulationParDistanceGRU = MultiplicateurBonusDissimulationParDistanceGRU
        self.OutmapShootPositionYaw = OutmapShootPositionYaw
        self.OutmapShootPositionRelativeAltitude = OutmapShootPositionRelativeAltitude
        self.OutmapShootPositionPitch = OutmapShootPositionPitch
        self.WithdrawalDuration = WithdrawalDuration
        self.DeploymentDuration = DeploymentDuration
        self.AllowMultipleBuildingSelection = AllowMultipleBuildingSelection
        self.AllowMixedSelection = AllowMixedSelection
        self.AllowGhostCrossUnitSelection = AllowGhostCrossUnitSelection
        self.CooldownBeforeKillInSeconds = CooldownBeforeKillInSeconds
        self.ResaleDistanceGRU = ResaleDistanceGRU
        self.ResalePriceRatio = ResalePriceRatio
        self.TagDecrochage = TagDecrochage
        self.DecalageDepuisLeCentreDansCouloirGRU = DecalageDepuisLeCentreDansCouloirGRU
        self.ToleranceLargeurRoutePourMouvementsRapidesShiftes = ToleranceLargeurRoutePourMouvementsRapidesShiftes
        self.LargeurRouteGRU = LargeurRouteGRU
        self.ForcerMarcheAvantPourAttaquer = ForcerMarcheAvantPourAttaquer
        self.DistancePourDeclencherMarcheArriereGRU = DistancePourDeclencherMarcheArriereGRU
        self.AngleArrierePourMarcheArriereEnDegre = AngleArrierePourMarcheArriereEnDegre
        self.TempsAutoriseHorsMondePourMissileSansCible = TempsAutoriseHorsMondePourMissileSansCible
        self.DefaultTimeLimitInMinutes = DefaultTimeLimitInMinutes
        self.TimeLimitTable = TimeLimitTable
        self.DefaultGhostColors = DefaultGhostColors
        self.ShowroomMinSoldiersPerLine = ShowroomMinSoldiersPerLine
        self.ShowroomNumberOfLines = ShowroomNumberOfLines
        self.ShowroomOffsetBetweenSoldiers = ShowroomOffsetBetweenSoldiers
        self.ShowroomOffsetBetweenLines = ShowroomOffsetBetweenLines
        self.LandingPositionTimePredictionInSeconds = LandingPositionTimePredictionInSeconds
        self.DistanceMaxSmallMovementsInMeters = DistanceMaxSmallMovementsInMeters
        self.MaxTerrainAngleForLanding = MaxTerrainAngleForLanding
        self.DistanceCoherenceGRU = DistanceCoherenceGRU
        self.TacticVictoryLevelConstantes = TacticVictoryLevelConstantes
        self.DureeRetraitControleZone = DureeRetraitControleZone
        self.DureeDeploiementControleZone = DureeDeploiementControleZone
        self.MinimumNumberOfUnitToStayInGameWithoutCmdOrProductionInDestructionMode = MinimumNumberOfUnitToStayInGameWithoutCmdOrProductionInDestructionMode
        self.SuddenDeathTime = SuddenDeathTime
        self.DefaultAIDifficultyForPlayerReplacement = DefaultAIDifficultyForPlayerReplacement
        self.BaseAttackingAllianceNum = BaseAttackingAllianceNum
        self.Persistance_Bruit = Persistance_Bruit
        self.CanUseAlliedAllianceCorridors = CanUseAlliedAllianceCorridors
        self.CommanderRadiusEffectByLevelGRU = CommanderRadiusEffectByLevelGRU
        self.CommanderEffect = CommanderEffect
        self.StunEffectDuration = StunEffectDuration
        self.LaunchDeathAmmoOutmap = LaunchDeathAmmoOutmap
        self.PerteDeSuppressParPointDeVieEntierPerdu = PerteDeSuppressParPointDeVieEntierPerdu
        self.EfficiencyShotSearchDistanceTolerance = EfficiencyShotSearchDistanceTolerance
        self.PorteeRadioArtillerieGRU = PorteeRadioArtillerieGRU
        self.TagRadioJammed = TagRadioJammed
        self.TagRadioArtillerie = TagRadioArtillerie
        self.ReductionDegatsSuppressDansVehicule = ReductionDegatsSuppressDansVehicule
        self.Color_OutmapDispersionAreaOutline = Color_OutmapDispersionAreaOutline
        self.Color_OutmapDispersionAreaFill = Color_OutmapDispersionAreaFill
        self.Color_ObserverDebugOutline = Color_ObserverDebugOutline
        self.Color_ObserverDebugFill = Color_ObserverDebugFill
        self.UnitPositionVerticalOffsetFromRoofGRU = UnitPositionVerticalOffsetFromRoofGRU
        self.CadavreOffsetMin = CadavreOffsetMin
        self.CadavreOffsetMax = CadavreOffsetMax
        self.AltitudeVolGRU = AltitudeVolGRU
        self.TireursIgnoreesPourLaFuite = TireursIgnoreesPourLaFuite
        self.RatioPuissancePourRetaliation = RatioPuissancePourRetaliation
        self.AutoSmokeQuandRatioPvInferieurA = AutoSmokeQuandRatioPvInferieurA
        self.TempsEnSecondesEntreDeuxSmokeAutomatiques = TempsEnSecondesEntreDeuxSmokeAutomatiques
        self.TagBloquantLeMoveAndAttack = TagBloquantLeMoveAndAttack
        self.MaxPullDistanceForAirplaneGRU = MaxPullDistanceForAirplaneGRU
        self.MaxPullDistanceGRU = MaxPullDistanceGRU
        self.AutoCover_TagEmpechantLAutocover = AutoCover_TagEmpechantLAutocover
        self.AutoCover_DistanceMaxEntreLesChecksDeTerrainsGRU = AutoCover_DistanceMaxEntreLesChecksDeTerrainsGRU
        self.FumigeneTimeout = FumigeneTimeout
        self.FumigeneMaxCount = FumigeneMaxCount
        self.FumigeneAlphaGhost = FumigeneAlphaGhost
        self.EliminationWarningsDuration = EliminationWarningsDuration


class TVictoryLevelConstantes(BaseDescription):
    def __init__(self, TotalVictoryLimit=None, MajorVictoryLimit=None, MinorVictoryLimit=None):
        self.TotalVictoryLimit = TotalVictoryLimit
        self.MajorVictoryLimit = MajorVictoryLimit
        self.MinorVictoryLimit = MinorVictoryLimit


class TModernWarfareTunableConstante(BaseDescription):
    def __init__(self, SplashCollisionPlanes=None, TagNonRadarTargetable=None, TagAllowedForMissileRoE=None, SplashRatioDistance=None, SplashRatioDamage=None, SplashSurTirRate=None, ShootingAdjustmentAngleMax=None, NbSalveDesignatedShot=None, IgnoreTirPenetrantSiAucunBlindage=None, RearSideAngleInDeg=None, FrontSideAngleInDeg=None, DistanceMinFleeFireGRU=None, DistanceFriendlyFireGRU=None, ArtilleryDispersionTargetNotVisible=None, AdditionalSuppressDamagePerLostPhysicalDamage=None, MergeAllWeaponOnSameTurretInUI=None, RatioSupplyAmmoAndFuel=None, SpreadDistanceGroupGRU=None, SpreadDistanceUnitGRU=None, TandemModifierType=None, TandemModifierValue=None, MultiplicateurConsommationUnitesArretees=None, MoteurHelicos_TempsDemarrage=None, MoteurHelicos_TempsArret=None, RelativeBonusMoneyByIADifficulty=None, ClustersDimensionMaxGRU=None, TransformerAttackEnMoveSiPasDArmeAdaptee=None, DurationForLeavingDistrict=None, MargePourLesTestsDeSortieDeDistrictLBU=None, FuirDistrictEnFeu=None, TagUberstress=None, TagStunned=None, TempsSansTirNiDamagePourPasserHorsCombat=None, TempsSansStressPourRegen=None, RegenStressParSeconde=None, PorteeMinArmeEstConsidereCommeArtillerieGRU=None, FacteurMinTempsViseeReel=None, DureeDeRevelationApresAttaque=None, DistanceToAddToEnnemiDetectionForOtherWeaponGRU=None, DistanceToAddToEnnemiDetectionForAntiProjectileWeaponGRU=None, DistanceToAddToEnnemiDetectionForAAWeaponGRU=None, DistanceRelaunchMouvementForMoveAndAttackGRU=None, DistanceInfanterieEnnemiDetectionGRU=None, LinkToCommonConstantes=None):
        self.SplashCollisionPlanes = SplashCollisionPlanes
        self.TagNonRadarTargetable = TagNonRadarTargetable
        self.TagAllowedForMissileRoE = TagAllowedForMissileRoE
        self.SplashRatioDistance = SplashRatioDistance
        self.SplashRatioDamage = SplashRatioDamage
        self.SplashSurTirRate = SplashSurTirRate
        self.ShootingAdjustmentAngleMax = ShootingAdjustmentAngleMax
        self.NbSalveDesignatedShot = NbSalveDesignatedShot
        self.IgnoreTirPenetrantSiAucunBlindage = IgnoreTirPenetrantSiAucunBlindage
        self.RearSideAngleInDeg = RearSideAngleInDeg
        self.FrontSideAngleInDeg = FrontSideAngleInDeg
        self.DistanceMinFleeFireGRU = DistanceMinFleeFireGRU
        self.DistanceFriendlyFireGRU = DistanceFriendlyFireGRU
        self.ArtilleryDispersionTargetNotVisible = ArtilleryDispersionTargetNotVisible
        self.AdditionalSuppressDamagePerLostPhysicalDamage = AdditionalSuppressDamagePerLostPhysicalDamage
        self.MergeAllWeaponOnSameTurretInUI = MergeAllWeaponOnSameTurretInUI
        self.RatioSupplyAmmoAndFuel = RatioSupplyAmmoAndFuel
        self.SpreadDistanceGroupGRU = SpreadDistanceGroupGRU
        self.SpreadDistanceUnitGRU = SpreadDistanceUnitGRU
        self.TandemModifierType = TandemModifierType
        self.TandemModifierValue = TandemModifierValue
        self.MultiplicateurConsommationUnitesArretees = MultiplicateurConsommationUnitesArretees
        self.MoteurHelicos_TempsDemarrage = MoteurHelicos_TempsDemarrage
        self.MoteurHelicos_TempsArret = MoteurHelicos_TempsArret
        self.RelativeBonusMoneyByIADifficulty = RelativeBonusMoneyByIADifficulty
        self.ClustersDimensionMaxGRU = ClustersDimensionMaxGRU
        self.TransformerAttackEnMoveSiPasDArmeAdaptee = TransformerAttackEnMoveSiPasDArmeAdaptee
        self.DurationForLeavingDistrict = DurationForLeavingDistrict
        self.MargePourLesTestsDeSortieDeDistrictLBU = MargePourLesTestsDeSortieDeDistrictLBU
        self.FuirDistrictEnFeu = FuirDistrictEnFeu
        self.TagUberstress = TagUberstress
        self.TagStunned = TagStunned
        self.TempsSansTirNiDamagePourPasserHorsCombat = TempsSansTirNiDamagePourPasserHorsCombat
        self.TempsSansStressPourRegen = TempsSansStressPourRegen
        self.RegenStressParSeconde = RegenStressParSeconde
        self.PorteeMinArmeEstConsidereCommeArtillerieGRU = PorteeMinArmeEstConsidereCommeArtillerieGRU
        self.FacteurMinTempsViseeReel = FacteurMinTempsViseeReel
        self.DureeDeRevelationApresAttaque = DureeDeRevelationApresAttaque
        self.DistanceToAddToEnnemiDetectionForOtherWeaponGRU = DistanceToAddToEnnemiDetectionForOtherWeaponGRU
        self.DistanceToAddToEnnemiDetectionForAntiProjectileWeaponGRU = DistanceToAddToEnnemiDetectionForAntiProjectileWeaponGRU
        self.DistanceToAddToEnnemiDetectionForAAWeaponGRU = DistanceToAddToEnnemiDetectionForAAWeaponGRU
        self.DistanceRelaunchMouvementForMoveAndAttackGRU = DistanceRelaunchMouvementForMoveAndAttackGRU
        self.DistanceInfanterieEnnemiDetectionGRU = DistanceInfanterieEnnemiDetectionGRU
        self.LinkToCommonConstantes = LinkToCommonConstantes


class TWargameTunableConstante(BaseDescription):
    def __init__(self, WargameBuildingAllowedTerrainsMask=None, DissimulationEnumToValue=None, OrdersAcceptedByTransporterIfTransportedUnitsCanDo=None, OrderBlockedWhenOutOfFuel=None, InfantryTrenchDepthGRU=None, AmphibiousSpawnLandSeaRatio=None, UpkeepPercentDefaultSetting=None, UpkeepPercentAvailableSettings=None, VictoryTypeDestructionLevelsTable=None, ArgentInitialMinimumPourGererLIA=None, DefaultDestructionScoreToReachSetting=None, ArgentInitialSetting=None, DefaultArgentInitial=None, ConquestPointsDefaultIndex=None, ValeurOptionTailleNewLabelVeryLarge=None, ValeurOptionTailleNewLabelLarge=None, ValeurOptionTailleNewLabelNormal=None, ValeurOptionTailleNewLabelSmall=None, ValeurOptionTailleNewLabelVerySmall=None, ValeurOptionTailleNewLabelMinimal=None, ValeurMinimumCoverTresLeger=None, ValeurMinimumCoverMoyen=None, ValeurMinimumCoverLeger=None, ValeurMaxBarMoralLabel=None, ValeurMinAffichageBarMoralLabel=None, TempsAttenteAffichageIconeConflitQuartier=None, TagDInfanteriePinned=None, PaliersDeVitesse=None, PaliersDeResilience=None, PaliersDOptique=None, PaliersDOptiqueDAltitude=None, PaliersDeDissimulation=None, PaliersDAgiliteGRU=None, PlatingAndApDisplayFactor=None, NomDAffichageDesUnitesNonIdentifiees=None, MaxNbMergedUnitsInGroup=None, FactoriesWhichNeverCloseProductionMenuAfterValidation=None, UnitValueLimitForSurrender=None, UpkeepReductionByIADifficulty=None, DeckUnitExpLevelAdditiveModifierByIADifficulty=None, DeckUnitCountMultiplierByIADifficulty=None, RelativeBonusFluxByIADifficulty=None, IncomeMultiplierInDestructionMode=None, IncomeMultiplierTokensInDestructionMode=None, DefaultIncomeMultiplierIndexInDestructionMode=None, TimeBeforeEarningCommandPointsFactorToAddByNbPlayers=None, TimeBeforeEarningCommandPoints=None, IncomeMultiplier=None, DefaultIncomeMultiplierIndex=None, BaseIncome=None, CoeffMoneyMaxIfUsingUpkeep=None, ConquestPossibleScores=None, MoneyWinPerAllianceInConquestMode=None, MoneyWinLocalisationTokensInConquestMode=None, TimeBeforeEarningConquestPoints=None, DefaultMoneyWinPerAllianceRateInConquestMode=None):
        self.WargameBuildingAllowedTerrainsMask = WargameBuildingAllowedTerrainsMask
        self.DissimulationEnumToValue = DissimulationEnumToValue
        self.OrdersAcceptedByTransporterIfTransportedUnitsCanDo = OrdersAcceptedByTransporterIfTransportedUnitsCanDo
        self.OrderBlockedWhenOutOfFuel = OrderBlockedWhenOutOfFuel
        self.InfantryTrenchDepthGRU = InfantryTrenchDepthGRU
        self.AmphibiousSpawnLandSeaRatio = AmphibiousSpawnLandSeaRatio
        self.UpkeepPercentDefaultSetting = UpkeepPercentDefaultSetting
        self.UpkeepPercentAvailableSettings = UpkeepPercentAvailableSettings
        self.VictoryTypeDestructionLevelsTable = VictoryTypeDestructionLevelsTable
        self.ArgentInitialMinimumPourGererLIA = ArgentInitialMinimumPourGererLIA
        self.DefaultDestructionScoreToReachSetting = DefaultDestructionScoreToReachSetting
        self.ArgentInitialSetting = ArgentInitialSetting
        self.DefaultArgentInitial = DefaultArgentInitial
        self.ConquestPointsDefaultIndex = ConquestPointsDefaultIndex
        self.ValeurOptionTailleNewLabelVeryLarge = ValeurOptionTailleNewLabelVeryLarge
        self.ValeurOptionTailleNewLabelLarge = ValeurOptionTailleNewLabelLarge
        self.ValeurOptionTailleNewLabelNormal = ValeurOptionTailleNewLabelNormal
        self.ValeurOptionTailleNewLabelSmall = ValeurOptionTailleNewLabelSmall
        self.ValeurOptionTailleNewLabelVerySmall = ValeurOptionTailleNewLabelVerySmall
        self.ValeurOptionTailleNewLabelMinimal = ValeurOptionTailleNewLabelMinimal
        self.ValeurMinimumCoverTresLeger = ValeurMinimumCoverTresLeger
        self.ValeurMinimumCoverMoyen = ValeurMinimumCoverMoyen
        self.ValeurMinimumCoverLeger = ValeurMinimumCoverLeger
        self.ValeurMaxBarMoralLabel = ValeurMaxBarMoralLabel
        self.ValeurMinAffichageBarMoralLabel = ValeurMinAffichageBarMoralLabel
        self.TempsAttenteAffichageIconeConflitQuartier = TempsAttenteAffichageIconeConflitQuartier
        self.TagDInfanteriePinned = TagDInfanteriePinned
        self.PaliersDeVitesse = PaliersDeVitesse
        self.PaliersDeResilience = PaliersDeResilience
        self.PaliersDOptique = PaliersDOptique
        self.PaliersDOptiqueDAltitude = PaliersDOptiqueDAltitude
        self.PaliersDeDissimulation = PaliersDeDissimulation
        self.PaliersDAgiliteGRU = PaliersDAgiliteGRU
        self.PlatingAndApDisplayFactor = PlatingAndApDisplayFactor
        self.NomDAffichageDesUnitesNonIdentifiees = NomDAffichageDesUnitesNonIdentifiees
        self.MaxNbMergedUnitsInGroup = MaxNbMergedUnitsInGroup
        self.FactoriesWhichNeverCloseProductionMenuAfterValidation = FactoriesWhichNeverCloseProductionMenuAfterValidation
        self.UnitValueLimitForSurrender = UnitValueLimitForSurrender
        self.UpkeepReductionByIADifficulty = UpkeepReductionByIADifficulty
        self.DeckUnitExpLevelAdditiveModifierByIADifficulty = DeckUnitExpLevelAdditiveModifierByIADifficulty
        self.DeckUnitCountMultiplierByIADifficulty = DeckUnitCountMultiplierByIADifficulty
        self.RelativeBonusFluxByIADifficulty = RelativeBonusFluxByIADifficulty
        self.IncomeMultiplierInDestructionMode = IncomeMultiplierInDestructionMode
        self.IncomeMultiplierTokensInDestructionMode = IncomeMultiplierTokensInDestructionMode
        self.DefaultIncomeMultiplierIndexInDestructionMode = DefaultIncomeMultiplierIndexInDestructionMode
        self.TimeBeforeEarningCommandPointsFactorToAddByNbPlayers = TimeBeforeEarningCommandPointsFactorToAddByNbPlayers
        self.TimeBeforeEarningCommandPoints = TimeBeforeEarningCommandPoints
        self.IncomeMultiplier = IncomeMultiplier
        self.DefaultIncomeMultiplierIndex = DefaultIncomeMultiplierIndex
        self.BaseIncome = BaseIncome
        self.CoeffMoneyMaxIfUsingUpkeep = CoeffMoneyMaxIfUsingUpkeep
        self.ConquestPossibleScores = ConquestPossibleScores
        self.MoneyWinPerAllianceInConquestMode = MoneyWinPerAllianceInConquestMode
        self.MoneyWinLocalisationTokensInConquestMode = MoneyWinLocalisationTokensInConquestMode
        self.TimeBeforeEarningConquestPoints = TimeBeforeEarningConquestPoints
        self.DefaultMoneyWinPerAllianceRateInConquestMode = DefaultMoneyWinPerAllianceRateInConquestMode


class TRollParameters(BaseDescription):
    def __init__(self, MinimalHitChanceWithECM=None, SuccessiveHitModifiersTable=None, RangeModifiersTable=None, InterpolateRangeTable=None, DicesNumberFaces=None, PiercingThresholdBias=None, DistanceToleranceGRU=None):
        self.MinimalHitChanceWithECM = MinimalHitChanceWithECM
        self.SuccessiveHitModifiersTable = SuccessiveHitModifiersTable
        self.RangeModifiersTable = RangeModifiersTable
        self.InterpolateRangeTable = InterpolateRangeTable
        self.DicesNumberFaces = DicesNumberFaces
        self.PiercingThresholdBias = PiercingThresholdBias
        self.DistanceToleranceGRU = DistanceToleranceGRU
