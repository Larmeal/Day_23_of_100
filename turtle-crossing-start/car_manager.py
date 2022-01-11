from turtle import Turtle, Screen, position
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_car = []
        self.speed = STARTING_MOVE_DISTANCE

    def random_position(self):
        self.car_position = []
        for i in range(-200, 260, 20):
            self.car_position.append(i)

    def genarate(self):
        probability_car = random.randint(0, 6)
        if probability_car == 1:
            taxi = Turtle()
            taxi.shape("square")
            taxi.color(random.choice(COLORS))
            taxi.shapesize(stretch_wid=1, stretch_len=2)
            taxi.setheading(180)
            taxi.penup()
            self.random_position()
            taxi.goto(300, random.choice(self.car_position))
            self.all_car.append(taxi)
        
    def move(self):
        for i in self.all_car:
            i.forward(self.speed)

    def increment(self):
        self.speed += MOVE_INCREMENT
