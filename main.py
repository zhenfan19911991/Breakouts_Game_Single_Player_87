from turtle import Turtle, Screen, TurtleScreen
import time
from bricks import Bricks
from paddle import Paddle
from ball import Ball
from score import Score
from functools import partial



screen = Screen()
TurtleScreen._RUNNING=True
screen.bgcolor('black')
screen.setup(width=790, height = 900)
screen.title('Breakouts')
screen.tracer(0)

bricks = Bricks()
ball = Ball()

paddle = Paddle((0, -400))

screen.listen()

screen.onkey(fun = partial(paddle.moveleft,ball.paddle_length) , key = "Right" )
screen.onkey(fun = partial(paddle.moveright, ball.paddle_length), key = "Left" )


scoreboard = Score()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball(bricks.brick_list, paddle)
    bricks.update_brick(ball.hit_brick_loc)
    scoreboard.add_score(ball.points_add)
    scoreboard.update()
    if ball.ycor() < -390:
        scoreboard.update_chances()
        if scoreboard.chances == 0:
            game_is_on = False
        scoreboard.update()
        ball.goto((0,-370))
        ball.setheading(45)
        paddle.goto((0, -400))

screen_brick = 0
for n in bricks.brick_list:
    if n.pos() != (-1000, 1000):
        screen_brick += 1
print(screen_brick)


screen.clear()
text = Turtle()
text.color('black')
text.penup()
text.hideturtle()
text.goto(0,0)

if scoreboard.chances == 0:
    text.write(f"Game Over. Your final Score is {scoreboard.score}.", align='center', font=("Counier", 30, 'normal'))
elif screen_brick == 0:
    text.write(f"Congrats, You have hit all bricks. Your final Score is {scoreboard.score}.", align='center', font=("Counier", 30, 'normal'))


screen.exitonclick()
