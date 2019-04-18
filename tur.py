import turtle

turtle.shape('classic')
x = int(input())
dx = 10

while True:
	for i in range(10):
		turtle.pendown()
		turtle.forward(x)
		turtle.left(90)
		turtle.forward(x)
		turtle.left(90)
		turtle.forward(x)
		turtle.left(90)
		turtle.forward(x)
		turtle.penup()
		turtle.right(45)
		turtle.forward(dx)
		turtle.left(135)
		x += 2*(0.5 * dx ** 2) ** 0.5
		print(x, i)

	turtle.clear()
	turtle.goto(0,0)