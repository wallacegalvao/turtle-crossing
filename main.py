from turtle import Turtle, Screen
import time
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

##screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("My Turtle Crossing Game")
screen.tracer(0)

player = Player()

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    screen.listen()
    screen.onkey(player.move, "Up")

    if player.won():
        player.starting_position()
        car_manager.speed_up()
        scoreboard.update_score()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()