from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color('White')
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score}",align="center",font=('Arial',24,'normal'))
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}",align="center",font=('Arial',24,'normal'))


    def game_over(self): 
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=('Arial',24,'normal'))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

   