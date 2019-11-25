import pygame
import math

pygame.init()
blade_list = []
size = [width, height] = [201, 201]
speed = 0
running = True
f_motion = False
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    for i in range(3):
        pass
    pygame.draw.circle(screen, (255, 255, 255), (width // 2, height // 2), 10)
    pygame.display.flip()
    clock.tick(60)