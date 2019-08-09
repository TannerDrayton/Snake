import random
from game_objects import Game_Objects

class Apple():
    def __init__(self, snake_Segment, game_settings):
        self.body = self.get_RNG_generated_game_object(game_settings)
        while self.apple_is_on_snake(snake_Segment):
            self.body = self.get_RNG_generated_game_object(game_settings)

    def get_RNG_generated_game_object(self, game_settings):
        xcor = random.randrange(0, game_settings.GAME_SIZE / game_settings.BLOCK_SIZE) * game_settings.BLOCK_SIZE
        ycor = random.randrange(0, game_settings.GAME_SIZE / game_settings.BLOCK_SIZE) * game_settings.BLOCK_SIZE
        return Game_Objects(xcor, ycor, game_settings.APPLE_COLOR)

    def apple_is_on_snake(self, snake_Segment):
        for snake_part in snake_Segment:
            if snake_part.xcor == self.body.xcor and snake_part.ycor == self.body.ycor:
                return True

    def show(self, game_display, game_settings):
        self.body.show_as_circle(game_display, game_settings.BLOCK_SIZE)
