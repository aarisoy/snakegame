from turtle import Screen
import time, random
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Default size for screen
SCREEN_SIZE = 600

# Speed for screen
SPEED = {
    "FAST":     0.1,
    "MEDIUM":   0.2,
    "LOW":      0.3
}

screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Snake Game by Alpay")
screen.tracer(0)

userSelectionSpeed = screen.textinput(title="Speed Selection", prompt="Select a speed: FAST, MEDIUM, LOW")

game_ends = True

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")    
screen.onkey(snake.down,"Down")    
screen.onkey(snake.left,"Left")    
screen.onkey(snake.right, "Right") 
screen.update()

while game_ends:
    screen.update()
    time.sleep(SPEED[userSelectionSpeed])
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.hit(SPEED[userSelectionSpeed])
        snake.extend()

    if snake.headPosition():
        scoreboard.gameover()
        game_ends = False

    for body in snake.snakes[1::]:
        if snake.head.distance(body) < 10:
            scoreboard.gameover()
            game_ends = False

screen.exitonclick()