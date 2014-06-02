"""
resourceloader.py
loads all necessary images before the game starts to reduce possible
bottlenecks from happening in game
written by: Yao S (qoire)
"""
import pygame as pg
import os

from arisu.global_const import ch_img


def load_characters():
    character_f = os.path.join('data', 'last-guardian-sprites')
    try:
        """
        Wizard character
        contains: front, back, leftside, rightside
        """
        ch_img['amg2_sd1'] = pg.image.load(os.path.join(character_f, 'amg1_fr1')).convert_alpha()

        #Wizard front:
        ch_img['amg2_fr1'] = pg.image.load(os.path.join(character_f, 'amg1_fr1')).convert_alpha()
        ch_img['amg2_fr2'] = pg.image.load(os.path.join(character_f, 'amg1_fr2')).convert_alpha()

        #Wizard left:
        ch_img['amg2_lf1'] = pg.image.load(os.path.join(character_f, 'amg1_lf1')).convert_alpha()
        ch_img['amg2_lf2'] = pg.image.load(os.path.join(character_f, 'amg1_lf2')).convert_alpha()

        #Wizard right:
        ch_img['amg2_rt1'] = pg.image.load(os.path.join(character_f, 'amg1_rt1')).convert_alpha()
        ch_img['amg2_rt2'] = pg.image.load(os.path.join(character_f, 'amg1_rt2')).convert_alpha()

        #Wizard back
        ch_img['amg2_bk1'] = pg.image.load(os.path.join(character_f, 'amg1_bk1')).convert_alpha()
        ch_img['amg2_bk2'] = pg.image.load(os.path.join(character_f, 'amg1_bk2')).convert_alpha()
    except pg.error as e:
        raise e #raise the error as this is a major problem

