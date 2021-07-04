from pygame import Rect
from random import randint
from constants import *
from entities.entity import Entity


class Enemy(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 'enemy', ENEMY_MAX_HEALTH, ENEMY_SPEED, ENEMY_SHOOT_DELAY)
        self.direction = -1
        self.player = None

        self.vision = Rect(0, 0, ENEMY_FOV_X, ENEMY_FOV_Y)

        self.is_idle = False
        self.idle_timer = IDLE_TIMER
        self.patrol_timer = PATROL_TIMER

        self.patrol_direction = self.direction

    def update(self, scroll: int, obstacle_list: list):
        super().update(scroll, obstacle_list)

        if self.is_alive:
            self.ai()

    def on_collision(self):
        self.patrol_direction *= -1

    def ai(self):
        if self.player.is_alive and self.player_is_visible():
            self.shoot_at_player()
        else:
            self.patrol()

    def player_is_visible(self) -> int:
        self.vision.center = (self.rect.centerx + ENEMY_FOV_X * self.direction // 3, self.rect.centery)
        return self.vision.colliderect(self.player.rect)

    def shoot_at_player(self):
        dx = self.player.rect.x - self.rect.x

        if dx != 0:
            self.direction = dx // abs(dx)
            self.flip = self.direction < 0

        self.vel_x = 0
        self.shoot()

    def patrol(self):
        if not self.is_idle:
            if randint(1, IDLE_CHANCE) == 1:
                self.vel_x = 0
                self.is_idle = True
                return

            self.direction = self.patrol_direction
            self.move(self.direction)

            self.patrol_timer -= 1
            if self.patrol_timer == 0:
                self.patrol_direction *= -1
                self.patrol_timer = PATROL_TIMER * 2
        else:
            self.idle_timer -= 1
            if self.idle_timer == 0:
                self.is_idle = False
                self.idle_timer = IDLE_TIMER
