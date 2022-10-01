import sys

import pygame

from settings import *
from scene import Scene

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCR_SIZE)
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        self.scene = Scene()

    def run(self):
        # main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.scene.run(dt)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
