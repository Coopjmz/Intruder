from pygame.time import get_ticks
from constants import EXPLOSION_ANIMATION_TIMER
from loaders.imageloader import animation_lists
from abstract.gameobject import GameObject


class Explosion(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, animation_lists['explosion'][0])

        self.animation_list = animation_lists['explosion']
        self.frame_index = 0
        self.animation_timer = get_ticks()

    def update(self, scroll: int):
        super().update(scroll)
        self.animation_update()

    def animation_update(self):
        if get_ticks() - self.animation_timer < EXPLOSION_ANIMATION_TIMER:
            return

        self.frame_index += 1

        if self.frame_index < len(self.animation_list):
            self.image = self.animation_list[self.frame_index]
            self.animation_timer = get_ticks()
        else:
            self.kill()
