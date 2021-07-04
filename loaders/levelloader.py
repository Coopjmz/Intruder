from csv import reader
from map.world import World

LEVEL_PATH = 'levels'


def load_level_from_file(level: int):
    level_data = []

    with open(f'{LEVEL_PATH}\\level_{level}.dat', newline='') as file:
        for i, row in enumerate(reader(file, delimiter=',')):
            level_data.append([])
            for tile_index in row:
                level_data[i].append(int(tile_index))

    world = World()
    return world, *world.process_data(level_data)
