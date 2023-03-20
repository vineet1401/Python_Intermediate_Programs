from turtle import Screen, Turtle

tt = Turtle()

tt.color(0, 0, 0)
tt.pensize(10)
tt.hideturtle()
tt.penup()
tt.setheading(225)
tt.forward(250)
tt.setheading(0)
tt.pendown()

for i in range(4):
	tt.forward(400)
	tt.left(90)








screen = Screen()
screen.exitonclick()