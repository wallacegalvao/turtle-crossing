from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level:{self.level}", align="center", font="Arial")
        self.level += 1

    def game_over(self):
       self.goto(0, 0)
       self.write("GAME OVER", align='center', font="Arial")

