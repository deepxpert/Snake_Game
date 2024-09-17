from turtle import Turtle,Screen
import time
from snake_body import Snake
from food import Food
from scoreBoard import Scoreboard
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()    
    if snake.head.distance(food)<15:
        food.reposition()
        snake.increase_snake()
        score.total_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset_snake()
    for i in snake.body[1:]:
            if snake.head.distance(i) < 10:
                 snake.reset_snake()
                 score.reset()
            
screen.exitonclick()
