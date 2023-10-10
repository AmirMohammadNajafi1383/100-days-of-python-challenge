from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.goto(-230, 260)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Arial", 16, "normal"))

    def increase_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
