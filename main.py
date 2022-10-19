from turtle import *
import turtle
from ball import Ball
from paddle import Paddle
from score import Score
from blocks import Blocks
import time


def main():
    screen = Screen()
    screen.clear()
    screen.bgcolor("black")
    screen.title("Breakout")
    screen.setup(width=1350, height=600)
    screen.listen()
    screen.tracer(0)

    paddle = Paddle((0, -280))
    screen.update()
    time.sleep(.5)

    ball = Ball()
    screen.update()
    time.sleep(.5)

    score = Score()
    screen.update()
    time.sleep(.5)

    blocks = Blocks()
    blocks.rows()

    def paddle_position(event):
        new_x = event.x - 675
        paddle.goto(x=new_x, y=-280)

    ws = turtle.getcanvas()
    ws.bind('<Motion>', paddle_position)

    game_on = True

    while game_on:
        screen.update()
        time.sleep(.03)
        ball.move()

        if ball.ycor() > 280:  # bounce on the top
            ball.bounce_up()
            score.increase_score()

        if ball.xcor() > 650 or ball.xcor() < -660:  # bounce to the sides
            ball.bounce_side()
            score.increase_score()

        if ball.distance(paddle) < 25:  # bounce on the paddle
            ball.bounce_up()
            score.increase_score()

        for i in blocks.all_bricks:
            if i.distance(ball) < 25:
                i.hideturtle()
                blocks.all_bricks.remove(i)
                score.increase_score()
                ball.bounce_up()
                if len(blocks.all_bricks) == 0:
                    blocks.rows()
                    score.lives += 1
                    score.p_1 *= 2

        if ball.ycor() < -310:
            ball.miss()
            score.decrease_lives()
            ball.lives -= 1
            if score.lives == 0:
                game_on = False

    score.game_over()
    screen.onkey(main, "space")
    screen.onkey(quit, "BackSpace")
    screen.exitonclick()


main()
