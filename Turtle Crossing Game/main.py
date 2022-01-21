import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.move, 'Up')

game_state = True
counter = 0
while game_state:
    time.sleep(0.05)
    screen.update()

    # will generate car in specific intervals randomly
    if counter % 6 == 0:
        car.gen_car(600, 600)

    counter += 1

    car.move_cars()

    if car.check_collision(player):
        game_state = False

    if player.ycor() >= player.FINISH_LINE_Y:
        car.clear_cars()
        player.reset_pos()
        score.update_level()
        car.increment_speed()

score.game_over()

screen.mainloop()
