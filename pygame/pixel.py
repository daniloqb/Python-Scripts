#! /usr/bin/env python
 
# Plot random pixels on the screen.
 
import pygame
import random
 
# Window dimensions
width = 640
height = 400
background_colour = (255, 255, 255)

center_x = width / 2
center_y = height / 2

screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)

clock = pygame.time.Clock()
running = True

x = -100;
y = 0;

color = (255,0,0)
#eixo X
start_pos = (0+10,height/2)
end_pos = (width-10,height/2)
pygame.draw.line(screen, color, start_pos, end_pos, 4)
#eixo y
start_pos = (center_x,height-10)
end_pos = (width/2,0+10)
pygame.draw.line(screen, color, start_pos, end_pos, 4)

for i in range(width):
    start_pos = ((10*i)+10,center_y+3)
    end_pos = ((10*i)+10,center_y-3)
    pygame.draw.line(screen, color, start_pos, end_pos, 1)


for i in range(width):
    start_pos = (center_x+3,(10*i)+10)
    end_pos = (center_x-3,(10*i)+10)
    pygame.draw.line(screen, color, start_pos, end_pos, 1)


while running:
    y = -(x**2);
    red = 0
    green = 0
    blue = 255
    screen.set_at((center_x + x, center_y + y), (red, green, blue))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(240)
    x += 1;
