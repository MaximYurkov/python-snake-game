# objects/snake.py
import random
import pygame
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE,
    SNAKE_COLOR, BOARD_BACKGROUND_COLOR
)
from objects.game_object import GameObject


class Snake(GameObject):
    def __init__(self):
        center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        super().__init__(center, SNAKE_COLOR)
        self.length = 1
        self.positions = [center]
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.next_direction = None
        self.last = None

    def get_head_position(self):
        return self.positions[0]

    def update_direction(self):
        if self.next_direction is None:
            return

        # Запрещаем движение в противоположную сторону
        x, y = self.direction
        nx, ny = self.next_direction
        if (x + nx, y + ny) != (0, 0):
            self.direction = self.next_direction
        self.next_direction = None

    def move(self):
        cur = self.get_head_position()
        dx, dy = self.direction
        new = (
            (cur[0] + dx * GRID_SIZE) % SCREEN_WIDTH,
            (cur[1] + dy * GRID_SIZE) % SCREEN_HEIGHT
        )

        # Проверка на столкновение с собой
        if new in self.positions[2:]:
            self.reset()
            return

        self.positions.insert(0, new)

        if len(self.positions) > self.length:
            self.last = self.positions.pop()

    def reset(self):
        center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.length = 1
        self.positions = [center]
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.next_direction = None
        self.last = None

    def draw(self, surface):
        if self.last:
            pygame.draw.rect(
                surface,
                BOARD_BACKGROUND_COLOR,
                pygame.Rect(
                    self.last[0], self.last[1],
                    GRID_SIZE, GRID_SIZE
                )
            )
        for pos in self.positions:
            pygame.draw.rect(
                surface,
                self.body_color,
                pygame.Rect(
                    pos[0], pos[1],
                    GRID_SIZE, GRID_SIZE
                )
            )
