# main.py
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from objects.apple import Apple
from objects.snake import Snake

def handle_keys(snake):
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
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Змейка")

    clock = pygame.time.Clock()
    snake = Snake()
    apple = Apple()

    running = True
    while running:
        clock.tick(FPS)
        running = handle_keys(snake)

        snake.update_direction()
        snake.move()

        # Проверка: съела ли змейка яблоко
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()

        # Отрисовка
        snake.draw(screen)
        apple.draw(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
