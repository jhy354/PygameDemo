import pygame

from settings import *
from utils import Debug
from player import Player
from sprites import Generic
from support import import_folder


class Scene:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()

        self.ground = None
        self.player = None

        self.setup()

        Debug(DEBUG_MODE) << "Inited Scene" << "\n"

    def setup(self):
        self.ground = Generic(
            pos=(0, 0),
            surf=import_folder(PATH_WORLD)[0],
            group=self.all_sprites,
            z=LAYERS["ground"]
        )
        self.player = Player(SCR_CENTER, self.all_sprites)

    def run(self, dt):
        self.display_surface.fill("black")
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCR_CENTER[0]
        self.offset.y = player.rect.centery - SCR_CENTER[1]

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
