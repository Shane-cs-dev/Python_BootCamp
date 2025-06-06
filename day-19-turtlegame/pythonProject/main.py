from turtle import *

tur = Turtle()
screen = Screen()





def move_forward():
    tur.forward(50)
def move_backward():
    tur.forward(-50)
def counter_clockwise():
    tur.circle(120, -20)
def clockwise():
    tur.circle(120, 20)
def clear_drawing():
    tur.clear()
def reset_location():
    tur.home()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="z", fun=reset_location)














screen.exitonclick()