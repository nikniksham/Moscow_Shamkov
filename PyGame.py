import pygame


pygame.init()
N = int(input())
# N = 1
width, height = 300, 300
size = width, height
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
pi = 3.14
for i in range(N):
    pygame.draw.ellipse(screen, (255, 255, 255), (0, 150 - ((150 // N) * (i + 1)), 300, (300 // N) * (i + 1)), 1)
    pygame.draw.ellipse(screen, (255, 255, 255), (150 - ((150 // N) * (i + 1)), 0, (300 // N) * (i + 1), 300), 1)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()