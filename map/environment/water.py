from pygame.sprite import collide_rect
from map.tile import Tile


class Water(Tile):
    def __init__(self, x: int, y: int, tile_index: int):
        super().__init__(x, y, tile_index)

    def update(self, scroll: int, entities: list):
        super().update(scroll)
        self.collision_update(entities)

    def collision_update(self, entities: list):
        for entity in entities:
            if collide_rect(self, entity) and entity.is_alive:
                entity.die()
