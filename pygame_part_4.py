import pygame


class Board:
    # создание поля
    def __init__(self, x, y):
        self.cell = []
        self.width = x
        self.height = y
        self.board = [[0] * self.width for _ in range(self.height)]
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
        for i in range(len(self.board[0])):
            for j in range(len(self.board)):
                color = self.board[j][i]
                c, col = 1, (255, 255, 255)
                if color == 1:
                    c, col = 0, (0, 255, 0)

                pygame.draw.rect(screen, col, (self.left + i * self.cell_size,
                                 self.top + j * self.cell_size, self.cell_size, self.cell_size), c)
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
        if self.board[y][x] == 0:
            self.cell.append([y, x])
            self.board[y][x] = 1
        else:
            self.board[y][x] = 0
            self.cell.remove([y, x])

    def on_click(self, xy):
        self.switch_color(xy[0], xy[1])


class Life(Board):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.list_contacts = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]

    def next_move(self):
        cell_contact = []
        for elem in self.cell:
            for i in range(8):
                cell = [elem[0] + self.list_contacts[i][0], elem[1] + self.list_contacts[i][1]]
                if cell not in cell_contact and -1 < cell[0] < self.width and -1 < cell[1] < self.height:
                    cell_contact.append(cell)

        for elem in self.cell:
            if elem in cell_contact:
                cell_contact.remove(elem)

        new_cell = []
        for elem in cell_contact:
            contact = 0
            for elem_2 in self.cell:
                if elem[0] in [elem_2[0] - 1, elem_2[0], elem_2[0] + 1] and elem[1] in [elem_2[1] - 1, elem_2[1], elem_2[1] + 1]:
                    contact += 1
            if contact == 3:
                new_cell.append(elem)

        del_l = []
        for elem in self.cell:
            contact = 0
            for elem_2 in self.cell:
                if elem != elem_2:
                    if elem[0] in [elem_2[0] - 1, elem_2[0], elem_2[0] + 1] \
                            and elem[1] in [elem_2[1] - 1, elem_2[1], elem_2[1] + 1]:
                        contact += 1
            if contact not in [2, 3]:
                del_l.append(elem)

        for elem in del_l:
            self.board[elem[0]][elem[1]] = 0
            self.cell.remove(elem)

        for elem in new_cell:
            self.board[elem[0]][elem[1]] = 1
            self.cell.append(elem)


board = Life(20, 20)
board.set_view(10, 10, 20)  # Можно задавать параметры: крайний левый угол, верхний угол, размер клетки соответственно
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
            if event.button == 4:
                speed += 1
            if event.button == 5 and speed > 0:
                speed -= 1
        if event.type == pygame.KEYDOWN:
            if f_pause:
                f_pause = False
            else:
                f_pause = True
    if tick * speed > 60 and f_pause is False:
        tick = 0
        board.next_move()
    if tick < 60:
        tick += 1
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
    clock.tick(60)
