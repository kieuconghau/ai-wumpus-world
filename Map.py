import pygame
from Specification import *


class Map:
    def __init__(self):
        pygame.init()
        self.spacing = 10
        self.size = (10, 10)
        self.cell_size = 60
        self.cell = pygame.image.load(initcell_img).convert()
        self.discover_cell = pygame.image.load(discovercell_img).convert()

    def draw(self, screen):
        x = self.spacing
        y = self.spacing
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                screen.blit(self.cell, (x, y))
                x += self.spacing + self.cell_size
            y += self.spacing + self.cell_size
        x = self.spacing
