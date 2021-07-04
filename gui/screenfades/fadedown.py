from pygame import draw
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from gui.screenfades.screenfade import ScreenFade


class FadeDown(ScreenFade):
    def __init__(self, speed: int, color: tuple[int, int, int]):
        super().__init__(speed, color)
        self.max_fade_counter = SCREEN_HEIGHT

    def fade(self, screen) -> bool:
        is_fading = super().fade(screen)

        if is_fading:
            draw.rect(screen, self.color, (0, 0, SCREEN_WIDTH, self.fade_counter))
        else:
            draw.rect(screen, self.color, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

        return is_fading
