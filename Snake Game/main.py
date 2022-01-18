from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from wall import Wall
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
Wall()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# Once done screen is updated to show the changes
screen.update()

# Stores the state of game
game_state = True
speed = 0.2
while game_state:

    screen.update()
    time.sleep(speed)
    snake.move()
    if snake.HEAD.distance(food) < 15:
        food.refresh()
        snake.grow_snake()
        score.increment_score()

    if score.score >= 5:
        speed = 0.15
    if score.score >= 10:
        speed = 0.1
    if score.score >= 17:
        speed = 0.08

    if snake.HEAD.xcor() > 290 or snake.HEAD.xcor() < -290 or snake.HEAD.ycor() > 290 or snake.HEAD.ycor() < -290:
        game_state = False

    for segment in snake.segments[1:]:
        if snake.HEAD.distance(segment) < 10:
            game_state = False
            break

# When game is over
score.game_over()

# Maintains the screen created. Must be last statement in program
screen.mainloop()
