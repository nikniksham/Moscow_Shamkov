import pygame

pygame.init()
coords = []
zoom = 10
center = [300, 300]
point_list = []
for elem in input().split(', '):
    a, b = elem.split(';')[0][1:], elem.split(';')[1][:-1]
    if ',' in a:
        a = a[:a.find(',')]
    if ',' in b:
        b = b[:b.find(',')]
    point_list.append([round(float(a)), round(float(b)) * -1])
    coords.append([round(float(a)), round(float(b)) * -1])
size = [width, height] = [600, 600]
running = True
f_zoom = True
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    if f_zoom:
        f_zoom = False
        for i in range(len(coords)):
            elem = coords[i]
            elem = [elem[0] * zoom + center[0], elem[1] * zoom + center[1]]
            point_list[i] = elem
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                zoom += 1
                f_zoom = True
            if event.button == 5:
                if zoom > 1:
                    zoom -= 1
                f_zoom = True
    pygame.draw.polygon(screen, (255, 255, 255), point_list, 1)
    pygame.display.flip()
    clock.tick(60)