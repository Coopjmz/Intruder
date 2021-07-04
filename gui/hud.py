from constants import *
from loaders.imageloader import images
from gui.draw import draw_text
from gui.healthbar import HealthBar


class HUD:
    def __init__(self, font):
        self.font = font
        self.player = None
        self.health_bar = HealthBar(HUD_X, HUD_HEALTH_BAR_Y)

    def update(self):
        self.health_bar.update(self.player.health)

    def draw(self, surface):
        self.health_bar.draw(surface)

        text = 'AMMO: '
        draw_text(surface, self.font, text, HUD_X, HUD_AMMO_Y)
        for i in range(self.player.ammo):
            surface.blit(images['bullet'],
                         (self.font.size(text)[0] + 20 + i * HUD_AMMO_SPACE, HUD_AMMO_Y + 5))

        text = 'GRENADES: '
        draw_text(surface, self.font, text, HUD_X, HUD_GRENADES_Y)
        for i in range(self.player.grenades):
            surface.blit(images['grenade'],
                         (self.font.size(text)[0] + 20 + i * HUD_GRENADE_SPACE, HUD_GRENADES_Y + 2.5))

    def refresh(self, player):
        self.player = player
