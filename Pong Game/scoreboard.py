from tkinter import CENTER
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.write_score()

    def write_left_score(self):
        self.goto(-100, 240)
        self.write(self.l_score, align="center",
                   font=("Verdana", 40, "normal"))

    def write_right_score(self):
        self.goto(100, 240)
        self.write(self.r_score, align="center",
                   font=("Verdana", 40, "normal"))

    def write_score(self):
        self.clear()
        self.write_left_score()
        self.write_right_score()

    def update_score(self, player):
        if player == "left":
            self.r_score += 1
        else:
            self.l_score += 1
        self.write_score()
