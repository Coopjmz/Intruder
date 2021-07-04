class ScreenFade:
    def __init__(self, speed: int, color: tuple[int, int, int]):
        self.speed = speed
        self.color = color
        self.fade_counter = 0

    def fade(self, screen) -> bool:
        if self.fade_counter >= self.max_fade_counter:
            return False

        self.fade_counter += self.speed
        return True

    def reset(self):
        self.fade_counter = 0
