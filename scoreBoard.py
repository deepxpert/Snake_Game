from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.game_score = 0        
        with open("day20-21(snake_game)\highscore.txt") as f:
            self.high_score = int(f.read())

        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()
       

    def update_scoreboard(self):
         self.clear()
         self.write(f'SCORE : {self.game_score}    HIGH SCORE : {self.high_score}',align="center", font = ("bold",15,"normal"))


    def reset(self):
        if self.game_score > self.high_score:
            self.high_score = self.game_score
            with open("day20-21(snake_game)\highscore.txt","w") as f:
                f.write(f"{self.high_score}")
        self.game_score = 0
        self.update_scoreboard()

    def total_score(self): 
            self.game_score += 1
            self.clear()
            self.update_scoreboard()
            
            
            
            