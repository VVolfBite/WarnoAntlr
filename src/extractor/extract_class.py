from src.extractor.base_class import BaseDescription


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


class TAirplaneConstantesModernWarfareDescriptor(BaseDescription):
    def __init__(
        self,
        TempsEntreDeuxDecollagesEnSecondes=None,
        UtiliserArmesPendantEvac=None,
        EvacuationAltitudeGRU=None,
        EvacWinchesterToutesLesArmesPrincipales=None,
        FrontLandingGearMeshNodeName=None,
        BackLandingGearMeshNodeName=None,
    ):
        self.TempsEntreDeuxDecollagesEnSecondes = TempsEntreDeuxDecollagesEnSecondes
        self.UtiliserArmesPendantEvac = UtiliserArmesPendantEvac
        self.EvacuationAltitudeGRU = EvacuationAltitudeGRU
        self.EvacWinchesterToutesLesArmesPrincipales = (
            EvacWinchesterToutesLesArmesPrincipales
        )
        self.FrontLandingGearMeshNodeName = FrontLandingGearMeshNodeName
        self.BackLandingGearMeshNodeName = BackLandingGearMeshNodeName

    def __repr__(self):
        return (
            f"<TAirplaneConstantesModernWarfareDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "TempsEntreDeuxDecollagesEnSecondes",
                        "UtiliserArmesPendantEvac",
                        "EvacuationAltitudeGRU",
                        "EvacWinchesterToutesLesArmesPrincipales",
                        "FrontLandingGearMeshNodeName",
                        "BackLandingGearMeshNodeName",
                    ]
                ]
            )
            + ">"
        )


class TRoutConstants(BaseDescription):
    def __init__(
        self,
        TestMoralNombreFacesDes=None,
        TempsEntreDeuxTestsMoralSeuilSuppression=None,
        TempsEntreDeuxTestsMoralPertePV=None,
        EffetConditionSuppression=None,
        LanceTestMoralSeuilSuppression=None,
        EffetAppliqueSuppression=None,
        LanceTestMoralPertePV=None,
        TestMoralNombreDes=None,
        TestMoralSeuil=None,
        SortieSeuilSuppression=None,
    ):
        self.TestMoralNombreFacesDes = TestMoralNombreFacesDes
        self.TempsEntreDeuxTestsMoralSeuilSuppression = (
            TempsEntreDeuxTestsMoralSeuilSuppression
        )
        self.TempsEntreDeuxTestsMoralPertePV = TempsEntreDeuxTestsMoralPertePV
        self.EffetConditionSuppression = EffetConditionSuppression
        self.LanceTestMoralSeuilSuppression = LanceTestMoralSeuilSuppression
        self.EffetAppliqueSuppression = EffetAppliqueSuppression
        self.LanceTestMoralPertePV = LanceTestMoralPertePV
        self.TestMoralNombreDes = TestMoralNombreDes
        self.TestMoralSeuil = TestMoralSeuil
        self.SortieSeuilSuppression = SortieSeuilSuppression

    def __repr__(self):
        return (
            f"<TRoutConstants "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "TestMoralNombreFacesDes",
                        "TempsEntreDeuxTestsMoralSeuilSuppression",
                        "TempsEntreDeuxTestsMoralPertePV",
                        "EffetConditionSuppression",
                        "LanceTestMoralSeuilSuppression",
                        "EffetAppliqueSuppression",
                        "LanceTestMoralPertePV",
                        "TestMoralNombreDes",
                        "TestMoralSeuil",
                        "SortieSeuilSuppression",
                    ]
                ]
            )
            + ">"
        )


class TEvaluationMenaceConstantesDescriptor(BaseDescription):
    def __init__(
        self,
        EscapeRadiusGRU=None,
        DureeDeMemoireDeLaMenaceEnSecondes=None,
        CercleMenaceGRU=None,
        ConsidererLesMenacesEnMouvementCommeDirectes=None,
    ):
        self.EscapeRadiusGRU = EscapeRadiusGRU
        self.DureeDeMemoireDeLaMenaceEnSecondes = DureeDeMemoireDeLaMenaceEnSecondes
        self.CercleMenaceGRU = CercleMenaceGRU
        self.ConsidererLesMenacesEnMouvementCommeDirectes = (
            ConsidererLesMenacesEnMouvementCommeDirectes
        )

    def __repr__(self):
        return (
            f"<TEvaluationMenaceConstantesDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "EscapeRadiusGRU",
                        "DureeDeMemoireDeLaMenaceEnSecondes",
                        "CercleMenaceGRU",
                        "ConsidererLesMenacesEnMouvementCommeDirectes",
                    ]
                ]
            )
            + ">"
        )


class TSpecificFactoryResources(BaseDescription):
    def __init__(self, FactoryDescriptions=None, FactoryDisplayOrder=None):
        self.FactoryDescriptions = FactoryDescriptions
        self.FactoryDisplayOrder = FactoryDisplayOrder

    def __repr__(self):
        return (
            f"<TSpecificFactoryResources "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["FactoryDescriptions", "FactoryDisplayOrder"]
                ]
            )
            + ">"
        )


class TSpecificFactoryDescription(BaseDescription):
    def __init__(
        self,
        FactoryHintTitle=None,
        FactoryHintBody=None,
        FactoryName=None,
        FactoryHintExtended=None,
    ):
        self.FactoryHintTitle = FactoryHintTitle
        self.FactoryHintBody = FactoryHintBody
        self.FactoryName = FactoryName
        self.FactoryHintExtended = FactoryHintExtended

    def __repr__(self):
        return (
            f"<TSpecificFactoryDescription "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "FactoryHintTitle",
                        "FactoryHintBody",
                        "FactoryName",
                        "FactoryHintExtended",
                    ]
                ]
            )
            + ">"
        )


class TActionPointConsumptionGridConstantsDescriptor(BaseDescription):
    def __init__(
        self,
        TailleDeCaseApproximativeGRU=None,
        EpaisseurDeLaCourbe=None,
        TerrainsBloquants=None,
        CouleurDeLaCourbe=None,
        TerrainsRalentisseurs=None,
    ):
        self.TailleDeCaseApproximativeGRU = TailleDeCaseApproximativeGRU
        self.EpaisseurDeLaCourbe = EpaisseurDeLaCourbe
        self.TerrainsBloquants = TerrainsBloquants
        self.CouleurDeLaCourbe = CouleurDeLaCourbe
        self.TerrainsRalentisseurs = TerrainsRalentisseurs

    def __repr__(self):
        return (
            f"<TActionPointConsumptionGridConstantsDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "TailleDeCaseApproximativeGRU",
                        "EpaisseurDeLaCourbe",
                        "TerrainsBloquants",
                        "CouleurDeLaCourbe",
                        "TerrainsRalentisseurs",
                    ]
                ]
            )
            + ">"
        )


class TTunableConstante(BaseDescription):
    def __init__(
        self,
        WithdrawalDuration=None,
        ShowroomMinSoldiersPerLine=None,
        DefaultTimeLimitInMinutes=None,
        TagBloquantLeMoveAndAttack=None,
        Color_ObserverDebugOutline=None,
        ForcerMarcheAvantPourAttaquer=None,
        AllowMultipleBuildingSelection=None,
        CadavreOffsetMax=None,
        MaxPullDistanceGRU=None,
        TempsEnSecondesEntreDeuxSmokeAutomatiques=None,
        AutoSmokeQuandRatioPvInferieurA=None,
        LargeurRouteGRU=None,
        RelativeScanningPositionGRU=None,
        ResaleDistanceGRU=None,
        Persistance_Bruit=None,
        TacticVictoryLevelConstantes=None,
        TimerRechercheDeCibleRiposte=None,
        EfficiencyShotSearchDistanceTolerance=None,
        CadavreOffsetMin=None,
        TimeLimitTable=None,
        MaxTerrainAngleForLanding=None,
        BaseAttackingAllianceNum=None,
        UtiliserMouvementRapideParDefaut=None,
        TagControleZone=None,
        DeploymentDuration=None,
        StunEffectDuration=None,
        DefaultGhostColors=None,
        AllowGhostCrossUnitSelection=None,
        FumigeneAlphaGhost=None,
        LaunchDeathAmmoOutmap=None,
        TempsAutoriseHorsMondePourMissileSansCible=None,
        DistancePourDeclencherMarcheArriereGRU=None,
        ShowroomOffsetBetweenLines=None,
        DureeRetraitControleZone=None,
        DistanceCoherenceGRU=None,
        PerteDeSuppressParPointDeVieEntierPerdu=None,
        OutmapShootPositionRelativeAltitude=None,
        EliminationWarningsDuration=None,
        MultiplicateurDistancePourBonusDissimulationGRU=None,
        Color_ObserverDebugFill=None,
        ConsidereUniteConcealmentSurTerrainAvecDissimulation=None,
        AutoCover_DistanceMaxEntreLesChecksDeTerrainsGRU=None,
        TagRadioArtillerie=None,
        TireursIgnoreesPourLaFuite=None,
        ReductionDegatsSuppressDansVehicule=None,
        UnitPositionVerticalOffsetFromRoofGRU=None,
        Color_OutmapDispersionAreaOutline=None,
        DefaultAIDifficultyForPlayerReplacement=None,
        TagRadioJammed=None,
        ShowroomNumberOfLines=None,
        SuddenDeathTime=None,
        AllowMixedSelection=None,
        CanUseAlliedAllianceCorridors=None,
        CommanderRadiusEffectByLevelGRU=None,
        RotationLignesDInfanterie=None,
        DureeDeploiementControleZone=None,
        ToleranceLargeurRoutePourMouvementsRapidesShiftes=None,
        AltitudeVolGRU=None,
        RatioPuissancePourRetaliation=None,
        AutoCover_TagEmpechantLAutocover=None,
        ShowroomOffsetBetweenSoldiers=None,
        DecalageDepuisLeCentreDansCouloirGRU=None,
        RapprocherFormationsSelonObstacles=None,
        PorteeRadioArtillerieGRU=None,
        ResalePriceRatio=None,
        FumigeneMaxCount=None,
        AngleArrierePourMarcheArriereEnDegre=None,
        DistanceMaxSmallMovementsInMeters=None,
        OutmapShootPositionPitch=None,
        MinimumNumberOfUnitToStayInGameWithoutCmdOrProductionInDestructionMode=None,
        OutmapShootPositionYaw=None,
        LandingPositionTimePredictionInSeconds=None,
        CooldownBeforeKillInSeconds=None,
        Color_OutmapDispersionAreaFill=None,
        CommanderEffect=None,
        TagDecrochage=None,
        MaxPullDistanceForAirplaneGRU=None,
        FumigeneTimeout=None,
    ):
        self.WithdrawalDuration = WithdrawalDuration
        self.ShowroomMinSoldiersPerLine = ShowroomMinSoldiersPerLine
        self.DefaultTimeLimitInMinutes = DefaultTimeLimitInMinutes
        self.TagBloquantLeMoveAndAttack = TagBloquantLeMoveAndAttack
        self.Color_ObserverDebugOutline = Color_ObserverDebugOutline
        self.ForcerMarcheAvantPourAttaquer = ForcerMarcheAvantPourAttaquer
        self.AllowMultipleBuildingSelection = AllowMultipleBuildingSelection
        self.CadavreOffsetMax = CadavreOffsetMax
        self.MaxPullDistanceGRU = MaxPullDistanceGRU
        self.TempsEnSecondesEntreDeuxSmokeAutomatiques = (
            TempsEnSecondesEntreDeuxSmokeAutomatiques
        )
        self.AutoSmokeQuandRatioPvInferieurA = AutoSmokeQuandRatioPvInferieurA
        self.LargeurRouteGRU = LargeurRouteGRU
        self.RelativeScanningPositionGRU = RelativeScanningPositionGRU
        self.ResaleDistanceGRU = ResaleDistanceGRU
        self.Persistance_Bruit = Persistance_Bruit
        self.TacticVictoryLevelConstantes = TacticVictoryLevelConstantes
        self.TimerRechercheDeCibleRiposte = TimerRechercheDeCibleRiposte
        self.EfficiencyShotSearchDistanceTolerance = (
            EfficiencyShotSearchDistanceTolerance
        )
        self.CadavreOffsetMin = CadavreOffsetMin
        self.TimeLimitTable = TimeLimitTable
        self.MaxTerrainAngleForLanding = MaxTerrainAngleForLanding
        self.BaseAttackingAllianceNum = BaseAttackingAllianceNum
        self.UtiliserMouvementRapideParDefaut = UtiliserMouvementRapideParDefaut
        self.TagControleZone = TagControleZone
        self.DeploymentDuration = DeploymentDuration
        self.StunEffectDuration = StunEffectDuration
        self.DefaultGhostColors = DefaultGhostColors
        self.AllowGhostCrossUnitSelection = AllowGhostCrossUnitSelection
        self.FumigeneAlphaGhost = FumigeneAlphaGhost
        self.LaunchDeathAmmoOutmap = LaunchDeathAmmoOutmap
        self.TempsAutoriseHorsMondePourMissileSansCible = (
            TempsAutoriseHorsMondePourMissileSansCible
        )
        self.DistancePourDeclencherMarcheArriereGRU = (
            DistancePourDeclencherMarcheArriereGRU
        )
        self.ShowroomOffsetBetweenLines = ShowroomOffsetBetweenLines
        self.DureeRetraitControleZone = DureeRetraitControleZone
        self.DistanceCoherenceGRU = DistanceCoherenceGRU
        self.PerteDeSuppressParPointDeVieEntierPerdu = (
            PerteDeSuppressParPointDeVieEntierPerdu
        )
        self.OutmapShootPositionRelativeAltitude = OutmapShootPositionRelativeAltitude
        self.EliminationWarningsDuration = EliminationWarningsDuration
        self.MultiplicateurDistancePourBonusDissimulationGRU = (
            MultiplicateurDistancePourBonusDissimulationGRU
        )
        self.Color_ObserverDebugFill = Color_ObserverDebugFill
        self.ConsidereUniteConcealmentSurTerrainAvecDissimulation = (
            ConsidereUniteConcealmentSurTerrainAvecDissimulation
        )
        self.AutoCover_DistanceMaxEntreLesChecksDeTerrainsGRU = (
            AutoCover_DistanceMaxEntreLesChecksDeTerrainsGRU
        )
        self.TagRadioArtillerie = TagRadioArtillerie
        self.TireursIgnoreesPourLaFuite = TireursIgnoreesPourLaFuite
        self.ReductionDegatsSuppressDansVehicule = ReductionDegatsSuppressDansVehicule
        self.UnitPositionVerticalOffsetFromRoofGRU = (
            UnitPositionVerticalOffsetFromRoofGRU
        )
        self.Color_OutmapDispersionAreaOutline = Color_OutmapDispersionAreaOutline
        self.DefaultAIDifficultyForPlayerReplacement = (
            DefaultAIDifficultyForPlayerReplacement
        )
        self.TagRadioJammed = TagRadioJammed
        self.ShowroomNumberOfLines = ShowroomNumberOfLines
        self.SuddenDeathTime = SuddenDeathTime
        self.AllowMixedSelection = AllowMixedSelection
        self.CanUseAlliedAllianceCorridors = CanUseAlliedAllianceCorridors
        self.CommanderRadiusEffectByLevelGRU = CommanderRadiusEffectByLevelGRU
        self.RotationLignesDInfanterie = RotationLignesDInfanterie
        self.DureeDeploiementControleZone = DureeDeploiementControleZone
        self.ToleranceLargeurRoutePourMouvementsRapidesShiftes = (
            ToleranceLargeurRoutePourMouvementsRapidesShiftes
        )
        self.AltitudeVolGRU = AltitudeVolGRU
        self.RatioPuissancePourRetaliation = RatioPuissancePourRetaliation
        self.AutoCover_TagEmpechantLAutocover = AutoCover_TagEmpechantLAutocover
        self.ShowroomOffsetBetweenSoldiers = ShowroomOffsetBetweenSoldiers
        self.DecalageDepuisLeCentreDansCouloirGRU = DecalageDepuisLeCentreDansCouloirGRU
        self.RapprocherFormationsSelonObstacles = RapprocherFormationsSelonObstacles
        self.PorteeRadioArtillerieGRU = PorteeRadioArtillerieGRU
        self.ResalePriceRatio = ResalePriceRatio
        self.FumigeneMaxCount = FumigeneMaxCount
        self.AngleArrierePourMarcheArriereEnDegre = AngleArrierePourMarcheArriereEnDegre
        self.DistanceMaxSmallMovementsInMeters = DistanceMaxSmallMovementsInMeters
        self.OutmapShootPositionPitch = OutmapShootPositionPitch
        self.MinimumNumberOfUnitToStayInGameWithoutCmdOrProductionInDestructionMode = (
            MinimumNumberOfUnitToStayInGameWithoutCmdOrProductionInDestructionMode
        )
        self.OutmapShootPositionYaw = OutmapShootPositionYaw
        self.LandingPositionTimePredictionInSeconds = (
            LandingPositionTimePredictionInSeconds
        )
        self.CooldownBeforeKillInSeconds = CooldownBeforeKillInSeconds
        self.Color_OutmapDispersionAreaFill = Color_OutmapDispersionAreaFill
        self.CommanderEffect = CommanderEffect
        self.TagDecrochage = TagDecrochage
        self.MaxPullDistanceForAirplaneGRU = MaxPullDistanceForAirplaneGRU
        self.FumigeneTimeout = FumigeneTimeout

    def __repr__(self):
        return (
            f"<TTunableConstante "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "WithdrawalDuration",
                        "ShowroomMinSoldiersPerLine",
                        "DefaultTimeLimitInMinutes",
                        "TagBloquantLeMoveAndAttack",
                        "Color_ObserverDebugOutline",
                        "ForcerMarcheAvantPourAttaquer",
                        "AllowMultipleBuildingSelection",
                        "CadavreOffsetMax",
                        "MaxPullDistanceGRU",
                        "TempsEnSecondesEntreDeuxSmokeAutomatiques",
                        "AutoSmokeQuandRatioPvInferieurA",
                        "LargeurRouteGRU",
                        "RelativeScanningPositionGRU",
                        "ResaleDistanceGRU",
                        "Persistance_Bruit",
                        "TacticVictoryLevelConstantes",
                        "TimerRechercheDeCibleRiposte",
                        "EfficiencyShotSearchDistanceTolerance",
                        "CadavreOffsetMin",
                        "TimeLimitTable",
                        "MaxTerrainAngleForLanding",
                        "BaseAttackingAllianceNum",
                        "UtiliserMouvementRapideParDefaut",
                        "TagControleZone",
                        "DeploymentDuration",
                        "StunEffectDuration",
                        "DefaultGhostColors",
                        "AllowGhostCrossUnitSelection",
                        "FumigeneAlphaGhost",
                        "LaunchDeathAmmoOutmap",
                        "TempsAutoriseHorsMondePourMissileSansCible",
                        "DistancePourDeclencherMarcheArriereGRU",
                        "ShowroomOffsetBetweenLines",
                        "DureeRetraitControleZone",
                        "DistanceCoherenceGRU",
                        "PerteDeSuppressParPointDeVieEntierPerdu",
                        "OutmapShootPositionRelativeAltitude",
                        "EliminationWarningsDuration",
                        "MultiplicateurDistancePourBonusDissimulationGRU",
                        "Color_ObserverDebugFill",
                        "ConsidereUniteConcealmentSurTerrainAvecDissimulation",
                        "AutoCover_DistanceMaxEntreLesChecksDeTerrainsGRU",
                        "TagRadioArtillerie",
                        "TireursIgnoreesPourLaFuite",
                        "ReductionDegatsSuppressDansVehicule",
                        "UnitPositionVerticalOffsetFromRoofGRU",
                        "Color_OutmapDispersionAreaOutline",
                        "DefaultAIDifficultyForPlayerReplacement",
                        "TagRadioJammed",
                        "ShowroomNumberOfLines",
                        "SuddenDeathTime",
                        "AllowMixedSelection",
                        "CanUseAlliedAllianceCorridors",
                        "CommanderRadiusEffectByLevelGRU",
                        "RotationLignesDInfanterie",
                        "DureeDeploiementControleZone",
                        "ToleranceLargeurRoutePourMouvementsRapidesShiftes",
                        "AltitudeVolGRU",
                        "RatioPuissancePourRetaliation",
                        "AutoCover_TagEmpechantLAutocover",
                        "ShowroomOffsetBetweenSoldiers",
                        "DecalageDepuisLeCentreDansCouloirGRU",
                        "RapprocherFormationsSelonObstacles",
                        "PorteeRadioArtillerieGRU",
                        "ResalePriceRatio",
                        "FumigeneMaxCount",
                        "AngleArrierePourMarcheArriereEnDegre",
                        "DistanceMaxSmallMovementsInMeters",
                        "OutmapShootPositionPitch",
                        "MinimumNumberOfUnitToStayInGameWithoutCmdOrProductionInDestructionMode",
                        "OutmapShootPositionYaw",
                        "LandingPositionTimePredictionInSeconds",
                        "CooldownBeforeKillInSeconds",
                        "Color_OutmapDispersionAreaFill",
                        "CommanderEffect",
                        "TagDecrochage",
                        "MaxPullDistanceForAirplaneGRU",
                        "FumigeneTimeout",
                    ]
                ]
            )
            + ">"
        )


class TGhostColors(BaseDescription):
    def __init__(self, GhostBlends=None, GhostColor=None, GhostAlphas=None):
        self.GhostBlends = GhostBlends
        self.GhostColor = GhostColor
        self.GhostAlphas = GhostAlphas

    def __repr__(self):
        return (
            f"<TGhostColors "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["GhostBlends", "GhostColor", "GhostAlphas"]
                ]
            )
            + ">"
        )


class TVictoryLevelConstantes(BaseDescription):
    def __init__(
        self,
        PalierVictoireMineure=None,
        PalierVictoireMajeure=None,
        PalierVictoireTotale=None,
    ):
        self.PalierVictoireMineure = PalierVictoireMineure
        self.PalierVictoireMajeure = PalierVictoireMajeure
        self.PalierVictoireTotale = PalierVictoireTotale

    def __repr__(self):
        return (
            f"<TVictoryLevelConstantes "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "PalierVictoireMineure",
                        "PalierVictoireMajeure",
                        "PalierVictoireTotale",
                    ]
                ]
            )
            + ">"
        )


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


class TWargameTunableConstante(BaseDescription):
    def __init__(
        self,
        IncomeMultiplierTokensInDestructionMode=None,
        MaxNbMergedUnitsInGroup=None,
        PlatingAndApDisplayFactor=None,
        ValeurMinAffichageBarMoralLabel=None,
        OrdersAcceptedByTransporterIfTransportedUnitsCanDo=None,
        UpkeepPercentAvailableSettings=None,
        TimeBeforeEarningConquestPoints=None,
        RelativeBonusFluxByIADifficulty=None,
        InfantryTrenchDepthGRU=None,
        UpkeepReductionByIADifficulty=None,
        CommandUnitToSpawnForNation=None,
        DefaultMoneyWinPerAllianceRateInConquestMode=None,
        PaliersDOptique=None,
        BaseIncome=None,
        ValeurMinimumCoverLeger=None,
        DeckUnitExpLevelAdditiveModifierByIADifficulty=None,
        TagDInfanteriePinned=None,
        ValeurMinimumCoverMoyen=None,
        DefaultIncomeMultiplierIndexInDestructionMode=None,
        ValeurOptionTailleNewLabelSmall=None,
        TimeBeforeEarningCommandPointsFactorToAddByNbPlayers=None,
        WargameBuildingAllowedTerrainsMask=None,
        OrderBlockedWhenOutOfFuel=None,
        ValeurOptionTailleNewLabelVeryLarge=None,
        IncomeMultiplier=None,
        VictoryTypeDestructionLevelsTable=None,
        PaliersDAgiliteGRU=None,
        MoneyWinLocalisationTokensInConquestMode=None,
        DissimulationEnumToValue=None,
        CoeffMoneyMaxIfUsingUpkeep=None,
        AmphibiousSpawnLandSeaRatio=None,
        ValeurOptionTailleNewLabelNormal=None,
        PaliersDeDissimulation=None,
        ValeurOptionTailleNewLabelVerySmall=None,
        FactoriesWhichNeverCloseProductionMenuAfterValidation=None,
        PaliersDOptiqueDAltitude=None,
        ConquestPointsDefaultIndex=None,
        TempsAttenteAffichageIconeConflitQuartier=None,
        ValeurMinimumCoverTresLeger=None,
        DeckUnitCountMultiplierByIADifficulty=None,
        UpkeepPercentDefaultSetting=None,
        ConquestPossibleScores=None,
        ArgentInitialSetting=None,
        ValeurOptionTailleNewLabelMinimal=None,
        PaliersDeVitesse=None,
        DefaultIncomeMultiplierIndex=None,
        NomDAffichageDesUnitesNonIdentifiees=None,
        ValeurMaxBarMoralLabel=None,
        DefaultArgentInitial=None,
        TimeBeforeEarningCommandPoints=None,
        UnitValueLimitForSurrender=None,
        ValeurOptionTailleNewLabelLarge=None,
        MoneyWinPerAllianceInConquestMode=None,
        PaliersDeResilience=None,
        ArgentInitialMinimumPourGererLIA=None,
        DestructionScoreToReachSetting=None,
        IncomeMultiplierInDestructionMode=None,
        CommandUnitToSpawnOverWaterForNation=None,
    ):
        self.IncomeMultiplierTokensInDestructionMode = (
            IncomeMultiplierTokensInDestructionMode
        )
        self.MaxNbMergedUnitsInGroup = MaxNbMergedUnitsInGroup
        self.PlatingAndApDisplayFactor = PlatingAndApDisplayFactor
        self.ValeurMinAffichageBarMoralLabel = ValeurMinAffichageBarMoralLabel
        self.OrdersAcceptedByTransporterIfTransportedUnitsCanDo = (
            OrdersAcceptedByTransporterIfTransportedUnitsCanDo
        )
        self.UpkeepPercentAvailableSettings = UpkeepPercentAvailableSettings
        self.TimeBeforeEarningConquestPoints = TimeBeforeEarningConquestPoints
        self.RelativeBonusFluxByIADifficulty = RelativeBonusFluxByIADifficulty
        self.InfantryTrenchDepthGRU = InfantryTrenchDepthGRU
        self.UpkeepReductionByIADifficulty = UpkeepReductionByIADifficulty
        self.CommandUnitToSpawnForNation = CommandUnitToSpawnForNation
        self.DefaultMoneyWinPerAllianceRateInConquestMode = (
            DefaultMoneyWinPerAllianceRateInConquestMode
        )
        self.PaliersDOptique = PaliersDOptique
        self.BaseIncome = BaseIncome
        self.ValeurMinimumCoverLeger = ValeurMinimumCoverLeger
        self.DeckUnitExpLevelAdditiveModifierByIADifficulty = (
            DeckUnitExpLevelAdditiveModifierByIADifficulty
        )
        self.TagDInfanteriePinned = TagDInfanteriePinned
        self.ValeurMinimumCoverMoyen = ValeurMinimumCoverMoyen
        self.DefaultIncomeMultiplierIndexInDestructionMode = (
            DefaultIncomeMultiplierIndexInDestructionMode
        )
        self.ValeurOptionTailleNewLabelSmall = ValeurOptionTailleNewLabelSmall
        self.TimeBeforeEarningCommandPointsFactorToAddByNbPlayers = (
            TimeBeforeEarningCommandPointsFactorToAddByNbPlayers
        )
        self.WargameBuildingAllowedTerrainsMask = WargameBuildingAllowedTerrainsMask
        self.OrderBlockedWhenOutOfFuel = OrderBlockedWhenOutOfFuel
        self.ValeurOptionTailleNewLabelVeryLarge = ValeurOptionTailleNewLabelVeryLarge
        self.IncomeMultiplier = IncomeMultiplier
        self.VictoryTypeDestructionLevelsTable = VictoryTypeDestructionLevelsTable
        self.PaliersDAgiliteGRU = PaliersDAgiliteGRU
        self.MoneyWinLocalisationTokensInConquestMode = (
            MoneyWinLocalisationTokensInConquestMode
        )
        self.DissimulationEnumToValue = DissimulationEnumToValue
        self.CoeffMoneyMaxIfUsingUpkeep = CoeffMoneyMaxIfUsingUpkeep
        self.AmphibiousSpawnLandSeaRatio = AmphibiousSpawnLandSeaRatio
        self.ValeurOptionTailleNewLabelNormal = ValeurOptionTailleNewLabelNormal
        self.PaliersDeDissimulation = PaliersDeDissimulation
        self.ValeurOptionTailleNewLabelVerySmall = ValeurOptionTailleNewLabelVerySmall
        self.FactoriesWhichNeverCloseProductionMenuAfterValidation = (
            FactoriesWhichNeverCloseProductionMenuAfterValidation
        )
        self.PaliersDOptiqueDAltitude = PaliersDOptiqueDAltitude
        self.ConquestPointsDefaultIndex = ConquestPointsDefaultIndex
        self.TempsAttenteAffichageIconeConflitQuartier = (
            TempsAttenteAffichageIconeConflitQuartier
        )
        self.ValeurMinimumCoverTresLeger = ValeurMinimumCoverTresLeger
        self.DeckUnitCountMultiplierByIADifficulty = (
            DeckUnitCountMultiplierByIADifficulty
        )
        self.UpkeepPercentDefaultSetting = UpkeepPercentDefaultSetting
        self.ConquestPossibleScores = ConquestPossibleScores
        self.ArgentInitialSetting = ArgentInitialSetting
        self.ValeurOptionTailleNewLabelMinimal = ValeurOptionTailleNewLabelMinimal
        self.PaliersDeVitesse = PaliersDeVitesse
        self.DefaultIncomeMultiplierIndex = DefaultIncomeMultiplierIndex
        self.NomDAffichageDesUnitesNonIdentifiees = NomDAffichageDesUnitesNonIdentifiees
        self.ValeurMaxBarMoralLabel = ValeurMaxBarMoralLabel
        self.DefaultArgentInitial = DefaultArgentInitial
        self.TimeBeforeEarningCommandPoints = TimeBeforeEarningCommandPoints
        self.UnitValueLimitForSurrender = UnitValueLimitForSurrender
        self.ValeurOptionTailleNewLabelLarge = ValeurOptionTailleNewLabelLarge
        self.MoneyWinPerAllianceInConquestMode = MoneyWinPerAllianceInConquestMode
        self.PaliersDeResilience = PaliersDeResilience
        self.ArgentInitialMinimumPourGererLIA = ArgentInitialMinimumPourGererLIA
        self.DestructionScoreToReachSetting = DestructionScoreToReachSetting
        self.IncomeMultiplierInDestructionMode = IncomeMultiplierInDestructionMode
        self.CommandUnitToSpawnOverWaterForNation = CommandUnitToSpawnOverWaterForNation

    def __repr__(self):
        return (
            f"<TWargameTunableConstante "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "IncomeMultiplierTokensInDestructionMode",
                        "MaxNbMergedUnitsInGroup",
                        "PlatingAndApDisplayFactor",
                        "ValeurMinAffichageBarMoralLabel",
                        "OrdersAcceptedByTransporterIfTransportedUnitsCanDo",
                        "UpkeepPercentAvailableSettings",
                        "TimeBeforeEarningConquestPoints",
                        "RelativeBonusFluxByIADifficulty",
                        "InfantryTrenchDepthGRU",
                        "UpkeepReductionByIADifficulty",
                        "CommandUnitToSpawnForNation",
                        "DefaultMoneyWinPerAllianceRateInConquestMode",
                        "PaliersDOptique",
                        "BaseIncome",
                        "ValeurMinimumCoverLeger",
                        "DeckUnitExpLevelAdditiveModifierByIADifficulty",
                        "TagDInfanteriePinned",
                        "ValeurMinimumCoverMoyen",
                        "DefaultIncomeMultiplierIndexInDestructionMode",
                        "ValeurOptionTailleNewLabelSmall",
                        "TimeBeforeEarningCommandPointsFactorToAddByNbPlayers",
                        "WargameBuildingAllowedTerrainsMask",
                        "OrderBlockedWhenOutOfFuel",
                        "ValeurOptionTailleNewLabelVeryLarge",
                        "IncomeMultiplier",
                        "VictoryTypeDestructionLevelsTable",
                        "PaliersDAgiliteGRU",
                        "MoneyWinLocalisationTokensInConquestMode",
                        "DissimulationEnumToValue",
                        "CoeffMoneyMaxIfUsingUpkeep",
                        "AmphibiousSpawnLandSeaRatio",
                        "ValeurOptionTailleNewLabelNormal",
                        "PaliersDeDissimulation",
                        "ValeurOptionTailleNewLabelVerySmall",
                        "FactoriesWhichNeverCloseProductionMenuAfterValidation",
                        "PaliersDOptiqueDAltitude",
                        "ConquestPointsDefaultIndex",
                        "TempsAttenteAffichageIconeConflitQuartier",
                        "ValeurMinimumCoverTresLeger",
                        "DeckUnitCountMultiplierByIADifficulty",
                        "UpkeepPercentDefaultSetting",
                        "ConquestPossibleScores",
                        "ArgentInitialSetting",
                        "ValeurOptionTailleNewLabelMinimal",
                        "PaliersDeVitesse",
                        "DefaultIncomeMultiplierIndex",
                        "NomDAffichageDesUnitesNonIdentifiees",
                        "ValeurMaxBarMoralLabel",
                        "DefaultArgentInitial",
                        "TimeBeforeEarningCommandPoints",
                        "UnitValueLimitForSurrender",
                        "ValeurOptionTailleNewLabelLarge",
                        "MoneyWinPerAllianceInConquestMode",
                        "PaliersDeResilience",
                        "ArgentInitialMinimumPourGererLIA",
                        "DestructionScoreToReachSetting",
                        "IncomeMultiplierInDestructionMode",
                        "CommandUnitToSpawnOverWaterForNation",
                    ]
                ]
            )
            + ">"
        )


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


class TSupplyDescriptor(BaseDescription):
    def __init__(
        self,
        FuelSupplyBySecond=None,
        FeedbackDrawer=None,
        SupplySupplyBySecond=None,
        AmmunitionSupplyBySecond=None,
        CriticsSupplyCostBySecond=None,
        DefaultSupplyRangeGRU=None,
        HealthSupplyCostBySecond=None,
        SupplySupplyCostBySecond=None,
        FuelSupplyCostBySecond=None,
        CriticsSupplyBySecond=None,
        HealthSupplyBySecond=None,
    ):
        self.FuelSupplyBySecond = FuelSupplyBySecond
        self.FeedbackDrawer = FeedbackDrawer
        self.SupplySupplyBySecond = SupplySupplyBySecond
        self.AmmunitionSupplyBySecond = AmmunitionSupplyBySecond
        self.CriticsSupplyCostBySecond = CriticsSupplyCostBySecond
        self.DefaultSupplyRangeGRU = DefaultSupplyRangeGRU
        self.HealthSupplyCostBySecond = HealthSupplyCostBySecond
        self.SupplySupplyCostBySecond = SupplySupplyCostBySecond
        self.FuelSupplyCostBySecond = FuelSupplyCostBySecond
        self.CriticsSupplyBySecond = CriticsSupplyBySecond
        self.HealthSupplyBySecond = HealthSupplyBySecond

    def __repr__(self):
        return (
            f"<TSupplyDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "FuelSupplyBySecond",
                        "FeedbackDrawer",
                        "SupplySupplyBySecond",
                        "AmmunitionSupplyBySecond",
                        "CriticsSupplyCostBySecond",
                        "DefaultSupplyRangeGRU",
                        "HealthSupplyCostBySecond",
                        "SupplySupplyCostBySecond",
                        "FuelSupplyCostBySecond",
                        "CriticsSupplyBySecond",
                        "HealthSupplyBySecond",
                    ]
                ]
            )
            + ">"
        )


class TSupplyFeedbackDrawer(BaseDescription):
    def __init__(
        self, FeedbackDescriptor=None, ZOffset=None, LineColor=None, LineThickness=None
    ):
        self.FeedbackDescriptor = FeedbackDescriptor
        self.ZOffset = ZOffset
        self.LineColor = LineColor
        self.LineThickness = LineThickness

    def __repr__(self):
        return (
            f"<TSupplyFeedbackDrawer "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "FeedbackDescriptor",
                        "ZOffset",
                        "LineColor",
                        "LineThickness",
                    ]
                ]
            )
            + ">"
        )


class TSupplyFeedbackDescriptor(BaseDescription):
    def __init__(self, FeedbackScreenResilienceDuration=None, FeedbackFadeOutTime=None):
        self.FeedbackScreenResilienceDuration = FeedbackScreenResilienceDuration
        self.FeedbackFadeOutTime = FeedbackFadeOutTime

    def __repr__(self):
        return (
            f"<TSupplyFeedbackDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "FeedbackScreenResilienceDuration",
                        "FeedbackFadeOutTime",
                    ]
                ]
            )
            + ">"
        )


class TTransportConstantesDescriptor(BaseDescription):
    def __init__(self, MaximalSpeedToUnload=None):
        self.MaximalSpeedToUnload = MaximalSpeedToUnload

    def __repr__(self):
        return (
            f"<TTransportConstantesDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["MaximalSpeedToUnload"]]
            )
            + ">"
        )


class TVisionConstantesDescriptor(BaseDescription):
    def __init__(self, PorteeDeVisionGlobaleGRU=None):
        self.PorteeDeVisionGlobaleGRU = PorteeDeVisionGlobaleGRU

    def __repr__(self):
        return (
            f"<TVisionConstantesDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["PorteeDeVisionGlobaleGRU"]
                ]
            )
            + ">"
        )


class TWeaponConstantsDescriptor(BaseDescription):
    def __init__(
        self,
        DefaultStressMultiplier=None,
        SuppressDamagePerFamily=None,
        PierceBonusForDamageFamilies=None,
        EfficientShotMinPenetration=None,
        DefaultMimeticProjectile=None,
        DefaultSuppressDamage=None,
        BlindagesToIgnoreForDamageFamilies=None,
        DefensiveSmokeRangeMaxGRU=None,
        ResistanceFamiliesNeedPiercing=None,
        StressMultiplierPerDamageFamily=None,
        DamageTypeToMimeticProjectile=None,
        EfficientShotMinAccuracy=None,
        ResistanceToMimeticImpact=None,
    ):
        self.DefaultStressMultiplier = DefaultStressMultiplier
        self.SuppressDamagePerFamily = SuppressDamagePerFamily
        self.PierceBonusForDamageFamilies = PierceBonusForDamageFamilies
        self.EfficientShotMinPenetration = EfficientShotMinPenetration
        self.DefaultMimeticProjectile = DefaultMimeticProjectile
        self.DefaultSuppressDamage = DefaultSuppressDamage
        self.BlindagesToIgnoreForDamageFamilies = BlindagesToIgnoreForDamageFamilies
        self.DefensiveSmokeRangeMaxGRU = DefensiveSmokeRangeMaxGRU
        self.ResistanceFamiliesNeedPiercing = ResistanceFamiliesNeedPiercing
        self.StressMultiplierPerDamageFamily = StressMultiplierPerDamageFamily
        self.DamageTypeToMimeticProjectile = DamageTypeToMimeticProjectile
        self.EfficientShotMinAccuracy = EfficientShotMinAccuracy
        self.ResistanceToMimeticImpact = ResistanceToMimeticImpact

    def __repr__(self):
        return (
            f"<TWeaponConstantsDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "DefaultStressMultiplier",
                        "SuppressDamagePerFamily",
                        "PierceBonusForDamageFamilies",
                        "EfficientShotMinPenetration",
                        "DefaultMimeticProjectile",
                        "DefaultSuppressDamage",
                        "BlindagesToIgnoreForDamageFamilies",
                        "DefensiveSmokeRangeMaxGRU",
                        "ResistanceFamiliesNeedPiercing",
                        "StressMultiplierPerDamageFamily",
                        "DamageTypeToMimeticProjectile",
                        "EfficientShotMinAccuracy",
                        "ResistanceToMimeticImpact",
                    ]
                ]
            )
            + ">"
        )


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


class TBombAttackStrategyDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TBombAttackStrategyDescriptor>"


class TDiveAttackStrategyDescriptor(BaseDescription):
    def __init__(
        self,
        MinDiveAlignmentDuration=None,
        MaxPitchForDiveInDegree=None,
        MinPitchForDiveInDegree=None,
    ):
        self.MinDiveAlignmentDuration = MinDiveAlignmentDuration
        self.MaxPitchForDiveInDegree = MaxPitchForDiveInDegree
        self.MinPitchForDiveInDegree = MinPitchForDiveInDegree

    def __repr__(self):
        return (
            f"<TDiveAttackStrategyDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "MinDiveAlignmentDuration",
                        "MaxPitchForDiveInDegree",
                        "MinPitchForDiveInDegree",
                    ]
                ]
            )
            + ">"
        )


class TDiveMissileAttackStrategyDescriptor(BaseDescription):
    def __init__(
        self,
        MinDiveAlignmentDuration=None,
        MaxPitchForDiveInDegree=None,
        MinPitchForDiveInDegree=None,
    ):
        self.MinDiveAlignmentDuration = MinDiveAlignmentDuration
        self.MaxPitchForDiveInDegree = MaxPitchForDiveInDegree
        self.MinPitchForDiveInDegree = MinPitchForDiveInDegree

    def __repr__(self):
        return (
            f"<TDiveMissileAttackStrategyDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "MinDiveAlignmentDuration",
                        "MaxPitchForDiveInDegree",
                        "MinPitchForDiveInDegree",
                    ]
                ]
            )
            + ">"
        )


class TDiveBombAttackStrategyDescriptor(BaseDescription):
    def __init__(
        self,
        DiveBombRecoveryDuration=None,
        MinPitchForDiveBombInDegree=None,
        PitchForDiveBombInDegree=None,
        MaxPitchForDiveBombInDegree=None,
    ):
        self.DiveBombRecoveryDuration = DiveBombRecoveryDuration
        self.MinPitchForDiveBombInDegree = MinPitchForDiveBombInDegree
        self.PitchForDiveBombInDegree = PitchForDiveBombInDegree
        self.MaxPitchForDiveBombInDegree = MaxPitchForDiveBombInDegree

    def __repr__(self):
        return (
            f"<TDiveBombAttackStrategyDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "DiveBombRecoveryDuration",
                        "MinPitchForDiveBombInDegree",
                        "PitchForDiveBombInDegree",
                        "MaxPitchForDiveBombInDegree",
                    ]
                ]
            )
            + ">"
        )


class TDogfightAttackStrategyDescriptor(BaseDescription):
    def __init__(
        self,
        SpeedRatioForAttackOnVerySlowAirplaneStrategy=None,
        SpeedRatioForAttackOnSlowAirplaneStrategy=None,
        AngleToFakeTargetPositionInDegree=None,
        MaxDistanceBetweenFighterAndTargetForLateralMoveOnSlowAirplaneStrategy=None,
        MinDistanceBetweenFighterAndTargetForAttackOnSlowAirplaneStrategy=None,
        MaxAngleToConsiderTargetAheadInDegree=None,
        MaxAngleDifferenceWithTargetInDegree=None,
    ):
        self.SpeedRatioForAttackOnVerySlowAirplaneStrategy = (
            SpeedRatioForAttackOnVerySlowAirplaneStrategy
        )
        self.SpeedRatioForAttackOnSlowAirplaneStrategy = (
            SpeedRatioForAttackOnSlowAirplaneStrategy
        )
        self.AngleToFakeTargetPositionInDegree = AngleToFakeTargetPositionInDegree
        self.MaxDistanceBetweenFighterAndTargetForLateralMoveOnSlowAirplaneStrategy = (
            MaxDistanceBetweenFighterAndTargetForLateralMoveOnSlowAirplaneStrategy
        )
        self.MinDistanceBetweenFighterAndTargetForAttackOnSlowAirplaneStrategy = (
            MinDistanceBetweenFighterAndTargetForAttackOnSlowAirplaneStrategy
        )
        self.MaxAngleToConsiderTargetAheadInDegree = (
            MaxAngleToConsiderTargetAheadInDegree
        )
        self.MaxAngleDifferenceWithTargetInDegree = MaxAngleDifferenceWithTargetInDegree

    def __repr__(self):
        return (
            f"<TDogfightAttackStrategyDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "SpeedRatioForAttackOnVerySlowAirplaneStrategy",
                        "SpeedRatioForAttackOnSlowAirplaneStrategy",
                        "AngleToFakeTargetPositionInDegree",
                        "MaxDistanceBetweenFighterAndTargetForLateralMoveOnSlowAirplaneStrategy",
                        "MinDistanceBetweenFighterAndTargetForAttackOnSlowAirplaneStrategy",
                        "MaxAngleToConsiderTargetAheadInDegree",
                        "MaxAngleDifferenceWithTargetInDegree",
                    ]
                ]
            )
            + ">"
        )


class TStukaNosediveAttackStrategyDescriptor(BaseDescription):
    def __init__(
        self,
        AgilityMultiplicator=None,
        DistanceNosediveGRU=None,
        WaypointDistanceFromTargetGRU=None,
    ):
        self.AgilityMultiplicator = AgilityMultiplicator
        self.DistanceNosediveGRU = DistanceNosediveGRU
        self.WaypointDistanceFromTargetGRU = WaypointDistanceFromTargetGRU

    def __repr__(self):
        return (
            f"<TStukaNosediveAttackStrategyDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "AgilityMultiplicator",
                        "DistanceNosediveGRU",
                        "WaypointDistanceFromTargetGRU",
                    ]
                ]
            )
            + ">"
        )


class TAirGroundMissileAttackStrategyDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TAirGroundMissileAttackStrategyDescriptor>"


class TWeaponTypePrioritiesHolder(BaseDescription):
    def __init__(
        self,
        Score_OutOfRange=None,
        WeaponTypes=None,
        DistanceToConsiderAsFarGRU=None,
        Score_OnRange=None,
    ):
        self.Score_OutOfRange = Score_OutOfRange
        self.WeaponTypes = WeaponTypes
        self.DistanceToConsiderAsFarGRU = DistanceToConsiderAsFarGRU
        self.Score_OnRange = Score_OnRange

    def __repr__(self):
        return (
            f"<TWeaponTypePrioritiesHolder "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "Score_OutOfRange",
                        "WeaponTypes",
                        "DistanceToConsiderAsFarGRU",
                        "Score_OnRange",
                    ]
                ]
            )
            + ">"
        )


class TWreckageConstantsDescriptor(BaseDescription):
    def __init__(
        self,
        ExploserQuandEcrase=None,
        DetruireQuandEcrase=None,
        MultiplicateurMasseObstacle=None,
    ):
        self.ExploserQuandEcrase = ExploserQuandEcrase
        self.DetruireQuandEcrase = DetruireQuandEcrase
        self.MultiplicateurMasseObstacle = MultiplicateurMasseObstacle

    def __repr__(self):
        return (
            f"<TWreckageConstantsDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "ExploserQuandEcrase",
                        "DetruireQuandEcrase",
                        "MultiplicateurMasseObstacle",
                    ]
                ]
            )
            + ">"
        )


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


class TCriticalEffectModuleDescriptor(BaseDescription):
    def __init__(
        self,
        PierceEffectsOnRear=None,
        RicochetEffectsOnRear=None,
        TerrainCriticalEffectTimer=None,
        PierceEffectsOnFront=None,
        Bounds=None,
        EffectsOnRear=None,
        EffectsOnSides=None,
        EffectsFromTerrain=None,
        EffectsOnFront=None,
        RicochetEffectsOnSides=None,
        PierceEffectsOnTop=None,
        RicochetEffectsOnTop=None,
        RicochetEffectsOnFront=None,
        EffectsOnTop=None,
        PierceEffectsOnSides=None,
    ):
        self.PierceEffectsOnRear = PierceEffectsOnRear
        self.RicochetEffectsOnRear = RicochetEffectsOnRear
        self.TerrainCriticalEffectTimer = TerrainCriticalEffectTimer
        self.PierceEffectsOnFront = PierceEffectsOnFront
        self.Bounds = Bounds
        self.EffectsOnRear = EffectsOnRear
        self.EffectsOnSides = EffectsOnSides
        self.EffectsFromTerrain = EffectsFromTerrain
        self.EffectsOnFront = EffectsOnFront
        self.RicochetEffectsOnSides = RicochetEffectsOnSides
        self.PierceEffectsOnTop = PierceEffectsOnTop
        self.RicochetEffectsOnTop = RicochetEffectsOnTop
        self.RicochetEffectsOnFront = RicochetEffectsOnFront
        self.EffectsOnTop = EffectsOnTop
        self.PierceEffectsOnSides = PierceEffectsOnSides

    def __repr__(self):
        return (
            f"<TCriticalEffectModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "PierceEffectsOnRear",
                        "RicochetEffectsOnRear",
                        "TerrainCriticalEffectTimer",
                        "PierceEffectsOnFront",
                        "Bounds",
                        "EffectsOnRear",
                        "EffectsOnSides",
                        "EffectsFromTerrain",
                        "EffectsOnFront",
                        "RicochetEffectsOnSides",
                        "PierceEffectsOnTop",
                        "RicochetEffectsOnTop",
                        "RicochetEffectsOnFront",
                        "EffectsOnTop",
                        "PierceEffectsOnSides",
                    ]
                ]
            )
            + ">"
        )


class AirplaneCriticalEffect_WingsDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_WingsDamaged "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_EngineOnFire(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_EngineOnFire "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_PropellerDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_PropellerDamaged "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_EngineDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_EngineDamaged "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_FloatCarburatorFailure(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_FloatCarburatorFailure "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_OilLeak(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_OilLeak "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_EngineOverheating(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_EngineOverheating "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_EngineStalling(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_EngineStalling "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_ElevatorDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_ElevatorDamaged "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_FuelTankLeaking(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_FuelTankLeaking "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_RadiatorDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_RadiatorDamaged "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_RadiatorOverheating(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_RadiatorOverheating "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_PilotInjured(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_PilotInjured "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_PilotPanicked(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_PilotPanicked "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_PilotUnconscious(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_PilotUnconscious "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_WeaponsJammed(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_WeaponsJammed "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_AileronDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_AileronDamaged "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_TailDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_TailDamaged "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_FuelTankOnFire(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_FuelTankOnFire "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class AirplaneCriticalEffect_RudderDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<AirplaneCriticalEffect_RudderDamaged "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class TemplateCriticalEffectModule_GroundUnit(BaseDescription):
    def __init__(self, EffectsFromTerrain=None, PackEffetCritique=None):
        self.EffectsFromTerrain = EffectsFromTerrain
        self.PackEffetCritique = PackEffetCritique

    def __repr__(self):
        return (
            f"<TemplateCriticalEffectModule_GroundUnit "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["EffectsFromTerrain", "PackEffetCritique"]
                ]
            )
            + ">"
        )


class HelicoCriticalEffect_HUD(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<HelicoCriticalEffect_HUD "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class HelicoCriticalEffect_CrewInjured(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<HelicoCriticalEffect_CrewInjured "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class HelicoCriticalEffect_MainRotorDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<HelicoCriticalEffect_MainRotorDamaged "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class HelicoCriticalEffect_Turbine_Engine_Failure(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<HelicoCriticalEffect_Turbine_Engine_Failure "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class HelicoCriticalEffect_turbineOnFire(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<HelicoCriticalEffect_turbineOnFire "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class HelicoCriticalEffect_FuelTankOnFire(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<HelicoCriticalEffect_FuelTankOnFire "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class HelicoCriticalEffect_FuelTankLeaking(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<HelicoCriticalEffect_FuelTankLeaking "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class HelicoCriticalEffect_WeaponsJammed(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<HelicoCriticalEffect_WeaponsJammed "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class HelicoCriticalEffect_Hydraulic_Fluid_Fire(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<HelicoCriticalEffect_Hydraulic_Fluid_Fire "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


class HelicoCriticalEffect_TailRotorDamaged(BaseDescription):
    def __init__(self, Roll=None):
        self.Roll = Roll

    def __repr__(self):
        return (
            f"<HelicoCriticalEffect_TailRotorDamaged "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Roll"]])
            + ">"
        )


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


class TPositionModuleDescriptor(BaseDescription):
    def __init__(self, InGeoDb=None):
        self.InGeoDb = InGeoDb

    def __repr__(self):
        return (
            f"<TPositionModuleDescriptor "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["InGeoDb"]])
            + ">"
        )


class TApparenceModelModuleDescriptor(BaseDescription):
    def __init__(self, ReferenceMesh=None, DefaultVisibility=None, Depiction=None):
        self.ReferenceMesh = ReferenceMesh
        self.DefaultVisibility = DefaultVisibility
        self.Depiction = Depiction

    def __repr__(self):
        return (
            f"<TApparenceModelModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ReferenceMesh", "DefaultVisibility", "Depiction"]
                ]
            )
            + ">"
        )


class Template_DescriptorFire_Depiction(BaseDescription):
    def __init__(self, Density=None, Radius=None, FX=None):
        self.Density = Density
        self.Radius = Radius
        self.FX = FX

    def __repr__(self):
        return (
            f"<Template_DescriptorFire_Depiction "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["Density", "Radius", "FX"]
                ]
            )
            + ">"
        )


class TFireModuleDescriptor(BaseDescription):
    def __init__(
        self,
        OverridenSpreadDescriptor=None,
        IsNewFireProbability=None,
        TimeToLive=None,
        IgniteDistricts=None,
        TimeBetweenBurns=None,
        TimeBeforeSpreading=None,
        TimeBeforeSpreadAttempt=None,
        RadiusGRU=None,
        AmmunitionForBurn=None,
        SmokeDescriptor=None,
        SpreadProbability=None,
    ):
        self.OverridenSpreadDescriptor = OverridenSpreadDescriptor
        self.IsNewFireProbability = IsNewFireProbability
        self.TimeToLive = TimeToLive
        self.IgniteDistricts = IgniteDistricts
        self.TimeBetweenBurns = TimeBetweenBurns
        self.TimeBeforeSpreading = TimeBeforeSpreading
        self.TimeBeforeSpreadAttempt = TimeBeforeSpreadAttempt
        self.RadiusGRU = RadiusGRU
        self.AmmunitionForBurn = AmmunitionForBurn
        self.SmokeDescriptor = SmokeDescriptor
        self.SpreadProbability = SpreadProbability

    def __repr__(self):
        return (
            f"<TFireModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "OverridenSpreadDescriptor",
                        "IsNewFireProbability",
                        "TimeToLive",
                        "IgniteDistricts",
                        "TimeBetweenBurns",
                        "TimeBeforeSpreading",
                        "TimeBeforeSpreadAttempt",
                        "RadiusGRU",
                        "AmmunitionForBurn",
                        "SmokeDescriptor",
                        "SpreadProbability",
                    ]
                ]
            )
            + ">"
        )


class TLinkTeamModuleDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TLinkTeamModuleDescriptor>"


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



class Template_DescriptorSmoke_Depiction(BaseDescription):
    def __init__(self, Height=None, Density=None, Radius=None):
        self.Height = Height
        self.Density = Density
        self.Radius = Radius

    def __repr__(self):
        return (
            f"<Template_DescriptorSmoke_Depiction "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["Height", "Density", "Radius"]
                ]
            )
            + ">"
        )


class TSmokeModuleDescriptor(BaseDescription):
    def __init__(self, TimeToLive=None, Terrain=None, RadiusGRU=None, AltitudeGRU=None):
        self.TimeToLive = TimeToLive
        self.Terrain = Terrain
        self.RadiusGRU = RadiusGRU
        self.AltitudeGRU = AltitudeGRU

    def __repr__(self):
        return (
            f"<TSmokeModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["TimeToLive", "Terrain", "RadiusGRU", "AltitudeGRU"]
                ]
            )
            + ">"
        )


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


class TDeckDescriptor(BaseDescription):
    def __init__(
        self,
        DeckCombatGroupList=None,
        DeckDivision=None,
        DeckName=None,
        DeckPackList=None,
        DeckIdentifier=None,
    ):
        self.DeckCombatGroupList = DeckCombatGroupList
        self.DeckDivision = DeckDivision
        self.DeckName = DeckName
        self.DeckPackList = DeckPackList
        self.DeckIdentifier = DeckIdentifier

    def __repr__(self):
        return (
            f"<TDeckDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "DeckCombatGroupList",
                        "DeckDivision",
                        "DeckName",
                        "DeckPackList",
                        "DeckIdentifier",
                    ]
                ]
            )
            + ">"
        )


class TDeckCombatGroupDescriptor(BaseDescription):
    def __init__(self, Name=None, SmartGroupList=None):
        self.Name = Name
        self.SmartGroupList = SmartGroupList

    def __repr__(self):
        return (
            f"<TDeckCombatGroupDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["Name", "SmartGroupList"]]
            )
            + ">"
        )


class TDeckSmartGroupDescriptor(BaseDescription):
    def __init__(self, Name=None, PackIndexUnitNumberList=None):
        self.Name = Name
        self.PackIndexUnitNumberList = PackIndexUnitNumberList

    def __repr__(self):
        return (
            f"<TDeckSmartGroupDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["Name", "PackIndexUnitNumberList"]
                ]
            )
            + ">"
        )


class TDeckDescriptorList(BaseDescription):
    def __init__(self, DeckListForIdentifier=None, DeckListForAutoFill=None):
        self.DeckListForIdentifier = DeckListForIdentifier
        self.DeckListForAutoFill = DeckListForAutoFill

    def __repr__(self):
        return (
            f"<TDeckDescriptorList "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["DeckListForIdentifier", "DeckListForAutoFill"]
                ]
            )
            + ">"
        )


class TDeckSerializer(BaseDescription):
    def __init__(self, UnitIds=None, DivisionIds=None):
        self.UnitIds = UnitIds
        self.DivisionIds = DivisionIds

    def __repr__(self):
        return (
            f"<TDeckSerializer "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["UnitIds", "DivisionIds"]]
            )
            + ">"
        )


class TDeckDivisionList(BaseDescription):
    def __init__(self, DivisionList=None):
        self.DivisionList = DivisionList

    def __repr__(self):
        return (
            f"<TDeckDivisionList "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["DivisionList"]])
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


class TResistanceTypeRTTI(BaseDescription):
    def __init__(self, Index=None, Family=None):
        self.Index = Index
        self.Family = Family

    def __repr__(self):
        return (
            f"<TResistanceTypeRTTI "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["Index", "Family"]]
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


class TModernWarfareDistanceMultiplierRollRuleDescriptor(BaseDescription):
    def __init__(
        self,
        MultiplicateurAPorteeMinimaleEnMouvement=None,
        MultiplicateurAPorteeMinimale=None,
        MultiplicateurAPorteeMaximale=None,
        MultiplicateurAPorteeMaximaleEnMouvement=None,
        ExposantEnMouvement=None,
        Exposant=None,
    ):
        self.MultiplicateurAPorteeMinimaleEnMouvement = (
            MultiplicateurAPorteeMinimaleEnMouvement
        )
        self.MultiplicateurAPorteeMinimale = MultiplicateurAPorteeMinimale
        self.MultiplicateurAPorteeMaximale = MultiplicateurAPorteeMaximale
        self.MultiplicateurAPorteeMaximaleEnMouvement = (
            MultiplicateurAPorteeMaximaleEnMouvement
        )
        self.ExposantEnMouvement = ExposantEnMouvement
        self.Exposant = Exposant

    def __repr__(self):
        return (
            f"<TModernWarfareDistanceMultiplierRollRuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "MultiplicateurAPorteeMinimaleEnMouvement",
                        "MultiplicateurAPorteeMinimale",
                        "MultiplicateurAPorteeMaximale",
                        "MultiplicateurAPorteeMaximaleEnMouvement",
                        "ExposantEnMouvement",
                        "Exposant",
                    ]
                ]
            )
            + ">"
        )


class BuildingApparenceModelModuleDescriptor(BaseDescription):
    def __init__(self, BlackHoleIdentifier=None, SymbolName=None):
        self.BlackHoleIdentifier = BlackHoleIdentifier
        self.SymbolName = SymbolName

    def __repr__(self):
        return (
            f"<BuildingApparenceModelModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["BlackHoleIdentifier", "SymbolName"]
                ]
            )
            + ">"
        )


class TCadavreGeneratorModuleDescriptor(BaseDescription):
    def __init__(self, CadavreDescriptor=None):
        self.CadavreDescriptor = CadavreDescriptor

    def __repr__(self):
        return (
            f"<TCadavreGeneratorModuleDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["CadavreDescriptor"]]
            )
            + ">"
        )


class TIAStratModuleDescriptor(BaseDescription):
    def __init__(self, DatabaseId=None, GameplayBehavior=None):
        self.DatabaseId = DatabaseId
        self.GameplayBehavior = GameplayBehavior

    def __repr__(self):
        return (
            f"<TIAStratModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["DatabaseId", "GameplayBehavior"]
                ]
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


class TTacticalLabelModuleDescriptor(BaseDescription):
    def __init__(
        self,
        IdentifiedTexture=None,
        MultiSelectionSortingOrder=None,
        NbSoldiers=None,
        PositionHeightOffset=None,
        UnidentifiedTexture=None,
    ):
        self.IdentifiedTexture = IdentifiedTexture
        self.MultiSelectionSortingOrder = MultiSelectionSortingOrder
        self.NbSoldiers = NbSoldiers
        self.PositionHeightOffset = PositionHeightOffset
        self.UnidentifiedTexture = UnidentifiedTexture

    def __repr__(self):
        return (
            f"<TTacticalLabelModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "IdentifiedTexture",
                        "MultiSelectionSortingOrder",
                        "NbSoldiers",
                        "PositionHeightOffset",
                        "UnidentifiedTexture",
                    ]
                ]
            )
            + ">"
        )


class TBUCKToolAlternativeValues_TUIValueTextureNameFromTEugBMutableInteger(
    BaseDescription
):
    def __init__(self, Values=None, CommandNameTrigger=None, Alterator=None):
        self.Values = Values
        self.CommandNameTrigger = CommandNameTrigger
        self.Alterator = Alterator

    def __repr__(self):
        return (
            f"<TBUCKToolAlternativeValues_TUIValueTextureNameFromTEugBMutableInteger "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["Values", "CommandNameTrigger", "Alterator"]
                ]
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


class TConditionTagRaisedInUnit(BaseDescription):
    def __init__(self, Tag=None, DescriptorId=None, Amount=None):
        self.Tag = Tag
        self.DescriptorId = DescriptorId
        self.Amount = Amount

    def __repr__(self):
        return (
            f"<TConditionTagRaisedInUnit "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["Tag", "DescriptorId", "Amount"]
                ]
            )
            + ">"
        )


class TConditionTagNotRaisedInUnit(BaseDescription):
    def __init__(self, Tag=None, DescriptorId=None, Amount=None):
        self.Tag = Tag
        self.DescriptorId = DescriptorId
        self.Amount = Amount

    def __repr__(self):
        return (
            f"<TConditionTagNotRaisedInUnit "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["Tag", "DescriptorId", "Amount"]
                ]
            )
            + ">"
        )


class TConditionNotInMovement(BaseDescription):
    def __init__(self, DescriptorId=None):
        self.DescriptorId = DescriptorId

    def __repr__(self):
        return (
            f"<TConditionNotInMovement "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["DescriptorId"]])
            + ">"
        )


class TDamageLevelsPackDescriptor(BaseDescription):
    def __init__(
        self, DescriptorId=None, NameForDebug=None, DamageLevelsDescriptors=None
    ):
        self.DescriptorId = DescriptorId
        self.NameForDebug = NameForDebug
        self.DamageLevelsDescriptors = DamageLevelsDescriptors

    def __repr__(self):
        return (
            f"<TDamageLevelsPackDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "DescriptorId",
                        "NameForDebug",
                        "DamageLevelsDescriptors",
                    ]
                ]
            )
            + ">"
        )


class TDamageLevelDescriptor(BaseDescription):
    def __init__(
        self,
        MoralModifier=None,
        EffectsPacks=None,
        DescriptorId=None,
        NameForDebug=None,
        FeedbackOnSelf=None,
        TextColor=None,
        AnimationType=None,
        HitRollModifier=None,
        LocalizationToken=None,
        Value=None,
    ):
        self.MoralModifier = MoralModifier
        self.EffectsPacks = EffectsPacks
        self.DescriptorId = DescriptorId
        self.NameForDebug = NameForDebug
        self.FeedbackOnSelf = FeedbackOnSelf
        self.TextColor = TextColor
        self.AnimationType = AnimationType
        self.HitRollModifier = HitRollModifier
        self.LocalizationToken = LocalizationToken
        self.Value = Value

    def __repr__(self):
        return (
            f"<TDamageLevelDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "MoralModifier",
                        "EffectsPacks",
                        "DescriptorId",
                        "NameForDebug",
                        "FeedbackOnSelf",
                        "TextColor",
                        "AnimationType",
                        "HitRollModifier",
                        "LocalizationToken",
                        "Value",
                    ]
                ]
            )
            + ">"
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


class TResistanceFamilyList(BaseDescription):
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return (
            f"<TResistanceFamilyList "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Values"]])
            + ">"
        )


class TDamageFamilyList(BaseDescription):
    def __init__(self, Values=None):
        self.Values = Values

    def __repr__(self):
        return (
            f"<TDamageFamilyList "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Values"]])
            + ">"
        )


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


class TDistrictUnitsContainerModuleDescriptor(BaseDescription):
    def __init__(self, AllowedTagSet=None, NbSlots=None):
        self.AllowedTagSet = AllowedTagSet
        self.NbSlots = NbSlots

    def __repr__(self):
        return (
            f"<TDistrictUnitsContainerModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["AllowedTagSet", "NbSlots"]
                ]
            )
            + ">"
        )


class TDynamicTerrainModuleDescriptor(BaseDescription):
    def __init__(self, TerrainToApplyOnInit=None, TerrainToApplyOnDeath=None):
        self.TerrainToApplyOnInit = TerrainToApplyOnInit
        self.TerrainToApplyOnDeath = TerrainToApplyOnDeath

    def __repr__(self):
        return (
            f"<TDynamicTerrainModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["TerrainToApplyOnInit", "TerrainToApplyOnDeath"]
                ]
            )
            + ">"
        )


class TShootingPointsModuleDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TShootingPointsModuleDescriptor>"


class TMinimapDisplayModuleDescriptor(BaseDescription):
    def __init__(self, FollowUnitOrientation=None, Texture=None):
        self.FollowUnitOrientation = FollowUnitOrientation
        self.Texture = Texture

    def __repr__(self):
        return (
            f"<TMinimapDisplayModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["FollowUnitOrientation", "Texture"]
                ]
            )
            + ">"
        )


class TGameplayEffectsPacksList(BaseDescription):
    def __init__(self, EffectsPacks=None):
        self.EffectsPacks = EffectsPacks

    def __repr__(self):
        return (
            f"<TGameplayEffectsPacksList "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["EffectsPacks"]])
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


class TDerouteUnitEffectDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TDerouteUnitEffectDescriptor>"


class TEffectInflictPhysicalDamageDescriptor(BaseDescription):
    def __init__(self, ModifierType=None, PhysicalDamageValue=None):
        self.ModifierType = ModifierType
        self.PhysicalDamageValue = PhysicalDamageValue

    def __repr__(self):
        return (
            f"<TEffectInflictPhysicalDamageDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ModifierType", "PhysicalDamageValue"]
                ]
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


class TKillUnitEffectDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TKillUnitEffectDescriptor>"


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


class TTeamIdentifierForUnitEffect(BaseDescription):
    def __init__(self, TeamType=None, TeamNumber=None):
        self.TeamType = TeamType
        self.TeamNumber = TeamNumber

    def __repr__(self):
        return (
            f"<TTeamIdentifierForUnitEffect "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["TeamType", "TeamNumber"]]
            )
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


class TEvacAirplaneEffectDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TEvacAirplaneEffectDescriptor>"


class TExperienceLevelsPackDescriptor(BaseDescription):
    def __init__(
        self, DescriptorId=None, ExperienceLevelsDescriptors=None, NameForDebug=None
    ):
        self.DescriptorId = DescriptorId
        self.ExperienceLevelsDescriptors = ExperienceLevelsDescriptors
        self.NameForDebug = NameForDebug

    def __repr__(self):
        return (
            f"<TExperienceLevelsPackDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "DescriptorId",
                        "ExperienceLevelsDescriptors",
                        "NameForDebug",
                    ]
                ]
            )
            + ">"
        )


class TExperienceLevelDescriptor(BaseDescription):
    def __init__(
        self,
        DescriptorId=None,
        NameForDebug=None,
        LevelEffectsPacks=None,
        HintTitleToken=None,
        HintBodyToken=None,
        IconsByNationality=None,
        ThresholdPriceMultiplier=None,
        LocalizationToken=None,
        ThresholdAdditionalValue=None,
    ):
        self.DescriptorId = DescriptorId
        self.NameForDebug = NameForDebug
        self.LevelEffectsPacks = LevelEffectsPacks
        self.HintTitleToken = HintTitleToken
        self.HintBodyToken = HintBodyToken
        self.IconsByNationality = IconsByNationality
        self.ThresholdPriceMultiplier = ThresholdPriceMultiplier
        self.LocalizationToken = LocalizationToken
        self.ThresholdAdditionalValue = ThresholdAdditionalValue

    def __repr__(self):
        return (
            f"<TExperienceLevelDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "DescriptorId",
                        "NameForDebug",
                        "LevelEffectsPacks",
                        "HintTitleToken",
                        "HintBodyToken",
                        "IconsByNationality",
                        "ThresholdPriceMultiplier",
                        "LocalizationToken",
                        "ThresholdAdditionalValue",
                    ]
                ]
            )
            + ">"
        )


class TMissileCarriageConnoisseur(BaseDescription):
    def __init__(self, WeaponInfos=None, PylonSet=None, MeshDescriptor=None):
        self.WeaponInfos = WeaponInfos
        self.PylonSet = PylonSet
        self.MeshDescriptor = MeshDescriptor

    def __repr__(self):
        return (
            f"<TMissileCarriageConnoisseur "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["WeaponInfos", "PylonSet", "MeshDescriptor"]
                ]
            )
            + ">"
        )


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


class TemplateDepictionMissileGroundUnit(BaseDescription):
    def __init__(
        self, ProjectileModelResource=None, MissileNumber=None, PhysicalProperty=None
    ):
        self.ProjectileModelResource = ProjectileModelResource
        self.MissileNumber = MissileNumber
        self.PhysicalProperty = PhysicalProperty

    def __repr__(self):
        return (
            f"<TemplateDepictionMissileGroundUnit "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "ProjectileModelResource",
                        "MissileNumber",
                        "PhysicalProperty",
                    ]
                ]
            )
            + ">"
        )


class TStaticMissileCarriageSubDepictionGenerator(BaseDescription):
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
            f"<TStaticMissileCarriageSubDepictionGenerator "
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


class TStaticMissileCarriageSubDepictionMissileInfo(BaseDescription):
    def __init__(self, WeaponIndex=None, Depiction=None, MissileCount=None):
        self.WeaponIndex = WeaponIndex
        self.Depiction = Depiction
        self.MissileCount = MissileCount

    def __repr__(self):
        return (
            f"<TStaticMissileCarriageSubDepictionMissileInfo "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["WeaponIndex", "Depiction", "MissileCount"]
                ]
            )
            + ">"
        )


class TemplateDepictionMissileShowroom(BaseDescription):
    def __init__(self, ProjectileModelResource=None):
        self.ProjectileModelResource = ProjectileModelResource

    def __repr__(self):
        return (
            f"<TemplateDepictionMissileShowroom "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ProjectileModelResource"]
                ]
            )
            + ">"
        )


class TDepictionDescriptor(BaseDescription):
    def __init__(self, MeshDescriptor=None, SelectorId=None):
        self.MeshDescriptor = MeshDescriptor
        self.SelectorId = SelectorId

    def __repr__(self):
        return (
            f"<TDepictionDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["MeshDescriptor", "SelectorId"]
                ]
            )
            + ">"
        )


class TemplateDepictionStaticMissilesGroundUnit(BaseDescription):
    def __init__(self, ProjectileModelResource=None, PhysicalProperty=None):
        self.ProjectileModelResource = ProjectileModelResource
        self.PhysicalProperty = PhysicalProperty

    def __repr__(self):
        return (
            f"<TemplateDepictionStaticMissilesGroundUnit "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ProjectileModelResource", "PhysicalProperty"]
                ]
            )
            + ">"
        )


class TemplateDepictionStaticMissilesAirUnit(BaseDescription):
    def __init__(self, ProjectileModelResource=None, PhysicalProperty=None):
        self.ProjectileModelResource = ProjectileModelResource
        self.PhysicalProperty = PhysicalProperty

    def __repr__(self):
        return (
            f"<TemplateDepictionStaticMissilesAirUnit "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["ProjectileModelResource", "PhysicalProperty"]
                ]
            )
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


class TTagsModuleDescriptor(BaseDescription):
    def __init__(self, TagSet=None):
        self.TagSet = TagSet

    def __repr__(self):
        return (
            f"<TTagsModuleDescriptor "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["TagSet"]])
            + ">"
        )


class VehicleApparenceModelModuleDescriptor(BaseDescription):
    def __init__(
        self,
        ReferenceMesh=None,
        GameplayBBoxBoneName=None,
        BlackHoleIdentifier=None,
        Depiction=None,
    ):
        self.ReferenceMesh = ReferenceMesh
        self.GameplayBBoxBoneName = GameplayBBoxBoneName
        self.BlackHoleIdentifier = BlackHoleIdentifier
        self.Depiction = Depiction

    def __repr__(self):
        return (
            f"<VehicleApparenceModelModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "ReferenceMesh",
                        "GameplayBBoxBoneName",
                        "BlackHoleIdentifier",
                        "Depiction",
                    ]
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


class TDangerousnessModuleDescriptor(BaseDescription):
    def __init__(self, Dangerousness=None):
        self.Dangerousness = Dangerousness

    def __repr__(self):
        return (
            f"<TDangerousnessModuleDescriptor "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Dangerousness"]])
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


class TemplateUnitMissileCarriage(BaseDescription):
    def __init__(self, Connoisseur=None):
        self.Connoisseur = Connoisseur

    def __repr__(self):
        return (
            f"<TemplateUnitMissileCarriage "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Connoisseur"]])
            + ">"
        )


class TAutomaticBehaviorModuleDescriptor(BaseDescription):
    def __init__(
        self,
        CanAssist=None,
        MaxDistanceForOffensiveReactionGRU=None,
        MaxDistanceForEngagementGRU=None,
        DistanceToFleeGRU=None,
        SearchedTagsInEngagementTarget=None,
        AssistRequestBroadcastRadiusGRU=None,
    ):
        self.CanAssist = CanAssist
        self.MaxDistanceForOffensiveReactionGRU = MaxDistanceForOffensiveReactionGRU
        self.MaxDistanceForEngagementGRU = MaxDistanceForEngagementGRU
        self.DistanceToFleeGRU = DistanceToFleeGRU
        self.SearchedTagsInEngagementTarget = SearchedTagsInEngagementTarget
        self.AssistRequestBroadcastRadiusGRU = AssistRequestBroadcastRadiusGRU

    def __repr__(self):
        return (
            f"<TAutomaticBehaviorModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "CanAssist",
                        "MaxDistanceForOffensiveReactionGRU",
                        "MaxDistanceForEngagementGRU",
                        "DistanceToFleeGRU",
                        "SearchedTagsInEngagementTarget",
                        "AssistRequestBroadcastRadiusGRU",
                    ]
                ]
            )
            + ">"
        )


class TCubeActionModuleDescriptor(BaseDescription):
    def __init__(self, CubeActionDescriptor=None):
        self.CubeActionDescriptor = CubeActionDescriptor

    def __repr__(self):
        return (
            f"<TCubeActionModuleDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["CubeActionDescriptor"]]
            )
            + ">"
        )


class TOrderConfigModuleDescriptor(BaseDescription):
    def __init__(self, ValidOrders=None):
        self.ValidOrders = ValidOrders

    def __repr__(self):
        return (
            f"<TOrderConfigModuleDescriptor "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["ValidOrders"]])
            + ">"
        )


class TOrderableModuleDescriptor(BaseDescription):
    def __init__(self, UnlockableOrders=None):
        self.UnlockableOrders = UnlockableOrders

    def __repr__(self):
        return (
            f"<TOrderableModuleDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["UnlockableOrders"]]
            )
            + ">"
        )


class TStrategicDataModuleDescriptor(BaseDescription):
    def __init__(
        self, UnitDefenseValue=None, UnitAttackValue=None, UnitBonusXpPerLevelValue=None
    ):
        self.UnitDefenseValue = UnitDefenseValue
        self.UnitAttackValue = UnitAttackValue
        self.UnitBonusXpPerLevelValue = UnitBonusXpPerLevelValue

    def __repr__(self):
        return (
            f"<TStrategicDataModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "UnitDefenseValue",
                        "TInfantrySquadModuleDescriptorUnitAttackValue",
                        "UnitBonusXpPerLevelValue",
                    ]
                ]
            )
            + ">"
        )


class TVisualShootPositionsModuleDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TVisualShootPositionsModuleDescriptor>"


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


class TCapaciteModuleDescriptor(BaseDescription):
    def __init__(self, DefaultSkillList=None):
        self.DefaultSkillList = DefaultSkillList

    def __repr__(self):
        return (
            f"<TCapaciteModuleDescriptor "
            + ", ".join(
                [f"{attr}={getattr(self, attr)}" for attr in ["DefaultSkillList"]]
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


class TCommanderModuleDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TCommanderModuleDescriptor>"


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


class TInfluenceScoutModuleDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TInfluenceScoutModuleDescriptor>"


class InfantryApparenceModelModuleDescriptor(BaseDescription):
    def __init__(self, Depiction=None):
        self.Depiction = Depiction

    def __repr__(self):
        return (
            f"<InfantryApparenceModelModuleDescriptor "
            + ", ".join([f"{attr}={getattr(self, attr)}" for attr in ["Depiction"]])
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


class Descriptor_Unit_MimeticUnit(BaseDescription):
    def __init__(self, DescriptorId=None, MimeticName=None):
        self.DescriptorId = DescriptorId
        self.MimeticName = MimeticName

    def __repr__(self):
        return (
            f"<Descriptor_Unit_MimeticUnit "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["DescriptorId", "MimeticName"]
                ]
            )
            + ">"
        )


class TInfantrySquadWeaponAssignmentModuleDescriptor(BaseDescription):
    def __init__(self, InitialSoldiersToTurretIndexMap=None):
        self.InitialSoldiersToTurretIndexMap = InitialSoldiersToTurretIndexMap

    def __repr__(self):
        return (
            f"<TInfantrySquadWeaponAssignmentModuleDescriptor "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in ["InitialSoldiersToTurretIndexMap"]
                ]
            )
            + ">"
        )


class TLinkToDistrictModuleDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TLinkToDistrictModuleDescriptor>"


class TSellModuleDescriptor(BaseDescription):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<TSellModuleDescriptor>"


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


class TFlareModuleDescriptor_MW(BaseDescription):
    def __init__(
        self,
        BonusTimeBetweenFlareByProjectile=None,
        DistanceActivationGRU=None,
        MinimalTimeBetweenFlare=None,
        ProjectileSpeed=None,
        TimeBetweenFlare=None,
    ):
        self.BonusTimeBetweenFlareByProjectile = BonusTimeBetweenFlareByProjectile
        self.DistanceActivationGRU = DistanceActivationGRU
        self.MinimalTimeBetweenFlare = MinimalTimeBetweenFlare
        self.ProjectileSpeed = ProjectileSpeed
        self.TimeBetweenFlare = TimeBetweenFlare

    def __repr__(self):
        return (
            f"<TFlareModuleDescriptor_MW "
            + ", ".join(
                [
                    f"{attr}={getattr(self, attr)}"
                    for attr in [
                        "BonusTimeBetweenFlareByProjectile",
                        "DistanceActivationGRU",
                        "MinimalTimeBetweenFlare",
                        "ProjectileSpeed",
                        "TimeBetweenFlare",
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

class TNDFTransaction(BaseDescription):
    def __init__(self, BaseName=None, NameSpace=None, Optional=None, Moddable=None, UsingNamespaces=None):
        self.BaseName = BaseName
        self.NameSpace = NameSpace
        self.Optional = Optional
        self.Moddable = Moddable
        self.UsingNamespaces = UsingNamespaces


class TClusterNdfTransaction(BaseDescription):
    def __init__(self, NdfTransaction=None):
        self.NdfTransaction = NdfTransaction
