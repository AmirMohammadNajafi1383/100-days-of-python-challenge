from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color('White')
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score},High_Score:{self.high_score}",align="center",font=('Arial',24,'normal'))
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score},High_Score:{self.high_score}",align="center",font=('Arial',24,'normal'))



    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
    
    def restart_high_score(self):
        if self.score > self.high_score:
            self.score = self.high_score
        with open('data.txt',mode='w') as data:
            data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def increase_high_score(self):
        self.high_score+=2 
        self.update_scoreboard()


    