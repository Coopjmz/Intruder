from constants import *
from groups import *
from loaders.imageloader import tiles
from map.tile import Tile
from map.environment.water import Water
from map.environment.exitsign import ExitSign
from entities.player import Player
from entities.enemy import Enemy
from itemboxes.ammobox import AmmoBox
from itemboxes.grenadebox import GrenadeBox
from itemboxes.healthbox import HealthBox


class World:
    def __init__(self):
        self.tile_list = []
        self.obstacle_list = []
        self.exit_sign = None

    def process_data(self, data: list[list[int]]):
        player = None
        entities = []

        clear_groups()

        for y, row in enumerate(data):
            y *= TILE_SIZE

            for x, tile_index in enumerate(row):
                if tile_index < 0:
                    continue

                x *= TILE_SIZE

                if tile_index <= OBSTACLE_TILES:
                    obstacle = Tile(x, y, tile_index)
                    self.obstacle_list.append(obstacle)
                    self.tile_list.append(obstacle)
                elif tile_index <= WATER_TILES:
                    water = Water(x, y, tile_index)
                    water_group.add(water)
                elif tile_index <= DECORATION_TILES:
                    decoration = Tile(x, y, tile_index)
                    self.tile_list.append(decoration)
                elif tile_index == PLAYER_TILE:
                    player = Player(x, y)
                    entities.append(player)
                elif tile_index == ENEMY_TILE:
                    enemy = Enemy(x, y)
                    entities.append(enemy)
                elif tile_index == AMMO_BOX_TILE:
                    ammo_box = AmmoBox(x, y)
                    item_box_group.add(ammo_box)
                elif tile_index == GRENADE_BOX_TILE:
                    grenade_box = GrenadeBox(x, y)
                    item_box_group.add(grenade_box)
                elif tile_index == HEALTH_BOX_TILE:
                    health_box = HealthBox(x, y)
                    item_box_group.add(health_box)
                elif tile_index == EXIT_SIGN_TILE:
                    self.exit_sign = ExitSign(x, y)
                    self.tile_list.append(self.exit_sign)

        for entity in entities:
            if isinstance(entity, Enemy):
                entity.player = player

        return player, entities

    def update(self, scroll: int):
        for tile in self.tile_list:
            tile.update(scroll)

    def draw(self, surface):
        for tile in self.tile_list:
            tile.draw(surface)
