from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Sets up the screen to display the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Mo (Github: @1Hanif1)")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# Once done screen is updated to show the changes
screen.update()

# Stores the state of game
game_state = True
while game_state:

    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.HEAD.distance(food) < 15:
        food.refresh()
        score.increment_score()

# Maintains the screen created. Must be last statement in program
screen.mainloop()
