from constants import HEALTH_IN_BOX
from itemboxes.itembox import ItemBox


class HealthBox(ItemBox):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 'health_box')

    def pickup_box(self, player) -> bool:
        return player.gain_health(HEALTH_IN_BOX)
