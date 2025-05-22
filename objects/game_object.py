import pygame
from config import GRID_SIZE


class GameObject:
    """Базовый класс для всех игровых объектов."""

    def __init__(self, position, body_color):
        """Инициализирует координаты и цвет объекта."""
        self.position = position
        self.body_color = body_color

    def draw(self, surface):
        """Отрисовывает объект как квадрат."""
        pygame.draw.rect(
            surface,
            self.body_color,
            pygame.Rect(
                self.position[0],
                self.position[1],
                GRID_SIZE,
                GRID_SIZE
            )
        )
