import pygame


class Board:
    # создание поля
    def __init__(self, width, height, cell_size):
        self.width = width
        self.cell_size = cell_size
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, cell_size):
        self.cell_size = cell_size

    def render(self):
        for i in range(len(self.board[0])):
            i += 1
            for j in range(len(self.board)):
                j += 1
                c = self.board[i - 1][j - 1]
                pygame.draw.rect(screen, (255, 255, 255), (i * self.cell_size, j * self.cell_size, self.cell_size,
                                                           self.cell_size), c)

    def get_cell(self):
        mouse = pygame.mouse.get_pos()
        if 30 <= mouse[0] <= 570 and 30 <= mouse[1] <= 570:
            return round((mouse[0] - 45) / self.cell_size), round((mouse[1] - 45) / self.cell_size)
        else:
            return None

    def get_click(self):
        cell = self.get_cell()
        if cell is not None:
            self.on_click(cell)

    def on_click(self, xy):
        x, y = xy
        if self.board[x][y] == 1:
            self.board[x][y] = 0
        else:
            self.board[x][y] = 1


size = [width, height] = [600, 600]
screen = pygame.display.set_mode(size)
board = Board(18, 18, 30)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.get_click()
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()