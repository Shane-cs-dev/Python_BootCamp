from turtle import Turtle
ALIGN = "center"
FONT = ("GeeksForGeeks", 25, "italic")
POSITION = [(0, 260)]
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(POSITION[0])
        self.write(arg=f"{self.score_1} : {self.score_2}", move=False, align=ALIGN, font=FONT)

    def scoring_1(self):
        self.score_1 += 1
        self.clear()
        self.write(arg=f"{self.score_1} : {self.score_2}", move=False, align=ALIGN, font=FONT)
    def scoring_2(self):
        self.score_2 += 1
        self.clear()
        self.write(arg=f"{self.score_1} : {self.score_2}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!", move=False, align=ALIGN, font=FONT)


















