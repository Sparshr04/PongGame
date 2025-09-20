from turtle import Screen, Turtle

# x_pos = 350
# y_pos = 0

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

#no need for speeding up the turtule when we can use the Tracer method
#here '0' in the parenthesis means that to turn the animation off.
screen.tracer(0) 

paddle = Turtle()
paddle.color("white")
paddle.shape("square")
# paddle.speed("fastest")
paddle.pu()
paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.goto(x_pos, y_pos)
paddle.goto(350, 0)



def paddle_up():
    # global y_pos
    # y_pos += 20
    # paddle.goto(x_pos, y_pos)
    new_y_cor = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y_cor)

def paddle_down():
    # global y_pos
    # y_pos -= 20
    # paddle.goto(x_pos, y_pos)
    new_y_cor = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y_cor)

screen.listen()
screen.onkey(fun=paddle_up, key='Up')
screen.onkey(fun=paddle_down, key='Down')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
