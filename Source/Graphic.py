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
        self.agent = Agent(1, 1)
        self.agent.load_image()
        self.font = pygame.font.Font(FONT_MRSMONSTER, 30)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.agent)

    def draw(self):
        self.screen.fill(WHITE)
        self.map.draw(self.screen)
        score = self.agent.get_score()
        text = self.font.render('Your score: ' + str(score), True, BLACK)
        textRect = text.get_rect()
        textRect.center = (820, 25)
        self.screen.blit(text, textRect)

    def run(self):
        self.draw()
        self.agent.appear(self.screen)
        pygame.display.update()
        self.agent.smell_stench(self.screen, self.font)
        while True:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.agent.move_down()
                        i, j = self.agent.get_pos()
                        self.map.discover_cell_i_j(i, j)
                        self.all_sprites.update()
                        self.draw()
                        self.all_sprites.draw(self.screen)
                        pygame.display.update()
                    elif event.key == pygame.K_UP:
                        self.agent.move_up()
                        i, j = self.agent.get_pos()
                        self.map.discover_cell_i_j(i, j)
                        self.all_sprites.update()
                        self.draw()
                        self.all_sprites.draw(self.screen)
                        pygame.display.update()
                    elif event.key == pygame.K_LEFT:
                        self.agent.move_left()
                        i, j = self.agent.get_pos()
                        self.map.discover_cell_i_j(i, j)
                        self.all_sprites.update()
                        self.draw()
                        self.all_sprites.draw(self.screen)
                        pygame.display.update()
                    elif event.key == pygame.K_RIGHT:
                        self.agent.move_right()
                        i, j = self.agent.get_pos()
                        self.map.discover_cell_i_j(i, j)
                        self.all_sprites.update()
                        self.draw()
                        self.all_sprites.draw(self.screen)
                        pygame.display.update()





