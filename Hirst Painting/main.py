from random import choice
from turtle import Turtle, Screen, position, setpos
import turtle

# COLORGRAM MODULE TO EXTRACT COLORS FROM IMAGES
# import colorgram

# rgb = colorgram.extract('./image.jpg', 20)
# colors = []

# for obj in rgb:
#     color = tuple([obj.rgb.r, obj.rgb.g, obj.rgb.b])
#     colors.append(color)

# print(colors)


class HirstPaint:
    turtle = Turtle()
    screen = Screen()
    colors = [(236, 35, 108), (145, 28, 64), (239, 75, 35),
              (6, 148, 93), (231, 168, 40), (184, 158, 46),
              (44, 191, 233), (27, 127, 195), (126, 193, 74),
              (253, 223, 0), (85, 28, 93), (173, 36, 97),
              (246, 219, 44), (44, 172, 112), (215, 130, 165),
              (215, 56, 27)]

    def draw_spot(self, dot_size):
        color = choice(self.colors)
        self.turtle.dot(dot_size, color)

    def draw_painting(self, dot_size, num_dots, space):
        x = y = -((num_dots * space) / 2)
        self.turtle.setpos(x, y)

        for _ in range(num_dots):
            for _ in range(num_dots):
                self.draw_spot(dot_size)
                self.turtle.fd(space)
            y += space
            self.turtle.setpos(x, y)

    def __init__(self, dot_size, num_dots, space):
        self.screen.colormode(255)
        self.turtle.speed(0)
        self.turtle.up()
        self.draw_painting(dot_size, num_dots, space)
        self.screen.exitonclick()
        pass


if __name__ == "__main__":
    # Arguments: size of dots, number of dots(n) ~ forms [n x n] matrix, space between dots.
    HirstPaint(10, 20, 30)
