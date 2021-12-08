
from property import Property
from parameter import Parameter


class NodeBase(object):
    def __init__(self, _id=None):
        self._id = _id
        self._properties = {}
        self._parameters = {}
        self._cache = {}
        self._dirty_flag = False

        self.SetParams()
        self.SetProps()

    def IsOutputNode(self):
        return False

    def Props(self):
        return []

    def SetProps(self):
        self._properties = {p.name: Property(p) for p in self.Props()}

    def Params(self):
        return []            

    def SetParams(self):
        self._parameters = {p.name: Parameter(p) for p in self.Params()}

    def EditProperty(self, name, value):
        self._properties[name].value = value

    def EditParameter(self, name, binding):
        self._parameters[name].binding = binding

    def IsInCache(self, name):
        try:
            c = self._cache[name]
            return True
        except KeyError:
            return False

    def EvalParameter(self, eval_info, name):
        cached = self.IsInCache(name)
        if self._dirty_flag == True and cached == True:
            value = self._cache[name]
            print("Used Cache")
        else:
            value = eval_info.EvaluateParameter(name)
            self._cache[name] = value
            self._dirty_flag = False
            print("Evaluated")
        return value

    def EvalProperty(self, eval_info, name):
        return eval_info.EvaluateProperty(name)

    @property
    def EvaluateNode(self):
        """ Internal method. Please do not override. """
        return self.NodeEvaluation

    def NodeEvaluation(self, eval_info):
        return None
