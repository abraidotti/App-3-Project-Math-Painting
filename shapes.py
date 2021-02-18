class Rectangle:
    """
    This class draws a 4-sided shape with 90° angles ;) on a canvas
    """
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        """
        Draws the object on a canvas
        """
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """
        Draws the object on a canvas
        """
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color
