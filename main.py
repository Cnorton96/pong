from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong developed by Christian Norton")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle((350, 0))
right_paddle.color("green")
left_paddle = Paddle((-350, 0))
left_paddle.color("green")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detecting when the ball hits the wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detecting collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_collision()

    # Detecting collision with the left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_collision()

    # Detect when the right paddle misses ball.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect when the left paddle misses the ball.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

    if scoreboard.right_score == 7 or scoreboard.left_score == 7:
        scoreboard.game_finished()
        is_on = False


screen.exitonclick()
