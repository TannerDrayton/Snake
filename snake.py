
import pygame
import random
from apple import Apple
from snake_class import Snake
from color_cycler import Color_Cycler
from game_objects import Game_Objects
from game_settings import Game_settings

# Game Settings
gs = Game_settings()

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((gs.GAME_SIZE, gs.GAME_SIZE))
score_font = pygame.font.SysFont('Comic Sans', int(gs.GAME_SIZE * .065), True)
title_font = pygame.font.SysFont('Comic Sans', int(gs.GAME_SIZE * .2), True)
title_press_start_font = pygame.font.SysFont('Comic Sans', int(gs.GAME_SIZE * 0.1), True)
title_copyright_font = pygame.font.SysFont('Comic Sans', int(gs.GAME_SIZE * 0.05), True)
pygame.display.set_caption(' SNAKE ')


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            snake.is_alive = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.set_direction_left()
            elif event.key == pygame.K_RIGHT:
                snake.set_direction_right()
            elif event.key == pygame.K_UP:
                snake.set_direction_up()
            elif event.key == pygame.K_DOWN:
                snake.set_direction_down()
            elif event.key == pygame.K_p:
                pause_game()


def pause_game():
    game_is_paused = True
    while game_is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                snake.is_alive = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_is_paused = False

            pygame.display.update()
            clock.tick(5)


color_cycler = Color_Cycler(gs.BLUE, gs.LIME_GREEN,gs.FOREST_GREEN, gs.YELLOW, gs.CYAN)
snake = Snake(gs.BLOCK_SIZE * 5, gs.BLOCK_SIZE * 5,gs.LIME_GREEN, gs.BLOCK_SIZE, gs.BLUE)
apple = Apple(snake.body, gs)

# Title Screen
show_title_screen = True
while show_title_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            snake.is_alive = False
            show_title_screen = False
        if event.type == pygame.KEYDOWN:
            show_title_screen = False
    title_text = title_font.render('| SNAKE |', False, gs.LIME_GREEN)
    title_press_start_text = title_press_start_font.render('PRESS TO START', False, gs.CYAN)

    game_display.blit(title_text, (gs.GAME_SIZE / 2 -title_text.get_width() / 2, 50))

    game_display.blit(title_press_start_text, (gs.GAME_SIZE /  4 - title_press_start_text.get_width() / 10, 150))

    pygame.display.flip()
    clock.tick(gs.GAME_FPS)

# Main Game Loop
FRAME_COUNTER = 0
while snake.is_alive:
    handle_events()
    game_display.blit(game_display, (0, 0))
    if FRAME_COUNTER % 2 == 0:
        snake.move(color_cycler, gs.BLOCK_SIZE)
        if snake.has_collided_with_wall(gs.BLOCK_SIZE, gs.GAME_SIZE) or snake.has_collided_with_itself():
            snake.is_alive = False
        if snake.has_eaten_apple(apple):
            snake.grow()
            for i in range(0, snake.score):
                snake.grow()
            snake.score += 1
            apple = Apple(snake.body, gs)
    game_display.fill(gs.BACKGROUND_COLOR)
    snake.show(game_display, gs.GAP_SIZE, gs.BLOCK_SIZE)
    apple.show(game_display, gs)
    FRAME_COUNTER += 1
    snake.refresh_RGB_cycled_colors(color_cycler)
    score_text = score_font.render(str(snake.score), False, (255, 255, 255))
    game_display.blit(score_text, (0, 0))
    pygame.display.set_caption('SNAKE | Score = ' + str(snake.score) + ' | Press P to pause')
    pygame.display.flip()
    if snake.is_alive == False:
        clock.tick(.7)

    clock.tick(gs.GAME_FPS)
pygame.display.quit()  # For Mac
pygame.quit()
