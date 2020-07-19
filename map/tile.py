import csv
import pygame
import os
import sys
from pathlib import Path

from map import background_util

TILE_WIDTH = 32
TILE_HEIGHT = 32

class Tile():
    def __init__(self, x, y):
        self.name = ''
        self.image = None
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x, self.y), background_util.WALL_PIC.get_rect().size)
        self.solid = False

    def collision_action(self):
        self.message = None

    def no_collision(self):
        self.message = None

    def draw(self, window, image):
        if image == "WALL":
            window.blit(background_util.WALL_PIC, (self.x, self.y))
            self.solid = True
        elif image == "GRASS":
            window.blit(background_util.GRASS_PIC, (self.x, self.y))
            self.solid = False