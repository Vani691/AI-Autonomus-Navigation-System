import pygame

CELL_SIZE = 30

class Robot:
    def __init__(self, start, path):
        self.path = path
        self.index = 0
        self.position = start

    def move(self):
        if self.index < len(self.path):
            self.position = self.path[self.index]
            self.index += 1

    def draw(self, screen):
        rect = pygame.Rect(
            self.position[1]*CELL_SIZE,
            self.position[0]*CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
        pygame.draw.rect(screen, (255,0,0), rect)