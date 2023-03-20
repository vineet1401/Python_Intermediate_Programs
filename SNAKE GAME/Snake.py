from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-10, 0), (-20, 0)]
SNAKE_DISTANCE = 10
SNAKE_SIZE = 0.5
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake_Prop:
    def __init__(self):
        self.my_snake = []
        self.Create_Snake()


    def Create_Snake(self):
        for pos in SNAKE_POSITION:
            self.Create_Body(pos)


    def Create_Body(self, pos):
            self.body = Turtle('square')  # type: ignore
            self.body.shapesize(SNAKE_SIZE)
            self.body.penup()
            self.body.goto(pos)
            self.body.color('white')
            self.my_snake.append(self.body)


    def Extend_Body(self):
        self.Create_Body(self.my_snake[-1].position())
        

    def Move_Forward(self):
        for b in range(len(self.my_snake)-1, 0, -1):
            self.new_x = self.my_snake[b-1].xcor()
            self.new_y = self.my_snake[b-1].ycor()
            self.my_snake[b].goto(self.new_x, self.new_y)
        self.my_snake[0].forward(SNAKE_DISTANCE)

    def Move_Left(self):
        if (self.my_snake[0].heading() != RIGHT):
            self.my_snake[0].setheading(LEFT)

    def Move_Right(self):
        if (self.my_snake[0].heading() != LEFT):
            self.my_snake[0].setheading(RIGHT)

    def Move_Up(self):
        if (self.my_snake[0].heading() != DOWN):
            self.my_snake[0].setheading(UP)

    def Move_Down(self):
        if (self.my_snake[0].heading() != UP):
            self.my_snake[0].setheading(DOWN)


