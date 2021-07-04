from pygame.sprite import Group

# Initialize sprite groups
item_box_group = Group()
water_group = Group()
projectile_group = Group()
explosion_group = Group()
groups = (item_box_group, water_group, projectile_group, explosion_group)


def update_groups(scroll: int, player, entities: list, obstacle_list: list):
    item_box_group.update(scroll, player)
    water_group.update(scroll, entities)
    projectile_group.update(scroll, entities, obstacle_list)
    explosion_group.update(scroll)


def draw_groups(screen):
    for group in groups:
        group.draw(screen)


def clear_groups():
    for group in groups:
        group.empty()
