from re import A
import pygame
from Grid import Grid
from Snake import Snake
from apple import Apple

# Инициализация
pygame.init()
screen = pygame.display.set_mode((640, 640))  # Размер окна

# Главный цикл
running = True
game_grid = Grid(screen)
food = Apple(game_grid)
player_snake = Snake(game_grid, food)

MOVE = pygame.USEREVENT
pygame.time.set_timer(MOVE, 200)

clock = pygame.time.Clock()

prev_direction = "right"

while running:
    pygame.display.flip()
    for event in pygame.event.get():  # Получаем все события
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if (len(player_snake.body) > 1):
                    if (player_snake.body[1].direction != "right"):
                        player_snake.body[0].direction = "left"
                        prev_direction = "left"
                else:
                    player_snake.body[0].direction = "left"
                    prev_direction = "left"
            elif event.key == pygame.K_RIGHT:
                if (len(player_snake.body) > 1):
                    if (player_snake.body[1].direction != "left"):
                        player_snake.body[0].direction = "right"
                        prev_direction = "right"
                else:
                    player_snake.body[0].direction = "right"
                    prev_direction = "right"
            elif event.key == pygame.K_UP:
                if (len(player_snake.body) > 1):
                    if (player_snake.body[1].direction != "down"):
                        player_snake.body[0].direction = "up"
                        prev_direction = "up"
                else:
                    player_snake.body[0].direction = "up"
                    prev_direction = "up"
            elif event.key == pygame.K_DOWN:
                if (len(player_snake.body) > 1):
                    if (player_snake.body[1].direction != "up"):
                        player_snake.body[0].direction = "down"
                        prev_direction = "down"
                else:
                    player_snake.body[0].direction = "down"
                    prev_direction = "down"
        elif event.type == MOVE:
            player_snake.move()
        elif event.type == pygame.QUIT:  # Выход по крестику
            running = False

    # Отрисовка
    # screen.fill((255, 0, 0))  # Чёрный фон (на самом деле красный, 255,0,0)
    clock.tick(30)
    pygame.display.flip()  # Обновление экрана

# Завершение
pygame.quit()