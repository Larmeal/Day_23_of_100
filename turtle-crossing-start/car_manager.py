from turtle import Turtle, Screen, position
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    # ในส่วนของ attribute กำหนดเฉพาะแค่ส่วนของตัวแปรที่จำเป็นต้องใช้ใน method ก็พอ ถ้าตัวแปรไหนมีความเฉพาะใน method นั้นก็กำหนดใช้ใน method นั้น ๆ เลย  
    def __init__(self):
        self.all_car = []
        self.speed = STARTING_MOVE_DISTANCE
        self.car_position = []

    # method นี้ต้องการจำสุ่มตำแหน่งที่รถจะเกิดในแนวแกน y ว่าควรจะเกิดตอนไหนโดยมีระยะห่าง 20 pixels ในการเกิด
    def random_position(self):
        for i in range(-200, 260, 20):
            self.car_position.append(i)

    # method ที่ genarate ตัวรถออกมา
    def genarate(self):
        # ที่กำหนดความน่าจะเป็นเพราะว่า ไม่ต้องการให้สุ่มรถออกมามากจนเกินไป
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
            # เพิ่มจำนวนรถที่เกิดขึ้นเข้าไปใน all_car list เพื่อที่จะนำ attribute นี้ไปดำเนินการใน method อื่น ๆ
            self.all_car.append(taxi)
    
    # เนื่องจาก attribute ของเราเป็นข้อมูลแบบ list ถ้าต้องการให้ข้อมูลทั้งหมดเข้ากระบวนการ method เราควรกำหนด loop ขึ้นมาเพื่อดึงข้อมูลทีละตัวเข้าสู่ method
    def move(self):
        for i in self.all_car:
            i.forward(self.speed)

    # ดึง attribute มาปรับปรุงโดยการ เปลี่ยนแปลงค่าให้เพิ่มขึ้น เพื่อจะนำเอา method นี้ไปใช้ใน main.py
    def increment(self):
        self.speed += MOVE_INCREMENT
