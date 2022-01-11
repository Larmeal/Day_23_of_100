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

    # เป็น method ที่สามารถมาเพื่อเป็นตัวกลางในการอัพเดทข้อมูล เพื่อความสะดวกในการดึงไปใช้ต่อได้เลย
    def score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level {self.score_board}", align="center", font=("Courier", 24, "normal"))

    # เป็น method ที่เกี่ยวเนื่องกับ attribute score() แม้ว่าจริง ๆ แล้วนั้นเป็น method ก็ตาม เมื่อมีการผ่านกระบวนการ method add_score แล้วจำเป็น้ต้อง update ข้อมูลโดยทำผ่าน method score ที่กำหนดขึ้นมาเป็นตัวกลาง 
    def add_score(self):
        self.score_board += 1
        self.score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))