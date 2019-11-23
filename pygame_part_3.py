import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
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
                c = self.board[j][i]
                pygame.draw.rect(screen, (255, 255, 255), (self.left + i * self.cell_size,
                                 self.top + j * self.cell_size, self.cell_size, self.cell_size), c)

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

    def on_click(self, xy):
        x, y = xy
        if self.board[y][x] == 1:
            self.board[y][x] = 0
        else:
            self.board[y][x] = 1


board = Board(10, 10)
# board.set_view(10, 10, 10)  # Можно задавать параметры: крайний левый угол, верхний угол, размер клетки соответственно
clock = pygame.time.Clock()
size = [width, height] = [board.width * board.cell_size + board.left * 2,  # Размеры поля будут подстраиваться так, что
                          board.height * board.cell_size + board.top * 2]  # бы ваше поле было ровно по цетру

screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
    clock.tick(60)