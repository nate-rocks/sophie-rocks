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
    def __init__(self, map_string, window_x, window_y):
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
        map_file = self.map_dir + "\\{}.map".format(map_string)

        self.csv_map = list(csv.reader(open(map_file)))

    def calculate_tile(self, map_position, character_position, divisor):
        if character_position < 0:
            character_position = 0
        tile_position = (map_position - character_position) / divisor
        return int(tile_position)

    def draw_map(self, window, x, y):
        #  x and y are the beginning of the window at 0,0 as it overlays only the map file
        # a and b track the map file in general as you loop over it to find the window

        a = 0
        b = 0
        for row in self.csv_map:
            for square in row:
                if a < x or b < y:
                    a += 32
                    continue
                if a >= self.window_x:
                    break
                square = square.strip()
                y_tile = self.calculate_tile(b, y, TILE_HEIGHT)
                x_tile = self.calculate_tile(a, x, TILE_WIDTH)
                try:
                    if square == "W":
                        self.window_tiles[y_tile][x_tile].draw(window, "WALL")
                    elif square == "G":
                        self.window_tiles[y_tile][x_tile].draw(window, "GRASS")
                except Exception as error:
                    print(error)
                    raise error
                a += 32
            a = 0
            b += 32
            if b >= self.window_y:
                break


