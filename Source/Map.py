import pygame
from Specification import *

class Map:
    def __init__(self):
        self.space = 10
        self.size = 10
        self.cell_size = 60
        self.cell = pygame.image.load(IMG_INITIAL_CELL).convert()
        self.discover_cell = pygame.image.load(IMG_DISCOVERED_CELL).convert()
        self.is_discover = [[False for i in range(self.size)] for j in range(self.size)]
        self.is_discover[0][0] = True

    def draw(self, screen):
        x = self.space
        y = self.space

        for i in range(0, self.size):
            for j in range(0, self.size):
                if(self.is_discover[i][j]):
                    screen.blit(self.discover_cell, (x, y))
                    x += self.space + self.cell_size
                else:
                    screen.blit(self.cell, (x, y))
                    x += self.space + self.cell_size
            y += self.space + self.cell_size
            x = self.space

    def discover_cell_i_j(self, i, j):
        self.is_discover[i][j] = True

    def discovered(self):
        return self.is_discover

    def agent_climb(self, screen, font):
        text = font.render('Climbed out!!!', True, BLACK)
        textRect = text.get_rect()
        textRect.center = (830, 100)
        screen.blit(text, textRect)
        text = font.render('Score + 10', True, BLACK)
        textRect.center = (850, 150)
        screen.blit(text, textRect)