import pygame

from settings import *


class Generic(pygame.sprite.Sprite):

    def __init__(self, pos, surf, group, z=LAYERS["main"]):
        # 调用超类使实例加入 group
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
