import pygame
from random import choice

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

SNAKE_COLOR = (0, 255, 0)
APPLE_COLOR = (255, 0, 0)
BOARD_BACKGROUND_COLOR = (0, 0, 0)
FPS = 20


class GameObject:
    """Базовый класс для игровых объектов."""

    def __init__(self, position, body_color):
        self.position = position
        self.body_color = body_color

    def draw(self, surface):
        """Заглушка для отрисовки (реализуется в наследниках)."""
        pass


class Apple(GameObject):
    """Яблоко, которое ест змейка."""

    def __init__(self):
        super().__init__((0, 0), APPLE_COLOR)

    def randomize_position(self, forbidden_positions=None):
        """Генерирует случайную позицию вне тела змейки."""
        if forbidden_positions is None:
            forbidden_positions = []

        all_cells = [
            (x * GRID_SIZE, y * GRID_SIZE)
            for x in range(GRID_WIDTH)
            for y in range(GRID_HEIGHT)
        ]
        available = list(set(all_cells) - set(forbidden_positions))
        self.position = choice(available) if available else (0, 0)

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            self.body_color,
            pygame.Rect(
                self.position[0], self.position[1],
                GRID_SIZE, GRID_SIZE
            )
        )


class Snake(GameObject):
    """Класс, представляющий змейку."""

    def __init__(self):
        center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        super().__init__(center, SNAKE_COLOR)
        self.length = 1
        self.positions = [center]
        self.direction = choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.next_direction = None
        self.last = None

    def get_head_position(self):
        """Возвращает координаты головы змейки."""
        return self.positions[0]

    def update_direction(self):
        """Обновляет направление, если оно не противоположно текущему."""
        if self.next_direction is None:
            return
        x, y = self.direction
        nx, ny = self.next_direction
        if (x + nx, y + ny) != (0, 0):
            self.direction = self.next_direction
        self.next_direction = None

    def move(self):
        """Двигает змейку и проверяет столкновения."""
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
        """Сброс змейки в начальное состояние."""
        center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.length = 1
        self.positions = [center]
        self.direction = choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.next_direction = None
        self.last = None

    def draw(self, surface):
        """Отрисовка тела змейки и стирание последнего сегмента."""
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


def handle_keys(snake):
    """Обрабатывает нажатия клавиш."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            elif event.key == pygame.K_UP:
                snake.next_direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake.next_direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake.next_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake.next_direction = (1, 0)
    return True


def main():
    """Главная функция запуска игры."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Змейка")

    clock = pygame.time.Clock()
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
