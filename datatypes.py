

import cv2
import numpy as np
import OpenImageIO as oiio


class RenderImage(object):
    def __init__(self, size=(100, 100)):
        self._img = np.zeros((size[0], size[1], 4), dtype=np.uint16)

    def Image(self):
        """ Returns the numpy array image.
        :returns: ``numpy.ndarray`` object
        """
        return self._img

    def OIIOImage(self):
        """ Returns the OIIO ImageBuf image.
        :returns: ``oiio.ImageBuf`` object
        """
        height, width = self._img.shape[:2]
        spec = oiio.ImageSpec(width, height, 4, "uint16")
        buf = oiio.ImageBuf(spec)
        buf.set_pixels(oiio.ROI(), self._img)
        return buf

    def SetAsOpenedImage(self, path):
        """ Sets the image and opens it.
        :param path: image filepath to be opened
        """
        try:
            # Open the image as an array
            img_input = oiio.ImageInput.open(path)
            image = img_input.read_image(format="uint16")

            # Enforce RGBA
            if image.shape[2] == 3:
                self._img = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
            else:
                self._img = image
        except FileNotFoundError:
            print("WARNING: COULD NOT GET IMAGE!")


    def SetAsImage(self, image):
        """ Sets the render image. Automatically converts the image to
        a numpy array for internal use.
        :param image: ``numpy.ndarray`` or ``oiio.ImageBuf`` object
        """
        img_type = type(image)
        if img_type == oiio.ImageBuf:
            self._img = image.get_pixels()
        else:
            self._img = image
