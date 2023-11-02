class Rectangle:
    def __init__(self, x, y, height, width, color):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.color = color

    def draw(self, canvas):
        pass


class Square:
    def __init__(self, x, y, side, color):
        self.side = side
        self.x = x
        self.y = y
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color
