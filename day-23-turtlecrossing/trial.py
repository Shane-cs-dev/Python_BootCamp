from turtle import Turtle

POSITION = (-400, 200)
class Trial(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.color("yellow")
        self.pencolor("black")
        self.setheading(0)
        self.pensize(5)
        self.draw_trial()

    def draw_single_trial(self):
        for steps in range(12):
            self.pendown()
            self.forward(40)
            self.penup()
            self.forward(30)
    def turn(self):
        self.setheading(270)
        self.forward(50)
        self.setheading(180)
        self.forward(840)
        self.setheading(0)
    def draw_trial(self):
        for time in range(9):
            self.draw_single_trial()
            self.turn()

