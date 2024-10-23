# Snake Game

This project is a simple snake game developed using Python and Pygame. The game features a start menu, a score system, and different graphical representations of the snake's body.

## Installation

1. **Install Python:** Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

2. **Install Pygame:** Install the Pygame library using pip:
   ```bash
   pip install pygame
   ```

3. **Clone the Repository:** Clone this repository or download the code.

4. **Assets:** Ensure the following image assets are placed in an `./asset/` directory:
   - `apple.png`
   - `head_up.png`
   - `head_down.png`
   - `head_right.png`
   - `head_left.png`
   - `tail_up.png`
   - `tail_down.png`
   - `tail_right.png`
   - `tail_left.png`
   - `body_vertical.png`
   - `body_horizontal.png`
   - `body_topright.png`
   - `body_topleft.png`
   - `body_bottomright.png`
   - `body_bottomleft.png`

## How to Run

1. **Navigate to the Project Directory:** Open your terminal and navigate to the directory where the script is located.

2. **Run the Game:**
   ```bash
   python snake_game.py
   ```

## Game Features

- **Start Menu:**
  - The game starts with a menu where you can choose to `Play` or `Quit`.

- **Snake Movement:**
  - The snake moves automatically in the direction it is facing.
  - You can control the snake's direction using the arrow keys:
    - `Up Arrow` to move up
    - `Right Arrow` to move right
    - `Down Arrow` to move down
    - `Left Arrow` to move left

- **Fruit Collection:**
  - The snake grows in length when it eats the fruit (represented by an apple).

- **Collision Detection:**
  - The game ends when the snake collides with the walls or itself.

- **Score Display:**
  - The current score (based on the length of the snake) is displayed in the bottom-right corner.

- **Game Over Screen:**
  - When the game ends, a "GAME OVER" message and the final score are displayed.

## Code Structure

### Classes

- **SNAKE:**
  - Handles the snake's properties and behavior, including movement, growth, and graphical representation.

- **FRUIT:**
  - Manages the fruit's position and rendering.

- **MAIN:**
  - Coordinates the game's core logic, such as updating game state, checking for collisions, and drawing game elements.

- **Button:**
  - Manages the interactive buttons in the start menu.

- **STARTMENU:**
  - Controls the start menu display and user interaction.

### Main Game Loop

- **Event Handling:** Processes user inputs and game events.
- **Game State Management:** Controls transitions between the start menu, game play, and game over states.
- **Rendering:** Updates the display with the current state of the game.

## License

This project is open-source and can be freely used and modified.
