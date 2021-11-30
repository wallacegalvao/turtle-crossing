from turtle import Turtle

class Player(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.left(90)


    def move(self):
        self.forward(20)

    def won(self):
        if self.ycor() >= 270:
            return True
        else:
            return False

    def starting_position(self):
        self.goto(0, -280)
