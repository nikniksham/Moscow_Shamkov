import pygame


pygame.init()
input_ = input().split()
W, Hue = int(input_[0]), int(input_[1])
# W = 300
screen = pygame.display.set_mode((500, 500))
color = pygame.Color(0, 0, 0)
hsv = color.hsva
color.hsva = (Hue, 100, 100, hsv[3])
color2 = pygame.Color(0, 0, 0)
hsv = color2.hsva
color2.hsva = (Hue, 100, 75, hsv[3])
color3 = pygame.Color(0, 0, 0)
hsv = color3.hsva
color3.hsva = (Hue, 100, 50, hsv[3])
width, height = 300, 300
size = width, height
H = 150 - W * 0.8
V = 150

screen = pygame.display.set_mode(size)
pygame.draw.rect(screen, color2, (H, V, W, W + 1))
pygame.draw.polygon(screen, color, ((H, V), (H + W // 2, V - W // 2),
                                    (H + W + W // 2, V - W // 2), (H + W, V)))
pygame.draw.polygon(screen, color3, ((H + W + W // 2, V - W // 2), (H + W, V),
                                     (H + W, V + W), (H + W // 2 + W, V + W // 2)))
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()