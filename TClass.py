class TClass(BaseDescription):
    def __init__(self, Mem=None):
        self.Mem = Mem


class TCriticalEffectModuleDescriptor(BaseDescription):
    def __init__(self, TerrainCriticalEffectTimer=None, EffectsFromTerrain=None, PierceEffectsOnFront=None, PierceEffectsOnTop=None, RicochetEffectsOnFront=None):
        self.TerrainCriticalEffectTimer = TerrainCriticalEffectTimer
        self.EffectsFromTerrain = EffectsFromTerrain
        self.PierceEffectsOnFront = PierceEffectsOnFront
        self.PierceEffectsOnTop = PierceEffectsOnTop
        self.RicochetEffectsOnFront = RicochetEffectsOnFront
