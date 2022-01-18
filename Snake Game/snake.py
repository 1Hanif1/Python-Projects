from turtle import Turtle


class Snake:
    STARTING_POSITIONS = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self) -> None:
        self.last_input = "right"
        self.segments = []
        self.create_snake()
        self.HEAD = self.segments[0]

    def up(self):
        if self.last_input == "down":
            return
        self.HEAD.seth(self.UP)
        self.last_input = "up"

    def down(self):
        if self.last_input == "up":
            return
        self.HEAD.seth(self.DOWN)
        self.last_input = "down"

    def left(self):
        if self.last_input == "right":
            return
        self.HEAD.seth(self.LEFT)
        self.last_input = "left"

    def right(self):
        if self.last_input == "left":
            return
        self.HEAD.seth(self.RIGHT)
        self.last_input = "right"

    def create_snake(self):
        for position in self.STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].fd(self.MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def grow_snake(self):
        last_segment_position = self.segments[-1].position()
        self.add_segment(last_segment_position)
