from turtle import Turtle
import random
COLOR = ["white", "blue", "yellow", "green", "black"]
CHANGE = True
MOVE_DISTANCE = 15
MOVEMENT = [15, -15]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = random.choice(MOVEMENT)
        self.y_move = random.choice(MOVEMENT)
        self.move_speed = 0.08
    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(x=0, y=0)

    def change_color(self):
        self.color(random.choice(COLOR))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1
        self.change_speed()
    def bounce_pad(self):
        self.x_move *= -1
        self.change_speed()

    def reset(self):
        self.clear()
        self.move_speed = 0.1
        self.create_ball()
        self.x_move *= -1

    def change_speed(self):
        self.move_speed *= 0.95
