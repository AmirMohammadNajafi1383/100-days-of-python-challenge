import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard= Scoreboard()

# Associate the 'Up' key with the player's Up() method
screen.onkey(player.go_up, 'Up')
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    cars = car_manager.all_cars
    
    for car in cars:
        if player.distance_to(car) < 20:
            scoreboard.game_over()
            game_is_on=False

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
