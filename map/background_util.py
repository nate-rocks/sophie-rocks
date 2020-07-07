import os
import pygame
from pathlib import Path


current_directory = Path(os.path.realpath(__file__)).parent
image_dir = "{}\\{}".format(current_directory, "images")

print(os.listdir(image_dir))

GRASS_PIC = pygame.image.load(r"{}\\{}".format(image_dir, 'grass.png'))
WALL_PIC = pygame.image.load(r"{}\\{}".format(image_dir, 'wall.png'))
