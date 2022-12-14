import sys

import pygame

from utils import Debug
from settings import *
from scene import Scene
from scene import CameraGroup


class Game:

    def __init__(self):
        # Pygame Init
        pygame.init()
        pygame.display.set_caption(CAPTION)
        self.screen = pygame.display.set_mode(SCR_SIZE)
        self.clock = pygame.time.Clock()

        Debug(DEBUG_MODE).div()

        # Attribute definition
        self.main_scene = Scene()

        Debug(DEBUG_MODE) << "Inited Game" << "\n"
        Debug(DEBUG_MODE).div()

    def run(self):
        # MAIN LOOP
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick(FPS) / 1000
            self.main_scene.run(dt)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
