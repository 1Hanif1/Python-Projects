from turtle import Turtle


class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.up()
        self.hideturtle()
        self.goto(-290, 290)
        self.draw_wall()

    def draw_wall(self):
        self.down()
        self.fd(580)
        self.right(90)
        self.fd(580)
        self.right(90)
        self.fd(580)
        self.right(90)
        self.fd(580)
