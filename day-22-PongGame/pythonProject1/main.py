from turtle import Screen, Turtle

MOVE_DISTANCE = 50
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong game")
screen.tracer(0)
###Pad creation###
new_pad1 = Turtle()
new_pad1.color("white")
new_pad1.penup()
new_pad1.shape("square")
new_pad1.shapesize(stretch_wid=4, stretch_len=1)
new_pad1.goto(x=370, y=0)

new_pad2 = Turtle()
new_pad2.color("white")
new_pad2.penup()
new_pad2.shape("square")
new_pad2.shapesize(stretch_wid=4, stretch_len=1)
new_pad2.goto(x=-370, y=0)

###Define moving###
def move_up1():
    new_y_1 = new_pad1.ycor()
    new_x_1 = new_pad1.xcor()
    new_pad1.goto(new_x_1, new_y_1 + MOVE_DISTANCE)
def move_down1():
    new_y_1 = new_pad1.ycor()
    new_x_1 = new_pad1.xcor()
    new_pad1.goto(new_x_1, new_y_1 - MOVE_DISTANCE)
def move_up2():
    new_y_2 = new_pad2.ycor()
    new_x_2 = new_pad2.xcor()
    new_pad2.goto(new_x_2, new_y_2 + MOVE_DISTANCE)
def move_down2():
    new_y_2 = new_pad2.ycor()
    new_x_2 = new_pad2.xcor()
    new_pad2.goto(new_x_2, new_y_2 - MOVE_DISTANCE)

##Control the screen###
screen.listen()
screen.onkey(move_up1, "Up")
screen.onkey(move_down1, "Down")
screen.onkey(move_up2, "w")
screen.onkey(move_down2, "s")


game_on = True
while game_on:
    screen.update()




screen.exitonclick()