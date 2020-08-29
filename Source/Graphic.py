import sys
from Map import *
from Agent import *

class Graphic:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.caption = pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        self.map = Map()
        self.arrow = Arrow()
        #self.wumpus = Wumpus(1, 1)
        self.pit = Pit(1, 1)
        self.gold = Gold()
        self.agent = Agent(1, 1)
        self.agent.load_image()
        self.font = pygame.font.Font(FONT_MRSMONSTER, 30)
        self.noti = pygame.font.Font(FONT_MRSMONSTER, 15)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.agent)
        self.state = MAP
        self.map_i = 1

    def running_draw(self):
        self.screen.fill(WHITE)
        self.map.draw(self.screen)
        score = self.agent.get_score()
        text = self.font.render('Your score: ' + str(score), True, BLACK)
        textRect = text.get_rect()
        textRect.center = (820, 25)
        self.screen.blit(text, textRect)

    def draw_button(self, surf, rect, button_color, text_color, text):
        pygame.draw.rect(surf, button_color, rect)
        text_surf = self.font.render(text, True, text_color)
        text_rect = text_surf.get_rect()
        text_rect.center = rect.center
        self.screen.blit(text_surf, text_rect)

    def home_draw(self):
        self.screen.fill(WHITE)

    def home_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 235 <= self.mouse[0] <= 735 and 120 <= self.mouse[1] <= 170:
                    self.state = RUNNING
                    self.map_i = 1
                elif 235 <= self.mouse[0] <= 735 and 200 <= self.mouse[1] <= 250:
                    self.state = RUNNING
                    self.map_i = 2
                elif 235 <= self.mouse[0] <= 735 and 280 <= self.mouse[1] <= 330:
                    self.state = RUNNING
                    self.map_i = 3
                elif 235 <= self.mouse[0] <= 735 and 360 <= self.mouse[1] <= 410:
                    self.state = RUNNING
                    self.map_i = 4
                elif 235 <= self.mouse[0] <= 735 and 440 <= self.mouse[1] <= 490:
                    self.state = RUNNING
                    self.map_i = 5
                elif 235 <= self.mouse[0] <= 735 and 520 <= self.mouse[1] <= 570:
                    pygame.quit()
                    sys.exit()
            self.mouse = pygame.mouse.get_pos()
            if 235 <= self.mouse[0] <= 735 and 120 <= self.mouse[1] <= 170:
                self.draw_button(self.screen, LEVEL_1_POS, DARK_GREY, RED, "MAP 1")
            else:
                self.draw_button(self.screen, LEVEL_1_POS, LIGHT_GREY, BLACK, "MAP 1")
            if 235 <= self.mouse[0] <= 735 and 200 <= self.mouse[1] <= 250:
                self.draw_button(self.screen, LEVEL_2_POS, DARK_GREY, RED, "MAP 2")
            else:
                self.draw_button(self.screen, LEVEL_2_POS, LIGHT_GREY, BLACK, "MAP 2")
            if 235 <= self.mouse[0] <= 735 and 280 <= self.mouse[1] <= 330:
                self.draw_button(self.screen, LEVEL_3_POS, DARK_GREY, RED, "MAP 3")
            else:
                self.draw_button(self.screen, LEVEL_3_POS, LIGHT_GREY, BLACK, "MAP 3")
            if 235 <= self.mouse[0] <= 735 and 360 <= self.mouse[1] <= 410:
                self.draw_button(self.screen, LEVEL_4_POS, DARK_GREY, RED, "MAP 4")
            else:
                self.draw_button(self.screen, LEVEL_4_POS, LIGHT_GREY, BLACK, "MAP 4")
            if 235 <= self.mouse[0] <= 735 and 440 <= self.mouse[1] <= 490:
                self.draw_button(self.screen, LEVEL_5_POS, DARK_GREY, RED, "MAP 5")
            else:
                self.draw_button(self.screen, LEVEL_5_POS, LIGHT_GREY, BLACK, "MAP 5")
            if 235 <= self.mouse[0] <= 735 and 520 <= self.mouse[1] <= 570:
                self.draw_button(self.screen, EXIT_POS, DARK_GREY, RED, "EXIT")
            else:
                self.draw_button(self.screen, EXIT_POS, LIGHT_GREY, BLACK, "EXIT")
            pygame.display.update()

    def run(self):
        '''self.running_draw()
        self.agent.appear(self.screen)
        pygame.display.update()'''

        while True:
            if self.state == MAP:
                self.home_draw()
                self.home_event()
            self.clock.tick(60)
            '''for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.agent.move_down()
                        i, j = self.agent.get_pos()
                        self.map.discover_cell_i_j(i, j)
                        self.all_sprites.update()
                        self.running_draw()
                        self.wumpus.update(self.screen, self.noti)
                        self.all_sprites.draw(self.screen)
                        pygame.display.update()
                    elif event.key == pygame.K_SPACE:
                        self.wumpus.wumpus_killed(3, 1)
                        i, j = self.agent.get_pos()
                        self.map.discover_cell_i_j(i, j)
                        self.all_sprites.update()
                        self.running_draw()
                        self.all_sprites.draw(self.screen)
                        pygame.display.update()'''


