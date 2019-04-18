import numpy as np 
from matplotlib import pl

f = 16000 

t = linspace(0,1,8000)
y = np.sin(2*np.pi*f*t)


plt.plot(t, y)
plot().show()

