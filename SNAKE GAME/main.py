from turtle import Screen, Turtle
import time
import Snake
import Food_Score


screen = Screen()
screen.setup(600, 600)
screen.title("SNAKE GAME".center(150))
screen.bgcolor('black')
screen.tracer(0)

snake = Snake.Snake_Prop()
food = Food_Score.Food()
score = Food_Score.Score()


is_on = True
while is_on:
    screen.update()
    time.sleep(0.09)

    snake.Move_Forward()

    screen.listen()
    screen.onkey(fun=snake.Move_Up, key="Up")
    screen.onkey(fun=snake.Move_Left, key="Left")
    screen.onkey(fun=snake.Move_Right, key="Right")
    screen.onkey(fun=snake.Move_Down, key="Down")

    if (snake.my_snake[0].distance(food) < 20):
        food.Refresh()
        score.Show_Score()
        snake.Extend_Body()

    if (snake.my_snake[0].xcor() > 290 or snake.my_snake[0].xcor() < -290 or snake.my_snake[0].ycor() > 290 or snake.my_snake[0].ycor() < -290):
        score.Game_Over()
        is_on = False


    for i in range(1, len(snake.my_snake)):
        if (snake.my_snake[0].position() == snake.my_snake[i].position()):
            score.Game_Over()
            is_on = False
     
screen.exitonclick()
