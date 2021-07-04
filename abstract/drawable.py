from pygame.sprite import Sprite


class Drawable(Sprite):
    def __init__(self, x: int, y: int, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
