from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

screen.tracer(0) 

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()



screen.listen()
screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collusion with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collusion with the padddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >  320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when Right Paddle misses
    if ball.xcor() > 360:
        ball.reset_pos()
        score.l_point()

    #detect when left paddle misses
    if ball.xcor() < -360:
        ball.reset_pos()
        score.r_point()


screen.exitonclick()
