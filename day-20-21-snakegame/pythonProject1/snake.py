from turtle import *
import random

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
COLOR_LIST =[(143, 153, 198), (194, 149, 187), (229, 197, 219), (203, 205, 231), (65, 88, 154), (101, 112, 181), (178, 180, 222), (201, 225, 205), (221, 172, 202), (225, 221, 192), (30, 49, 135), (8, 29, 75), (148, 185, 168), (212, 162, 124), (172, 205, 181), (203, 209, 147), (61, 115, 85), (161, 105, 153), (11, 48, 26), (234, 171, 162), (131, 76, 132), (164, 203, 210), (31, 85, 51), (94, 149, 121), (66, 12, 56), (90, 143, 155), (103, 35, 94), (116, 116, 40), (161, 152, 47), (23, 79, 94), (69, 96, 9), (203, 99, 82), (36, 44, 12), (163, 28, 16)]
HELL = (900, 900)
class Snake:
    def __init__(self):
        self.list = []
        self.create_snake()
        self.head = self.list[0]


    def create_snake(self):
        for segment in STARTING_POSITION:
            self.add_body(segment)

    def add_body(self, location):
        new_tur = Turtle(shape="square")
        random_color = random.choice(COLOR_LIST)
        new_tur.color(random_color)
        new_tur.penup()
        new_tur.goto(location)
        self.list.append(new_tur)

    def extend(self):
        self.add_body(self.list[-1].position())

    def move(self):
        #Last body follow the previous one
        for seg_num in range(len(self.list) - 1, 0, -1):
            new_x = self.list[seg_num - 1].xcor()
            new_y = self.list[seg_num - 1].ycor()
            self.list[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset_snake(self):
        for remain_snake in self.list:
            remain_snake.goto(HELL)
        self.list.clear()
        self.create_snake()
        self.head = self.list[0]