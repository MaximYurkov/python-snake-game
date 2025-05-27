import pygame
from config import GRID_SIZE


class GameObject:
    def __init__(self, position=(0, 0), body_color=(255, 255, 255)):
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
