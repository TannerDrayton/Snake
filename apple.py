import random
from game_objects import Game_Object
from game_settings import Game_settings

GS = Game_settings()
GO = Game_objects()


class Apple():
    def __init__(self, snake_Segment):
        self.body = self.get_RNG_generated_game_object()
        while self.apple_is_on_snake(snake_Segment):
            self.body = self.get_RNG_generated_game_object()

    def get_RNG_generated_game_object(self):
        xcor = random.randrange(0, GS.GAME_SIZE / GS.BLOCK_SIZE) * GS.BLOCK_SIZE
        ycor = random.randrange(0, GS.GAME_SIZE / GS.BLOCK_SIZE) * GS.BLOCK_SIZE
        return GO.Game_Object(xcor, ycor, GS.APPLE_COLOR)

    def apple_is_on_snake(self, snake_Segment):
        for snake_part in snake_Segment:
            if snake_part.xcor == self.body.xcor and snake_part.ycor == self.body.ycor:
                return True

    def show(self):
        self.body.show_as_circle(game_display, GS.BLOCK_SIZE)
