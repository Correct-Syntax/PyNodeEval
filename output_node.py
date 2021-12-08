

from eval_info import EvalInfo


class OutputNode(object):
    """ Represents the evaluation of the composite output node. """

    def __init__(self):
        self.node = None

    def SetNode(self, node):
        """ Set the node object connected to the output node
        this class represents.

        :param node: output node object
        """
        self.node = node._parameters["image"].binding

    def RenderImage(self):
        """ Render the image for this output node. If the output
        node is not connected then the default image will be rendered.
        """
        if self.node is not None:
            eval_info = EvalInfo(self.node)
            image = eval_info.node.EvaluateNode(eval_info)
            return image
