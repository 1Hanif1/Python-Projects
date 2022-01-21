from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.current_level = 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.goto(-280, 270)
        self.write(arg=f"Level: {self.current_level}",
                   move="center", font=("Courier", 20, "normal"))

    def update_level(self):
        self.current_level += 1
        self.write_level()

    def game_over(self):
        self.goto(-80, 0)
        self.write(arg=f"Game Over",
                   move="center", font=("Courier", 20, "normal"))
