import pygame


pygame.init()
input_ = input().split()
W, Hue = int(input_[0]), int(input_[1])
if Hue > 360:
    Hue = 360
if Hue <= 0:
    Hue = 1
color = pygame.Color(100, Hue, 100)
color2 = pygame.Color(75, Hue, 100)
color3 = pygame.Color(50, Hue, 100)
hsv = color.hsva
color.hsva = (hsv[0], hsv[1], hsv[2], hsv[3])
# W = 300
width, height = 300, 300
size = width, height
screen = pygame.display.set_mode(size)
pygame.draw.rect(screen, color2, (80, 160, W, W))
pygame.draw.polygon(screen, color, ((80, 160), (80 + W // 2, 160 - W // 2),
                                          (80 + W + W // 2, 160 - W // 2), (80 + W, 160)))
pygame.draw.polygon(screen, color3, ((80 + W + W // 2, 160 - W // 2), (80 + W, 160),
                                          (80 + W, 160 + W), (80 + W // 2 + W, 160 + W // 2)))
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()