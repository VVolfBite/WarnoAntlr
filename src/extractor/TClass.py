from src.extractor.base_class import BaseDescription

class TBaseObject(BaseDescription):
    def __init__(self, value=None, name=None):
        self.value = value
        self.name = name


class TChildObject(BaseDescription):
    def __init__(self, value=None, name=None):
        self.value = value
        self.name = name


class TParentObject(BaseDescription):
    def __init__(self, count=None, child=None):
        self.count = count
        self.child = child


class TComplexObject(BaseDescription):
    def __init__(self, array=None, value=None):
        self.array = array
        self.value = value


class TChildTemplate(BaseDescription):
    def __init__(self, name=None):
        self.name = name


class TBaseTemplate(BaseDescription):
    def __init__(self, child=None, value=None):
        self.child = child
        self.value = value


class Simple(TBaseObject):
    def __init__(self, T=1, T1=1, T2=None, T3=100, T4=None):
        super().__init__(value=T4)
        self.T = T
        self.T1 = T1
        self.T2 = T2
        self.T3 = T3
        self.T4 = T4


class Complex(TBaseObject):
    def __init__(self, T=1, S="test"):
        super().__init__(name=S, value=T)
        self.T = T
        self.S = S


class NestedTemplate(TBaseTemplate):
    def __init__(self, T=1, S="test"):
        super().__init__(child=TChildTemplate(name=S), value=T)
        self.T = T
        self.S = S
