import pygame
from Specification import *

class Pit:
    def __init__(self, x, y):
        self.is_discovered = None
        self.size = 10
        self.noti = [[False for i in range(self.size)] for j in range(self.size)]
        self.pit_pos = [[False for i in range(self.size)] for j in range(self.size)]
        for i in range(len(x)):
            self.pit_pos[x[i]][y[i]] = True

    def pit_discovered(self):
        self.is_discovered = True

    def pit_notification(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.pit_pos[i][j]:
                    if i > 0:
                        self.noti[i - 1][j] = True
                    if i < self.size - 1:
                        self.noti[i + 1][j] = True
                    if j > 0:
                        self.noti[i][j - 1] = True
                    if j < self.size - 1:
                        self.noti[i][j + 1] = True

    def update(self, screen, font, is_discovered):
        for i in range(self.size):
            for j in range (self.size):
                if self.noti[i][j] and is_discovered[i][j]:
                    text = font.render('Breeze', True, BLACK)
                    textRect = text.get_rect()
                    textRect.center = (42 + j * 70, 40 + i * 70)
                    screen.blit(text, textRect)
                    pygame.display.update()

class Wumpus:
    def __init__(self, x, y):
        self.image = pygame.image.load(IMG_WUMPUS).convert()
        self.image = pygame.transform.scale(self.image, (100, 200))
        self.size = 10
        self.pos = (835, 100)
        self.is_discovered = None
        self.noti = [[False for i in range(self.size)] for j in range(self.size)]
        self.wumpus_pos = [[False for i in range(self.size)] for j in range(self.size)]
        for i in range(len(x)):
            self.wumpus_pos[x[i]][y[i]] = True

    def wumpus_kill(self, screen, font):
        text = font.render('Killed a wumpus!!!', True, BLACK)
        textRect = text.get_rect()
        textRect.center = self.pos
        screen.blit(text, textRect)
        screen.blit(self.image, (800, 200))
        pygame.display.update()

    def wumpus_notification(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.wumpus_pos[i][j]:
                    if i > 0:
                        self.noti[i - 1][j] = True
                    if i < self.size - 1:
                        self.noti[i + 1][j] = True
                    if j > 0:
                        self.noti[i][j - 1] = True
                    if j < self.size - 1:
                        self.noti[i][j + 1] = True

    def wumpus_killed(self, i, j):
        self.wumpus_pos[i][j] = False
        if i > 0:
            self.noti[i-1][j] = False
        if i < self.size - 1:
            self.noti[i+1][j] = False
        if j > 0:
            self.noti[i][j - 1] = False
        if j < self.size - 1:
            self.noti[i][j + 1] = False

    def update(self, screen, font, is_discovered):
        for i in range(self.size):
            for j in range (self.size):
                if self.noti[i][j] and is_discovered[i][j]:
                    text = font.render('Stench', True, BLACK)
                    textRect = text.get_rect()
                    textRect.center = (45 + j * 70, 30 + i * 70)
                    screen.blit(text, textRect)
                    pygame.display.update()

    def stench_i_j(self, i, j):
        return self.noti[i][j]


class Gold:
    def __init__(self):
        self.image = pygame.image.load(IMG_GOLD).convert()
        self.image = pygame.transform.scale(self.image, (150,300))
        self.pos = (835, 100)

    def grab_gold(self, screen, font):
        text = font.render('You found a gold!!!', True, BLACK)
        textRect = text.get_rect()
        textRect.center = self.pos
        screen.blit(text, textRect)
        screen.blit(self.image, (750, 200))
        text = font.render('Score + 100', True, BLACK)
        textRect.center = (900, 600)
        screen.blit(text, textRect)
        pygame.display.update()


class Arrow:
    def __init__(self):
        self.img_list = []
        temp = [IMG_ARROW_RIGHT, IMG_ARROW_LEFT, IMG_ARROW_UP, IMG_ARROW_DOWN]
        for i in range(0, 4):
            img = pygame.image.load(temp[i]).convert()
            self.img_list.append(img)

    def shoot(self, direct, screen, y, x):
        if direct == 0:
            self.shoot_up(screen, x, y)
        elif direct == 1:
            self.shoot_down(screen, x, y)
        elif direct == 2:
            self.shoot_left(screen, x, y)
        elif direct == 3:
            self.shoot_right(screen, x, y)

    def shoot_right(self, screen, x, y):
        x = 10 + (x + 1) * 70
        y = 10 + y * 70
        screen.blit(self.img_list[0], (x, y))
        pygame.display.update()

    def shoot_left(self, screen, x, y):
        x = 10 + (x - 1) * 70
        y = 10 + y * 70
        screen.blit(self.img_list[1], (x, y))
        pygame.display.update()

    def shoot_up(self, screen, x, y):
        x = 10 + x * 70
        y = 10 + (y - 1) * 70
        screen.blit(self.img_list[2], (x, y))
        pygame.display.update()

    def shoot_down(self, screen, x, y):
        i = 10 + x * 70
        j = 10 + (y + 1) * 70
        screen.blit(self.img_list[3], (i, j))
        pygame.display.update()


