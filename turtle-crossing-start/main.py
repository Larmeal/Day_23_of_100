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
    # ต้องการจะสร้าง รถ หลาย ๆ คันซึ่งเป็น instance ที่แตกต่างกัน หากอยู่ใน loop อยู่แล้วก็จะสร้าง instance หลาย ๆ อันขึ้นมาได้เลยไม่ต้องกำหนด loop เพื่อสร้างอีกที
    car.genarate()
    car.move()
    scoreboard.score()

    if play.ycor() >= 280:
        scoreboard.add_score()
        car.increment()
        play.finish()
    
    # ที่ต้องวนลูปแบบนี้เพราะว่า ต้องการจะ check กับรถทุกคันว่าตัว player ได้เข้าใกล้กับตัวรถ รึป่าว
    for i in car.all_car:
        if i.distance(play) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()