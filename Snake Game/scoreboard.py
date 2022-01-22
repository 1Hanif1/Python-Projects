from operator import mod
from statistics import mode
from turtle import Turtle


class ScoreBoard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        with open("data.txt", "r") as file:
            self.high_score = int(file.readline())

        self.color("white")
        self.up()
        self.speed("fastest")
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(arg=f"Score = {self.score} | High Score : {self.high_score}", move=True, align="center",
                   font=("Verdana", 15, "normal"))

    def increment_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        self.high_score = self.score if self.score > self.high_score else self.high_score

        with open("data.txt", mode="w") as file:
            content = str(self.high_score)
            file.write(content)

        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("GAME OVER", align="center", font=("Verdana", 15, "normal"))
