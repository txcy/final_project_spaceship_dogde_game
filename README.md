🚀 Spaceship Dodge Game
Spaceship Dodge Game is a Python-based game created using the Turtle Graphics library. Players control a spaceship to dodge falling asteroids while collecting fuel for bonus points. The game progressively becomes more challenging as the player's score increases.

🎮 How to Play
Main Menu:

Press 'S' to Start the game.
Press 'Q' to Quit the game.
Game Controls:

Use the arrow keys to move the spaceship:
Up Arrow: Move up
Down Arrow: Move down
Left Arrow: Move left
Right Arrow: Move right
Objective:

Dodge the falling asteroids.
Collect fuel (yellow icons) to earn bonus points.
Game Over:

When the spaceship collides with an asteroid, the game ends.
A Game Over Screen will display:
Final Score
Total Fuel Collected
Highest Level Reached
Press 'S' to Restart or 'Q' to Quit.

🗂️ Project Structure
Spaceship_Dodge_Game/
│
├── ball.py          # Class for Asteroid objects
├── paddle.py        # Class for Spaceship objects
├── fuel.py          # Class for Fuel objects
├── my_event.py      # Event class (optional usage)
├── run_ball.py      # Main game script
└── assets/          
    ├── galaxy.gif   # Background image
    ├── spaceship.gif# Spaceship image
    ├── fuel.gif     # Fuel icon image
    └── game_over.gif# Optional explosion image


🔧 Installation and Execution
1. Prerequisites:
Install Python 3.8+.
Install Turtle Graphics (comes with Python by default).
2. Download the Game:
Clone the repository or download it as a ZIP file.
git clone https://github.com/txcy/final_project_spaceship_dogde_game.git
cd spaceship-dodge-game
3. Run the Game:
Open a terminal in the project directory and run:


🚀 Game Features
1.Spaceship Control:
:Players use arrow keys to control the movement of the spaceship.

2.Falling Asteroids:
:Asteroids drop continuously from the top of the screen.
:The speed of asteroids increases as the player advances through levels.

3.Fuel Collection:
:Randomly spawning yellow fuel items can be collected for bonus points.

4.Dynamic Difficulty:
:The game becomes progressively more difficult with higher levels, but the gameplay remains smooth and fair.

5.Game Over Screen:
:Displays a summary of the player's progress:
:Final Score
:Fuel Collected
:Level Reached

6.Restart and Quit:
:Players can restart the game or quit directly from the Game Over screen.
----------------------------
🛠️ Future Improvements
1.Sound Effects:
Add sound when collecting fuel or when colliding with an asteroid.

2.Power-Ups:
Introduce temporary shields or speed boosts.

3.High Score Saving
Save the player's highest score to a file.

4.Multiple Difficulty Modes:
Allow players to choose from Easy, Medium, or Hard modes.

👨‍💻 Developer
Name: Thanakrit BUNGSRI
Email: thanakrit.bung@ku.th
GitHub: https://github.com/txcy

