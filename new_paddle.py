from turtle import Turtle

class Create(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(4.5, 1)
        self.goto(position,0)

    def upL(self):
        self.goto(self.xcor(),self.ycor()+20)

    def upR(self):
        self.goto(self.xcor(),self.ycor()+20)

    def downL(self):
        self.goto(self.xcor(),self.ycor()-20)

    def downR(self):
        self.goto(self.xcor(),self.ycor()-20)