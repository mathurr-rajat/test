# Wrong program
# Will give you error
# TypeError: Point.pointsInRectangle() missing 1 required positional argument: 'upRight'
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pointsInRectangle(self, lowLeft, upRight):
        if (lowLeft[0] < self.x < upRight[0]) and (lowLeft[1] < self.y < upRight[1]):
            return True
        else:
            return False

    def distanceFromPoint(self, x, y):
        return math.dist(self.x, self.y)


class rectangle:
    def __init__(self, lowLeft, upRight):
        self.lowLeft = lowLeft
        self.upRight = upRight


object = Point(6, 7)
points = rectangle(Point(6, 7), Point(3, 9))
output = object.pointsInRectangle(points)
print(output)














# object = Point(6, 7)
# print(points.lowLeft)
# print(points.upRight)
# output = object.pointsInRectangle(points)
# print(output)
#
# print(f"area of rectangle = {points.area()}")
