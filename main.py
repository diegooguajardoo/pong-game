import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.y_bounce()

    # Detect ball bounce with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        ball.x_bounce()
        scoreboard.add_point(player=2)
        scoreboard.refresh()

    if ball.xcor() < -380:
        ball.reset_position()
        ball.x_bounce()
        scoreboard.add_point(player=1)
        scoreboard.refresh()

screen.exitonclick()
