from turtle import Turtle
import turtle

STARTING_POSITION = [0, -280]
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.move = MOVE_DISTANCE
        self.setheading(90)

    def up(self):
        self.forward(self.move)

    def down(self):
        if self.ycor() > -280:
            self.back(self.move)
        else:
            pass

    def finish(self):
        self.goto(STARTING_POSITION)
        
    