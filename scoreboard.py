from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.highScore = 0
        self.getHighScore()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score: {self.score}, High Score: {self.highScore}",move=False, align="center",font=("Courier", 20, "normal"))

    def hit(self, speed):
        if speed == 0.1:
            self.score += 10
            self.updateScoreBoard(self.score)
        elif speed == 0.2:
            self.score += 5
            self.updateScoreBoard(self.score)

        elif speed == 0.3:
            self.score += 1
            self.updateScoreBoard(self.score)

    def updateHighScore(self):
        if self.score > self.highScore:
            self.highScore = self.score
        self.score = 0
        self.updateScoreBoard(self.score)
        self.writeHighScore()

    def updateScoreBoard(self, score):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore}",move=False,align="center",font=("Courier", 20, "normal"))

    def getHighScore(self):
        with open("HighScore.txt", mode = "r") as fd:
            highScore = int(fd.read())
            self.highScore = highScore # Write the last highest score to object variable

    def writeHighScore(self):
        with open("HighScore.txt", mode = "w") as fd:
            fd.write("%d" % self.highScore)