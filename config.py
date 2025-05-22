# config.py
"""
Конфигурация параметров игры: размеры экрана, размеры ячейки, цвета и FPS.
"""

# Размеры игрового окна
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Размер одной ячейки (квадрата)
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Цвета (RGB)
SNAKE_COLOR = (0, 255, 0)
APPLE_COLOR = (255, 0, 0)
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Частота обновления экрана
FPS = 20
