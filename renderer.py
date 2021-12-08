from output_node import OutputNode


class Renderer(object):
    """ The core renderer which evaluates the data of the node tree and
    outputs the final render image.
    """

    def __init__(self, parent):
        self._parent = parent
        self._render = None

        self.i = 0

    def GetParent(self):
        return self._parent

    def GetRender(self):
        return self._render

    def SetRender(self, render):
        self._render = render

    def Render(self, nodes):
        """ Render method for evaluating the Node Graph
        to render an image.

        :param nodes: dictionary of nodes of the Node Graph
        :returns: rendered image
        """
  
        # Render the image
        output_node = self.GetOutputNode(nodes)
        rendered_image = self.RenderNodeGraph(output_node, nodes)

        # Get rendered image, otherwise use
        # the default transparent image.
        if rendered_image is not None:
            image = rendered_image
        else:
            image = output_node._parameters["image"].value

        # For testing
        image = image.OIIOImage()
        image.write("output-{}.jpg".format(self.i))
        self.i += 1

        return image

    def RenderNodeGraph(self, output_node, nodes):
        """ Render the image, starting from the output node.

        :param output_node: the output node object
        :param nodes: dictionary of nodes of the Node Graph
        :returns: RenderImage object
        """
        output_data = OutputNode()
        output_data.SetNode(output_node)
        return output_data.RenderImage()

    def GetOutputNode(self, nodes):
        """ Get the output composite node.

        :param nodes: dictionary of nodes of the Node Graph
        :returns: node object of output node
        """
        for nodeid in nodes:
            if nodes[nodeid].IsOutputNode() is True:
                output_node = nodes[nodeid]
        return output_node
