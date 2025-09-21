from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates , shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.shape("square")
        self.pu()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.coordinates = coordinates
        self.goto(coordinates)


    def go_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor(), new_y_cor)

    def go_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), new_y_cor)
