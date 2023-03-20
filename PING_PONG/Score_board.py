from turtle import Turtle
from ball import Ball


class Score(Ball):

    def __init__(self, pos) -> None:
        super().__init__()
        self.player_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(pos)
        self.write(arg=f"{self.player_score}",
                   align='center', font=('Arial', 30, 'bold'))

    def Increase_Score(self):
        self.clear()
        self.player_score += 1
        self.ball_speed += 1
        self.write(arg=f"{self.player_score}",
                     align='center', font=('Arial', 30, 'bold'))

    def Reset_Score(self):
        self.clear()
        self.player_score = 0


class Winner(Turtle):

    def __init__(self, winner) -> None:
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.write(arg=f'Winnner\n   {winner}', align='center',
                   font=('Arial', 40, 'bold'))
