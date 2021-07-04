from constants import GRAVITY
from abstract.gameobject import GameObject


class GravityObject(GameObject):
    def __init__(self, x: int, y: int, image):
        super().__init__(x, y, image)

        self.vel_y = 0
        self.is_airborne = True

    def update(self, scroll: int):
        super().update(scroll)

        if not self.is_airborne:
            return

        if self.vel_y > -10:
            self.vel_y -= GRAVITY
        else:
            self.vel_y = -10
