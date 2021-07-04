import pygame
from loaders.imageloader import images
from abstract.drawable import Drawable


class Button(Drawable):
    def __init__(self, x: int, y: int, button_type: str):
        super().__init__(x, y, images[button_type])
        self.rect.topleft = (x, y)

        self.pressed = False

    def is_clicked(self) -> bool:
        pos = pygame.mouse.get_pos()

        if not self.pressed:
            # Left click (press)
            self.pressed = self.rect.collidepoint(pos) and pygame.mouse.get_pressed(3)[0] == 1
        else:
            # Left click (release)
            if pygame.mouse.get_pressed(3)[0] == 0:
                self.pressed = False
                return self.rect.collidepoint(pos)

        return False
