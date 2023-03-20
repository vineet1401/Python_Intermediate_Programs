import turtle


t = turtle.Turtle()

t.speed('fastest')
t.penup()
t.goto(-50,0)
t.pendown()
t.color('red')
t.hideturtle()

x = 0
for i in range(36):
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.left((10))

    
screen = turtle.Screen()
screen.exitonclick()
