from Map import *
from Specification import *
import sys
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
        self.font = pygame.font.Font('mrsmonster.ttf', 30)
        self.text = self.font.render('Your score:', True, BLACK)
    def draw(self):
        self.screen.fill(WHITE)
        self.map.draw(self.screen)
        textRect = self.text.get_rect()
        textRect.center = (790, 25)
        self.screen.blit(self.text, textRect)
        self.agent.update(self.screen, self.font)
        pygame.display.update()
    def run(self):
        self.draw()
        while True:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()