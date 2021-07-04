"""Intruder - 2D Platformer Shooter"""

import pygame
from groups import *
from loaders.imageloader import *
from loaders.levelloader import *
from loaders.musicloader import *
from gui.draw import *
from gui.screenfades.fadeall import FadeAll
from gui.screenfades.fadedown import FadeDown
from gui.button import Button
from gui.hud import HUD


# Input variables
moving_left = False
moving_right = False
jumping = False
shooting = False
throwing_grenade = False
direction = 0

# Game state
game_state = MAIN_MENU_STATE

# Initialize screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

# Initialize sound mixer
pygame.mixer.init()

# Initialize clock
clock = pygame.time.Clock()

# Load fonts
title_font = pygame.font.SysFont(FONT_TYPE, FONT_TITLE_SIZE)
normal_font = pygame.font.SysFont(FONT_TYPE, FONT_NORMAL_SIZE)

# Load images
load_tiles(TILE_TYPES, TILE_SIZE)

load_image('start', 'buttons', BUTTON_SCALE)
load_image('restart', 'buttons', BUTTON_SCALE * 2.5)
load_image('exit', 'buttons', BUTTON_SCALE)

for image_name in ('sky', 'mountains', 'forest_1', 'forest_2'):
    load_image(image_name, 'background', BACKGROUND_SCALE)

for image_name in ('bullet', 'grenade'):
    load_image(image_name, 'projectiles', PROJECTILE_SCALE)

for image_name in ('health_box', 'ammo_box', 'grenade_box'):
    load_image(image_name, 'item_boxes', ITEM_BOX_SCALE)

load_animation('explosion', EFFECT_SCALE)
load_entity_animation('player', ENTITY_SCALE)
load_entity_animation('enemy', ENTITY_SCALE)

# Load music and sounds
play_music('main_menu', MUSIC_VOLUME, MUSIC_FADE)

load_sound('jump', JUMP_SFX_VOLUME)
load_sound('bullet', BULLET_SFX_VOLUME)
load_sound('explosion', EXPLOSION_SFX_VOLUME)

# Initialize screen fades
intro_screen = FadeAll(FADE_SPEED, BLACK)
win_game_screen = FadeDown(FADE_SPEED, LIGHT_GREEN)
game_over_screen = FadeDown(FADE_SPEED, PINK)
fades = (intro_screen, win_game_screen, game_over_screen)

# Initialize buttons
start_button = Button((SCREEN_WIDTH - images['start'].get_width()) // 2, SCREEN_HEIGHT // 2 - 50, 'start')
restart_button = Button((SCREEN_WIDTH - images['restart'].get_width()) // 2, SCREEN_HEIGHT // 2 - 50, 'restart')
exit_button = Button((SCREEN_WIDTH - images['exit'].get_width()) // 2, SCREEN_HEIGHT // 2 + 100, 'exit')
main_menu_state_buttons = (start_button, exit_button)
play_state_buttons = (restart_button, exit_button)

# Initilaize HUD
hud = HUD(normal_font)


# Scroll
def calculate_scroll():
    global scroll, total_scroll

    if (direction == 1 and player.rect.right > SCREEN_WIDTH - SCROLL_THRESHOLD and
        total_scroll < WORLD_LENGTH - SCREEN_WIDTH) or \
            (direction == -1 and player.rect.left < SCROLL_THRESHOLD and total_scroll > 0):
        scroll = -player.vel_x
    else:
        scroll = 0

    total_scroll -= scroll


# Level
def load_level(level: int):
    global current_level, world, player, entities, scroll, total_scroll

    if level > FINAL_LEVEL:
        win_game()
        return

    current_level = level
    world, player, entities = load_level_from_file(level)
    scroll = total_scroll = 0

    hud.refresh(player)
    play_music(f'level_{level}', MUSIC_VOLUME, MUSIC_FADE)

    for fade in fades:
        fade.reset()


def load_first_level():
    load_level(1)


def load_next_level():
    load_level(current_level + 1)


def reset_level():
    load_level(current_level)


# End screens
def win_game():
    global running

    if win_game_screen.fade(screen):
        return

    text = 'YOU WIN'
    draw_text(screen, title_font, text, (SCREEN_WIDTH - title_font.size(text)[0]) // 2, 100)

    if restart_button.is_clicked():
        load_first_level()

    if exit_button.is_clicked():
        running = False

    for button in play_state_buttons:
        button.draw(screen)


def game_over():
    global running

    if game_over_screen.fade(screen):
        return

    text = 'GAME OVER'
    draw_text(screen, title_font, text, (SCREEN_WIDTH - title_font.size(text)[0]) // 2, 100)

    if restart_button.is_clicked():
        reset_level()

    if exit_button.is_clicked():
        running = False

    for button in play_state_buttons:
        button.draw(screen)


# Game states
def main_menu_state():
    global game_state, running

    screen.fill(LIGHT_GREEN)

    text = TITLE.upper()
    draw_text(screen, title_font, text, (SCREEN_WIDTH - title_font.size(text)[0]) // 2, 100, RED)

    if start_button.is_clicked():
        load_first_level()
        game_state = PLAY_STATE

    if exit_button.is_clicked():
        running = False

    for button in main_menu_state_buttons:
        button.draw(screen)


def play_state():
    global jumping, throwing_grenade

    # Scroll
    calculate_scroll()

    # Background
    draw_background(screen, total_scroll)

    # HUD
    hud.update()
    hud.draw(screen)

    # World
    world.update(scroll)
    world.draw(screen)

    # Entities
    for entity in entities:
        entity.update(scroll, world.obstacle_list)
        entity.draw(screen)

    # Sprite groups
    update_groups(scroll, player, entities, world.obstacle_list)
    draw_groups(screen)

    # Intro fade
    if intro_screen.fade(screen):
        return

    # Level management
    if world.exit_sign.is_reached(player):
        player.move(0)
        load_next_level()
        return

    # Player behaviour
    if player.is_alive:
        player.move(direction)

        if jumping:
            player.jump()
            jumping = False

        if shooting:
            player.shoot()

        if throwing_grenade:
            player.throw_grenade()
            throwing_grenade = False
    else:
        game_over()


# Game loop
running = True
while running:
    clock.tick(FPS)

    if game_state == MAIN_MENU_STATE:
        main_menu_state()
    elif game_state == PLAY_STATE:
        play_state()

    pygame.display.update()

    # Event handling
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            running = False
        # Input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_a:
                moving_left = True
                direction = -1
            elif event.key == pygame.K_d:
                moving_right = True
                direction = 1
            elif event.key == pygame.K_w:
                jumping = True
            elif event.key == pygame.K_SPACE:
                shooting = True
            elif event.key == pygame.K_q:
                throwing_grenade = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
                direction = (0, 1)[moving_right]
            elif event.key == pygame.K_d:
                moving_right = False
                direction = (0, -1)[moving_left]
            elif event.key == pygame.K_SPACE:
                shooting = False
