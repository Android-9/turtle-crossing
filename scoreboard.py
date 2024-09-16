from turtle import Turtle
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.setposition(-230, 270)
        self.level = 1

    def next_level(self):
        self.level += 1

    def game_over(self):
        over = Turtle()
        over.hideturtle()
        over.penup()
        over.color('black')
        over.write("GAME OVER", align='center', font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=FONT)
