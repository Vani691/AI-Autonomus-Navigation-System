import pygame
import random

CELL_SIZE = 30

class GridEnvironment:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Initialize grid with 0 (empty space)
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

        self.screen = pygame.display.set_mode((cols * CELL_SIZE, rows * CELL_SIZE))
        pygame.display.set_caption("Autonomous Navigation")

        self.generate_obstacles()

    def generate_obstacles(self):
        """Initializes the grid with static obstacles."""
        for i in range(self.rows):
            for j in range(self.cols):
                if random.random() < 0.2:
                    self.grid[i][j] = 1

    def update_from_sensor(self):
        """
        Simulates dynamic obstacle detection.
        Now correctly indented inside the class.
        """
        x = random.randint(0, self.rows - 1)
        y = random.randint(0, self.cols - 1)
        self.grid[x][y] = 1            

    def draw(self):
        """Renders the environment to the Pygame window."""
        self.screen.fill((255, 255, 255)) # White background

        for i in range(self.rows):
            for j in range(self.cols):
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)

                # Draw obstacles in Black
                if self.grid[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), rect)

                # Draw grid lines in Light Gray
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)