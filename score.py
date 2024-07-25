from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.chances = 3
        self.update()


    def update(self):
        self.clear()
        self.goto(330, 400)
        self.write(f"Score: {self.score}", align='center', font=("Counier", 20, 'normal'))
        self.goto(-310, 400)
        self.write(f"Chances Left: {self.chances}", align='center', font=("Counier", 20, 'normal'))

    def add_score(self, point):
        self.score += point

    def update_chances(self):
        self.chances -= 1
