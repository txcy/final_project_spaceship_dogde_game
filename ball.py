import turtle
import random

class Asteroid:
    """คลาสสำหรับอุกกาบาต"""
    def __init__(self, size, x, y, vx, vy, color):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

    def move(self):
        """อัปเดตตำแหน่งอุกกาบาต"""
        self.y += self.vy
        self.x += self.vx

        # รีเซ็ตอุกกาบาตเมื่อหลุดจอ
        if self.y < -300:
            self.y = 300
            self.x = random.randint(-380, 380)

    def draw(self):
        """วาดอุกกาบาต"""
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.dot(self.size, self.color)