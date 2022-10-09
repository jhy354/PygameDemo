import sys

import pygame

from utils import Debug
from settings import *


class Player(pygame.sprite.Sprite):

    def __init__(self, size: tuple, pos: tuple, group):
        super().__init__(group)
        self.pos = pos

        # general setup
        self.image = pygame.Surface(size)
        self.image.fill("green")
        self.rect = self.image.get_rect(center=pos)

        # movement attributes
        self.direction = pygame.math.Vector2()

    def respond_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            Debug(DEBUG_MODE) << "Key Up" << "\n"
            self.direction.y = -1

        elif keys[pygame.K_DOWN]:
            Debug(DEBUG_MODE) << "Key Down" << "\n"
            self.direction.y = 1

        if keys[pygame.K_LEFT]:
            Debug(DEBUG_MODE) << "Key Left" << "\n"
            self.direction.x = -1

        elif keys[pygame.K_RIGHT]:
            Debug(DEBUG_MODE) << "Key Right" << "\n"
            self.direction.x = 1

        if keys[pygame.K_SPACE]:
            pass
            Debug(DEBUG_MODE) << "Key Space" << "\n"

    def update(self, dt):
        super().update()
        self.respond_input()
