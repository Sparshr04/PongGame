from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.pu()
        # Just realised that in the Dot method the turtle is moving but the dot dosen't move
        # self.hideturtle()
        # self.dot(22, 'white')
        self.shape('circle')
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1

    
    

        

