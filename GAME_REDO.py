import pygame
import os
import sys
from pathlib import Path

import colors
from characters.cat import Cat
from characters.bunny import Bunny


class SophieGame():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.window_width = 600
        self.window_height = 500
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("hello...")
        self.window_edge = self.window.get_rect()
        self.cat = Cat(50, 50)
        self.bunny = Bunny(200,200)
        self.sprites = [self.cat, self.bunny]

    def check_window_bounds(self, sprite):
        sprite.rect.clamp_ip(self.window_edge)

    def detect_collision(self, dx, dy):
        # If you collide move out based on velocity
        for sprite in self.sprites:
            if sprite is not self.cat:
                if self.cat.rect.colliderect(sprite.rect):
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
        for sprite in self.sprites:
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
        #main game loop
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