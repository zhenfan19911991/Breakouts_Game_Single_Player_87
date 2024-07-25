from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, posi):
        super().__init__()
        self.penup()
        self.color('blue')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len = 3)
        self.goto(posi)

    def moveleft(self, pl):
        if self.xcor() < 385-pl:
            self.forward(20)

    def moveright(self, pl):
        if self.xcor() > -(410-pl):
            self.backward(20)

