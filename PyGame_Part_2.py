import pygame

pygame.init()
size = [width, height] = [200, 200]
running = True
number = 0
font = pygame.font.Font(None, 150)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    text = font.render(str(number), 1, (255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == 17:
            number += 1
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.flip()
    clock.tick(60)