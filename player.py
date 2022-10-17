import sys

import pygame

from utils import Debug
from settings import *


class Player(pygame.sprite.Sprite):

    def __init__(self, size: tuple, pos: tuple, group):
        super().__init__(group)

        # * General Setup * #
        self.image = pygame.Surface(size)
        self.image.fill("green")
        self.rect = self.image.get_rect(center=pos)

        # * Movement Attributes * #
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)

        # Speed Attributes
        self.speed_x = 0
        self.speed_y = 0
        self.acceleration = 10
        self.max_speed = 200

        """
        # Physical Attributes
        self.mass = 1
        self.speed = 0
        self.push_force = 30
        self.friction = 20
        self.resultant_force = pygame.math.Vector2()

        # self.push_a = self.push_force / self.mass
        # self.friction_a = self.friction / self.mass
        """

    def respond_input(self):
        # Better than "event.type == KEYDOWN"
        keys = pygame.key.get_pressed()

        # Horizontal Movement
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            if self.speed_x <= self.max_speed:
                self.speed_x += self.acceleration

        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            if self.speed_x <= self.max_speed:
                self.speed_x += self.acceleration

        else:
            if self.speed_x >= 0:
                self.speed_x -= self.acceleration
            else:
                self.direction.x = 0

        # Vertical Movement
        if keys[pygame.K_UP]:
            self.direction.y = -1
            if self.speed_y <= self.max_speed:
                self.speed_y += self.acceleration

        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            if self.speed_y <= self.max_speed:
                self.speed_y += self.acceleration

        else:
            if self.speed_y >= 0:
                self.speed_y -= self.acceleration
            else:
                self.direction.y = 0

        # Other Movement
        if keys[pygame.K_SPACE]:
            pass
        else:
            pass

    def horizontal_move(self, dt):
        # Vector Normalize
        # 获取单位向量, 防止斜走速度为根号2倍
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
            Debug(DEBUG_MODE) << self.direction << "\n"

        self.pos.x += self.direction.x * self.speed_x * dt
        self.rect.centerx = self.pos.x

    def vertical_move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction.normalize()

        self.pos.y += self.direction.y * self.speed_y * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        super().update()

        self.respond_input()
        self.horizontal_move(dt)
        self.vertical_move(dt)
