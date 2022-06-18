from turtle import Screen
import time, random
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from speed import Speed

# Default size for screen
SCREEN_SIZE = 600

screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Snake Game by Alpay")
screen.tracer(0)

userSelectionSpeed = screen.textinput(title="Speed Selection", prompt="Select a speed: FAST, MEDIUM, LOW")
selectedSpeed = userSelectionSpeed.lower()

# Global variables for controlling
game_ends = True
isSpeedCalibrated = False

# Object creations
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
speed = Speed((selectedSpeed))

# Keybounds
screen.listen()
screen.onkey(snake.up,"Up")    
screen.onkey(snake.down,"Down")    
screen.onkey(snake.left,"Left")    
screen.onkey(snake.right, "Right") 

while game_ends:
    screen.update()
    time.sleep(speed.localSpeed)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.hit(speed.selection[selectedSpeed])
        snake.extend()

    if snake.headPosition():
        scoreboard.updateHighScore()
        snake.reset()

    if (len(snake.snakes)%5) == 0 and (isSpeedCalibrated == False):
        isSpeedCalibrated = speed.calibrate(isSpeedCalibrated)

    if len(snake.snakes)%6 == 0:
        isSpeedCalibrated = False

    speed.checkMaxSpeed()
    
    for body in snake.snakes[1::]:
        if snake.head.distance(body) < 10:
            snake.reset()

screen.exitonclick()