from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.shape("circle")
        self.speed("slow")
        self.color("black")
        self.fillcolor("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(x=0, y=-260)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_up(self):
        self.y_move *= -1

    def bounce_side(self):
        self.y_move *= +1
        self.x_move *= -1

    def hit_paddle(self):
        self.x_move *= -1

    def miss(self):
        time.sleep(2)
        if self.lives == 0:
            quit()
        else:
            self.__init__()
