from turtle import Turtle
SNAKE_POSITION = [(0,0),(-20,0),(-40,0)]
SNAKE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        

    def create_snake(self):
        for position in SNAKE_POSITION:
            self.add_body(position)



    def add_body(self,position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.body.append(snake)

    def reset_snake(self):
        for i in self.body:
            i.goto(1000,1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]



    def increase_snake(self):
        self.add_body(self.body[-1].position())


    def move(self):
        for i in range(len(self. body)-1,0,-1):
            t_x = self.body[i-1].xcor()        
            t_y = self.body[i-1].ycor()
            self.body[i].goto(t_x,t_y)
        self.head.fd(SNAKE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
