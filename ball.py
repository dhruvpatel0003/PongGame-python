from turtle import Turtle

class Ball(Turtle):

     def __init__(self):
         super().__init__()
         self.shape("circle")
         self.color("white")
         self.penup()
         self.x_cor = 10
         self.y_cor = 10
         # self.ball_move()

     def ball_move(self):
         self.goto(self.xcor()+self.x_cor,self.ycor()+self.y_cor)

     def bouncing(self):
         self.y_cor *= -1


     def x_bouncing(self):
         self.x_cor *= -1