# objects/game_object.py
import pygame
from config import GRID_SIZE

class GameObject:
    """
    Базовый класс для всех объектов на игровом поле.
    """
    def __init__(self, position, body_color):
        """
        Инициализация игрового объекта.
        :param position: Кортеж с координатами (x, y)
        :param body_color: Цвет объекта (RGB)
        """
        self.position = position
        self.body_color = body_color

    def draw(self, surface):
        """
        Отрисовка объекта на экране.
        :param surface: Игровая поверхность (экран)
        """
        pygame.draw.rect(
            surface,
            self.body_color,
            pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE)
        )
