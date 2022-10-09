import pygame

from utils import Debug
from settings import *
from player import Player


class Scene:

    def __init__(self):
        # Get display surface
        self.display_surface = pygame.display.get_surface()

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()

        # Instance attribute definition
        self.player = None

        self.setup()

        Debug(DEBUG_MODE) << "Init Scene" << "\n"

    def setup(self):
        """
        Setup attributes

        :return: None
        """
        self.player = Player((36, 64), (640, 360), self.all_sprites)

    def run(self, dt):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
