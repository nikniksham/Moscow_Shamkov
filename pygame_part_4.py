import pygame
import random


class Board:
    # создание поля
    def __init__(self, x, y):
        self.font = pygame.font.Font(None, int(30 * 0.7))
        self.del_list = []
        self.list_contacts = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]
        self.mine_list = []
        self.width = x
        self.del_open = []
        self.height = y
        self.board = [[-1] * self.width for _ in range(self.height)]
        # значения по умолчанию
        self.left = 30
        self.top = 30
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.font = pygame.font.Font(None, int(cell_size * 1.2))
        self.cell_size = cell_size

    def render(self):
        for i in range(len(self.board[0])):
            for j in range(len(self.board)):
                if self.board[j][i] == 10:
                    pygame.draw.rect(screen, (255, 0, 0), (self.left + i * self.cell_size,
                                     self.top + j * self.cell_size, self.cell_size, self.cell_size))
                if self.board[j][i] not in [-1, 10]:
                    text = self.font.render(str(self.board[j][i]), 1, (0, 255, 100))
                    screen.blit(text, (i * self.cell_size + self.left + 3, j * self.cell_size + self.top + 3))
                pygame.draw.rect(screen, (255, 255, 255), (self.left + i * self.cell_size,
                                 self.top + j * self.cell_size, self.cell_size, self.cell_size), 1)

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
            self.on_click(cell)

    def switch_color(self, x, y):
        if self.board[y][x] == -1:
            self.open_group_cell(x, y)

    def on_click(self, xy):
        self.switch_color(xy[0], xy[1])

    def open_cell(self, x, y):
        contacts = 0
        for i in range(8):
            cell = [y + self.list_contacts[i][0], x + self.list_contacts[i][1]]
            if cell in self.mine_list:
                contacts += 1
        return contacts

    def contact_cell(self, x, y, open_list):
        self.del_open.append([y, x])
        for i in range(8):
            cell = [y + self.list_contacts[i][0], x + self.list_contacts[i][1]]
            if -1 < cell[0] < self.height and -1 < cell[1] < self.width:
                if self.board[cell[0]][cell[1]] == -1 and cell not in self.del_list:
                    if self.open_cell(cell[1], cell[0]) == 0:
                        open_list.append([cell[0], cell[1]])
                        self.del_list.append(cell)
                    if self.open_cell(cell[1], cell[0]) != 0 and self.open_cell(x, y) == 0:
                        open_list.append([cell[0], cell[1]])
                        self.del_list.append(cell)
                        self.del_open.append([cell[0], cell[1]])
        return open_list

    def open_group_cell(self, x, y):
        self.board[y][x] = self.open_cell(x, y)
        open_list = []
        open_list = self.contact_cell(x, y, open_list)
        while True:
            l_p = len(open_list)
            for elem in open_list:
                if elem not in self.del_open:
                    open_list = self.contact_cell(elem[1], elem[0], open_list)
            if len(open_list) == l_p:
                break
        for elem in open_list:
            self.board[elem[0]][elem[1]] = self.open_cell(elem[1], elem[0])


class Minesweeper(Board):
    def __init__(self, x, y, mine):
        super().__init__(x, y)
        self.mine = mine
        self.cell = [[0] * self.width for _ in range(self.height)]
        self.create_mine_field()

    def create_mine_field(self):
        for i in range(self.mine):
            random_pos = [random.choice(range(self.height)), random.choice(range(self.width))]
            if random_pos not in self.mine_list:
                self.mine_list.append(random_pos)
                self.board[random_pos[0]][random_pos[1]] = 10


pygame.font.init()
board = Minesweeper(20, 20, 10)
# board.set_view(10, 10, 20)  # Можно задавать параметры: крайний левый угол, верхний угол, размер клетки соответственно
clock = pygame.time.Clock()
size = [width, height] = [board.width * board.cell_size + board.left * 2,  # Размеры поля будут подстраиваться так, что
                          board.height * board.cell_size + board.top * 2]  # бы ваше поле было ровно по цетру

tick = 0
speed = 0
screen = pygame.display.set_mode(size)
running = True
f_pause = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
    clock.tick(60)
