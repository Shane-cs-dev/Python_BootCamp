import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from trial import Trial

###Control screen###
screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
###Create Car###
car = CarManager()
###iport Trial###
trial = Trial()
###Scoreboard###
level = Scoreboard()
###Introduce Player###
player = Player()
screen.update()
###Screen function control###
screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)
screen.onkey(key="Left", fun=player.move_left)
screen.onkey(key="Right", fun=player.move_right)

###GAME TIME###
game_is_on = True
while game_is_on:
    car.r_car()
    car.l_car()
    car.all_car_move()
    screen.update()
    time.sleep(level.speed)

    ###Detection of collision of car###
    for cars in car.car_list:
        if player.distance(cars) <15:
            game_is_on = False
            level.game_over()

    ###Detection of level up###
    if player.ycor() > 250:
        level.level_up()
        player.reset_player()
        car.level_up()











screen.exitonclick()