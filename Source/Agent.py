import pygame
from Specification import *

class Agent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.image = pygame.image.load(IMG_HUNTER_RIGHT).convert()
        self.x = 40
        self.y = 40
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.spacing = 70

    def appear(self, screen):
        screen.blit(self.image, (10, 10))

    def get_score(self):
        return self.score

    def move_up(self):
        self.y -= self.spacing

    def move_down(self):
        self.y += self.spacing

    def move_left(self):
        self.x -= self.spacing

    def move_right(self):
        self.x += self.spacing

    def update(self):
        if self.x > 670:
            self.x -= self.spacing
        elif self.x < 40:
            self.x += self.spacing
        elif self.y < 40:
            self.y += self.spacing
        elif self.y > 670:
            self.y -= self.spacing
        self.rect.center = (self.x, self.y)
