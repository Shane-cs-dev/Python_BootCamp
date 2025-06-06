from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50
MOVE_DISTANCE_2 = 30
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.shapesize(1.5)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)
    def move_down(self):
        self.forward(-MOVE_DISTANCE)
    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE_2
        self.goto(new_x, self.ycor())
    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE_2
        self.goto(new_x, self.ycor())
    def reset_player(self):
        self.clear()
        self.goto(STARTING_POSITION)