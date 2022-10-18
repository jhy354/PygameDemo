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

        Debug(DEBUG_MODE) << "Inited Scene" << "\n"

    def setup(self):
        """
        Setup attributes

        :return: None
        """
        self.player = Player((SCR_SIZE[0]//2, SCR_SIZE[1]//2), self.all_sprites)

    def run(self, dt):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
