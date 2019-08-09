import pygame
from game_settings import Game_settings


class Game_Objects():

    def __init__(self, xcor, ycor, color):
        self.xcor = xcor
        self.ycor = ycor
        self.color = color

    def show_as_circle(self, game_display, BLOCK_SIZE):
        pygame.draw.circle(game_display, self.color, (int(self.xcor + BLOCK_SIZE / 2),
            int(self.ycor + BLOCK_SIZE / 2)), int(BLOCK_SIZE / 2))

    def show_as_square(self, game_display, GAP_SIZE, BLOCK_SIZE):
        pygame.draw.rect(game_display, self.color, pygame.Rect(
            self.xcor + GAP_SIZE, self.ycor + GAP_SIZE, BLOCK_SIZE - GAP_SIZE * 2, BLOCK_SIZE - GAP_SIZE * 2))
