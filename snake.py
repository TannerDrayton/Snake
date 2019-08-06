
import pygame
import random
from snake_class import Snake
from game_objects import Game_Object
from game_settings import Game_settings

# Game Settings
GAME_SIZE = 400
BLOCK_SIZE = GAME_SIZE / 40
GAP_SIZE = GAME_SIZE * 0.002
APPLE_COLOR = (255, 25, 55)
BACKGROUND_COLOR = (0, 0, 0)
YELLOW = (255, 255, 0)
LIME_GREEN = (0, 255, 0)
FOREST_GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GAME_FPS = 30

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((GAME_SIZE, GAME_SIZE))
score_font = pygame.font.SysFont('Comic Sans', int(GAME_SIZE * .065), True)
title_font = pygame.font.SysFont('Comic Sans', int(GAME_SIZE * .2), True)
title_press_start_font = pygame.font.SysFont(
    'Comic Sans', int(GAME_SIZE * 0.1), True)
title_copyright_font = pygame.font.SysFont(
    'Comic Sans', int(GAME_SIZE * 0.05), True)
pygame.display.set_caption(' SNAKE ')


class Color_Cycler():
    def __init__(self, * colors):
        self.colors = []
        for color in colors:
            self.colors.append(color)

        self.cycle_count = 1
        self.color_change_frequency = 6

    def get_next_color(self):
        if self.cycle_count >= self.color_change_frequency:
            self.cycle_count = 1

        else:
            self.cycle_count += 1

        if self.cycle_count == self.color_change_frequency:
            next_color = self.colors.pop()
            self.colors.insert(0, next_color)
            return next_color

        else:
            return self.colors[0]


class Apple():
    def __init__(self, snake_Segment):
        self.body = self.get_RNG_generated_game_object()
        while self.apple_is_on_snake(snake_Segment):
            self.body = self.get_RNG_generated_game_object()

    def get_RNG_generated_game_object(self):
        xcor = random.randrange(0, GAME_SIZE / BLOCK_SIZE) * BLOCK_SIZE
        ycor = random.randrange(0, GAME_SIZE / BLOCK_SIZE) * BLOCK_SIZE
        return Game_Object(xcor, ycor, APPLE_COLOR)

    def apple_is_on_snake(self, snake_Segment):
        for snake_part in snake_Segment:
            if snake_part.xcor == self.body.xcor and snake_part.ycor == self.body.ycor:
                return True

    def show(self):
        self.body.show_as_circle(game_display, BLOCK_SIZE)


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


color_cycler = Color_Cycler(BLUE, LIME_GREEN, FOREST_GREEN, YELLOW, CYAN)
snake = Snake(BLOCK_SIZE * 5, BLOCK_SIZE * 5, LIME_GREEN, BLOCK_SIZE, BLUE)
apple = Apple(snake.body)

# Title Screen
show_title_screen = True
while show_title_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            snake.is_alive = False
            show_title_screen = False
        if event.type == pygame.KEYDOWN:
            show_title_screen = False
    title_text = title_font.render('| SNAKE |', False, LIME_GREEN)
    title_press_start_text = title_press_start_font.render(
        'PRESS TO START', False, CYAN)

    game_display.blit(title_text, (GAME_SIZE / 2 -
                                   title_text.get_width() / 2, 50))

    game_display.blit(title_press_start_text, (GAME_SIZE /
                                               4 - title_press_start_text.get_width() / 10, 150))

    pygame.display.flip()
    clock.tick(GAME_FPS)

# Main Game Loop
FRAME_COUNTER = 0
while snake.is_alive:
    handle_events()
    game_display.blit(game_display, (0, 0))
    if FRAME_COUNTER % 2 == 0:
        snake.move(color_cycler, BLOCK_SIZE)
        if snake.has_collided_with_wall(BLOCK_SIZE, GAME_SIZE) or snake.has_collided_with_itself():
            snake.is_alive = False
        if snake.has_eaten_apple(apple):
            snake.grow()
            for i in range(0, snake.score):
                snake.grow()
            snake.score += 1
            apple = Apple(snake.body)
    game_display.fill(BACKGROUND_COLOR)
    snake.show(game_display, GAP_SIZE, BLOCK_SIZE)
    apple.show()
    FRAME_COUNTER += 1
    snake.refresh_RGB_cycled_colors(color_cycler)
    score_text = score_font.render(str(snake.score), False, (255, 255, 255))
    game_display.blit(score_text, (0, 0))
    pygame.display.set_caption(
        'SNAKE | Score = ' + str(snake.score) + ' | Press P to pause')
    pygame.display.flip()
    if snake.is_alive == False:
        clock.tick(.7)

    clock.tick(GAME_FPS)
pygame.display.quit()  # For Mac
pygame.quit()
