import pygame
from settings import *

class Scene:
    def __init__(self):
        # get display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        print("Init Scene")

    def run(self, dt):
        print("Run Scene")

        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()

