import sys

import pygame

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
            print("Key Up")
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            print("Key Down")
            self.direction.y = 1

        if keys[pygame.K_LEFT]:
            print("Key Left")
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            print("Key Right")
            self.direction.x = 1

        if keys[pygame.K_SPACE]:
            print("Key Space")

    def update(self, dt):
        self.respond_input()
