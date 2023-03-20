from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5)
        self.color('red')
        self.penup()
        
    def Refresh(self):
        New_x = random.randint(-280, 280)
        New_y = random.randint(-280, 280)
        self.goto(New_x, New_y)


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()

        with open('HighScore.txt', 'r') as file:
            self.highscore = file.read()

        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color('white')
        self.write(arg=f"High Score : {self.highscore} | Score : {self.score}", align='center', font=('Arial', 25, 'normal'))

    def Show_Score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"High Score : {self.highscore} | Score : {self.score}", align='center', font=('Arial', 25, 'normal'))


    def Game_Over(self):
        self.goto(0, 0)
        self.write(arg=f"SCORE : {self.score}\nGame Over", align='center', font=('Arial', 35, 'bold'))

        with open('HighScore.txt', 'w') as file:
            if(int(self.highscore) < int(self.score)):
                file.write(str(self.score))


