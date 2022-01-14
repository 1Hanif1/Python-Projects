from turtle import Turtle, Screen
from random import randint


class TurtleRace():
    colors = ["violet", 'green', 'indigo', 'blue', 'yellow', 'orange', 'red']
    screen = Screen()
    turtles = []
    race_status = False
    user_input = ""

    def get_user_input(self):
        while True:
            user_input = self.screen.textinput(title="Make a bet",
                                               prompt="Which turtle will win the race? Enter a color (VIBGYOR)")
            if user_input not in self.colors:
                print("Please enter a valid color")
                continue
            self.user_input = user_input
            self.race_status = True
            break

    def get_screen_ready(self):
        self.screen.setup(width=500, height=400)
        self.get_user_input()

    def create_turtle(self, color):
        t = Turtle(shape="turtle")
        t.up()
        t.color(color)
        return t

    def get_turtles_ready(self):
        x = -230
        y = -100

        for color in self.colors:
            t = self.create_turtle(color)
            t.goto(x, y)
            self.turtles.append(t)
            y += 30

    def __init__(self) -> None:
        self.get_screen_ready()

        self.get_turtles_ready()

        while self.race_status:
            for racer in self.turtles:

                if racer.xcor() > 230:

                    if self.user_input == racer.pencolor():
                        print(f"You won the bet! {racer.pencolor()} won 🥳")
                    else:
                        print(f"You lost the bet! {racer.pencolor()} won 😥")

                    self.race_status = False

                dist = randint(1, 10)

                racer.fd(dist)

        self.screen.bye()


if __name__ == '__main__':
    TurtleRace()
