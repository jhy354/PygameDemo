import sys

import pygame

from utils import Debug
from settings import *
from scene import Scene


class Game:

    def __init__(self):
        # Pygame Init
        pygame.init()
        pygame.display.set_caption(CAPTION)
        self.screen = pygame.display.set_mode(SCR_SIZE)
        self.clock = pygame.time.Clock()

        # Attribute definition
        self.start_scene = Scene()

        Debug(DEBUG_MODE) << "Inited Game" << "\n"

    def run(self):
        # MAIN LOOP
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick(FPS) / 1000
            self.start_scene.run(dt)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
