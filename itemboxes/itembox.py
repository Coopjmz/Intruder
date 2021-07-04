from pygame.sprite import collide_rect
from loaders.imageloader import images
from abstract.gameobject import GameObject


class ItemBox(GameObject):
    def __init__(self, x: int, y: int, box_type: str):
        super().__init__(x, y, images[box_type])
        self.rect.topleft = (x, y)

    def update(self, scroll: int, player):
        super().update(scroll)

        if collide_rect(self, player) and self.pickup_box(player):
            self.kill()

    def pickup_box(self, player) -> bool:
        raise NotImplementedError('Abstract method')
