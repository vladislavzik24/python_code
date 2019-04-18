import turtle as tr
from math import sin, cos, pi

def deg_to_rad(deg, om):
	rad = deg * pi / 180
	return om * cos(rad), om * sin(rad)

a = int(input('Приращение за 1 круг: '))
n = int(input('Всего кругов спирали: '))
k = a / 360

for deg in range(0, n * 360):
	x, y = deg_to_rad(deg, k * deg)
	tr.goto(x, y)
	print(x, y)