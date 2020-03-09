import pygame
from random import choice
import time


class Board:
    # базовые настройки
    def __init__(self):
        self.width = 60
        self.height = 30
        self.board = [[0] * width for _ in range(height)]
        self.snake = [[14, 16], [14, 15], [14, 14]]  # координаты частей змеи
        self.fruit = []
        self.cell_size = 17
        self.side = 0
        self.over = False

    def set_side(self, side):
        if self.side + side % 2:
            self.side = side

    def set_fruit(self):  # появление фрукта
        if not self.fruit:
            self.fruit = self.snake[0]
            while self.fruit in self.snake:
                self.fruit = [choice(range(29)), choice(range(29))]

    def run(self):
        if self.side == 0:
            new = [self.snake[-1][0], self.snake[-1][1] - 1]
        elif self.side == 1:
            new = [self.snake[-1][0] + 1, self.snake[-1][1]]
        elif self.side == 2:
            new = [self.snake[-1][0], self.snake[-1][1] + 1]
        else:
            new = [self.snake[-1][0] - 1, self.snake[-1][1]]
        if new[0] < 0:
            new[0] += 30
        elif new[0] >= 30:
            new[0] -= 30
        if new[1] < 0:
            new[1] += 30
        elif new[1] >= 30:
            new[1] -= 30
        if new == self.fruit:
            self.snake.append(new)
            self.fruit = []
        elif new in self.snake:
            self.over = True
        else:
            self.snake.append(new)
            self.snake = self.snake[1:]

    # отрисовка поля
    def render(self):
        if self.over:
            pygame.draw.rect(screen, (250, 100, 0), (0, 0, 510, 510))
            for par in self.snake:
                i, g = par[0], par[1]
                pygame.draw.rect(screen, (255, 10, 10), (i * self.cell_size, g * self.cell_size,
                                                         self.cell_size, self.cell_size))
        else:
            for i in range(self.height):
                for g in range(self.width):
                    pygame.draw.rect(screen, (255, 255, 255), (i * self.cell_size, g * self.cell_size,
                                                               (g + 1) * self.cell_size, (i + 1) * self.cell_size), 1)
            for par in self.snake:
                i, g = par[0], par[1]
                pygame.draw.rect(screen, (255, 200, 10), (i * self.cell_size, g * self.cell_size,
                                                          self.cell_size, self.cell_size))
            if self.fruit:
                pygame.draw.rect(screen, (10, 10, 250), (self.fruit[0] * self.cell_size, self.fruit[1] * self.cell_size,
                                                         self.cell_size, self.cell_size))


pygame.init()
size = width, height = 510, 510
screen = pygame.display.set_mode(size)
fps = 30  # количество кадров в секунду
clock = pygame.time.Clock()
go = True

board = Board()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                board.set_side(0)
            if event.key == pygame.K_RIGHT:
                board.set_side(1)
            if event.key == pygame.K_DOWN:
                board.set_side(2)
            if event.key == pygame.K_LEFT:
                board.set_side(3)
            if event.key == pygame.K_RETURN:
                board.snake = [[14, 16], [14, 15], [14, 14]]
                board.side = 0
                board.over = False
            if event.key == pygame.K_SPACE:
                if go:
                    go = False
                else:
                    go = True
            if event.key == pygame.K_ESCAPE:
                running = False

    if go and not board.over:
        screen.fill((0, 0, 0))
        board.set_fruit()
        board.run()
        board.render()
    time.sleep(0.5)
    clock.tick(fps)

    pygame.display.flip()
