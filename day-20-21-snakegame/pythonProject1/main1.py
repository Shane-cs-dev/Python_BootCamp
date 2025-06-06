from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

##########################################
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to SNAKE GAME!")
screen.tracer(0)
screen.colormode(255)

#Class Snake, Food, Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Control screen
screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 20:
        print("yummy")
        food.gen_food()
        scoreboard.increase_score()
        scoreboard.update_score()
        snake.extend()

    #Detect collision with wall.
    if snake.head.xcor() > 310 or snake.head.ycor() > 310 or snake.head.xcor() < -310 or snake.head.ycor() < -310:
        scoreboard.reset()
        snake.reset_snake()
    #Detect collision with snake body
    for part_of_body in snake.list[1:]:
        if snake.head.distance(part_of_body) < 15:
            scoreboard.reset()
            snake.reset_snake()

















screen.exitonclick()