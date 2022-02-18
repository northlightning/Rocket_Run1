import pygame as pg

WIN_WIDTH = 400
WIN_HEIGHT = 600
WIN_SIZE = (WIN_WIDTH, WIN_HEIGHT)

PROJECT_NAME = "Rocket Run"

FPS = 60

# Colors

SPACE_COLOR = (80, 23, 153)

# Images

pg.init()
setting_screen = pg.display.set_mode(WIN_SIZE)

STAR_IMGS = [pg.image.load("star.png").convert_alpha(), pg.image.load("starSmall.png").convert_alpha(),
             pg.image.load("meteor.png").convert_alpha(), pg.image.load("meteorSmall.png").convert_alpha()]
