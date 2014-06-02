"""
Class derived from Mekires pygame samples repository:
https://github.com/Mekire/meks-pygame-samples/blob/master/eight_dir_move.py
Overall game flow follows his examples
"""
import os
import pygame as pg

from arisu.characters import player


SCREEN_SIZE = (500, 500)
WHITE = (255, 255, 255)

class control(object):
    """Keep things under control."""
    def __init__(self):
        """Initializing in the init; how novel."""
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pg.init()
        pg.display.set_caption("Move me with the Arrow Keys.")
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False
        self.keys = pg.key.get_pressed()
        self.player = player((0, 0, 100, 100), 5) #Create player instance.
        self.player.rect.center = self.screen_rect.center

    def event_loop(self):
        """One event loop. Never cut your game off from the event loop."""
        for event in pg.event.get():
            self.keys = pg.key.get_pressed()
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done = True

    def main_loop(self):
        """One game loop. Simple and clean."""
        while not self.done:
            self.event_loop()
            self.player.update(self.screen_rect, self.keys)
            self.screen.fill(WHITE)
            self.player.draw(self.screen)
            pg.display.update()
            self.clock.tick(self.fps)
