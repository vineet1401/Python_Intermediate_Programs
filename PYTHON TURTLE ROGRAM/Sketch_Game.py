import turtle

import turtle

t = turtle.Turtle()
screen = turtle.Screen()

screen.setup(height=600, width=600)


def Move_Forward():
    t.forward(10)


def Move_Backward():
    t.backward(10)


def Move_Left():
    t.left(10)


def Move_Right():
    t.right(10)


def Clear():
    t.clear()
    t.penup()
    t.reset()
    t.pendown()


screen.listen()
screen.onkeypress(fun=Move_Forward, key='w')
screen.onkeypress(fun=Move_Backward, key='s')
screen.onkeypress(fun=Move_Right, key='d')
screen.onkeypress(fun=Move_Left, key='a')
screen.onkeypress(fun=Clear, key='c')


screen.exitonclick()
