import pygame


pygame.init()
N = int(input('Введите размер ромбиков: '))
width, height = int(input('Введите ширину поля: ')), int(input('Введите высоту поля: '))
size = width, height
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 0))
for i in range(height // N):
    for j in range(width // N):
        pygame.draw.polygon(screen, (255, 125, 40), ((j * N + N // 2, i * N), ((j + 1) * N, i * N + N // 2),
                                                (j * N + N // 2, (i + 1) * N), (j * N, i * N + N // 2)))
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()