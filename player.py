from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280
player_speed = 0


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.setposition(STARTING_POSITION)
        self.player_speed = 0

    def move_forward(self):
        self.player_speed = 3

    def stop(self):
        self.player_speed = 0

    def level_complete(self):
        if self.ycor() > FINISH_LINE:
            self.setposition(STARTING_POSITION)
            return True
        else:
            return False
