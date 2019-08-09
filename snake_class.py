from game_objects import Game_Objects
from game_settings import Game_settings


class Snake():

    def __init__(self, xcor, ycor, LIME_GREEN, BLOCK_SIZE, BLUE):
        self.is_alive = True
        self.score = 0
        self.direction = "RIGHT"
        self.body = [Game_Objects(xcor, ycor, LIME_GREEN),
                     Game_Objects(xcor - BLOCK_SIZE, ycor, BLUE),
                     Game_Objects(xcor - BLOCK_SIZE * 2, ycor, LIME_GREEN)]

        self.previous_last_tail = self.body[len(self.body) - 1]
        self.color_counter = 0

    def grow(self):
        self.body.append(self.previous_last_tail)

    def show(self, game_display, GAP_SIZE, BLOCK_SIZE):
        for body_part in self.body:
            body_part.show_as_square(game_display, GAP_SIZE, BLOCK_SIZE)

    def set_direction_right(self):
        if self.direction != "LEFT":
            self.direction = "RIGHT"

    def set_direction_left(self):
        if self.direction != "RIGHT":
            self.direction = "LEFT"

    def set_direction_up(self):
        if self.direction != "DOWN":
            self.direction = "UP"

    def set_direction_down(self):
        if self.direction != "UP":
            self.direction = "DOWN"

    def move(self, color_cycler, BLOCK_SIZE):
        head_xcor = self.body[0].xcor
        head_ycor = self.body[0].ycor

        if self.direction == "RIGHT":
            head_xcor = head_xcor + BLOCK_SIZE

        elif self.direction == "LEFT":
            head_xcor = head_xcor - BLOCK_SIZE

        elif self.direction == "UP":
            head_ycor = head_ycor - BLOCK_SIZE

        elif self.direction == "DOWN":
            head_ycor = head_ycor + BLOCK_SIZE

        self.body.insert(0, Game_Objects(head_xcor, head_ycor, color_cycler.get_next_color()))

        self.previous_last_tail = self.body.pop()

    def refresh_RGB_cycled_colors(self, color_cycler):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].color = self.body[i-1].color

        self.body[0].color = color_cycler.get_next_color()

    def has_collided_with_wall(self, BLOCK_SIZE, GAME_SIZE):
        head = self.body[0]
        if head.xcor < 0 or head.ycor < 0 or head.xcor + BLOCK_SIZE > GAME_SIZE or head.ycor + BLOCK_SIZE > GAME_SIZE:
            return True
        return False

    def has_eaten_apple(self, apple_in_question):
        head = self.body[0]
        if head.xcor == apple_in_question.body.xcor and head.ycor == apple_in_question.body.ycor:
            return True
        return False

    def has_collided_with_itself(self):
        head = self.body[0]
        for i in range(1, len(self.body)):
            if head.xcor == self.body[i].xcor and head.ycor == self.body[i].ycor:
                return True
        return False
