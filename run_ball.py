import turtle
import random
import math
from ball import Asteroid
from paddle import Spaceship
import time
from fuel import Fuel


class Game:
    def __init__(self, num_asteroids):
        # ตั้งค่าหน้าจอ
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Spaceship Dodge Game")
        self.screen.tracer(0)

        # ตั้งค่าภาพ
        self.background_image = "galaxy.gif"
        self.spaceship_image = "spaceship.gif"
        turtle.register_shape(self.spaceship_image)
        try:
            self.screen.bgpic(self.background_image)
        except turtle.TurtleGraphicsError:
            print(f"Error: {self.background_image} not found.")

        # สร้างยานและออบเจกต์
        self.num_asteroids = num_asteroids
        self.running = False

    def setup_game(self):
        """รีเซ็ตเกมใหม่ทั้งหมด"""
        self.spaceship = Spaceship(20, 0, -250, self.spaceship_image)
        self.asteroids = [self.create_asteroid() for _ in range(self.num_asteroids)]
        self.fuel = Fuel(15, random.randint(-380, 380), random.randint(-250, 250), "yellow")
        self.score = 0
        self.fuel_score = 0
        self.level = 1
        self.running = True

        # ลงทะเบียนปุ่มควบคุมยาน
        self.screen.listen()
        self.screen.onkeypress(lambda: self.spaceship.move("up"), "Up")
        self.screen.onkeypress(lambda: self.spaceship.move("down"), "Down")
        self.screen.onkeypress(lambda: self.spaceship.move("left"), "Left")
        self.screen.onkeypress(lambda: self.spaceship.move("right"), "Right")

    def main_menu(self):
        """แสดงเมนูหลัก"""
        turtle.clear()
        turtle.penup()
        turtle.hideturtle()
        turtle.color("white")
        turtle.goto(0, 50)
        turtle.write("Spaceship Dodge Game", align="center", font=("Arial", 24, "bold"))
        turtle.goto(0, 0)
        turtle.write("Press 'S' to Start or 'Q' to Quit", align="center", font=("Arial", 16, "bold"))
        self.screen.listen()
        self.screen.onkeypress(self.start_game, "s")
        self.screen.onkeypress(self.quit_game, "q")
        self.screen.update()

    def start_game(self):
        """เริ่มเกมใหม่"""
        self.setup_game()
        self.run()

    def quit_game(self):
        """ออกจากเกม"""
        self.screen.bye()

    def create_asteroid(self):
        size = random.randint(10, 20)
        x = random.randint(-380, 380)
        y = 300
        vx = 0
        vy = random.uniform(-1.0, -1.5)  # ลดความเร็วให้ช้าลง
        color = random.choice(["gray", "darkgray", "lightgray"])
        return Asteroid(size, x, y, vx, vy, color)

    def check_collision(self):
        for asteroid in self.asteroids:
            distance = math.sqrt((self.spaceship.x - asteroid.x) ** 2 + (self.spaceship.y - asteroid.y) ** 2)
            if distance < self.spaceship.size + asteroid.size:
                return True
        return False

    def check_fuel_collision(self):
        distance = math.sqrt((self.spaceship.x - self.fuel.x) ** 2 + (self.spaceship.y - self.fuel.y) ** 2)
        if distance < self.spaceship.size + self.fuel.size:
            self.fuel_score += 1
            self.fuel.relocate()

    def display_score(self):
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(-380, 260)
        turtle.color("white")
        turtle.write(f"Score: {self.score}  Fuel Collected: {self.fuel_score}  Level: {self.level}",
                     font=("Arial", 16, "bold"))

    def reset_game(self):
        """รีเซ็ตสถานะเกมทั้งหมดเพื่อเริ่มใหม่"""
        turtle.clear()  # ล้างหน้าจอทั้งหมด
        self.spaceship.turtle.hideturtle()  # ซ่อนยานเก่าที่ค้างอยู่
        self.spaceship = Spaceship(20, 0, -250, self.spaceship_image)  # สร้างยานใหม่

        # สร้าง Asteroids ใหม่
        self.asteroids = [self.create_asteroid() for _ in range(10)]

        # สร้าง Fuel ใหม่
        self.fuel = Fuel(15, random.randint(-380, 380), random.randint(-250, 250), "yellow")

        # รีเซ็ตสถานะเกม
        self.score = 0
        self.fuel_score = 0
        self.level = 1
        self.running = True
        self.run()  # เริ่มเกมใหม่

    def game_over(self):
        """แสดงข้อความจบเกมพร้อมสรุปคะแนน"""
        turtle.clear()
        turtle.penup()
        turtle.hideturtle()
        turtle.color("red")

        # แสดงข้อความ GAME OVER
        turtle.goto(0, 50)
        turtle.write("GAME OVER", align="center", font=("Arial", 32, "bold"))

        # แสดงสรุปคะแนน
        turtle.color("white")
        turtle.goto(0, 0)
        turtle.write(f"Final Score: {self.score}", align="center", font=("Arial", 20, "bold"))
        turtle.goto(0, -40)
        turtle.write(f"Fuel Collected: {self.fuel_score}", align="center", font=("Arial", 20, "bold"))

        # แสดงปุ่มสำหรับ Restart หรือ Quit
        turtle.goto(0, -80)
        turtle.write("Press 'S' to Restart or 'Q' to Quit", align="center", font=("Arial", 16, "bold"))
        self.screen.update()

        # รอการกดปุ่ม Restart หรือ Quit
        self.screen.listen()
        self.screen.onkeypress(self.reset_game, "s")  # กด S เพื่อเริ่มใหม่
        self.screen.onkeypress(self.screen.bye, "q")  # กด Q เพื่อออกจากเกม

    def run(self):
        while self.running:
            turtle.clear()

            # วาด Spaceship
            self.spaceship.turtle.goto(self.spaceship.x, self.spaceship.y)

            # วาดอุกกาบาต
            for asteroid in self.asteroids:
                asteroid.move()
                asteroid.draw()

            # วาดน้ำมัน
            self.fuel.draw()

            # ตรวจสอบการชน
            self.check_fuel_collision()
            if self.check_collision():
                self.running = False
                break

            # เพิ่มคะแนน
            self.score += 1
            if self.score % 50 == 0:
                self.level += 1
                for asteroid in self.asteroids:
                    asteroid.vy *= 1.05

            self.display_score()
            self.screen.update()
            time.sleep(0.01)

        self.game_over()


if __name__ == "__main__":
    game = Game(10)
    while True:
        game.main_menu()
        game.screen.mainloop()
