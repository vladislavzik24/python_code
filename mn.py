import turtle as tr
from math import sin, radians

def figure(r, n):
	alfa = 360 / n
	a = r * 2 * sin(radians(alfa / 2)) #не забыть перевод в радианы
	tr.left(90 + alfa / 2)
	tr.forward(a)
	
	for i in range(n - 1):
		tr.left(alfa)
		tr.forward(a)
	
	tr.right(90 - alfa / 2)

r = 50
k = int(input())
dr = 15

for i in range(4, k + 1):
	figure(r, i)
	tr.penup()
	tr.forward(dr)
	r += dr
	tr.pendown()
input() 