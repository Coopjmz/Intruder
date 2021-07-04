from loaders.imageloader import tiles
from abstract.gameobject import GameObject


class Tile(GameObject):
    def __init__(self, x: int, y: int, tile_index: int):
        super().__init__(x, y, tiles[tile_index])
        self.rect.topleft = (x, y)
