import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.speed("fast")
        self.gen_food()

    def gen_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)