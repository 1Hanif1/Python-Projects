from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.movement = 10
        self.movement_speed = 0.1
        self.move_y = self.move_x = self.movement
        self.shape("circle")
        self.color("red")
        self.penup()

    def bounce(self):
        self.move_y = self.movement if self.move_y == -self.movement else -self.movement

    def paddle_bounce(self):
        self.move_x = self.movement if self.move_x == -self.movement else -self.movement
        self.movement_speed *= 0.9

    def reset(self):
        self.movement_speed = 0.1
        self.goto((0, 0))
        self.paddle_bounce()

    def move(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.bounce()

        x_cor = self.xcor() + self.move_x
        y_cor = self.ycor() + self.move_y
        self.goto(x_cor, y_cor)
