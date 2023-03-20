import turtle  # Outside_In


t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-200, -200)
t.pendown()
t.speed('fastest')

x = 400
for i in range(20):
    for j in range(4):
        x -= 5
        t.forward(x)
        t.left(90)


screen = turtle.Screen()
screen.exitonclick()
