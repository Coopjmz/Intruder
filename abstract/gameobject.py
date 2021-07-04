from abstract.drawable import Drawable


class GameObject(Drawable):
    def update(self, scroll: int):
        self.rect.x += scroll
