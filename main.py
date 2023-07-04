from turtle import Turtle,Screen
from new_paddle import Create
from ball import Ball
from score import scoreCount
import time
screen = Screen()
screen.title("Pong Game")

screen.setup(800,600)
screen.bgcolor("black")
# screen.tracer(0)
paddle_left = Create(350)
paddle_right =  Create(-350)
# screen.update()
new_ball = Ball()

screen.listen()
screen.onkeypress(paddle_left.upL,"l")
screen.onkeypress(paddle_right.upR,"w")
screen.onkeypress(paddle_left.downL,"k")
screen.onkeypress(paddle_right.downR,"e")
scoreL = scoreCount()
scoreR = scoreCount()
flage = True
minus = 0.1
while flage:
    time.sleep(minus)
    screen.update()
    new_ball.ball_move()

    if new_ball.ycor() > 280 or new_ball.ycor() < -280:
        new_ball.bouncing()

    if new_ball.distance(paddle_left) < 50 and new_ball.xcor() < 350 or new_ball.distance(paddle_right) <50 and new_ball.xcor() < 350:
        new_ball.x_bouncing()
        minus *= 0.9

    if new_ball.xcor() > 380:
        scoreL.scoreL()
        screen.tracer(0)
        new_ball.home()
        screen.update()
        new_ball.x_bouncing()
        minus = 0.1

    if new_ball.xcor() < -380:
        scoreR.scoreR()
        screen.tracer(0)
        new_ball.home()
        screen.update()
        new_ball.x_bouncing()
        minus = 0.1

screen.exitonclick()