from turtle import Turtle, Screen


class EtchASketch:
    turtle = Turtle()
    screen = Screen()
    movement_speed = (10)

    def forwards(self):
        self.turtle.fd(self.movement_speed)

    def backwards(self):
        self.turtle.bk(self.movement_speed)

    def turn_right(self):
        self.turtle.right(self.movement_speed)

    def turn_left(self):
        self.turtle.left(self.movement_speed)

    def clear_screen(self):
        self.turtle.reset()

    def add_listeners(self):
        self.screen.onkeypress(fun=self.forwards, key="w")
        self.screen.onkeypress(fun=self.backwards, key="s")
        self.screen.onkeypress(fun=self.turn_left, key="a")
        self.screen.onkeypress(fun=self.turn_right, key="d")
        self.screen.onkeypress(fun=self.clear_screen, key="c")

    def __init__(self) -> None:
        self.screen.listen()
        self.add_listeners()
        self.screen.exitonclick()
        pass


if __name__ == "__main__":
    EtchASketch()
