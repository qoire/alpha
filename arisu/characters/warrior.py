import pygame as pg
from ..helper import pyganim


class warrior(pg.sprite.Sprite):
    """
    Moves a warrior around the screen
    """
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
