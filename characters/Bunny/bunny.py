import pygame
import os
from pathlib import Path

from characters.dialog_box import DialogBox

class Bunny(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0

        self.step_size = 5
        self.message = None
        self.load_images(init_x, init_y)
        self.stand_still()
        self.solid = True

    def load_images(self, load_x, load_y):
        current_directory = Path(os.path.realpath(__file__)).parent
        image_dir = "{}".format(current_directory)
        self.front_cat = pygame.image.load(r"{}\\{}".format(image_dir,'bunny_front.png'))
        self.back_cat = pygame.image.load(r"{}\\{}".format(image_dir, 'bunny_back.png'))
        self.left_cat = pygame.image.load(r"{}\\{}".format(image_dir, 'bunny_left.png'))
        self.right_cat = pygame.image.load(r"{}\\{}".format(image_dir, 'bunny_right.png'))

        self.rect = pygame.Rect((load_x, load_y), self.front_cat.get_rect().size)
        self.width, self.height = self.front_cat.get_rect().size

    def go_up(self):
        self.up = True
        self.right = False
        self.left = False
        self.down = False
        self.y -= self.step_size

    def go_down(self):
        self.up = False
        self.right = False
        self.left = False
        self.down = True
        self.y += self.step_size

    def go_right(self):
        self.up = False
        self.right = True
        self.left = False
        self.down = False
        self.x += self.step_size

    def go_left(self):
        self.up = False
        self.right = False
        self.left = True
        self.down = False
        self.x -= self.step_size

    def stand_still(self):
        self.up = False
        self.right = False
        self.left = False
        self.down = False

    def redraw(self, window):

        if self.left:
            window.blit(self.left_cat, (self.rect.x, self.rect.y))
        elif self.right:
            window.blit(self.right_cat, (self.rect.x, self.rect.y))
        elif self.down:
            window.blit(self.front_cat, (self.rect.x, self.rect.y))
        elif self.up:
            window.blit(self.back_cat, (self.rect.x, self.rect.y))
        else:
            window.blit(self.front_cat, (self.rect.x, self.rect.y))
        if self.message:
            self.message.redraw(window)
        self.x = 0
        self.y = 0

    def collision_action(self):
        self.message = DialogBox("Ouch!", self)

    def no_collision(self):
        self.message = None