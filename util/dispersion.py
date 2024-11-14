PorteeMaximaleGRU = 500
PorteeMinimaleGRU = 30
DispersionAtMaxRangeGRU = 500
DispersionAtMinRangeGRU = 30
def modification_factor_of_dispersion( distance):
    return (distance - PorteeMinimaleGRU) * (
        DispersionAtMaxRangeGRU - DispersionAtMinRangeGRU
    ) / (PorteeMaximaleGRU - PorteeMinimaleGRU) + DispersionAtMinRangeGRU

print(modification_factor_of_dispersion(140))