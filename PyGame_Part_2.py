import pygame

pygame.init()
width, height = 1280, 720
speed = 3  # Скорость шариков
size = (width, height)
running = True
screen = pygame.display.set_mode(size)
c_l = []  # Список с кругами (circle_list)
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos_x, pos_y = pygame.mouse.get_pos()
                c_l.append([[-speed, -speed], [pos_x, pos_y]])
    for c in range(len(c_l)):
        x, y = c_l[c][1]
        motion_x, motion_y = c_l[c][0]
        if x + motion_x > width - 10 or x + motion_x < 0 + 10:
            motion_x *= -1
        if y + motion_y > height - 10 or y + motion_y < 0 + 10:
            motion_y *= -1
        x += motion_x
        y += motion_y
        c_l[c][1] = [x, y]
        c_l[c][0] = [motion_x, motion_y]

    for c in range(len(c_l)):
        pygame.draw.circle(screen, (255, 255, 255), (c_l[c][1]), 10)
    pygame.display.flip()
    clock.tick(60)