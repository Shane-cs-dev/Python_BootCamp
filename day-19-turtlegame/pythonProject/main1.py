from turtle import *
import random
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -50, 0, 50, 100, 150]
screen = Screen()
screen.setup(width=800, height=500)
user_bet = screen.textinput(title="Make a guess", prompt="Which turtle will win the raise? Pick a color: ")
all_turtle = []
for turtle_index in range(0, 6):
    tur = Turtle(shape="turtle")
    tur.shapesize(2)
    tur.penup()
    tur.color(colors[turtle_index])
    tur.goto(x=-380, y=y_position[turtle_index])
    all_turtle.append(tur)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 370:
            winning_color = turtle.pencolor()
            print(winning_color)
            if winning_color == user_bet:
                print("You won!")
                is_race_on = False
            else:
                print(f"You lose..... The {winning_color} color win the game!")
                is_race_on = False
        random_distance = random.randint(5, 25)
        turtle.forward(random_distance)










screen.exitonclick()