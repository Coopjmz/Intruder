from pygame.sprite import collide_rect
from constants import BULLET_SPEED, BULLET_DAMAGE
from loaders.imageloader import images
from loaders.musicloader import sfx
from abstract.gameobject import GameObject


class Bullet(GameObject):
    def __init__(self, x: int, y: int, direction: int):
        super().__init__(x, y, images['bullet'])
        self.vel_x = direction * BULLET_SPEED

        sfx['bullet'].play()

    def update(self, scroll: int, entities: list, obstacle_list: list):
        super().update(scroll)
        self.collision_update(entities, obstacle_list)

        self.rect.x += self.vel_x

    def collision_update(self, entities: list, obstacle_list: list):
        for entity in entities:
            if entity.is_alive and collide_rect(self, entity):
                entity.inflict_damage(BULLET_DAMAGE)
                self.kill()

        for tile in obstacle_list:
            if tile.rect.colliderect(self.rect):
                self.kill()
