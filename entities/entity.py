import pygame
from constants import *
from groups import projectile_group
from loaders.imageloader import animation_lists
from abstract.gravityobject import GravityObject
from projectiles.bullet import Bullet


class Entity(GravityObject):
    def __init__(self, x: int, y: int, char_type: str, health: int, speed: int, shoot_delay: int):
        super().__init__(x, y, animation_lists[char_type][0][0])

        self.health = health
        self.speed = speed
        self.shoot_delay = shoot_delay

        self.vel_x = 0
        self.direction = 1
        self.flip = False

        self.is_alive = True

        self.animation_list = animation_lists[char_type]
        self.action = 0
        self.frame_index = 0
        self.animation_timer = pygame.time.get_ticks()

        self.shoot_timer = 0

    def update(self, scroll: int, obstacle_list: list):
        super().update(scroll)

        self.collision_update(obstacle_list)
        self.action_update()
        self.animation_update()
        self.shoot_timer_update()

        self.rect.x += self.vel_x
        self.rect.y -= self.vel_y

    def collision_update(self, obstacle_list: list):
        self.is_airborne = True

        for tile in obstacle_list:
            if tile.rect.colliderect(self.rect.x, self.rect.y - self.vel_y + 1,
                                     self.rect.width, self.rect.height):
                if self.vel_y > 0:
                    self.vel_y = 0
                    self.rect.top = tile.rect.bottom
                elif self.vel_y <= 0:
                    self.vel_y = 0
                    self.rect.bottom = tile.rect.top
                    self.is_airborne = False

            elif tile.rect.colliderect(self.rect.x + self.vel_x, self.rect.y,
                                       self.rect.width, self.rect.height):
                self.on_collision()

    def on_collision(self):
        raise NotImplementedError('Abstract method')

    def action_update(self):
        new_action = IDLE

        if not self.is_alive:
            new_action = DEATH
        elif self.is_airborne:
            new_action = JUMP
        elif self.vel_x != 0:
            new_action = RUN

        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.animation_timer = pygame.time.get_ticks()

    def animation_update(self):
        if pygame.time.get_ticks() - self.animation_timer < ENTITY_ANIMATION_TIMER:
            return

        self.frame_index += 1
        max_frame_index = len(self.animation_list[self.action]) - 1

        if self.frame_index > max_frame_index:
            if self.action != DEATH:
                self.frame_index = 0
            else:
                self.frame_index = max_frame_index

        self.animation_timer = pygame.time.get_ticks()
        self.image = self.animation_list[self.action][self.frame_index]

    def shoot_timer_update(self):
        if self.shoot_timer > 0:
            self.shoot_timer -= 1

    def draw(self, surface):
        surface.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def move(self, direction: int) -> bool:
        if not self.is_alive:
            return False

        if direction != 0:
            self.flip = direction < 0

        self.vel_x = self.speed * direction
        return True

    def shoot(self) -> bool:
        if not self.is_alive or self.shoot_timer > 0:
            return False

        projectile_group.add(Bullet(self.rect.centerx + self.rect.size[0] * 0.7 * self.direction,
                                    self.rect.centery, self.direction))
        self.shoot_timer = self.shoot_delay
        return True

    def inflict_damage(self, damage: int):
        if not self.is_alive:
            return

        self.health -= damage

        if self.health <= 0:
            self.die()

    def die(self):
        self.is_alive = False
        self.health = 0
        self.vel_x = 0
