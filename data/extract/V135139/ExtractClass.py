class TDeckDivisionRules:
    def __init__(self, DivisionRules=None):
        self.DivisionRules = DivisionRules

    def __repr__(self):
        return f'<TDeckDivisionRules ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DivisionRules']]) + '>'


class TDeckDivisionRules:
    def __init__(self, DivisionRules=None):
        self.DivisionRules = DivisionRules

    def __repr__(self):
        return f'<TDeckDivisionRules ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['DivisionRules']]) + '>'

class TDeckUniteRule:
    def __init__(self, UnitDescriptor=None, NumberOfUnitInPack=None, NumberOfUnitInPackXPMultiplier=None, AvailableTransportList=None, AvailableWithoutTransport=None):
        self.UnitDescriptor = UnitDescriptor
        self.NumberOfUnitInPack = NumberOfUnitInPack
        self.NumberOfUnitInPackXPMultiplier = NumberOfUnitInPackXPMultiplier
        self.AvailableTransportList = AvailableTransportList
        self.AvailableWithoutTransport = AvailableWithoutTransport

    def __repr__(self):
        return f'<TDeckUniteRule ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['UnitDescriptor', 'NumberOfUnitInPack', 'NumberOfUnitInPackXPMultiplier', 'AvailableTransportList', 'AvailableWithoutTransport']]) + '>'

class TAirplaneConstantesModernWarfareDescriptor:
    def __init__(self, EvacuationAltitudeGRU=None, TempsEntreDeuxDecollagesEnSecondes=None, EvacWinchesterToutesLesArmesPrincipales=None, UtiliserArmesPendantEvac=None, FrontLandingGearMeshNodeName=None, BackLandingGearMeshNodeName=None):
        self.EvacuationAltitudeGRU = EvacuationAltitudeGRU
        self.TempsEntreDeuxDecollagesEnSecondes = TempsEntreDeuxDecollagesEnSecondes
        self.EvacWinchesterToutesLesArmesPrincipales = EvacWinchesterToutesLesArmesPrincipales
        self.UtiliserArmesPendantEvac = UtiliserArmesPendantEvac
        self.FrontLandingGearMeshNodeName = FrontLandingGearMeshNodeName
        self.BackLandingGearMeshNodeName = BackLandingGearMeshNodeName

    def __repr__(self):
        return f'<TAirplaneConstantesModernWarfareDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['EvacuationAltitudeGRU', 'TempsEntreDeuxDecollagesEnSecondes', 'EvacWinchesterToutesLesArmesPrincipales', 'UtiliserArmesPendantEvac', 'FrontLandingGearMeshNodeName', 'BackLandingGearMeshNodeName']]) + '>'


class TRoutConstants:
    def __init__(self, TestMoralNombreDes=None, TestMoralNombreFacesDes=None, TestMoralSeuil=None, LanceTestMoralPertePV=None, TempsEntreDeuxTestsMoralPertePV=None, LanceTestMoralSeuilSuppression=None, TempsEntreDeuxTestsMoralSeuilSuppression=None, EffetConditionSuppression=None, EffetAppliqueSuppression=None, SortieSeuilSuppression=None):
        self.TestMoralNombreDes = TestMoralNombreDes
        self.TestMoralNombreFacesDes = TestMoralNombreFacesDes
        self.TestMoralSeuil = TestMoralSeuil
        self.LanceTestMoralPertePV = LanceTestMoralPertePV
        self.TempsEntreDeuxTestsMoralPertePV = TempsEntreDeuxTestsMoralPertePV
        self.LanceTestMoralSeuilSuppression = LanceTestMoralSeuilSuppression
        self.TempsEntreDeuxTestsMoralSeuilSuppression = TempsEntreDeuxTestsMoralSeuilSuppression
        self.EffetConditionSuppression = EffetConditionSuppression
        self.EffetAppliqueSuppression = EffetAppliqueSuppression
        self.SortieSeuilSuppression = SortieSeuilSuppression

    def __repr__(self):
        return f'<TRoutConstants ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TestMoralNombreDes', 'TestMoralNombreFacesDes', 'TestMoralSeuil', 'LanceTestMoralPertePV', 'TempsEntreDeuxTestsMoralPertePV', 'LanceTestMoralSeuilSuppression', 'TempsEntreDeuxTestsMoralSeuilSuppression', 'EffetConditionSuppression', 'EffetAppliqueSuppression', 'SortieSeuilSuppression']]) + '>'


class TEvaluationMenaceConstantesDescriptor:
    def __init__(self, CercleMenaceGRU=None, EscapeRadiusGRU=None, DureeDeMemoireDeLaMenaceEnSecondes=None, ConsidererLesMenacesEnMouvementCommeDirectes=None):
        self.CercleMenaceGRU = CercleMenaceGRU
        self.EscapeRadiusGRU = EscapeRadiusGRU
        self.DureeDeMemoireDeLaMenaceEnSecondes = DureeDeMemoireDeLaMenaceEnSecondes
        self.ConsidererLesMenacesEnMouvementCommeDirectes = ConsidererLesMenacesEnMouvementCommeDirectes

    def __repr__(self):
        return f'<TEvaluationMenaceConstantesDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['CercleMenaceGRU', 'EscapeRadiusGRU', 'DureeDeMemoireDeLaMenaceEnSecondes', 'ConsidererLesMenacesEnMouvementCommeDirectes']]) + '>'

class TSpecificFactoryResources:
    def __init__(self, FactoryDisplayOrder=None, FactoryDescriptions=None):
        self.FactoryDisplayOrder = FactoryDisplayOrder
        self.FactoryDescriptions = FactoryDescriptions

    def __repr__(self):
        return f'<TSpecificFactoryResources ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FactoryDisplayOrder', 'FactoryDescriptions']]) + '>'

class TSpecificFactoryDescription:
    def __init__(self, FactoryHintExtended=None, FactoryName=None, FactoryHintTitle=None, FactoryHintBody=None):
        self.FactoryHintExtended = FactoryHintExtended
        self.FactoryName = FactoryName
        self.FactoryHintTitle = FactoryHintTitle
        self.FactoryHintBody = FactoryHintBody

    def __repr__(self):
        return f'<TSpecificFactoryDescription ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['FactoryHintExtended', 'FactoryName', 'FactoryHintTitle', 'FactoryHintBody']]) + '>'

class TActionPointConsumptionGridConstantsDescriptor:
    def __init__(self, TerrainsBloquants=None, TerrainsRalentisseurs=None, TailleDeCaseApproximativeGRU=None, CouleurDeLaCourbe=None, EpaisseurDeLaCourbe=None):
        self.TerrainsBloquants = TerrainsBloquants
        self.TerrainsRalentisseurs = TerrainsRalentisseurs
        self.TailleDeCaseApproximativeGRU = TailleDeCaseApproximativeGRU
        self.CouleurDeLaCourbe = CouleurDeLaCourbe
        self.EpaisseurDeLaCourbe = EpaisseurDeLaCourbe

    def __repr__(self):
        return f'<TActionPointConsumptionGridConstantsDescriptor ' + ', '.join([f'{attr}={getattr(self, attr)}' for attr in ['TerrainsBloquants', 'TerrainsRalentisseurs', 'TailleDeCaseApproximativeGRU', 'CouleurDeLaCourbe', 'EpaisseurDeLaCourbe']]) + '>'
