import random
from turtle import Turtle
from snake import Snake
class Food(Turtle):
#This class inherit everything from Turtle module
    def __init__(self):
        # With super we inherit from turtle
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()


    def refresh(self):

        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)