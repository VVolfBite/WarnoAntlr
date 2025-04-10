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
