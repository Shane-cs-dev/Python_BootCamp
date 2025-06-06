from turtle import Turtle

POSITION = [(0, -280), (0, -240), (0, -200), (0, -160), (0, -120),(0, -80), (0, -40), (0, 0), (0, 40), (0, 80), (0, 120), (0, 160), (0, 200), (0, 240)]

class Dash_line:
    def __init__(self):
        self.list = []
        self.create_dash()

    def create_dash(self):
        for count in POSITION:
            dash = Turtle()
            dash.color("white")
            dash.penup()
            dash.shape("square")
            dash.shapesize(stretch_wid=0.7, stretch_len=0.2)
            dash.goto(count)
            self.list.append(dash)
