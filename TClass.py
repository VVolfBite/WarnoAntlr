class TBaseObject(BaseDescription):
    def __init__(self, value="<T4>", name="<S>"):
        self.value = value
        self.name = name


class TChildObject(BaseDescription):
    def __init__(self, value=200, name="child"):
        self.value = value
        self.name = name


class TParentObject(BaseDescription):
    def __init__(self, count=1, child=[{id: value, type: assignment, export: False, private: False, member: True, value: type: 4, value: None}}, {id: name, type: assignment, export: False, private: False, member: True, value: type: 7, value: None}}]):
        self.count = count
        self.child = child


class TComplexObject(BaseDescription):
    def __init__(self, array=[type: 4, value: None}, type: 4, value: None}, type: 4, value: None}], value=100):
        self.array = array
        self.value = value


class TChildTemplate(BaseDescription):
    def __init__(self, name="<S>"):
        self.name = name


class TBaseTemplate(BaseDescription):
    def __init__(self, child=[{id: name, type: assignment, export: False, private: False, member: True, value: type: 20, value: None}}], value="<T>"):
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
        super().__init__(child=<src.extractor.test_class.TChildTemplate object at 0x000001F7FEABA9C0>, value=T)
        self.T = T
        self.S = S
