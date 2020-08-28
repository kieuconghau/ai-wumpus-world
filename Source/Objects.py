import pygame
from Specification import *

class Pit:
    def __init__(self, x, y):
        self.image = pygame.image.load(IMG_PIT).convert()
        self.pos = (x, y)
        self.is_discovered = False

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def pit_discovered(self):
        self.is_discovered = True

    def pit_notification(self):
        pass

    def update(self, screen):
        if self.is_discovered:
            self.draw(screen)
            pygame.display.update()

class Wumpus:
    def __init__(self, x, y):
        self.image = pygame.image.load(IMG_WUMPUS).convert()
        self.pos = (x, y)
        self.is_discovered = False

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def pit_discovered(self):
        self.is_discovered = True

    def update(self, screen):
        if self.is_discovered:
            self.draw(screen)
            pygame.display.update()

class Arrow:
    def __init__(self):
        self.img_list = []
        temp = [IMG_ARROW_RIGHT, IMG_ARROW_LEFT, IMG_ARROW_UP, IMG_ARROW_DOWN]
        for i in range(0, 4):
            img = pygame.image.load(temp[i]).convert()
            self.img_list.append(img)
