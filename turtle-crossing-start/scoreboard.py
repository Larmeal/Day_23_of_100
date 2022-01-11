from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score_board = 1
        self.score()

    def score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level {self.score_board}", align="center", font=("Courier", 24, "normal"))

    def add_score(self):
        self.score_board += 1
        self.score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))