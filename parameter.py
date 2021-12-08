

class ParameterDefinition(object):
    def __init__(self, name, param_type=None, value=None):
        self.name = name
        self.param_type = param_type
        self.value = value


class Parameter(object):
    def __init__(self, definition):
        self.definition = definition
        self.value = definition.value
        self.binding = None
