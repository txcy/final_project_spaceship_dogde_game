import turtle
class Spaceship:
    def __init__(self, size, x, y, shape):
        self.size = size
        self.x = x
        self.y = y

        # ลงทะเบียนรูปทรง
        self.turtle = turtle.Turtle()
        self.turtle.shape(shape)
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)

    def draw(self):
        """วาด Spaceship"""
        self.turtle.goto(self.x, self.y)

    def move(self, direction):
        """เคลื่อนที่ Spaceship"""
        if direction == "up" and self.y < 300:
            self.y += 20
        elif direction == "down" and self.y > -300:
            self.y -= 20
        elif direction == "left" and self.x > -380:
            self.x -= 20
        elif direction == "right" and self.x < 380:
            self.x += 20
        self.draw()