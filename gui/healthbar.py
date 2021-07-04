from pygame import draw
from constants import *


class HealthBar:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.health = PLAYER_MAX_HEALTH

    def update(self, health):
        self.health = health

    def draw(self, surface):
        draw.rect(surface, BLACK, (self.x - 2, self.y - 2, HEALTH_BAR_WIDTH + 4, HEALTH_BAR_HEIGHT + 4))
        draw.rect(surface, RED, (self.x, self.y, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
        draw.rect(surface, GREEN, (self.x, self.y, HEALTH_BAR_WIDTH * self.health // PLAYER_MAX_HEALTH,
                                   HEALTH_BAR_HEIGHT))
