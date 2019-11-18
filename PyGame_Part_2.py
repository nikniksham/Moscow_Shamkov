import pygame

pygame.init()
size = (1000, 1000)
running = True
x_pos, y_pos, r, f_push = 0, 0, 0, False
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = pygame.mouse.get_pos()
            f_push = True
            r = 0
    if f_push:
        r += 1
        pygame.draw.circle(screen, (255, 255, 0), (x_pos, y_pos), r)
    pygame.display.flip()
    clock.tick(150)