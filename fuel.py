import turtle
import random
class Fuel:
    """คลาสสำหรับน้ำมันที่เก็บได้"""
    def __init__(self, size, x, y, color):
        self.size = size
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        """วาดน้ำมัน"""
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.dot(self.size, self.color)

    def relocate(self):
        """สุ่มตำแหน่งใหม่ของน้ำมัน"""
        self.x = random.randint(-380, 380)
        self.y = random.randint(-250, 250)