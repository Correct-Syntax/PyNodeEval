
import OpenImageIO as oiio

from datatypes import RenderImage
from property import PropertyDefinition
from parameter import ParameterDefinition
from node import NodeBase


class MixNode(NodeBase):
    def __init__(self, _id):
        NodeBase.__init__(self, _id)

    def Props(self):
        return [
            PropertyDefinition("blend_mode", "INTEGER", 10)
        ]

    def Params(self):
        return [
            ParameterDefinition("image_1", "IMAGE", RenderImage()),
            ParameterDefinition("image_2", "IMAGE", RenderImage()),
        ]    

    def NodeEvaluation(self, eval_info):
        image1 = self.EvalParameter(eval_info, "image_1")
        image2 = self.EvalParameter(eval_info, "image_2")

        render_image = RenderImage()

        blend = self.EvalProperty(eval_info, "blend_mode")
        if blend == 10:
            val = oiio.ImageBufAlgo.add(image1.OIIOImage(), image2.OIIOImage())
        else:
            val = oiio.ImageBufAlgo.over(image2.OIIOImage(), image1.OIIOImage())
        
        render_image.SetAsImage(val)
        return render_image


class ImageNode(NodeBase):
    def __init__(self, _id):
        NodeBase.__init__(self, _id)

    def Props(self):
        return [
            PropertyDefinition("file_path", "STRING", "")
        ]

    def NodeEvaluation(self, eval_info):
        path = self.EvalProperty(eval_info, "file_path")

        render_image = RenderImage()
        render_image.SetAsOpenedImage(path)
        return render_image


class OutputNode(NodeBase):
    def __init__(self, _id):
        NodeBase.__init__(self, _id)
        
    def IsOutputNode(self):
        return True

    def Params(self):
        return [
            ParameterDefinition("image", "IMAGE", "")
        ]    

    def NodeEvaluation(self, eval_info):
        pass
