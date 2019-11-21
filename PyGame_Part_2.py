import pygame

pygame.init()
width, height = 300, 300
mouse_pos = [0, 0]
rect_pos = [0, 0]  # Координаты квадрата
size = (width, height)
running = True
f_click = False
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()
            if click[0] == 1 and rect_pos[0] <= mouse[0] <= rect_pos[0] + 100 and \
                    rect_pos[1] <= mouse[1] <= rect_pos[1] + 100 and f_click is False:
                f_click = True
                mouse_pos = [mouse[0] - rect_pos[0], mouse[1] - rect_pos[1]]
            if click[0] == 0 and f_click:
                f_click = False
            if f_click:
                rect_pos[0], rect_pos[1] = mouse[0] - mouse_pos[0], mouse[1] - mouse_pos[1]
    pygame.draw.rect(screen, (0, 255, 0), (rect_pos[0], rect_pos[1], 100, 100))
    pygame.display.flip()
    clock.tick(60)