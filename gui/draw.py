from constants import *
from loaders.imageloader import images


def draw_text(surface, font, text: str, x: int, y: int, color: tuple[int, int, int] = WHITE):
    surface.blit(font.render(text, True, color), (x, y))


def draw_background(surface, total_scroll: int):
    for i in range(BACKGROUND_REPEAT):
        surface.blit(images['sky'], (images['sky'].get_width() * i - total_scroll * SKY_SCROLL, 0))
        surface.blit(images['mountains'], (images['mountains'].get_width() * i - total_scroll * MOUNTAINS_SCROLL,
                                           SCREEN_HEIGHT - images['mountains'].get_height() - MOUNTAINS_OFFSET))
        surface.blit(images['forest_1'], (images['forest_1'].get_width() * i - total_scroll * FOREST_1_SCROLL,
                                          SCREEN_HEIGHT - images['forest_1'].get_height() - FOREST_1_OFFSET))
        surface.blit(images['forest_2'], (images['forest_2'].get_width() * i - total_scroll * FOREST_2_SCROLL,
                                          SCREEN_HEIGHT - images['forest_2'].get_height() - FOREST_2_OFFSET))
