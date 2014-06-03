"""
Program main, everything runs from here
Ideally, nothing should be done here except for instantiation and inclusion
"""
import pygame as pg
import sys
from arisu.control import control


if __name__ == "__main__":
    run_game = control()
    run_game.main_loop()
    pg.quit()
    sys.exit()
