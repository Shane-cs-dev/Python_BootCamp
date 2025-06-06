from turtle import Turtle
POSITION = (-390, 260)
FONT = ("GeeksForGeeks", 18, "italic")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(POSITION)
        self.write(arg=f"LEVEL:{self.level}", move= False, align= "left", font=FONT)
        self.speed = 0.1

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(arg=f"LEVEL: {self.level}", move=False, align="left", font=FONT)
        self.speed *= 0.9
    def game_over(self):
        self.penup()
        self.hideturtle()
        self.color("red")
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)
