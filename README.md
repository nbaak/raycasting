# 3D Raycasting Simulation in Pygame

This project is a 3D raycasting simulation built using Pygame, a popular Python library for game development. The simulation provides a visual representation of a simple 2D environment viewed through a first-person perspective. It uses raycasting to compute the distances from the player's position to walls in the scene, rendering a 3D-like view of the environment.

## Features

- **2D and 3D Views**: The display is split into two parts:
  - **Left Side**: Displays a top-down 2D map with the player position and rays extending to the walls.
  - **Right Side**: Displays a 3D first-person perspective of the environment, giving the illusion of depth.
- **Dynamic Wall Generation**: Press `W` to randomly generate a new set of walls.
- **View Direction Control**: Use `A` and `D` keys to rotate the player's view left and right, respectively.
- **Screenshot Capture**: Press `Space` to capture a screenshot of the current game view. Each screenshot is saved with a unique filename.

## Getting Started

### Prerequisites

- **Python 3.x**: Make sure you have Python 3 installed on your system.
- **Pygame**: Install Pygame by running:

```
	pip install pygame
```

### Running the Simulation

1. **Clone the Repository**:
   Clone this repository to your local machine or copy the code into a new Python file.

2. **Run the Script**:
   Open a terminal or command prompt and navigate to the directory where the script is located. Run the script using:

  python raycasting_3d.py

3. **Interact with the Simulation**:
   - `A` Key: Rotate the view left.
   - `D` Key: Rotate the view right.
   - `W` Key: Generate new random walls.
   - `Q` Key: Quit the simulation.
   - `Space` Key: Take a screenshot of the current screen. The screenshot will be saved in the same directory as the script with a unique name.

### Files

- **raycasting_3d.py**: The main Python script that contains the code for the raycasting simulation.

## Code Overview

### Key Components

- **create_walls()**: Generates a list of random walls within the given screen dimensions.
- **draw_walls()**: Draws the walls on the 2D map surface.
- **intersection()**: Calculates the intersection point between two line segments.
- **ray_casting()**: Casts rays from the player's position and calculates the distances to the walls, then renders the 2D and 3D views.
- **main()**: Initializes Pygame, sets up the display, handles user input, and contains the main game loop.

### Screenshot Functionality

When the `Space` key is pressed, the current frame of the game is saved as a PNG file in the same directory. A unique filename is generated using `uuid.uuid4()` to ensure that each screenshot is uniquely named.

### Example Screenshot

After pressing the `Space` key, you will see an output like:

Screenshot saved as screenshot_<unique-id>.png

The screenshot will be saved in the script's directory.

## Controls

- `A` - Rotate view left
- `D` - Rotate view right
- `W` - Generate new random walls
- `Q` - Quit the simulation
- `Space` - Capture a screenshot

## Customization

- **Adjust the Field of View**: Modify the `field_of_view` variable to change the player's field of view in degrees.
- **Change the Number of Walls**: Modify the `number_of_walls` variable to increase or decrease the number of walls in the scene.
- **Adjust the Screen Size**: Change the `window_size` variable to set a different screen resolution.

## License

This project is open source and free to use.

## Acknowledgments

- This simulation is inspired by classic raycasting techniques used in early 3D games like Wolfenstein 3D.
- Built using the [Pygame](https://www.pygame.org/) library.

Enjoy exploring and tweaking the code! Feel free to contribute by adding new features or optimizing the performance. Happy coding!
