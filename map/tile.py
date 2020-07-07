import csv
import pygame
import os
import sys
from pathlib import Path
import background_util
class Tile():
    def __init__(self, x, y):
        self.width = 32
        self.height = 32
        self.name = ''
        self.image = none
        self.x = x
        self.y = y
    def draw(self, window, image):
        if image == "WALL":
            window.blit(background_util.WALL_PIC, (self.x, self.y))
        elif image == "GRASS":
            window.blit(background_util.GRASS_PIC, (self.x, self.y))



