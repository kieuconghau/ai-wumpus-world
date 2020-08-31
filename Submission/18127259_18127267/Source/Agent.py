import pygame
from Specification import *
from Objects import *

class Agent(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.image = pygame.image.load(IMG_HUNTER_RIGHT).convert()
        self.img_list = []
        self.y = 40 + (x-1) * 70
        self.x = 40 + (y-1) * 70
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.spacing = 70
        self.i = x - 1
        self.j = y - 1

    def load_image(self):
        self.img_list.append(self.image)
        temp = [IMG_HUNTER_LEFT, IMG_HUNTER_UP, IMG_HUNTER_DOWN]
        for i in range (0, 3):
            img = pygame.image.load(temp[i]).convert()
            self.img_list.append(img)

    def appear(self, screen):
        screen.blit(self.image, (self.x - 30, self.y - 30))

    def get_score(self):
        return self.score

    def move_forward(self, direct):
        if direct == 0:
            self.move_up()
        elif direct == 1:
            self.move_down()
        elif direct == 2:
            self.move_left()
        elif direct == 3:
            self.move_right()

    def move_up(self):
        self.y -= self.spacing
        self.score -= 10
        if self.i > 0:
            self.i -= 1

    def move_down(self):
        self.y += self.spacing
        self.score -= 10
        if self.i < 9:
            self.i += 1

    def move_left(self):
        self.x -= self.spacing
        self.score -= 10
        if self.j > 0:
            self.j -= 1

    def move_right(self):
        self.x += self.spacing
        self.score -= 10
        if self.j < 9:
            self.j += 1

    def turn_up(self):
        self.image = self.img_list[3]
        return 0

    def turn_down(self):
        self.image = self.img_list[2]
        return 1

    def turn_left(self):
        self.image = self.img_list[1]
        return 2

    def turn_right(self):
        self.image = self.img_list[0]
        return 3

    def update(self):
        if self.x > 670:
            self.x -= self.spacing
            self.score += 10

        elif self.x < 40:
            self.x += self.spacing
            self.score += 10

        elif self.y < 40:
            self.y += self.spacing
            self.score += 10

        elif self.y > 670:
            self.y -= self.spacing
            self.score += 10

        self.rect.center = (self.x, self.y)

    def get_pos(self):
        return self.i, self.j

    def shoot(self):
        self.score -= 100

    def wumpus_or_pit_collision(self):
        self.score -= 10000

    def grab_gold(self):
        self.score += 100

    def climb(self):
        self.score += 10

