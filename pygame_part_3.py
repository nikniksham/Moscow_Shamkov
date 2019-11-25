import pygame
import random


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        self.win_c = None
        self.move = 1
        self.f_error = False
        for j in range(height):
            line = []
            for i in range(width):
                line.append(random.choice([0, 1]))
            self.board.append(line)
        # значения по умолчанию
        self.left = 30
        self.top = 30
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        r, g = 0, 0
        for i in range(len(self.board[0])):
            for j in range(len(self.board)):
                c = self.board[j][i]
                if c == 0:
                    r += 1
                    pygame.draw.circle(screen, (255, 0, 0), (self.left + i * self.cell_size + self.cell_size // 2,
                                                             self.top + j * self.cell_size + self.cell_size // 2),
                                       self.cell_size // 2 - 1, 2)
                if c == 1:
                    g += 1
                    pygame.draw.circle(screen, (0, 255, 0), (self.left + i * self.cell_size + self.cell_size // 2,
                                       self.top + j * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 1, 2)
                pygame.draw.rect(screen, (255, 255, 255), (self.left + i * self.cell_size,
                                 self.top + j * self.cell_size, self.cell_size, self.cell_size), 1)
        if r == self.width * self.height:
            self.win_c = 0
        if g == self.width * self.height:
            self.win_c = 1

    def get_cell(self, mouse):
        if self.left <= mouse[0] <= self.left + self.cell_size * len(self.board[0]) \
                and self.top <= mouse[1] <= self.top + self.cell_size * len(self.board):
            c = self.cell_size
            return (mouse[0] - self.left) // c, (mouse[1] - self.top) // c
        else:
            return None

    def get_click(self, mouse):
        cell = self.get_cell(mouse)
        if cell is not None:
            if self.board[cell[1]][cell[0]] == self.move:
                self.on_click(cell)
                self.f_error = False
            else:
                self.f_error = True

    def switch_color(self, x, y, c):
        if self.board[y][x] != c:
            self.board[y][x] = c

    def on_click(self, xy):
        if self.move == 0:
            self.move = 1
        else:
            self.move = 0
        x, y = xy
        c = self.board[y][x]
        for i in range(len(self.board[0])):
            self.switch_color(i, y, c)
        for j in range(len(self.board)):
            self.switch_color(x, j, c)

    def error(self):
        move_list = {1: 'Зелёного', 0: 'Красного'}
        text = font.render(f'Ход {move_list[self.move]}!', 1, (0, 255, 0))
        screen.blit(text, (self.left, width - 10))

    def win(self):
        list_players = {1: 'Зелёный', 0: 'Красный'}
        text = font.render(f'Победил {list_players[self.win_c]}!', 1, (0, 255, 0))
        screen.blit(text, (self.left, width - 10))


#                                        !!!!!!!!!!!!!!ПЕРВЫМ ХОДИТ ЗЕЛЁНЫЙ!!!!!!!!!!!!!!!
width_height = int(input())
board = Board(width_height, width_height)
# board.set_view(20, 20, 20)  # Можно задавать параметры: крайний левый угол, верхний угол, размер клетки соответственно
clock = pygame.time.Clock()
size = [width, height] = [board.width * board.cell_size + board.left * 2,  # Размеры поля будут подстраиваться так, что
                          board.height * board.cell_size + board.top * 2 + 50]  # бы ваше поле было ровно по цетру
pygame.font.init()
font = pygame.font.Font(None, 35)
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if board.win_c is None:
                board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    if board.f_error:
        board.error()
    if board.win_c is not None:
        board.win()
    pygame.display.flip()
    clock.tick(60)