from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score
from center_line import Dash_line
#################################
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong game")
screen.tracer(0)
###Pad creation###
r_location = (370, 0)
l_location = (-370, 0)
r_pad = Paddle(r_location)
l_pad = Paddle(l_location)
###Ball creation###
ball = Ball()
###Scoreboard creation###
score = Score()
###Dash line###
dash = Dash_line()
#Control the screen###
screen.listen()
screen.onkey(r_pad.move_up, "Up")
screen.onkey(r_pad.move_down, "Down")
screen.onkey(l_pad.move_up, "w")
screen.onkey(l_pad.move_down, "s")



###operaion###
game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if score.score_2 > 3 or score.score_1 > 3:
        ball.change_color()

    ###GAME OVER###
    if score.score_2 == 6 or score.score_1 == 6:
        game_on = False
        score.game_over()

    ###Detect collision with wall###
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    ###Detect collision with wall###
    if ball.distance(r_pad) < 45 and ball.xcor() > 320 or ball.distance(l_pad) < 45 and ball.xcor() < -320:
        ball.bounce_pad()

    ###Detect ball out od boundary###
    if ball.xcor() > 390:
        score.scoring_1()
        ball.reset()
    if ball.xcor() < -390:
        score.scoring_2()
        ball.reset()

screen.exitonclick()