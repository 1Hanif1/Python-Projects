from turtle import Turtle, Screen
import random
turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.shape("circle")
turtle.speed("fastest")
turtle.pensize(15)


def draw_shape(angle):
    turtle.fd(30)
    turtle.rt(angle)


for _ in range(200):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    turtle.color(red, green, blue)
    angle = random.choice([0, 90, 180, 270])
    draw_shape(angle)

# 0+3, 1+3, 2+3, 3+3, 4+3, 5+3, 6+3. 7+3


screen.exitonclick()
