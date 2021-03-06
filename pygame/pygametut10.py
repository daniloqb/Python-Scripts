#!/usr/bin/python
import pygame
import PyParticles_1

pygame.display.set_caption('Tutorial 10')
(width, height) = (1024, 768)
screen = pygame.display.set_mode((width, height))
env = PyParticles_1.Environment((width, height))

env.addParticles(25)
env.addParticles(x=200, y=250, size=10, speed=4, angle=0)

selected_particle = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_particle = env.findParticle(mouseX, mouseY)
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    if selected_particle:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        selected_particle.mouseMove(mouseX, mouseY)

    env.update()
    screen.fill(env.colour)

    for p in env.particles:
        pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), p.size, p.thickness)

    pygame.display.flip()

