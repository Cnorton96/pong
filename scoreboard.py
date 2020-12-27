from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("arial", 80, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def game_finished(self):
        message = "Game finished! A player has reached 7 points!"
        self.goto(0,0)
        self.write(message, align="center", font=("arial", 20, "normal"))
