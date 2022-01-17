from turtle import Turtle


class ScoreBoard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.speed("fastest")
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.goto(0, 270)
        self.write(arg=f"Score = {self.score}", move=True, align="center",
                   font=("Verdana", 15, "normal"))

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write_score()
