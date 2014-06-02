"""
Class derived from Mekires pygame samples repository:
https://github.com/Mekire/meks-pygame-samples/blob/master/eight_dir_move.py
Overall game flow follows his examples
"""
import os
import pygame as pg


class control(object):
    def __init__(self):
        global SCREEN_SIZE
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pg.init()
        pg.display.set_caption("Move me with the arrow Keys.")
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.clock()
        self.fps = 60.0
        self.done = False
        self.keys = pg.key.get_pressed()
        self.player = Player((0, 0, 100, 100), 5)
        self.player.rect.center = self.screen_rect.center

    def event_loop(self):
        for event in pg.event.get():
            self.keys = pg.key.get_pressed()
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]
                self.done = True

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.player.update(self.screen_rect, self.keys)
