import pygame

class Pit:
    def __init__(self, x, y):
        self.image = pygame.image.load('hole.png').convert()
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
        self.image = pygame.image.load('hole.png').convert()
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