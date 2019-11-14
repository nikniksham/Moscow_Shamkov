import pygame


pygame.init()
width, height = int(input()), int(input())
size = width, height
screen = pygame.display.set_mode(size)
pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), 5)
pygame.draw.line(screen, (255, 255, 255), (width, 0), (0, height), 5)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()