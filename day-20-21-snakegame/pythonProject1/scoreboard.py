from turtle import Turtle
SCOREBOARD_POSITION = [(-15, 270)]
ALIGN = "center"
FONT = ("GeeksForGeeks", 20, "italic")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.pencolor("white")
        self.goto(SCOREBOARD_POSITION[0])
        self.write(arg=f"Highest score:{self.highscore} Score:{self.score}", move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.write(arg=f"Highest score:{self.highscore} Score:{self.score}", move=False, align=ALIGN, font=FONT)


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER!", move=False, align=ALIGN, font=FONT)