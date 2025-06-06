from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LOT1 = [-175, -75, 25, 125]
LOT2 = [-125, -25, 75, 175]

class CarManager:
    def __init__(self):
        self.car_list = []
        self.difficulty = 10

    def r_car(self):
        number = random.randint(0, self.difficulty)
        if number == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=2, stretch_len=3)
            new_car.goto(400, random.choice(LOT1))
            self.car_list.append(new_car)

    def l_car(self):
        number = random.randint(0, self.difficulty)
        if number == 1:
                new_car = Turtle(shape="square")
                new_car.setheading(0)
                new_car.penup()
                new_car.color(random.choice(COLORS))
                new_car.shapesize(stretch_wid=2, stretch_len=3)
                new_car.goto(-400, random.choice(LOT2))
                self.car_list.append(new_car)

    def all_car_move(self):
        for car in self.car_list:
            car.forward(MOVE_INCREMENT)

    def level_up(self):
        self.difficulty -= 1