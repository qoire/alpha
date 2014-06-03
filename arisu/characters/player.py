"""
Inherited from:
https://github.com/Mekire/meks-pygame-samples/blob/master/eight_dir_move.py
"""
import pygame as pg
from .. import global_const

#This global constant serves as a very useful convenience for me.
DIRECT_DICT = {pg.K_LEFT : (-1, 0),
               pg.K_RIGHT : ( 1, 0),
               pg.K_UP : ( 0,-1),
               pg.K_DOWN : ( 0, 1)}

class player(object):
    """This class will represent our user controlled character."""
    def __init__(self, rect, speed):
        """The rect arg is (x, y, width, height); speed is in pixels/frame)"""
        self.rect = pg.Rect(rect)
        self.speed = speed
        self.image = self.make_image()

    def make_image(self):
        """Creates our hero (a red circle/ellipse with a black outline)."""
        image = pg.Surface(self.rect.size).convert_alpha()
        image.fill(global_const.TRANSPARENT)
        image_rect = image.get_rect()
        pg.draw.ellipse(image, global_const.BLACK, image_rect)
        pg.draw.ellipse(image, global_const.RED, image_rect.inflate(-12, -12))
        return image

    def update(self, screen_rect, keys):
        """Updates our player appropriately every frame."""
        for key in DIRECT_DICT:
            if keys[key]:
                self.rect.x += DIRECT_DICT[key][0]*self.speed
                self.rect.y += DIRECT_DICT[key][1]*self.speed
        self.rect.clamp_ip(screen_rect) #Keep player on screen.

    def draw(self, surface):
        """Blit image to the target surface."""
        surface.blit(self.image, self.rect)

