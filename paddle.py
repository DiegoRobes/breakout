from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.fillcolor("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(position)
        self.showturtle()