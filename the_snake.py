import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

# Константы направлений (нужны для тестов)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Инициализация pygame и глобальные переменные для тестов
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
