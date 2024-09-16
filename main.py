from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move_forward, key='Up')
screen.onkeyrelease(fun=player.stop, key='Up')


game_on = True
while game_on:
    screen.update()

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_on = False
            scoreboard.game_over()

    if player.level_complete():
        car_manager.level_up()
        scoreboard.next_level()

    scoreboard.update_scoreboard()

    player.sety(player.ycor() + player.player_speed)

screen.exitonclick()
