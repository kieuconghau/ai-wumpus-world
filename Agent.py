import pygame


class Agent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.hunter = pygame.image.load('hunter_right.png').convert()

    def update(self):
        pass
