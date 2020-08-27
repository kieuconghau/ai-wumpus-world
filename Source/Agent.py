import pygame
from Specification import *

class Agent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.hunter = pygame.image.load(IMG_HUNTER_RIGHT).convert()
        self.score = 0

    def draw_score(self, screen, font):
        text = font.render(str(self.score), True, BLACK)
        textRect = text.get_rect()
        textRect.center = (880, 25)
        screen.blit(text, textRect)

    def update(self, screen, font):
        self.draw_score(screen, font)
