import pygame

pygame.init()
size = [width, height] = [501, 501]
x, y = width // 2, height // 2
running = True
f_click = False
mouse_pos = [width // 2, height // 2]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
    if x < mouse_pos[0]:
        x += 1
    if x > mouse_pos[0]:
        x -= 1
    if y < mouse_pos[1]:
        y += 1
    if y > mouse_pos[1]:
        y -= 1
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)
    pygame.display.flip()
    clock.tick(60)