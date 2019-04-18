from numpy import arange, pi, sin, cos
from matplotlib import pyplot as plt
def qr():
	x = []
	y = []
	for teta in arange(0, 2 * pi, 0.1):
		#зададим параметрическое уравнение
		y.append(sin(teta))
		x.append(cos(teta))
	plt.plot(x, y)
	plt.show()

