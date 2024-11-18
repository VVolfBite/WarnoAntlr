class BaseDescription:
    def __init__(self):
        self.KeyName = None
        
    def __str__(self):
        return self.KeyName if self.KeyName is not None else "NameNotFound"