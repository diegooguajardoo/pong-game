from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("slowest")
        self.shapesize(1)
        self.fillcolor("white")
        self.penup()
        self.ball_speed = .06
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.speedup_ball()

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = .06

    def speedup_ball(self):
        self.ball_speed *= 0.9
