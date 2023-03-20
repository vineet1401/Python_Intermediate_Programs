from turtle import Screen
from paddle import Paddle
from ball import Ball
from Score_board import Score, Winner
import time


p1 = input('Enter First Player Name: ')
p2 = input('Enter Second Player Name: ')

screen = Screen()
screen.setup(height=400, width=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('PONG GAME'.center(150))


right_P = Paddle((275, 0))
left_P = Paddle((-275, 0))
left_S = Score((-30, 150))
right_S = Score((30, 150))
ball = Ball()


screen.listen()

screen.onkeypress(fun=right_P.Move_Up, key='Up')
screen.onkeypress(fun=right_P.Move_Down, key='Down')
screen.onkeypress(fun=left_P.Move_Up, key='w')
screen.onkeypress(fun=left_P.Move_Down, key='s')


game_on = True
while (game_on):

    screen.update()
    time.sleep(0.05)

    ball.Ball_Move()

    if (ball.ycor() > 180 or ball.ycor() < -180):
        ball.Ball_Bounce()

    if (right_P.distance(ball) < 35 or left_P.distance(ball) < 35):
        ball.Deflect_Ball()

    if (ball.xcor() > 300):
        screen.update()
        ball.Ball_Reset()

    if (ball.xcor() < -300):
        right_S.Increase_Score()
        screen.update()
        ball.Ball_Reset()

    if (right_S.player_score == 3 and left_S.player_score < 3):
        winner = Winner(p2)
        game_on = False

    if (left_S.player_score == 3 and right_S.player_score < 3):
        winner = Winner(p1)
        game_on = False


screen.exitonclick()
