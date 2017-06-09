#!/usr/bin/python
import random, math
import pygame
import PyParticles13

(width, height) = (1280, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Star formation')

universe = PyParticles13.Environment((width,height))
universe.colour = (0,0,0)
universe.addFunctions(['move','attract','combine'])
universe_screen = PyParticles13.UniverseScreen((width,height))

def calculateRadius(mass):
    return 0.5 * mass ** (0.5)

for p in range(50):
    i_x = random.randint(0,width)
    i_y = random.randint(0,height)
    speed = random.random()*2
    center_x = width*0.5
    center_y = height*0.5
    if i_x >=center_x and i_y >=center_y:        
        angle = math.radians(random.uniform(70,200))
    elif i_x >= center_x and i_y < center_y:
        angle = math.radians(random.uniform(0,110))
    elif i_x < center_x and i_y >=center_y:
        angle = math.radians(random.uniform(160,300))
    elif i_x < center_x and i_y < center_y:
        angle = math.radians(random.uniform(260,360))
        
    particle_mass = random.randint(15,80)
    particle_size = calculateRadius(particle_mass)
    universe.addParticles(x = i_x, y = i_y, speed = speed, angle = angle, mass=particle_mass,size=particle_size,colour=(255,255,255))
	

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
    
    particles_to_remove = []
    for p in universe.particles:
        if 'collide_with' in p.__dict__:
            particles_to_remove.append(p.collide_with)
            p.size = calculateRadius(p.mass)
            del p.__dict__['collide_with']
    
    
        x = int(universe_screen.mx + (universe_screen.dx + p.x) * universe_screen.magnification)
        y = int(universe_screen.my + (universe_screen.dy + p.y) * universe_screen.magnification)
        
        if p.size < 2:
            pygame.draw.rect(screen, p.colour, (x,y, 2, 2))
        else:
            pygame.draw.circle(screen, p.colour, (x,y), int(p.size), 0)
	    
    
    for p in particles_to_remove:
        if p in universe.particles:
            universe.particles.remove(p)
    
    pygame.display.flip()
