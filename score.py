from turtle import Turtle

class scoreCount(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.hideturtle()
        self.color("white")

    def scoreL(self):
        self.clear()
        self.score2 += 1
        self.penup()
        self.goto(-40,270)
        self.write(f"{self.score2}", align= "center", font=("Arial", 20, "bold"))


    def scoreR(self):
        self.clear()
        self.score1 += 1
        self.penup()
        self.goto(40,270)
        self.write(f"{self.score1}", align= "center", font=("Arial", 20, "bold"))