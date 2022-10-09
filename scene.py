import pygame

from settings import *

from player import Player

class Scene:
    def __init__(self):
        # get display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.setup()

        print("Init Scene")

    def setup(self):
        self.player = Player((36, 64), (640, 360), self.all_sprites)

    def run(self, dt):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
