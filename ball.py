from turtle import Turtle
from collections import Counter


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.color('blue')
        self.shape('circle')
        self.goto((0, -370))
        self.move_speed = 0.08
        self.setheading(45)
        self.hit_brick = 0
        self.hit_orange_brick = 0
        self.hit_red_brick = 0
        self.hit_brick_loc = None
        self.points_add = 0
        self.paddle_length = 43
        self.br_color_list = []



    def move_ball(self, br_l, pa):

        self.points_add = 0
        self.forward(10)
        for br in br_l[::-1]:
            if self.distance(-395,self.ycor()) <20 or self.distance(395,self.ycor()) <25:
                self.setheading(540 - self.heading())
                break

            elif self.ycor() > 435:
                self.setheading(360 - self.heading())
                pa.shapesize(stretch_wid=1, stretch_len=1.5)
                self.paddle_length = 23
                break

            elif self.ycor() < -373 and -self.paddle_length <= self.xcor() - pa.xcor() <= self.paddle_length:
                self.setheading(360 - self.heading())
                break

            elif self.distance(br.pos()) <40 and -22 <= self.ycor()-br.ycor()<=22 and -36<= self.xcor()-br.xcor()<=36:
                self.setheading(360 - self.heading())
                self.hit_brick += 1

                self.hit_brick_loc = br.pos()

                self.br_color_list.append(br.pencolor())
                orange_fre = Counter(self.br_color_list)['yellow']
                red_fre = Counter(self.br_color_list)['red']

                if br.pencolor() == 'orange':
                    self.points_add = 5
                elif br.pencolor() == 'red':
                    self.points_add = 7
                elif br.pencolor() == 'green':
                    self.points_add = 3
                elif br.pencolor() == 'yellow':
                    self.points_add = 1

                if (self.hit_brick == 4 or self.hit_brick == 12
                        or (orange_fre == 1 and self.br_color_list.index('yellow')+1 == self.hit_brick)
                        or (red_fre == 1 and self.br_color_list.index('red')+1 == self.hit_brick)):
                    self.move_speed = self.move_speed * 0.8

                break




