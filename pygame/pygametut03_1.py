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

number_of_particles = 20
my_particles = []
n = 1
while n <= number_of_particles:
    colision = False
    size = random.randint(1,20)
    x = random.randint(size,width-size)
    y = random.randint(size,height-size)
    if len(my_particles) > 0:
        print 'Particula',n
        for p in my_particles:            
            print 'X:',x+size,p.x-p.size,p.x+p.size
            print 'Y:',y+size,p.y-p.size,p.y+p.size
            if x+size > p.x-p.size:
                if x-size < p.x+p.size:
                    colision = True
                    break
            if y+size > p.y-p.size:
                if y-size < p.y+p.size:
                   colision = True
                   break
    if colision == False:
        my_particles.append(Particle((x,y),size))
        n+=1
n=1
for particle in my_particles:
    print 'Particle: ',n
    print 'X: ', particle.x-particle.size,particle.x+particle.size
    print 'Y: ', particle.y-particle.size,particle.y+particle.size
    n +=1
    particle.display()

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

