from turtle import Turtle

# Classic starting pos of snake
starting_pos =[(0,0),(-20,0),(-40,0)]

# Default variable for movement
DEFAULT_MOVEMENT = 20

# Default size for screen
SCREEN_SIZE = 600

# Direction headings
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180      

class Snake:
    def __init__(self):
        self.attrs = {"color": "white",
                      "shape": "square"}
        self.snakes = []
        self.createSnakes()
        self.head = self.snakes[0]
        self.tail = self.snakes[-1]
    
    def createSnakes(self):
        for snake_pos in starting_pos:
            self.addTail(snake_pos)
    
    def move(self):
        for snake_num in range((len(self.snakes)-1),0,-1):
            replacedx = self.snakes[snake_num-1].xcor()
            replacedy = self.snakes[snake_num-1].ycor()
            self.snakes[snake_num].goto(replacedx,replacedy)
        self.head.forward(DEFAULT_MOVEMENT)

    def addTail(self, position):
        newSnake = Turtle(shape = self.attrs["shape"])
        newSnake.penup()
        newSnake.color(self.attrs["color"])
        newSnake.goto(position)
        self.snakes.append(newSnake)

    def extend(self):
        self.addTail(self.tail.position())

    def headPosition(self):
        self.x = self.head.xcor()
        self.y= self.head.ycor()
        if abs(self.x) > (SCREEN_SIZE/2 - 20) or abs(self.y) > (SCREEN_SIZE/2 -20):
            return True
        else:
            return False        

    def up(self):
        if self.head.heading() == DOWN:
            pass
        else:    
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == RIGHT:
            pass
        else:    
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)

