import pygame
import os
import sys
from pathlib import Path

import colors
from map import world_map
from characters.Cat.cat import Cat
from characters.Bunny.bunny import Bunny
from map.tile import Tile

class SophieGame():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        # 20 wide and 15 tall (32x32 squares)
        self.window_width = 640
        self.window_height = 480
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("hello...")
        self.window_edge = self.window.get_rect()
        self.start_x = 304
        self.start_y = 224
        self.cat = Cat(self.start_x, self.start_y)
        self.bunny = Bunny(100,100)

        self.sprites = [self.cat, self.bunny]
        self.map = world_map.Map("map_a", self.window_width, self.window_height)
        self.add_array()

    def add_array(self):
        for i in range(len(self.map.window_tiles)):
            for j in range(len(self.map.window_tiles[i])):
                self.sprites.append(self.map.window_tiles[i][j])


    def check_window_bounds(self, sprite):
        sprite.rect.clamp_ip(self.window_edge)

    def detect_collision(self, dx, dy):
        # If you collide move out based on velocity
        for sprite in self.sprites:
            if sprite is not self.cat:
                if self.cat.rect.colliderect(sprite.rect):
                    if sprite.solid == True:
                        if dx > 0: # Moving right; Hit the left side of the wall
                            self.cat.rect.right = sprite.rect.left
                        if dx < 0: # Moving left; Hit the right side of the wall
                            self.cat.rect.left = sprite.rect.right
                        if dy > 0: # Moving down; Hit the top side of the wall
                            self.cat.rect.bottom = sprite.rect.top
                        if dy < 0: # Moving up; Hit the bottom side of the wall
                            self.cat.rect.top = sprite.rect.bottom
                    sprite.collision_action()
                else:
                    sprite.no_collision()


    def redraw_game_window(self):
        self.window.fill(colors.BLACK)
        self.map.draw_map(self.window, (self.cat.rect.x - self.start_x), (self.cat.rect.y - self.start_y))
        for sprite in self.sprites:
            if isinstance(sprite, Tile) == False:
                sprite.redraw(self.window)
        pygame.display.update()

    def move_cat(self):
        # Move each axis separately. Note that this checks for collisions both times.
        dx = self.cat.x
        dy = self.cat.y
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        # Move the rect
        self.cat.rect.x += dx
        self.cat.rect.y += dy

        self.detect_collision(dx, dy)

    def main_loop(self):
        running = True

        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed() 
            if keys[pygame.K_w]: 
                self.cat.go_up()
            if keys[pygame.K_a]:
                self.cat.go_left()
            if keys[pygame.K_s]: 
                self.cat.go_down()
            if keys[pygame.K_d]: 
                self.cat.go_right()

            self.move_cat()

            for sprite in self.sprites:
                self.check_window_bounds(sprite)

            self.redraw_game_window()

        pygame.quit()
        
if __name__ == "__main__":
    game = SophieGame()
    game.main_loop()