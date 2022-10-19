from turtle import Turtle
import time

FONT_SCORE = "Times New Roman", 10, "bold"
GAME_OVER = "Times New Roman", 25, "bold"
SCORE_GAME_OVER = "Times New Roman", 15, "bold"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 5
        self.p_1 = 0
        self.hideturtle()
        self.penup()
        self.color("white")

        self.goto(x=645, y=285)
        self.write(arg="SCORE", align="right", font=FONT_SCORE)
        time.sleep(.5)
        self.goto(x=645, y=265)
        self.write(arg=self.p_1, align="right", font=FONT_SCORE)
        time.sleep(.5)

        self.goto(x=-645, y=285)
        self.write(arg="LIVES", align="left", font=FONT_SCORE)
        time.sleep(.5)
        self.goto(x=-645, y=265)
        self.write(arg=self.lives, align="left", font=FONT_SCORE)

    def write_score(self):
        self.goto(x=645, y=285)
        self.write(arg="SCORE", align="right", font=FONT_SCORE)
        self.goto(x=645, y=265)
        self.write(arg=self.p_1, align="right", font=FONT_SCORE)

    def lives_write(self):
        self.goto(x=-645, y=285)
        self.write(arg="LIVES", align="left", font=FONT_SCORE)
        self.goto(x=-645, y=265)
        self.write(arg=self.lives, align="left", font=FONT_SCORE)

    def increase_score(self):
        self.p_1 += 1
        self.clear()
        self.write_score()
        self.lives_write()

    def decrease_lives(self):
        self.lives -= 1
        self.clear()
        self.write_score()
        self.lives_write()
    
    def game_over(self):
        self.clear()
        self.goto(x=0, y=50)
        self.write(arg="GAME OVER", align="center", font=GAME_OVER)
        self.goto(x=0, y=20)
        self.write(arg=f"SCORE: {self.p_1}", align="center", font=SCORE_GAME_OVER)
        self.goto(x=0, y=0)
        self.write(arg=f"Restart: Spacer", align="center", font=FONT_SCORE)
        self.goto(x=0, y=-20)
        self.write(arg=f"Close: Backspace", align="center", font=FONT_SCORE)
