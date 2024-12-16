import turtle
import random
class Fuel:
    def __init__(self, size, x, y, color):
        self.size = size
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.dot(self.size, self.color)

    def relocate(self):
        self.x = random.randint(-380, 380)
        self.y = random.randint(-250, 250)