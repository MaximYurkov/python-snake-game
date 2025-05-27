import pygame
import random

# Константы
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

SNAKE_COLOR = (0, 255, 0)
APPLE_COLOR = (255, 0, 0)
BOARD_BACKGROUND_COLOR = (0, 0, 0)
FPS = 20

# Направления
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


# GameObject
class GameObject:
    def __init__(self, position=(0, 0), body_color=(255, 255, 255)):
        self.position = position
        self.body_color = body_color

    def draw(self, surface):
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


# Apple
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


# Snake
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


# Управление
def handle_keys(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            elif event.key == pygame.K_UP:
                snake.next_direction = UP
            elif event.key == pygame.K_DOWN:
                snake.next_direction = DOWN
            elif event.key == pygame.K_LEFT:
                snake.next_direction = LEFT
            elif event.key == pygame.K_RIGHT:
                snake.next_direction = RIGHT
    return True


# Главный цикл
def main():
    snake = Snake()
    apple = Apple()
    apple.randomize_position(snake.positions)

    running = True
    while running:
        clock.tick(FPS)
        running = handle_keys(snake)

        snake.update_direction()
        snake.move()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position(snake.positions)

        snake.draw(screen)
        apple.draw(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
