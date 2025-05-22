import random
from config import GRID_WIDTH, GRID_HEIGHT, GRID_SIZE, APPLE_COLOR
from objects.game_object import GameObject


class Apple(GameObject):

    def __init__(self):

        super().__init__((0, 0), APPLE_COLOR)

    def randomize_position(self, forbidden_positions=None):

        if forbidden_positions is None:
            forbidden_positions = []

        all_cells = [
            (x * GRID_SIZE, y * GRID_SIZE)
            for x in range(GRID_WIDTH)
            for y in range(GRID_HEIGHT)
        ]
        available = list(set(all_cells) - set(forbidden_positions))

        self.position = random.choice(available) if available else (0, 0)
