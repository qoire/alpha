"""
Some global parameters inherited from:
https://github.com/Mekire/meks-pygame-samples/blob/master/eight_dir_move.py
"""
SCREEN_SIZE = (500, 500)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
TRANSPARENT = (0, 0, 0, 0)

#This global constant serves as a very useful convenience for me.
DIRECT_DICT = {pg.K_LEFT : (-1, 0),
               pg.K_RIGHT : ( 1, 0),
               pg.K_UP : ( 0,-1),
               pg.K_DOWN : ( 0, 1)}