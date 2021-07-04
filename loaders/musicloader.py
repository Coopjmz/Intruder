from pygame.mixer import music, Sound

AUDIO_PATH = 'res\\audio'
MUSIC_PATH = f'{AUDIO_PATH}\\music'
SFX_PATH = f'{AUDIO_PATH}\\sfx'

sfx = {}


def play_music(music_name: str, volume: float = 1, fade: int = 0):
    music.load(f'{MUSIC_PATH}\\{music_name}.mp3')
    music.set_volume(volume)
    music.play(-1, fade_ms=fade)


def load_sound(key: str, volume: float = 1):
    sfx[key] = Sound(f'{SFX_PATH}\\{key}.wav')
    sfx[key].set_volume(volume)
