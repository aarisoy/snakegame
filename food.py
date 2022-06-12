from turtle import Turtle
import random

randomX = random.randint(-260,260)
randomY = random.randint(-260,260)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(randomX,randomY)
        self.refresh()

    def refresh(self):
        randomX = random.randint(-280,280)
        randomY = random.randint(-280,280)
        self.goto(randomX,randomY)