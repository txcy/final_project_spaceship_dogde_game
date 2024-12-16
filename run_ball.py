import turtle
import random
import math
from ball import Asteroid
from paddle import Spaceship
import time
from fuel import Fuel


class Game:
    def __init__(self, num_asteroids):
        # Set up the screen
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Spaceship Dodge Game")
        self.screen.tracer(0)

        # Set up images
        self.background_image = "galaxy.gif"
        self.spaceship_image = "spaceship.gif"
        turtle.register_shape(self.spaceship_image)
        try:
            self.screen.bgpic(self.background_image)
        except turtle.TurtleGraphicsError:
            print(f"Error: {self.background_image} not found.")

        # Create spaceship and objects
        self.num_asteroids = num_asteroids
        self.running = False

    def setup_game(self):
        """Reset the entire game state."""
        self.spaceship = Spaceship(20, 0, -250, self.spaceship_image)
        self.asteroids = [self.create_asteroid() for _ in range(self.num_asteroids)]
        self.fuel = Fuel(15, random.randint(-380, 380), random.randint(-250, 250), "yellow")
        self.score = 0
        self.fuel_score = 0
        self.level = 1
        self.running = True

        # Register spaceship control keys
        self.screen.listen()
        self.screen.onkeypress(lambda: self.spaceship.move("up"), "Up")
        self.screen.onkeypress(lambda: self.spaceship.move("down"), "Down")
        self.screen.onkeypress(lambda: self.spaceship.move("left"), "Left")
        self.screen.onkeypress(lambda: self.spaceship.move("right"), "Right")

    def main_menu(self):
        """Display the main menu."""
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
        """Start a new game."""
        self.setup_game()
        self.run()

    def quit_game(self):
        """Exit the game."""
        self.screen.bye()

    def create_asteroid(self):
        """Create a new asteroid."""
        size = random.randint(10, 20)
        x = random.randint(-380, 380)
        y = 300
        vx = 0
        vy = random.uniform(-1.0, -1.5)  # Slow down the speed
        color = random.choice(["gray", "darkgray", "lightgray"])
        return Asteroid(size, x, y, vx, vy, color)

    def check_collision(self):
        """Check if the spaceship collides with an asteroid."""
        for asteroid in self.asteroids:
            distance = math.sqrt((self.spaceship.x - asteroid.x) ** 2 + (self.spaceship.y - asteroid.y) ** 2)
            if distance < self.spaceship.size + asteroid.size:
                return True
        return False

    def check_fuel_collision(self):
        """Check if the spaceship collects fuel."""
        distance = math.sqrt((self.spaceship.x - self.fuel.x) ** 2 + (self.spaceship.y - self.fuel.y) ** 2)
        if distance < self.spaceship.size + self.fuel.size:
            self.fuel_score += 1
            self.fuel.relocate()

    def display_score(self):
        """Display the current score and level."""
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(-380, 260)
        turtle.color("white")
        turtle.write(f"Score: {self.score}  Fuel Collected: {self.fuel_score}  Level: {self.level}",
                     font=("Arial", 16, "bold"))

    def reset_game(self):
        """Reset all game states to restart."""
        turtle.clear()  # Clear the screen
        self.spaceship.turtle.hideturtle()  # Hide the old spaceship
        self.spaceship = Spaceship(20, 0, -250, self.spaceship_image)  # Create a new spaceship

        # Create new asteroids
        self.asteroids = [self.create_asteroid() for _ in range(10)]

        # Create new fuel
        self.fuel = Fuel(15, random.randint(-380, 380), random.randint(-250, 250), "yellow")

        # Reset game state
        self.score = 0
        self.fuel_score = 0
        self.level = 1
        self.running = True
        self.run()  # Start a new game

    def game_over(self):
        """Display the game over screen with the final score."""
        turtle.clear()
        turtle.penup()
        turtle.hideturtle()
        turtle.color("red")

        # Display GAME OVER message
        turtle.goto(0, 50)
        turtle.write("GAME OVER", align="center", font=("Arial", 32, "bold"))

        # Display final scores
        turtle.color("white")
        turtle.goto(0, 0)
        turtle.write(f"Final Score: {self.score}", align="center", font=("Arial", 20, "bold"))
        turtle.goto(0, -40)
        turtle.write(f"Fuel Collected: {self.fuel_score}", align="center", font=("Arial", 20, "bold"))

        # Display restart and quit options
        turtle.goto(0, -80)
        turtle.write("Press 'S' to Restart or 'Q' to Quit", align="center", font=("Arial", 16, "bold"))
        self.screen.update()

        # Wait for restart or quit input
        self.screen.listen()
        self.screen.onkeypress(self.reset_game, "s")  # Press S to restart
        self.screen.onkeypress(self.screen.bye, "q")  # Press Q to quit the game

    def run(self):
        """Main game loop."""
        while self.running:
            turtle.clear()

            # Draw the spaceship
            self.spaceship.turtle.goto(self.spaceship.x, self.spaceship.y)

            # Draw the asteroids
            for asteroid in self.asteroids:
                asteroid.move()
                asteroid.draw()

            # Draw the fuel
            self.fuel.draw()

            # Check for collisions
            self.check_fuel_collision()
            if self.check_collision():
                self.running = False
                break

            # Increase score and difficulty
            self.score += 1
            if self.score % 50 == 0:
                self.level += 1
                for asteroid in self.asteroids:
                    asteroid.vy *= 1.05

            # Display the score
            self.display_score()

            # Update the screen
            self.screen.update()
            time.sleep(0.01)

        self.game_over()


if __name__ == "__main__":
    game = Game(10)
    while True:
        game.main_menu()
        game.screen.mainloop()
