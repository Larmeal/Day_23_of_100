import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("THE GAME")
screen.tracer(0)
screen.listen()

play = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(play.up, "Up")
screen.onkey(play.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.genarate()
    car.move()
    scoreboard.score()

    if play.ycor() >= 280:
        scoreboard.add_score()
        car.increment()
        play.finish()

    for i in car.all_car:
        if i.distance(play) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()