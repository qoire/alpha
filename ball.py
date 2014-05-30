# Main character class
# Ball

VERSION = '0.1'

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
except ImportError as e:
    print "couldn't load module %s"% (e)
    sys.exit(1)

def load_png(name):
    fullname = os.path.join('data', name)
    try:
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print 'Cannot load image: %s'%fullname
        raise SystemExit, message
    return image, image.get_rect()

class Ball(pygame.sprite.Sprite):
    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos
        (angle, z) = self.vector

        if not self.area.contains(newpos):
            tl = not self.area.collidepoint(newpos.topleft)
            tr = not self.area.collidepoint(newpos.topright)
            bl = not self.area.collidepoint(newpos.bottomleft)
            br = not self.area.collidepoint(newpos.bottomright)
            if tr and tl or (br and bl):
                angle = -angle
            if tl and bl:
                angle = math.pi - angle
            if tr and br:
                angle = math.pi - angle
        else:
            player1.rect.inflate(-3, -3)
            player2.rect.inflate(-3, -3)

    def calcnewpos(self,rect,vector):
        (angle, z) = vector
        (dx, dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx,dy)