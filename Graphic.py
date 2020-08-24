from Map import *
from Specification import *
import sys
class Graphic:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.caption = pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        self.map = Map()

    def draw(self):
        self.screen.fill(WHITE)
        self.map.draw(self.screen)
        pygame.display.update()
    def run(self):
        self.draw()
        while True:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()