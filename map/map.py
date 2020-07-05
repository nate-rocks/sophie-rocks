import csv
import pygame
import os
import sys
from pathlib import Path


class Map():
    def __init__(self):
        self.square_height = 32
        self.square_width = 32

        current_directory = Path(os.path.realpath(__file__)).parent
        self.map_dir = "{}\\{}".format(current_directory, "maps")

    def load_map(self, map_string):
        map_file = self.map_dir + "\\{}.map".format(map_string)
        with open(map_file) as csv_map_data:
            csv_map = csv.reader(csv_map_data)
            for row in csv_map:
                for square in row:
                    square = square.strip()
                    if square == "W":
                        print( "WALL")
                    elif square == "G":
                        print("GRASS")

