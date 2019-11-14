import pygame


pygame.init()
vvod = input().split()
size_window, col = int(vvod[0]), int(vvod[1])
# width, height = 500, 500
size = size_window, size_window
size_ = size_window // col
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
for i in range(col):
    for j in range(col):
        if i % 2 != 0 and j % 2 == 0:
            pygame.draw.rect(screen, (255, 255, 255), (i * size_, j * size_, size_, size_))
        if i % 2 == 0 and j % 2 != 0:
            pygame.draw.rect(screen, (255, 255, 255), (i * size_, j * size_, size_, size_))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()