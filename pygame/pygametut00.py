#!/usr/bin/python
import random, math
import pygame
import PyParticles00

def calculateRadius(mass):
    return 0.5 * mass ** (0.5)

(width, height) = (640, 480)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Star formation')

universe = PyParticles00.Environment((width,height))
universe.colour = (0,0,0)
universe.addFunctions(['move','attract','combine'])
universe_screen = PyParticles00.UniverseScreen((width,height))


for p in range(100):
    particle_mass = random.randint(1,4)
    particle_size = calculateRadius(particle_mass)
    universe.addParticles(mass=particle_mass,size=particle_size,colour=(255,255,255))
	

running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                universe_screen.scroll(dx=1)
            elif event.key == pygame.K_RIGHT:
                universe_screen.scroll(dx=-1)
            elif event.key == pygame.K_UP:
                universe_screen.scroll(dy=1)
            elif event.key == pygame.K_DOWN:
                universe_screen.scroll(dy=-1)
            elif event.key == pygame.K_EQUALS:
                universe_screen.zoom(2)
            elif event.key == pygame.K_MINUS:
                universe_screen.zoom(0.5)
            elif event.key == pygame.K_r:
                universe_screen.reset()
            elif event.key == pygame.K_SPACE:
                paused = (True, False) [paused]

    screen.fill(universe.colour)
    if not paused:
        universe.update()
    
    '''
    particles_to_remove = []
    for p in universe.particles:
        if 'collide_with' in p.__dict__:
            particles_to_remove.append(p.collide_with)
            p.size = calculateRadius(p.mass)
            del p.__dict__['collide_with']
    '''
    for p in universe.particles:
        x = int(universe_screen.mx + (universe_screen.dx + p.x) * universe_screen.magnification)
        y = int(universe_screen.my + (universe_screen.dy + p.y) * universe_screen.magnification)
        
        if p.size < 2:
            pygame.draw.rect(screen, p.colour, (x,y, 2, 2))
        else:
            pygame.draw.circle(screen, p.colour, (x,y), int(p.size), 0)
	    
    '''
    for p in universe.particles:
        if p.combine == True:
            universe.particles.remove(p)
    '''
    pygame.display.flip()
