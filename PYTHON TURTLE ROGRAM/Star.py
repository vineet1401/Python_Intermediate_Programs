import turtle


t = turtle.Turtle()
t.speed(100)
t.penup()
t.goto(-200, 50)


t.fillcolor(0,0,1)
t.begin_fill()
for i in range (5):
    t.forward(400)
    t.right(144)
t.end_fill()











screen = turtle.Screen()
screen.exitonclick()