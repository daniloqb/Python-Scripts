#!/usr/bin/python
import pygame
import random

(width,height)  = (640,480)
background_colour = (255,255,255)

class Particle:
    def __init__(self,(x,y),size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0,0,255)
        self.thickness = 1
    
    def display(self):
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.size,self.thickness)   

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tutorial 2')
screen.fill(background_colour)

number_of_particles = 10
my_particles = []
eixo_x = []
eixo_y = []

for n in range(number_of_particles):
    size = random.randint(10,20)
    print 'Particula: ',n
    print 'Size: ',size
    x = random.randint(size,width-size)
    print 'X: ',x
    while x in eixo_x: 
        x = random.randint(size,width-size)
        print 'X: ',x
    y = random.randint(size,height-size)
    print 'Y: ',y
    while y in eixo_y:
        
        y = random.randint(size,height-size)
        print 'Y: ',y
    
    my_particles.append(Particle((x,y),size))
    
    for num in range(x-size,x+size):
        eixo_x.append(num)
    print eixo_x
    for num in range(y-size,y+size):
        eixo_y.append(num)
    print eixo_y

for particle in my_particles:
    particle.display()

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

