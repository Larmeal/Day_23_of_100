from turtle import Turtle
import turtle

STARTING_POSITION = [0, -280]
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# เหตุผลที่ทำการดึง inheritance ก็เพราะว่าต้องการดึง attribute ของ class ก่อนหน้ามาใช้เลย ไม่ได้จะสร้างอะไร แค่เอามาแล้วปรังปรุงนิดหน่อย
class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        # เนื่องจากเราทำ inheritance class ขึ้นมาเลยสามารถกำหนด attribute เพิ่มเติมไปได้เลย
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
        
    