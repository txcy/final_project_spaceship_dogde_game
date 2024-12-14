import turtle
import random
import math
from ball import Asteroid
from paddle import Spaceship
import time
from my_event import Event
import heapq
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

        # สร้าง Spaceship
        self.spaceship = Spaceship(20, 0, -250, self.spaceship_image)

        # สร้าง Asteroids
        self.asteroids = [self.create_asteroid() for _ in range(num_asteroids)]

        # สร้าง Fuel
        self.fuel = Fuel(15, random.randint(-380, 380), random.randint(-250, 250), "yellow")

        # ตัวแปรสถานะเกม
        self.running = True
        self.score = 0
        self.fuel_score = 0  # จำนวนครั้งที่เก็บน้ำมัน
        self.level = 1

        # ตั้งค่าปุ่มควบคุม
        self.screen.listen()
        self.screen.onkeypress(lambda: self.spaceship.move("up"), "Up")
        self.screen.onkeypress(lambda: self.spaceship.move("down"), "Down")
        self.screen.onkeypress(lambda: self.spaceship.move("left"), "Left")
        self.screen.onkeypress(lambda: self.spaceship.move("right"), "Right")

    def check_fuel_collision(self):
        """ตรวจจับการชนของน้ำมันกับยาน"""
        distance = math.sqrt((self.spaceship.x - self.fuel.x) ** 2 + (self.spaceship.y - self.fuel.y) ** 2)
        if distance < self.spaceship.size + self.fuel.size:
            self.fuel_score += 1  # เพิ่มคะแนนจากน้ำมันทีละ 1
            self.fuel.relocate()  # สุ่มตำแหน่งใหม่ของน้ำมัน

    def check_collision(self):
        """ตรวจสอบการชนระหว่างยานอวกาศกับอุกกาบาต"""
        for asteroid in self.asteroids:
            distance = math.sqrt((self.spaceship.x - asteroid.x) ** 2 + (self.spaceship.y - asteroid.y) ** 2)
            if distance < self.spaceship.size + asteroid.size:
                self.spaceship_explode()
                return True  # มีการชน
        return False  # ไม่มีการชน

    def create_asteroid(self):
        size = random.randint(10, 20)  # ขนาด
        x = random.randint(-380, 380)  # ตำแหน่งแนวนอน
        y = 300  # ตำแหน่งแนวตั้งเริ่มต้นด้านบน
        vx = 0  # ไม่มีการเคลื่อนที่ในแนวนอน
        vy = random.uniform(-2, -4)  # ความเร็วในแนวตั้ง
        color = random.choice(["gray", "darkgray", "lightgray"])
        return Asteroid(size, x, y, vx, vy, color)

    def create_events(self):
        """สร้างเหตุการณ์การชนทั้งหมด"""
        for asteroid in self.asteroids:
            # ตัวอย่างการสร้าง Event การชนกับ Spaceship
            time_to_collision = calculate_time_to_collision(self.spaceship, asteroid)
            event = Event(time_to_collision, self.spaceship, asteroid)
            heapq.heappush(self.pq, event)  # เพิ่มใน Priority Queue

    def check_collision(self):
        """ตรวจสอบการชนระหว่างยานอวกาศกับอุกกาบาต"""
        for asteroid in self.asteroids:
            distance = math.sqrt((self.spaceship.x - asteroid.x) ** 2 + (self.spaceship.y - asteroid.y) ** 2)
            if distance < self.spaceship.size + asteroid.size:
                self.spaceship.turtle.hideturtle()  # ซ่อนยาน
                self.running = False  # หยุดเกม
                return True
        return False

    def display_score(self):
        """แสดงคะแนนและระดับ"""
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(-380, 260)
        turtle.color("white")
        turtle.write(f"Score: {self.score}  Fuel Collected: {self.fuel_score}  Level: {self.level}",
                     font=("Arial", 16, "bold"))

    def process_events(self):
        """ประมวลผลเหตุการณ์"""
        while self.running:
            if not self.pq:
                break
            event = heapq.heappop(self.pq)  # ดึงเหตุการณ์ที่เร็วที่สุดออกมา
            if not event.is_valid():
                continue  # ข้ามเหตุการณ์ที่ไม่ถูกต้อง
            self.handle_event(event)  # จัดการเหตุการณ์

    def game_over(self):
        """แสดงข้อความจบเกม"""
        turtle.clear()  # ล้างหน้าจอเพื่อแสดงเฉพาะข้อความจบเกม
        turtle.penup()
        turtle.hideturtle()
        turtle.color("red")
        turtle.goto(0, 0)
        turtle.write("GAME OVER", align="center", font=("Arial", 32, "bold"))
        self.screen.update()  # อัปเดตหน้าจอให้แสดงข้อความ

    def run(self):
        """ลูปหลักของเกม"""
        while self.running:
            turtle.clear()

            # วาด Spaceship
            self.spaceship.turtle.goto(self.spaceship.x, self.spaceship.y)

            # วาด Asteroids
            for asteroid in self.asteroids:
                asteroid.move()
                asteroid.draw()

            # วาด Fuel
            self.fuel.draw()

            # ตรวจสอบการชนของยานกับน้ำมัน
            self.check_fuel_collision()

            # ตรวจสอบการชนของยานกับอุกกาบาต
            if self.check_collision():
                self.spaceship.turtle.hideturtle()  # ซ่อนยานเมื่อชน
                self.running = False
                break  # ออกจากลูปทันทีเมื่อเกมจบ

            # เพิ่มคะแนน
            self.score += 1

            # เพิ่มระดับความยาก
            if self.score > 0 and self.score % 50 == 0:
                if self.level < (self.score // 50) + 1:  # เพิ่มเลเวลแค่ครั้งเดียวต่อ 50 คะแนน
                    self.level += 1
                    for asteroid in self.asteroids:
                        asteroid.vy *= 1.05

            # แสดงคะแนน
            self.display_score()

            # อัปเดตหน้าจอ
            self.screen.update()
            time.sleep(0.02)

        # แสดงข้อความจบเกม
        self.game_over()
        self.screen.mainloop()

if __name__ == "__main__":
    game = Game(10)
    game.run()