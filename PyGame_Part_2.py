import pygame

pygame.init()
rect_list = []
size = [width, height] = [600, 600]
running = True
f_motion = False
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    for elem in rect_list:
        pygame.draw.rect(screen, (255, 255, 255), elem, 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                f_motion = True
                mouse = pygame.mouse.get_pos()
                rect_list.append([mouse[0], mouse[1], 0, 0])
        if event.type == pygame.MOUSEMOTION and f_motion:
            if pygame.mouse.get_pressed()[0] == 1:
                mouse = pygame.mouse.get_pos()
                rect = rect_list[-1]
                x, y = mouse[0] - rect[0], mouse[1] - rect[1]
                rect_list[-1] = [rect[0], rect[1], x, y]
            else:
                f_motion = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    if len(rect_list) > 0:
                        rect_list = rect_list[:-1]
    pygame.display.flip()
    clock.tick(60)