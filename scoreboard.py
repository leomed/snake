from turtle import Turtle
ALIGNMENT = "LEFT"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.shapesize(1)
        self.hideturtle()
        self.penup()
        self.goto(-70, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"The score is:{self.score}", align=ALIGNMENT, font="10")

    def game_over(self):
        self.goto(-45,0)
        self.write("Game Over",align=ALIGNMENT, font="10")

    def add_score(self):
        """It adds one to the score if the collision gets triggered"""
        self.score += 1
        self.clear()
        self.update_scoreboard()