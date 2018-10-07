from PIL import Image, ImageFont
from pkg_resources import resource_filename
import pygame

def getfile(path):
    return resource_filename('magskeeball',path)

pygame.init()

FPS = 20

#these map to the physical pins on the arduino
B_1000L  = 2
B_1000R  = 3
B_500    = 4
B_400    = 5
B_300    = 6
B_200    = 7
B_100    = 8
B_RET    = 9
B_CONFIG = 10
B_START  = 11
B_SELECT = 12

FONTS = {
    'GameOver': ImageFont.truetype(getfile("fonts/GameCube.ttf"), 14),
    'Tiny': ImageFont.load(getfile('fonts/4x6.pil')),
    'Small': ImageFont.load(getfile('fonts/5x7.pil')),
    'Medium': ImageFont.load(getfile('fonts/6x10.pil')),
    'Digital14': ImageFont.load(getfile('fonts/digital-14.pil')),
    'Digital16': ImageFont.load(getfile('fonts/digital-16.pil'))
}

IMAGES = {
    'MainLogo' : Image.open(getfile('imgs/combined-logo.png'))
}

SOUNDS = {
    'OVER9000': pygame.mixer.Sound(getfile("sounds/its_over_9000.ogg")),
    'PLACE1': pygame.mixer.Sound(getfile("sounds/place_1.ogg")),
    'PLACE2': pygame.mixer.Sound(getfile("sounds/place_2.ogg")),
    'PLACE3': pygame.mixer.Sound(getfile("sounds/place_3.ogg")),
    'PLACE4': pygame.mixer.Sound(getfile("sounds/place_4.ogg")),
    'PLACE5': pygame.mixer.Sound(getfile("sounds/place_5.ogg")),
    'SCORE100': pygame.mixer.Sound(getfile("sounds/sonic_ring.ogg")),
    'SCORE200': pygame.mixer.Sound(getfile("sounds/mario_coin.ogg")),
    'SCORE300': pygame.mixer.Sound(getfile("sounds/pac_man_wakka.ogg")),
    'SCORE400': pygame.mixer.Sound(getfile("sounds/mega_man_item_get.ogg")),
    'SCORE500': pygame.mixer.Sound(getfile("sounds/colossus_roar.ogg")),
    'SCORE1000': pygame.mixer.Sound(getfile("sounds/colossus_roar.ogg")),
}

ATTRACT_MUSIC = {
    'BK2000': pygame.mixer.Sound(getfile("sounds/black_knight_2000.ogg")),
    'SKEEBALL': pygame.mixer.Sound(getfile("sounds/skeeball_jingle.ogg")),
    'SF2': pygame.mixer.Sound(getfile("sounds/street_fighter_ii.ogg")),
    'SANIC': pygame.mixer.Sound(getfile("sounds/sonic_title.ogg")),
}

START_MUSIC = {
    'FIRE': pygame.mixer.Sound(getfile("sounds/great_balls_of_fire.ogg")),
    'WRECKING': pygame.mixer.Sound(getfile("sounds/wrecking_ball.ogg")),
    'STEEL': pygame.mixer.Sound(getfile("sounds/balls_of_steel.ogg")),
}

ATTRACT_MUSIC_KEYS = list(ATTRACT_MUSIC.keys())
START_MUSIC_KEYS = list(START_MUSIC.keys())

class COLORS:
    RED = (255,0,0)
    YELLOW = (255,255,0)
    GREEN = (0,255,0)
    BLUE = (50,50,255)
    MAGENTA = (255,0,255)
    PINK = (255,150,150)
    WHITE = (255,255,255)
    CYAN = (0,255,255)
    PURPLE = (100,0,255)
    ORANGE = (255,69,0)

BALL_COLORS = [
    COLORS.RED,
    COLORS.RED,
    COLORS.YELLOW,
    COLORS.YELLOW,
    COLORS.GREEN,
    COLORS.GREEN,
    COLORS.GREEN,
    COLORS.GREEN,
    COLORS.GREEN,
    COLORS.GREEN,
]