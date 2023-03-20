import turtle


t = turtle.Turtle()

t.penup()
t.goto(-200, 100)

t.fillcolor(1, 0, 1)
t.begin_fill()
t.setheading(30)
for i in range(6):
    t.forward(200)
    t.right(60)
t.end_fill()

screen = turtle.Screen()
screen.exitonclick()