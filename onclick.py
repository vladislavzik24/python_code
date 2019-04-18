form turtle import onclick

def turn(x, y):
	for i in range(4):
		forward(100)
		left(90)

onclick(turn)