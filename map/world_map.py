import csv
import pygame
import os
import sys
from pathlib import Path

from map.tile import Tile
from map.tile import TILE_HEIGHT
from map.tile import TILE_WIDTH

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

    def draw_map(self, map_string, window):
        map_file = self.map_dir + "\\{}.map".format(map_string)
        with open(map_file) as csv_map_data:
            csv_map = csv.reader(csv_map_data)
            x = 0
            y = 0
            for row in csv_map:
                for square in row:
                    square = square.strip()
                    if square == "W":
                        self.window_tiles[int(y/TILE_HEIGHT)][int(x/TILE_WIDTH)].draw(window, "WALL")
                    elif square == "G":
                        self.window_tiles[int(y/TILE_HEIGHT)][int(x/TILE_WIDTH)].draw(window, "GRASS")
                    x += 32
                x = 0
                y += 32

