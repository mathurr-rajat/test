import turtle
from random import randint
import pandas as pd
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pointsInRectangle(self, rectangle):
        if (rectangle.lowLeft.x < self.x < rectangle.upRight.x) and (rectangle.lowLeft.y < self.y < rectangle.upRight.y):
            return True
        else:
            return False
class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x-self.point1.x)*(self.point2.y-self.point1.y)


class GuiRectangle(Rectangle):
    def draw(self, canvas, size = 5, color = 'green'):
        # canvas is object of turtle.Turtle() class
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        # canvas.goto(50,75)
        canvas.pendown()
        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)
        canvas.dot(size,color)
        # turtle.done()

gui_rectangle = GuiRectangle(Point(randint(0,20),randint(0,300)), Point(randint(10, 600),randint(10,90)))
# gui_rectangle = GuiRectangle(Point(20,30),Point(60,80))
print(f" area of rectangle  {gui_rectangle.area()}")
myturtle = turtle.Turtle()
gui_rectangle.draw(canvas=myturtle)
turtle.done()