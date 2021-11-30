from turtle import Turtle
import random

COLORS = ["blue", "yellow", "orange", "pink", "orange", "brown", "cyan", "navy", "grey"]


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = 1
        self.car_appear = 10

    def create_car(self):
        car_chance = random.randint(0, self.car_appear)
        if car_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(270, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += 1
        self.car_appear -= 1