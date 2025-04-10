# Asteroids Game

A classic Asteroids game built with Python and Pygame as part of a Boot.dev project. Control a spaceship to shoot and destroy asteroids while avoiding collisions.

## Features
- **Player Controls**:
  - `W` and `S`: Move forward and backward.
  - `A` and `D`: Rotate left and right.
  - `Spacebar`: Shoot bullets (0.3-second cooldown).
- **Gameplay**:
  - Asteroids spawn from screen edges and move across.
  - Shoot asteroids to split them: large → medium → small → disappear.
  - Colliding with an asteroid ends the game with "Game over!".
- **Technical Details**:
  - Runs at 60 FPS.
  - Uses Pygame sprite groups for managing objects.
  - Collision detection between player-asteroids and shots-asteroids.

## Requirements
- Python 3.12 or higher
- Pygame 2.6.1

## Setup Instructions
1. Clone the repository:
   git clone https://github.com/FLOYD-DEV/Asteroids.git
   cd Asteroids 

2. Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate  # On Windows WSL: source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the game:
python3 main.py

Built by C. Welton (FLOYD-DEV) as part of a project for the wonderful folks at Boot.dev. Enjoy.

