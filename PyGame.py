import pygame


pygame.init()
width, height = int(input('Введите ширину поля: ')), int(input('Введите высоту поля: '))  # Размеры поля
Pass = 2  # Пропуски между кирпичами
brick_size = [30, 15]  # Размеры кирпичей
brick_color = (255, 0, 0)  # Цвет кирпичей
#                                ВСЕ ЗНАЧЕНИЯ МОЖНО МЕНЯТЬ НА СВОЁ УСМОТРЕНИЕ!!!
#                                Лично я советую: Pass = 4; brick_size = [45, 20]
size = width, height
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
y = 0
for i in range(height // brick_size[1]):
    x = 0
    if i % 2 != 0:
        x -= brick_size[0] // 2
    for j in range(width // brick_size[0] + 1):
        pygame.draw.rect(screen, brick_color, (j * brick_size[0] + x, i * brick_size[1] + y, brick_size[0],
                                               brick_size[1]))
        x += Pass
    y += Pass
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()