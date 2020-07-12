import csv
import pygame
import os
import sys
from pathlib import Path

from map import background_util
#import world_map

TILE_WIDTH = 32
TILE_HEIGHT = 32

class Tile():
    def __init__(self, x, y):
        self.name = ''
        self.image = None
        self.x = x
        self.y = y
    def draw(self, window, image):
        #print("x={}, y={}".format(self.x, self.y))
        if image == "WALL":
            window.blit(background_util.WALL_PIC, (self.x, self.y))
        elif image == "GRASS":
            window.blit(background_util.GRASS_PIC, (self.x, self.y))