from math import sqrt
from constants import *
from groups import explosion_group
from loaders.imageloader import images
from loaders.musicloader import sfx
from abstract.gravityobject import GravityObject
from effects.explosion import Explosion


class Grenade(GravityObject):
    def __init__(self, x: int, y: int, direction: int, initial_velocity: int):
        super().__init__(x, y, images['grenade'])

        self.vel_x = GRENADE_SPEED_X * direction + initial_velocity
        self.vel_y = GRENADE_SPEED_Y

        self.timer = GRENADE_TIMER

    def update(self, scroll: int, entities: list, obstacle_list: list[dict]):
        super().update(scroll)
        self.collision_update(obstacle_list)
        self.timer_update(entities)

        self.rect.x += self.vel_x
        self.rect.y -= self.vel_y

    def collision_update(self, obstacle_list: list[dict]):
        self.is_airborne = True

        for tile in obstacle_list:
            if tile.rect.colliderect(self.rect.x + self.vel_x, self.rect.y,
                                     self.rect.width, self.rect.height):
                self.vel_x *= -1
            elif tile.rect.colliderect(self.rect.x, self.rect.y - self.vel_y + 1,
                                       self.rect.width, self.rect.height):
                if self.vel_y > 0:
                    self.vel_y = 0
                    self.rect.top = tile.rect.bottom
                elif self.vel_y <= 0:
                    self.vel_x = 0
                    self.vel_y = 0
                    self.rect.bottom = tile.rect.top
                    self.is_airborne = False

    def timer_update(self, entities: list):
        if self.timer > 0:
            self.timer -= 1
            return

        self.kill()
        explosion_group.add(Explosion(self.rect.x, self.rect.y))
        self.do_damage(entities)

        sfx['explosion'].play()

    def do_damage(self, entities: list):
        for entity in entities:
            dx = self.rect.centerx - entity.rect.centerx
            dy = self.rect.centery - entity.rect.centery
            distance = sqrt(dx * dx + dy * dy)

            if distance <= GRENADE_BLAST_RADIUS:
                entity.inflict_damage(GRENADE_DAMAGE)
