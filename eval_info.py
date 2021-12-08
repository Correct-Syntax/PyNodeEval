

class EvalInfo(object):
    """
    Evaluate node properties and parameters
    """

    def __init__(self, node):
        if node == None:
            raise TypeError
        self.node = node

    def EvaluateParameter(self, name):
        """
        Evaluates the value of a parameter.
        """
        param = self.node._parameters[name]
        if param.binding:
            # Evaluate the next node
            info = EvalInfo(param.binding)
            return param.binding.EvaluateNode(info)
        return param.value

    def EvaluateProperty(self, name):
        """
        Evaluates the value of a property.
        """
        prop = self.node._properties[name]
        return prop.value
