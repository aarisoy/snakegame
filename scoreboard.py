from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score: {self.score}",move=False, align="center",font=("Courier", 20, "normal"))

    def hit(self, speed):
        if speed == 0.1:
            self.score += 10
            self.clear()
            self.write(f"Score: {self.score}",move=False, align="center",font=("Courier", 20, "normal"))
        elif speed == 0.2:
            self.score += 5
            self.clear()
            self.write(f"Score: {self.score}",move=False, align="center",font=("Courier", 20, "normal"))
        elif speed == 0.3:
            self.score += 1
            self.clear()
            self.write(f"Score: {self.score}",move=False, align="center",font=("Courier", 20, "normal"))

        
    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER",move=False, align="center",font=("Courier", 20, "normal"))
