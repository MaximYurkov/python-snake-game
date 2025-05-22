# objects/apple.py
import random
from config import GRID_WIDTH, GRID_HEIGHT, GRID_SIZE, APPLE_COLOR
from objects.game_object import GameObject

class Apple(GameObject):
    """
    Класс, представляющий яблоко на игровом поле.
    """

    def __init__(self):
        """
        Создаёт яблоко с цветом и случайной позицией на игровом поле.
        """
        super().__init__((0, 0), APPLE_COLOR)
        self.randomize_position()

    def randomize_position(self):
        """
        Устанавливает яблоко в случайную позицию на игровом поле.
        """
        x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
        y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        self.position = (x, y)
