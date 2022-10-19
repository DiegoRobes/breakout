from turtle import Turtle


class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.all_bricks = []
        self.brick = None

    def rows(self):
        y = 250
        for j in range(6):
            x = -651
            y -= 20.5
            for i in range(33):
                brick = Turtle("square")
                brick.color("black")
                brick.fillcolor("white")
                brick.penup()
                brick.turtlesize(stretch_wid=1, stretch_len=2)
                brick.goto(x, y)
                self.all_bricks.append(brick)
                x += 40.5




