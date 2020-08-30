import pygame
from Specification import *

class Pit:
    def __init__(self, is_discovered, x, y):
        self.image = pygame.image.load(IMG_PIT).convert()
        self.is_discovered = is_discovered
        self.wind_sound = pygame.mixer.Sound('wind.wav')
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

    def update(self, screen, font):
        for i in range(self.size):
            for j in range (self.size):
                if self.noti[i][j] and self.is_discovered[i][j]:
                    text = font.render('Breeze', True, BLACK)
                    textRect = text.get_rect()
                    textRect.center = (40 + i * 70, 45 + j * 70)
                    screen.blit(text, textRect)
                    pygame.display.update()

class Wumpus:
    def __init__(self, is_discovered, x, y):
        self.image = pygame.image.load(IMG_WUMPUS).convert()
        self.size = 10
        self.is_discovered = is_discovered
        self.smell_sound = pygame.mixer.Sound('Sniff.wav')
        self.noti = [[False for i in range(self.size)] for j in range(self.size)]
        self.wumpus_pos = [[False for i in range(self.size)] for j in range(self.size)]
        for i in range(len(x)):
            self.wumpus_pos[x[i]][y[i]] = True


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

    def update(self, screen, font):
        for i in range(self.size):
            for j in range (self.size):
                if self.noti[i][j] and self.is_discovered[i][j]:
                    text = font.render('Stench', True, BLACK)
                    textRect = text.get_rect()
                    textRect.center = (40 + i * 70, 25 + j * 70)
                    screen.blit(text, textRect)
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

    def shoot(self, direct, screen, x, y):
        if direct == 0:
            self.shoot_up(screen, x, y)
        elif direct == 1:
            self.shoot_down(screen, x, y)
        elif direct == 2:
            self.shoot_left(screen, x, y)
        elif direct == 3:
            self.shoot_right(screen, x, y)

    def shoot_right(self, screen, x, y):
        x = 10 + (x-1) * 70
        y = 10 + (y-1) * 70
        x += 210
        screen.blit(self.img_list[0], (x, y))
        pygame.display.update()

    def shoot_left(self, screen, x, y):
        x = 10 + (x - 1) * 70
        y = 10 + (y - 1) * 70
        x -= 210
        screen.blit(self.img_list[1], (x, y))
        pygame.display.update()

    def shoot_up(self, screen, x, y):
        x = 10 + (x - 1) * 70
        y = 10 + (y - 1) * 70
        y -= 210
        screen.blit(self.img_list[2], (x, y))
        pygame.display.update()

    def shoot_down(self, screen, x, y):
        i = 10 + (x-1) * 70
        j = 10 + (y-1) * 70
        j += 210
        screen.blit(self.img_list[3], (i, j))
        pygame.display.update()


