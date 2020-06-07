import pygame

import colors

class DialogBox():
    def __init__(self, text, sprite):
        self.text = text
        self.x = sprite.rect.x + sprite.width
        self.y = sprite.rect.y

    def redraw(self, window):
        # If game isn't over, draw this stuff.
        font = pygame.font.Font(None, 18)
        text = font.render(self.text, True, colors.WHITE)
        text_rect = text.get_rect()

        window.blit(text, [self.x, self.y])