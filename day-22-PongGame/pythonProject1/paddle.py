from turtle import Turtle


MOVE_DISTANCE = 40

class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.goto(location)

    def move_up(self):
        new_x_1 = self.xcor()
        new_y_1 = self.ycor()
        self.goto(new_x_1, new_y_1 + MOVE_DISTANCE)

    def move_down(self):
        new_x_1 = self.xcor()
        new_y_1 = self.ycor()
        self.goto(new_x_1, new_y_1 - MOVE_DISTANCE)

