import pygame
from Specification import *

class Pit:
    def __init__(self, x, y):
        self.image = pygame.image.load(IMG_PIT).convert()
        self.pos = (x, y)
        self.is_discovered = False
        self.wind_sound = pygame.mixer.Sound('wind.wav')

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
        self.smell_sound = pygame.mixer.Sound('Sniff.wav')

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def wumpus_discovered(self):
        self.is_discovered = True

    def update(self, screen):
        if self.is_discovered:
            self.draw(screen)
            pygame.display.update()
class Gold:
    def __init__(self):
        self.image = pygame.image.load(IMG_GOLD).convert()
        self.pos = (840, 150)
        self.is_discovered = False

    def draw(self, screen):
        screen.blit(self.image, self.pos)
    def gold_discovered(self):
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

    def shoot_right(self, screen, x, y):
        screen.blit(self.img_list[0], (x, y))
        pygame.display.update()

    def shoot_left(self, screen, x, y):
        screen.blit(self.img_list[1], (x, y))
        pygame.display.update()

    def shoot_up(self, screen, x, y):
        screen.blit(self.img_list[2], (x, y))
        pygame.display.update()

    def shoot_down(self, screen, x, y):
        screen.blit(self.img_list[3], (x, y))
        pygame.display.update()


