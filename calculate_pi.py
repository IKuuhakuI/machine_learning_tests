import matplotlib.pyplot as pyplot
import numpy as np
'''
radius = 1

side = 2

n = 64

t = np.linspace(0, 2*np.pi, n+1)

x_circle = radius * np.cos(t)
y_circle = radius * np.sin(t)

pyplot.axis("equal")

pyplot.grid()
pyplot.plot(x_circle, y_circle)

x_square = side
y_square = side
'''

circle = pyplot.Circle((0, 0), radius=1, facecolor="white", edgecolor="black")
rectangle = pyplot.Rectangle((-1, -1), width=2, height=2, facecolor="white", edgecolor="black")

ax = pyplot.gca()
bx = pyplot.gca()

bx.add_patch(rectangle)
ax.add_patch(circle)

pyplot.axis("scaled")

pyplot.show()



