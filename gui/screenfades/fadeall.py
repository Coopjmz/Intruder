from pygame import draw
from constants import *
from gui.screenfades.screenfade import ScreenFade


class FadeAll(ScreenFade):
    def __init__(self, speed: int, color: tuple[int, int, int]):
        super().__init__(speed, color)
        self.max_fade_counter = SCREEN_WIDTH // 2

    def fade(self, screen) -> bool:
        is_fading = super().fade(screen)

        if is_fading:
            draw.rect(screen, self.color,
                      (0, 0, SCREEN_WIDTH // 2 - self.fade_counter, SCREEN_HEIGHT))
            draw.rect(screen, self.color,
                      (SCREEN_WIDTH // 2 + self.fade_counter, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT))
            draw.rect(screen, self.color,
                      (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT // 2 - self.fade_counter))
            draw.rect(screen, self.color,
                      (0, SCREEN_HEIGHT // 2 + self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT // 2))

        return is_fading
