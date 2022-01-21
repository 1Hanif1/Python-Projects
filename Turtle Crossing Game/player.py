from turtle import Turtle


class Player(Turtle):
    STARTING_POSITION = (0, -280)
    MOVE_DISTANCE = 10
    FINISH_LINE_Y = 280

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(self.STARTING_POSITION)
        self.seth(90)

    def move(self):
        self.fd(self.MOVE_DISTANCE)

    def reset_pos(self):
        self.goto(self.STARTING_POSITION)
