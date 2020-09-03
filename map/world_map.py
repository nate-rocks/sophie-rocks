import csv
import pygame
import os
import sys
from pathlib import Path

from map.tile import Tile
from map.tile import TILE_HEIGHT
from map.tile import TILE_WIDTH
from map import background_util
from GAME_REDO import SophieGame

class Map():
    def __init__(self, window_x, window_y):
        self.window_x = window_x
        self.window_y = window_y

        num_width = int(window_x / TILE_WIDTH)
        num_height = int(window_y / TILE_HEIGHT)

        self.window_tiles = []
        for y in range(num_height):
            row = []
            for x in range(num_width):
                row.append(Tile(x*TILE_WIDTH, y*TILE_HEIGHT))
            self.window_tiles.append(row)

        current_directory = Path(os.path.realpath(__file__)).parent
        self.map_dir = "{}\\{}".format(current_directory, "maps")

    '''def draw_map(self, map_string, window, x, y):
            a = 0
            b = 0
            map_file = self.map_dir + "\\{}.map".format(map_string)
            with open(map_file) as csv_map_data:
                csv_map = csv.reader(csv_map_data)
                for row in csv_map:
                    for square in row:
                        if a < x or b < y:
                            a += 32
                            continue
                        if (x + a) >= self.window_x:
                            break

                        print(
                            "x={} : y={}, a={} b={}".format(int(x / TILE_WIDTH), int(y / TILE_HEIGHT),
                                                            int(a / TILE_WIDTH),
                                                            int(b / TILE_HEIGHT)))'''

    def draw_map(self, map_string, window, x, y):
        a = 0
        b = 0
        map_file = self.map_dir + "\\{}.map".format(map_string)
        with open(map_file) as csv_map_data:
            csv_map = csv.reader(csv_map_data)
            for row in csv_map:
                for square in row:
                    if a < x or b < y:
                        a += 32
                        continue
                    if ((x + a) >= self.window_x):
                        break
                    square = square.strip()
                    if square == "W":
                        self.window_tiles[int(b/TILE_HEIGHT)][int(a/TILE_WIDTH)].draw(window, "WALL")
                    elif square == "G":
                        self.window_tiles[int(b/TILE_HEIGHT)][int(a/TILE_WIDTH)].draw(window, "GRASS")
                    a += 32
                a = 0
                b += 32
                if ((y + b) >= self.window_y):
                    breaka



