import pygame
import os
from pathlib import Path

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class DialogBox():
    def __init__(self, text, sprite):
        self.text = text
        self.x = sprite.rect.x + sprite.width
        self.y = sprite.rect.y

    def redraw(self, window):
        # If game isn't over, draw this stuff.
        font = pygame.font.Font(None, 18)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect()

        window.blit(text, [self.x, self.y])


class Cat(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        pygame.sprite.Sprite.__init__(self)
        self.x = init_x
        self.y = init_y
        self.prev_x = 0
        self.prev_y = 0
        self.step_size = 5
        self.message = None
        self.load_images()
        self.stand_still()

    def load_images(self):
        current_directory = Path(os.path.realpath(__file__)).parent
        image_dir = "{}\\{}".format(current_directory, "player1")
        self.front_cat = pygame.image.load(r"{}\\{}".format(image_dir,'front_still.png'))
        self.back_cat = pygame.image.load(r"{}\\{}".format(image_dir, 'back_still.png'))
        self.left_cat = pygame.image.load(r"{}\\{}".format(image_dir, 'left_still.png'))
        self.right_cat = pygame.image.load(r"{}\\{}".format(image_dir, 'right_still.png'))

        self.rect = pygame.Rect((self.x, self.y), self.front_cat.get_rect().size)
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

    def undo_move(self):
        self.x -= self.prev_x 
        self.y -= self.prev_y

    def redraw(self, window):
        self.rect.move_ip(self.x, self.y)
        self.prex_x = self.x
        self.prev_y = self.y
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
        self.cat2 = Cat(100,100)
        self.sprites = [self.cat, self.cat2]

    def check_window_bounds(self, sprite):
        sprite.rect.clamp_ip(self.window_edge)

    def detect_collision(self, sprite):
        if self.cat.rect.colliderect(sprite.rect):
            sprite.collision_action()
            self.cat.undo_move()

    def redraw_game_window(self):
        self.window.fill(BLACK)
        for sprite in self.sprites:
            sprite.redraw(self.window)
        pygame.display.update()

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

            for sprite in self.sprites:
                self.check_window_bounds(sprite)
                if sprite is not self.cat:
                    self.detect_collision(sprite)

            self.redraw_game_window()

        pygame.quit()

if __name__ == "__main__":
    game = SophieGame()
    game.main_loop()