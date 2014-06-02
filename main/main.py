"""
Program main, everything runs from here
Ideally, nothing should be done here except for instantiation and inclusion
"""
from arisu.control import control
import pygame as pg
import sys

if __name__ == "__main__":
    run_game = control()
    run_game.main_loop()
    pg.quit()
    sys.exit()
