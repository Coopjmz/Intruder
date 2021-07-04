import pygame
from os import listdir

IMG_PATH = 'res\\img'
TILE_PATH = f'{IMG_PATH}\\tiles'
ENTITY_PATH = f'{IMG_PATH}\\entities'

tiles = []
images = {}
animation_lists = {}


def get_tile(path: str, size: int):
    tile = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(tile, (size, size))


def get_image(path: str, scale: float):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))


def get_animation_list(path: str, scale: float):
    animation_list = []

    for file in listdir(path):
        animation_list.append(get_image(f'{path}\\{file}', scale))

    return animation_list


def load_tiles(types: int, size: int):
    for i in range(types):
        tiles.append(get_tile(f'{TILE_PATH}\\tile_{i}.png', size))


def load_image(key: str, directory: str, scale: float = 1):
    images[key] = get_image(f'{IMG_PATH}\\{directory}\\{key}.png', scale)


def load_animation(key: str, scale: float = 1):
    animation_lists[key] = get_animation_list(f'{IMG_PATH}\\{key}', scale)


def load_entity_animation(key: str, scale: float = 1):
    path = f'{ENTITY_PATH}\\{key}'
    animation_lists[key] = []

    for animation_type in ('idle', 'run', 'jump', 'death'):
        animation_lists[key].append(get_animation_list(f'{path}\\{animation_type}', scale))
