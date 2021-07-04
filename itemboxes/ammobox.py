from constants import AMMO_IN_BOX
from itemboxes.itembox import ItemBox


class AmmoBox(ItemBox):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 'ammo_box')

    def pickup_box(self, player) -> bool:
        return player.gain_ammo(AMMO_IN_BOX)
