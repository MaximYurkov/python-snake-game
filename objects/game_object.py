# objects/game_object.py
import pygame
from config import GRID_SIZE

class GameObject:
    def __init__(self, position, body_color):
        self.position = position
        self.body_color = body_color

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            self.body_color,
            pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE)
        )
