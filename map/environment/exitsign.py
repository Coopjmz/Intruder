from pygame.sprite import collide_rect
from constants import EXIT_SIGN_TILE
from map.tile import Tile


class ExitSign(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, EXIT_SIGN_TILE)

    def is_reached(self, player):
        return collide_rect(self, player) and player.is_alive
