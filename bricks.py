from turtle import Turtle

# class Bricks(Turtle):
#     def __init__(self, col, posi):
#         super().__init__()
#         self.penup()
#         self.color(col)
#         self.shape('square')
#         self.shapesize(stretch_wid=1, stretch_len = 3)
#         self.goto(posi)


class Bricks():
    def __init__(self):
        self.brick_list = []
        for y in range(300, 100, -25):
            if y <= 300 and y > 250:
                col = 'red'
            elif y <= 250 and y > 200:
                col = 'orange'
            elif y <= 200 and y > 150:
                col = 'green'
            elif y <= 150 and y > 100:
                col = 'yellow'
            for x in range(-365, 370, 65):
                self.brick = Turtle()
                self.brick.penup()
                self.brick.shape('square')
                self.brick.shapesize(stretch_wid=1, stretch_len=3)
                self.brick.color(col)
                self.brick.goto((x,y))
                self.brick_list.append(self.brick)

    def update_brick(self, hit_loc):
        for n in self.brick_list:
            if n.pos() == hit_loc:
                n.goto(-1000,1000)







