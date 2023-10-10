from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player:
    def __init__(self):
        self.create_player()
        self.go_to_start()

    def create_player(self):
        self.turtle = Turtle()
        self.turtle.shape('turtle')
        self.turtle.color('green')
        self.turtle.penup()
        
        self.turtle.setheading(90)

    def go_to_start(self):
        self.turtle.goto(STARTING_POSITION)

   
    def go_up(self):
        self.turtle.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.turtle.ycor() > FINISH_LINE_Y
      
    def distance_to(self, other_turtle):
        return self.turtle.distance(other_turtle)