from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.speed = MOVE_INCREMENT 

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle('square')
            car.penup()
            car.shapesize(stretch_len=4, stretch_wid=1)
            car.color(random.choice(COLORS)) 
            y_cor = random.randint(-280 , 280)
            car.goto(300, y_cor)


            self.all_cars.append(car)


    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT




    
       

    




