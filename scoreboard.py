from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)

        self.score1 = 0
        self.score2 = 0
        self.refresh()

    def add_point(self, player):
        if player == 1:
            self.score2 += 1
        elif player == 2:
            self.score1 += 1

    def refresh(self):
        self.clear()
        self.write(arg=f"{self.score1}    {self.score2}", align="center", font=("Menlo", 20, "normal"))
