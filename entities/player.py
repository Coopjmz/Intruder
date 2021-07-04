from constants import *
from groups import projectile_group
from loaders.musicloader import sfx
from entities.entity import Entity
from projectiles.grenade import Grenade


class Player(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 'player', PLAYER_MAX_HEALTH, PLAYER_SPEED, PLAYER_SHOOT_DELAY)
        self.ammo = START_AMMO
        self.grenades = START_GRENADES

    def collision_update(self, obstacle_list: list):
        if self.rect.left + self.vel_x < 0 or self.rect.right + self.vel_x > SCREEN_WIDTH:
            self.vel_x = 0

        if self.rect.top > SCREEN_HEIGHT:
            self.die()

        super().collision_update(obstacle_list)

    def on_collision(self):
        self.vel_x = 0

    def move(self, direction: int):
        if super().move(direction) and direction != 0:
            self.direction = direction

    def jump(self):
        if self.is_alive and not self.is_airborne:
            self.vel_y = PLAYER_JUMP_VELOCITY
            sfx['jump'].play()

    def shoot(self):
        if self.ammo > 0 and super().shoot():
            self.ammo -= 1

    def throw_grenade(self):
        if self.is_alive and self.grenades > 0:
            projectile_group.add(Grenade(self.rect.centerx + self.rect.size[0] * 0.7 * self.direction,
                                         self.rect.y, self.direction, self.vel_x))
            self.grenades -= 1

    def gain_health(self, health: int) -> bool:
        if not self.is_alive or self.health == PLAYER_MAX_HEALTH:
            return False

        self.health += health
        if self.health > PLAYER_MAX_HEALTH:
            self.health = PLAYER_MAX_HEALTH

        return True

    def gain_ammo(self, ammo: int) -> bool:
        if not self.is_alive or self.ammo == MAX_AMMO:
            return False

        self.ammo += ammo
        if self.ammo > MAX_AMMO:
            self.ammo = MAX_AMMO

        return True

    def gain_grenades(self, grenades: int) -> bool:
        if not self.is_alive or self.grenades == MAX_GRENADES:
            return False

        self.grenades += grenades
        if self.grenades > MAX_GRENADES:
            self.grenades = MAX_GRENADES

        return True
