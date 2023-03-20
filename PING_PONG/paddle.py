from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(pos)
        self.pad_move = 10
    
    def Move_Up(self):
        self.new_y = self.ycor() + self.pad_move
        self.new_x = self.xcor()
        if(self.ycor() < 150):
            self.goto(self.new_x, self.new_y)

    def Move_Down(self):
        self.new_y = self.ycor() - self.pad_move
        self.new_x = self.xcor() 
        if (self.ycor() > -150):
            self.goto(self.new_x, self.new_y)

