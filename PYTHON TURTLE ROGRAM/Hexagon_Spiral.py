import turtle


t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')

t.speed('fastest')
t.setheading(30)


colour = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

for x in range(180):
    t.pencolor(colour[x % 6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)


screen.exitonclick()

