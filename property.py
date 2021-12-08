

class PropertyDefinition(object):
    def __init__(self, name, prop_type=None, value=None):
        self.name = name
        self.prop_type = prop_type
        self.value = value

        
class Property(object):
    def __init__(self, definition):
        self.definition = definition
        self.value = definition.value
