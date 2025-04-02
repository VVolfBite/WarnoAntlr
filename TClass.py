class TestTemplate(BaseDescription):
    def __init__(self, Key=None, Value=None):
        self.Key = Key
        self.Value = Value


class TTestA(BaseDescription):
    def __init__(self, FieldA=None, FiledB=None, FieldC=None, FieldD=None, FieldE=None, FieldF=None):
        self.FieldA = FieldA
        self.FiledB = FiledB
        self.FieldC = FieldC
        self.FieldD = FieldD
        self.FieldE = FieldE
        self.FieldF = FieldF
