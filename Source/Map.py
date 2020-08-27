import pygame
from Specification import *

class Map:
    def __init__(self):
        self.space = 10
        self.size = (10, 10)
        self.cell_size = 60
        self.cell = pygame.image.load(IMG_INITIAL_CELL).convert()
        self.discover_cell = pygame.image.load(IMG_DISCOVERED_CELL).convert()

    def draw(self, screen):
        x = self.space
        y = self.space

        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                screen.blit(self.cell, (x, y))
                x += self.space + self.cell_size
            y += self.space + self.cell_size
            x = self.space
