import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game by Mo (GitHub: @1Hanif)")
screen.tracer(0)

right_paddle = Paddle((350, 0), (800, 600))
left_paddle = Paddle((-350, 0), (800, 600))
ball = Ball()
score_board = ScoreBoard()

screen.update()


screen.listen()

# paddle one
screen.onkeypress(right_paddle.moveup, "Up")
screen.onkeypress(right_paddle.movedown, "Down")

# paddle two
screen.onkeypress(left_paddle.moveup, "w")
screen.onkeypress(left_paddle.movedown, "s")

game_state = True

while game_state:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340) or (ball.distance(left_paddle) < 50 and ball.xcor() < -340):
        ball.paddle_bounce()
    if ball.xcor() > 400 or ball.xcor() < -400:
        score_board.update_score("left" if ball.xcor() < -400 else "right")
        ball.reset()


screen.mainloop()
