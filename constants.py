# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
TITLE = 'Intruder'
ICON = 'icon\\intruder.ico'

# Framerate
FPS = 60

# Font
FONT_TYPE = 'Futura'
FONT_TITLE_SIZE = 120
FONT_NORMAL_SIZE = 30

# Images
BACKGROUND_SCALE = 1
BUTTON_SCALE = 1
ITEM_BOX_SCALE = 1
PROJECTILE_SCALE = 1
EFFECT_SCALE = 1.25
ENTITY_SCALE = 1.65

# Music and sounds
MASTER_VOLUME = 1
MUSIC_VOLUME = 0.1 * MASTER_VOLUME
JUMP_SFX_VOLUME = 0.25 * MASTER_VOLUME
BULLET_SFX_VOLUME = 0.25 * MASTER_VOLUME
EXPLOSION_SFX_VOLUME = 1 * MASTER_VOLUME
MUSIC_FADE = 5000

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (235, 65, 55)
LIGHT_GREEN = (144, 200, 120)
WHITE = (255, 255, 255)

# Game states
MAIN_MENU_STATE = 1
PLAY_STATE = 2

# Level
FINAL_LEVEL = 2

# Scroll
SCROLL_THRESHOLD = 300

# World
ROWS = 16
COLS = 150
TILE_TYPES = 21
TILE_SIZE = SCREEN_HEIGHT // ROWS
WORLD_LENGTH = COLS * TILE_SIZE

# Tile types
OBSTACLE_TILES = 8
WATER_TILES = 10
DECORATION_TILES = 14
PLAYER_TILE = 15
ENEMY_TILE = 16
AMMO_BOX_TILE = 17
GRENADE_BOX_TILE = 18
HEALTH_BOX_TILE = 19
EXIT_SIGN_TILE = 20

# Fade
FADE_SPEED = 5

# Health bar
HEALTH_BAR_WIDTH = 200
HEALTH_BAR_HEIGHT = 20

# HUD
HUD_X = 20
HUD_Y = 20
HUD_DY = 40
HUD_HEALTH_BAR_Y = HUD_Y + HUD_DY * 0
HUD_AMMO_Y = HUD_Y + HUD_DY * 1
HUD_GRENADES_Y = HUD_Y + HUD_DY * 2
HUD_AMMO_SPACE = 10
HUD_GRENADE_SPACE = 20

# Background
BACKGROUND_REPEAT = 5
SKY_SCROLL = 0.5
MOUNTAINS_SCROLL = 0.6
FOREST_1_SCROLL = 0.7
FOREST_2_SCROLL = 0.8
MOUNTAINS_OFFSET = 300
FOREST_1_OFFSET = 150
FOREST_2_OFFSET = 0

# Environment
GRAVITY = 0.75

# Actions
IDLE = 0
RUN = 1
JUMP = 2
DEATH = 3

# Entity
ENTITY_ANIMATION_TIMER = 100

# Player
PLAYER_MAX_HEALTH = 100
PLAYER_SPEED = 4
PLAYER_SHOOT_DELAY = 10
PLAYER_JUMP_VELOCITY = 12
START_AMMO = 15
MAX_AMMO = 30
START_GRENADES = 3
MAX_GRENADES = 5

# Enemy
ENEMY_MAX_HEALTH = 50
ENEMY_SPEED = 2
ENEMY_SHOOT_DELAY = 20
ENEMY_FOV_X = 220
ENEMY_FOV_Y = 20
IDLE_CHANCE = 200
IDLE_TIMER = 100
PATROL_TIMER = 50

# Bullet
BULLET_SPEED = 20
BULLET_DAMAGE = 10

# Grenade
GRENADE_SPEED_X = 5
GRENADE_SPEED_Y = 10
GRENADE_DAMAGE = 50
GRENADE_TIMER = 100
GRENADE_BLAST_RADIUS = 75

# Explosion
EXPLOSION_ANIMATION_TIMER = 50

# Item Boxes
AMMO_IN_BOX = 15
GRENADES_IN_BOX = 3
HEALTH_IN_BOX = 50
