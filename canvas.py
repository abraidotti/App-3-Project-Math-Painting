import numpy as np
from PIL import Image


class Canvas:
    """
    The object on which all shapes are drawn
    """

    def __init__(self, height, width, color):
        self.color = color
        self.height = height
        self.width = width

        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change RGB color list to user-assigned values
        self.data[:] = self.color

    def make(self, imagepath):
        """
        Converts the current array into an image file
        """
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)