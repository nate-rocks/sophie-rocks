import pygame
import os
from pathlib import Path

pygame.init()
window = pygame.display.set_mode((600, 500))
pygame.display.set_caption("hello...")
clock = pygame.time.Clock()

current_directory = Path(os.path.realpath(__file__)).parent
image_dir = "{}\\{}".format(current_directory, "player1")
print("{}\\{}".format(image_dir,'front_still.png'))
front_cat = pygame.image.load(r"{}\\{}".format(image_dir,'front_still.png'))
back_cat = pygame.image.load(r"{}\\{}".format(image_dir, 'back_still.png'))
left_cat = pygame.image.load(r"{}\\{}".format(image_dir, 'left_still.png'))
right_cat = pygame.image.load(r"{}\\{}".format(image_dir, 'right_still.png'))

black = (0, 0, 0)
white = (255, 255, 255)

x = 50
y = 50
x_change = 0
y_change = 0
width = 32
height = 32
left = False
right = False
up = False
down = False
walkcount = 0

def redrawgamewindow():
    global walkcount
    window.fill(black)
    if walkcount >= 27:
        walkcount = 0
    if left:
        window.blit(left_cat, (x, y))
        walkcount += 1
    elif right:
        window.blit(right_cat, (x, y))
        walkcount += 1
    elif down:
        window.blit(front_cat, (x, y))
        walkcount += 1
    elif up:
        window.blit(back_cat, (x, y))
        walkcount += 1
    else:
        window.blit(front_cat, (x, y))
        walkcount = 0
    pygame.display.update()

#main game loop
running = True
while running:
    clock.tick(300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y_change -= 1.3
                up = True
                right = False
                left = False
                down = False
            elif event.key == pygame.K_s:
                y_change += 1.3
                down = True
                right = False
                left = False
                up = False
            elif event.key == pygame.K_a:
                x_change -= 1.3
                left = True
                right = False
                down = False
                up = False
            elif event.key == pygame.K_d:
                x_change += 1.3
                right = True
                left = False
                up = False
                down = False
            else:
                right = False
                up = False
                down = False
                left = False
                walkcount = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                y_change = 0
            if event.key == pygame.K_s:
                y_change = 0
            if event.key == pygame.K_a:
                x_change = 0
            if event.key == pygame.K_d:
                x_change = 0
    if x < 0:
        x = 0
    elif x > 760:
        x = 760
    elif y < 0:
        y = 0
    elif y > 540:
        y = 540
    x = x + x_change
    y = y + y_change
    redrawgamewindow()

pygame.quit()