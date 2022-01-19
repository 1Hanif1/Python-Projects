from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coords, screen_size):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coords)

        (self.screen_width, self.screen_height) = screen_size
        (self.height, self.width, self.outline) = self.shapesize()

    def moveup(self):
        if self.ycor() >= (self.screen_height / 2) - ((self.height * 20) / 2):
            return

        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def movedown(self):
        if self.ycor() <= -(self.screen_height / 2) + ((self.height * 20) / 2):
            return

        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)
