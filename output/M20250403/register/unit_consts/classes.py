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


class TCriticalEffectModuleDescriptor(BaseDescription):
    def __init__(self, EffectsOnRear=None, EffectsOnSides=None, EffectsOnFront=None, TerrainCriticalEffectTimer=None, Bounds=None, RicochetEffectsOnTop=None, RicochetEffectsOnRear=None, RicochetEffectsOnSides=None, RicochetEffectsOnFront=None, PierceEffectsOnTop=None, PierceEffectsOnRear=None, PierceEffectsOnSides=None, PierceEffectsOnFront=None, EffectsOnTop=None, EffectsFromTerrain=None):
        self.EffectsOnRear = EffectsOnRear
        self.EffectsOnSides = EffectsOnSides
        self.EffectsOnFront = EffectsOnFront
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
        self.EffectsFromTerrain = EffectsFromTerrain


class TemplateCriticalEffectModule_GroundUnit(BaseDescription):
    def __init__(self, PackEffetCritique=None, EffectsFromTerrain=None):
        self.PackEffetCritique = PackEffetCritique
        self.EffectsFromTerrain = EffectsFromTerrain
