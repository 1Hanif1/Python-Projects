from turtle import Turtle


class Snake:
    STARTING_POSITIONS = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.HEAD = self.segments[0]

    def up(self):
        if self.HEAD.heading() == self.DOWN:
            return
        self.HEAD.seth(self.UP)

    def down(self):
        if self.HEAD.heading() == self.UP:
            return
        self.HEAD.seth(self.DOWN)

    def left(self):
        if self.HEAD.heading() == self.RIGHT:
            return
        self.HEAD.seth(self.LEFT)

    def right(self):
        if self.HEAD.heading() == self.LEFT:
            return
        self.HEAD.seth(self.RIGHT)

    def create_snake(self):
        for position in self.STARTING_POSITIONS:
            # Creates body parts of snakes and positions them accordingly
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.up()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].fd(self.MOVE_DISTANCE)
