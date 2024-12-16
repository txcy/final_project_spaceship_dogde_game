# **Spaceship Dodge Game**

## **Project Title**
**Spaceship Dodge Game**  
A survival game where players control a spaceship to dodge falling asteroids and collect fuel for bonus points.

---

## **Project Description**

The **Spaceship Dodge Game** is a Python-based arcade game using the `turtle` module. Players navigate a spaceship to avoid asteroids and collect fuel. The game features dynamic difficulty levels, a scoring system, and interactive menus for starting, restarting, and exiting the game.

---

## **Key Features**

- **Spaceship Movement**: Navigate using arrow keys (`Up`, `Down`, `Left`, `Right`).
- **Asteroid Avoidance**: Dodge falling asteroids that increase in speed as you level up.
- **Fuel Collection**: Collect fuel for bonus points.
- **Dynamic Difficulty**: Asteroids fall faster as levels progress.
- **Game States**:
  - **Main Menu**: Start or exit the game.
  - **Gameplay**: Real-time interaction with asteroids and fuel.
  - **Game Over**: View final scores with options to restart or quit.
- **Score Tracking**: Display of current score, collected fuel, and current level.

---

## **How to Install and Run the Project**

### **1. Prerequisites**
Ensure you have:
- Python 3.8 or higher installed.

### **2. Steps to Run the Project**

1. Clone the repository:
   ```bash
   git clone https://github.com/txcy/final_project_spaceship_dogde_game.git
   cd Spaceship_Dodge_Game
2. Run the game:
   ```bash
   python run_ball.py


Usage
--------------
How to Play

1.Start the Game:
Press S to start the game from the Main Menu.
Press Q to quit.

2.Controls:
- **Arrow Up: Move spaceship up.
- **Arrow Down: Move spaceship down.
- **Arrow Left: Move spaceship left.
- **Arrow Right: Move spaceship right.
  
3.Objective:
- **Avoid falling asteroids.
- **Collect yellow fuel dots to increase your fuel score.
- **Survive as long as possible to reach higher levels.
  
4.Game Over:
- **The game ends if the spaceship collides with an asteroid.
- **Press S to restart or Q to quit.

Project Design and Implementation
UML Class Diagram
--------
+--------------------+       +------------------+       +------------------+
|       Game         |<----> |    Spaceship     |       |     Asteroid     |
|--------------------|       |------------------|       |------------------|
| - screen           |       | - size           |       | - size           |
| - spaceship        |       | - x, y           |       | - x, y           |
| - asteroids        |       | - turtle         |       | - vx, vy         |
| - fuel             |       |------------------|       | - color          |
| - score, level     |       | + move()         |       |------------------|
| - fuel_score       |       | + draw()         |       | + move()         |
|--------------------|       +------------------+       | + draw()         |
| + main_menu()      |                                  +------------------+
| + run()            |               +------------------+
| + check_collision()|<------------->|      Fuel         |
| + game_over()      |               |------------------|
+--------------------+               | - size           |
                                     | - x, y           |
                                     | - color          |
                                     |------------------|
                                     | + draw()         |
                                     | + relocate()     |
                                     +------------------+

                                     
Class Descriptions
---------------
1.Game:
Handles game states, user input, and the main game loop.
- **Manages interactions between the spaceship, asteroids, and fuel.
2.Spaceship:
- **Allows the player to control the spaceship's movement on the screen.
3.Asteroid:
- **Represents falling obstacles that the player must avoid.
- **Resets position when moving off-screen.
4.Fuel:
- **Represents collectible objects that give bonus points.
- **Relocates to a random position when collected.

Testing and Debugging
-------------
Testing Scenarios

1.Game Start:
- **Main Menu functions correctly.
- **Game starts upon pressing S.

2.Gameplay:
- **Asteroids fall continuously.
- **Fuel relocates after collection.
- **Collision detection with asteroids ends the game.
  
3.Game Over:
- **Scores are displayed correctly.
- **Restarting or quitting works as expected.

Known Issues
-------
No major bugs detected; the game works as intended.

Demo
----------
View a full demo of the project in this https://youtu.be/Aaxm28qSstc?si=bLOpxIxh9bSJc8Xb .

Project Status
----------
The project is fully implemented and functional, including all key features and menus.

Contributors
----------
Thanakrit BUNGSRI
GitHub: https://github.com/txcy
Contact: thanakrit.bung@ku.th

