import matplotlib.pyplot as pyplot
import random

# Calculates PI
totalPoints = int(input("Points: "))
insideCircle = 0

xValuesInside = []
yValuesInside = []

xValuesOutside = []
yValuesOutside =[]

for count in range(totalPoints):
    xValue = random.uniform(-1, 1)
    yValue = random.uniform(-1, 1)

    distance = xValue ** 2 + yValue ** 2
    if distance <= 1:
        insideCircle += 1

        xValuesInside.append(xValue)
        yValuesInside.append(yValue)

    else:
        xValuesOutside.append(xValue)
        yValuesOutside.append(yValue)

myPI = 4 * (insideCircle / totalPoints)

print(myPI)

# Plots solution
circle = pyplot.Circle((0, 0), radius=1, facecolor="white", edgecolor="red")
rectangle = pyplot.Rectangle((-1, -1), width=2, height=2, facecolor="white", edgecolor="blue")

drawFig = pyplot.gca()

drawFig.add_patch(rectangle)
drawFig.add_patch(circle)

#pyplot.plot(xValuesInside, yValuesInside)

for idx in range(len(xValuesInside)):
    pyplot.plot(xValuesInside[idx], yValuesInside[idx], marker='o', markersize=3, color="red")

for idx in range(len(xValuesOutside)):
    pyplot.plot(xValuesOutside[idx], yValuesOutside[idx], marker='o', markersize = 3, color="blue")

pyplot.axis("scaled")

pyplot.show()