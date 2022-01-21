from turtle import Turtle
import random


class CarManager():
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    STARTING_MOVE_DISTANCE = 5
    MOVE_INCREMENT = 10

    def __init__(self):
        super().__init__()
        self.cars = []
        pass

    def gen_car(self, width, height):
        car = Turtle("square")
        car.penup()
        car.speed("fastest")
        car.color(self.COLORS[random.randint(0, len(self.COLORS) - 1)])
        car.setheading(180)
        car.goto(x=(width/2), y=random.randint(-(height/2) + 50, (height/2) - 50))
        car.shapesize(stretch_wid=1, stretch_len=3)
        self.cars.append(car)
        pass

    def move_cars(self):
        for car in self.cars:
            car.forward(self.STARTING_MOVE_DISTANCE)

    def check_collision(self, turtle):
        for car in self.cars:
            if turtle.distance(car) < 20:
                return True

    def increment_speed(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT

    def clear_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                self.cars.remove(car)
