import pygame


pygame.init()
width, height = int(input()), int(input())
# width, height = 500, 500
size = width, height
screen = pygame.display.set_mode(size)
screen.fill((255, 0, 0))
pygame.draw.line(screen, (0, 0, 0), (0, 0), (width, 0))
pygame.draw.line(screen, (0, 0, 0), (width - 1, 1), (width - 1, height - 1))
pygame.draw.line(screen, (0, 0, 0), (width - 1, height - 1), (1, height - 1))
pygame.draw.line(screen, (0, 0, 0), (0, height), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()