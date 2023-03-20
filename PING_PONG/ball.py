from turtle import Turtle

class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.shape('circle')
		self.color('red')
		self.x_move = 5
		self.y_move = 5
		self.ball_speed = 40

	def Ball_Move(self):
		self.newx = self.xcor() + self.x_move
		self.newy = self.ycor() + self.y_move
		self.penup()
		self.goto(self.newx, self.newy)

	def Ball_Bounce(self):
		self.y_move *= -1

	def Deflect_Ball(self):
		self.x_move *= -1
		self.ball_speed += 0.1

	def Ball_Reset(self):
		self.penup()
		self.goto(0, 0)
		self.x_move *= -1

