from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball  # Make sure you have the Ball class defined in a 'ball.py' file.
import time
from scoreboard import Scoreboard
wn = Screen()
wn.title('pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball() # Make sure the Ball class is defined and imported correctly.
scoreboard = Scoreboard()


wn.listen()
wn.onkey(r_paddle.go_up, 'Up')
wn.onkey(r_paddle.go_down, 'Down')
wn.onkey(l_paddle.go_up, 'w')
wn.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    wn.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (
        (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or
        (ball.distance(l_paddle) < 50 and ball.xcor() < -320)
    ):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
# The conditions above should be inside the game loop to work correctly.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




wn.exitonclick()
