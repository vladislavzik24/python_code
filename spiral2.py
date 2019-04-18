import turtle as tr

x = int(input())
dx = int(input())
n = int(input())

for i in range(n * 4):
	tr.forward(x)
	tr.left(90)
	x += dx

input('')