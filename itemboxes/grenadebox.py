from constants import GRENADES_IN_BOX
from itemboxes.itembox import ItemBox


class GrenadeBox(ItemBox):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 'grenade_box')

    def pickup_box(self, player) -> bool:
        return player.gain_grenades(GRENADES_IN_BOX)
