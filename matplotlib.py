import matplotlib.pyplot as plot
import numpy as np

x = np.linspace(-2, 2, 100) #显示X轴的范围从-2至2
y = x**2

plot.figure()
plot.plot(x, y)
plot.show()
