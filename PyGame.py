import pygame


pygame.init()
vvod = input().split()
thickness, col = int(vvod[0]), int(vvod[1])
# width, height = 500, 500
size = col * thickness * 2, col * thickness * 2
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
RGB = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]
j = 0
for i in range(col):
    pygame.draw.circle(screen, RGB[j], ((col * thickness), (col * thickness)), thickness * (col - i))
    j += 1
    if j == len(RGB):
        j = 0
    pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()