import sys
from Map import *
from Agent import *
import Algorithms

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
        #self.pit = Pit(1, 1)
        self.gold = Gold()
        self.agent = Agent(1, 1)
        self.agent.load_image()
        self.font = pygame.font.Font(FONT_MRSMONSTER, 30)
        self.noti = pygame.font.Font(FONT_MRSMONSTER, 15)
        self.victory = pygame.font.Font(FONT_MRSMONSTER, 50)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.agent)
        self.state = MAP
        self.map_i = 1
        self.mouse = None
        self.bg = pygame.image.load('../Assets/Images/win.jpg').convert()
        self.bg = pygame.transform.scale(self.bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.direct = 3

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

    def win_draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.bg, (0, 0))
        text = self.victory.render('VICTORY!!!', True, BLACK)
        textRect = text.get_rect()
        textRect.center = (500, 50)
        self.screen.blit(text, textRect)

    def win_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    def run(self):
        while True:
            if self.state == MAP:
                self.home_draw()
                self.home_event()

            elif self.state == RUNNING:
                self.running_draw()

                action_list, cave_cell = Algorithms.AgentBrain(MAP_LIST[self.map_i - 1]).solve_wumpus_world()
                map_pos = cave_cell.map_pos     # Theo tọa độ của thầy.

                for action in action_list:
                    pygame.time.delay(50)
                    self.display_action(action)
                    print(action)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    pygame.time.delay(1000)

                self.state = MAP
            elif self.state == WIN:
                self.win_draw()
                self.win_event()
            self.clock.tick(60)


    def display_action(self, action: Algorithms.Action):
        if action == Algorithms.Action.TURN_LEFT:
            self.direct = self.agent.turn_left()
            self.all_sprites.update()
            self.running_draw()
            self.all_sprites.draw(self.screen)
            pygame.display.update()
        elif action == Algorithms.Action.TURN_RIGHT:
            self.direct = self.agent.turn_right()
            self.all_sprites.update()
            self.running_draw()
            self.all_sprites.draw(self.screen)
            pygame.display.update()
        elif action == Algorithms.Action.TURN_UP:
            self.direct = self.agent.turn_up()
            self.all_sprites.update()
            self.running_draw()
            self.all_sprites.draw(self.screen)
            pygame.display.update()
        elif action == Algorithms.Action.TURN_DOWN:
            self.direct = self.agent.turn_down()
            self.all_sprites.update()
            self.running_draw()
            self.all_sprites.draw(self.screen)
            pygame.display.update()
        elif action == Algorithms.Action.MOVE_FORWARD:
            self.agent.move_forward(self.direct)
            i, j = self.agent.get_pos()
            self.map.discover_cell_i_j(i, j)
            self.all_sprites.update()
            self.running_draw()
            self.all_sprites.draw(self.screen)
            pygame.display.update()
        elif action == Algorithms.Action.GRAB_GOLD:
            pass
        elif action == Algorithms.Action.PERCEIVE_BREEZE:
            pass
        elif action == Algorithms.Action.PERCEIVE_STENCH:
            pass
        elif action == Algorithms.Action.SHOOT:
            i, j = self.agent.get_pos()
            self.arrow.shoot(self.direct, self.screen, i, j)
            pygame.display.update()
        elif action == Algorithms.Action.KILL_WUMPUS:
            pass
        elif action == Algorithms.Action.KILL_NO_WUMPUS:
            pass
        elif action == Algorithms.Action.BE_EATEN_BY_WUMPUS:
            pass
        elif action == Algorithms.Action.FALL_INTO_PIT:
            pass
        elif action == Algorithms.Action.KILL_ALL_WUMPUS_AND_GRAB_ALL_FOOD:
            pass
        elif action == Algorithms.Action.CLIMB_OUT_OF_THE_CAVE:
            pass
        elif action == Algorithms.Action.DECTECT_PIT:
            pass
        elif action == Algorithms.Action.DETECT_WUMPUS:
            pass
        elif action == Algorithms.Action.DETECT_NO_PIT:
            pass
        elif action == Algorithms.Action.DETECT_NO_WUMPUS:
            pass
        elif action == Algorithms.Action.INFER_PIT:
            pass
        elif action == Algorithms.Action.INFER_NOT_PIT:
            pass
        elif action == Algorithms.Action.INFER_WUMPUS:
            pass
        elif action == Algorithms.Action.INFER_NOT_WUMPUS:
            pass
        else:
            raise TypeError("Error: " + self.display_action.__name__)
