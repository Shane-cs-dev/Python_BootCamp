from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to SNAKE GAME!")
screen.tracer(0)
#Pyton tuple
starting_position = [(0, 0), (-20, 0), (-40, 0)]
turtle_list = []


for segment in starting_position:
    new_tur = Turtle(shape="square")
    new_tur.color("white")
    new_tur.penup()
    new_tur.goto(segment)
    turtle_list.append(new_tur)


def turn_left():
    turtle_list[0].left(90)
def turn_right():
    turtle_list[0].left(-90)


screen.listen()
screen.onkey(key="up", fun=turn_left)
screen.onkey(key="down", fun=turn_right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(turtle_list)-1, 0, -1):
        new_x = turtle_list[seg_num - 1].xcor()
        new_y = turtle_list[seg_num - 1].ycor()
        turtle_list[seg_num].goto(new_x, new_y)
    turtle_list[0].forward(20)




















screen.exitonclick()