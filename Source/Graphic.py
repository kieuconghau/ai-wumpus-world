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
        self.agent = Agent()
        self.font = pygame.font.Font(FONT_MRSMONSTER, 30)
        self.text = self.font.render('Your score:', True, BLACK)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.agent)
        self.count = 2

    def draw(self):
        self.screen.fill(WHITE)
        self.map.draw(self.screen)
        textRect = self.text.get_rect()
        textRect.center = (790, 25)
        self.screen.blit(self.text, textRect)

    def run(self):
        self.draw()
        self.agent.appear(self.screen)
        pygame.display.update()

        while True:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.agent.move_down()
                        self.all_sprites.update()
                        self.draw()
                        self.all_sprites.draw(self.screen)
                        pygame.display.update()
                    elif event.key == pygame.K_UP:
                        self.agent.move_up()
                        self.all_sprites.update()
                        self.draw()
                        self.all_sprites.draw(self.screen)
                        pygame.display.update()
                    elif event.key == pygame.K_LEFT:
                        self.agent.move_left()
                        self.all_sprites.update()
                        self.draw()
                        self.all_sprites.draw(self.screen)
                        pygame.display.update()
                    elif event.key == pygame.K_RIGHT:
                        self.agent.move_right()
                        self.all_sprites.update()
                        self.draw()
                        self.all_sprites.draw(self.screen)
                        pygame.display.update()
