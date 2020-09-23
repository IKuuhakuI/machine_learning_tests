import matplotlib.pyplot as pyplot
import random
from numpy import pi

# Returns
OK = 0
MENU_OPTION_DOES_NOT_EXIST = 1
INVALID_INPUT = 2
NEGATIVE_NUMBER = 3

# Calculates PI
def EstimatePi(totalPoints):
    insideCircle = 0

    # Saves all the points inside the circle
    xValuesInside = []
    yValuesInside = []

    # Saves all the points outside the circle
    xValuesOutside = []
    yValuesOutside = []

    # Generates random points
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

    wantsToPlot = input("Wants to plot solution: [y] or [n]: ")

    if wantsToPlot == 'n' or wantsToPlot == 'N':
        return myPI

    elif wantsToPlot == 'y' or wantsToPlot == 'Y':
        PlotSolution(xValuesInside, yValuesInside, xValuesOutside, yValuesOutside)
        return myPI

    return -1


def PlotSolution(xInside, yInside, xOutside, yOutside):
    # Plots solution
    circle = pyplot.Circle((0, 0), radius=1, facecolor="white", edgecolor="red")
    rectangle = pyplot.Rectangle((-1, -1), width=2, height=2, facecolor="white", edgecolor="blue")

    drawFig = pyplot.gca()

    drawFig.add_patch(rectangle)
    drawFig.add_patch(circle)

    # Points inside circle
    for idx in range(len(xInside)):
        pyplot.plot(xInside[idx], yInside[idx], marker='o', markersize=3, color="red")

    # Points outside circle
    for idx in range(len(xOutside)):
        pyplot.plot(xOutside[idx], yOutside[idx], marker='o', markersize=3, color="blue")

    pyplot.axis("scaled")

    pyplot.show()


def Main():
    print("Hello, this a algorithm that estimates PI based on random points")

    userInput = '-1'

    # Menu
    while userInput != '2':
        print("To estimate the value of PI: 1")
        print("To exit the program: 2")

        userInput = input("Select your option: ")
        print()

        if userInput == '1':
            print("Great! Let's begin!")
            print("To estimate PI we need to know how much points you wanna randomize!")
            print("More points = More accuracy\n")

            totalPoints = input("Inform how many points you wanna try: ")
            print()

            try:
                totalPoints = int(totalPoints)

            except:
                print("Error (%d):\tInvalid Input!" % INVALID_INPUT)
                return INVALID_INPUT

            if totalPoints <= 0:
                print("Error (%d):\tInput must be a natural number different from 0" % NEGATIVE_NUMBER)

                return NEGATIVE_NUMBER

            myPI = EstimatePi(totalPoints)

            if myPI == -1:
                return INVALID_INPUT

            print("PI is approximately: ", myPI)
            print("PI is: ", pi)
            print()

        elif userInput != '2':
            print("Error (%d):\tInvalid Input!" % MENU_OPTION_DOES_NOT_EXIST)
            return MENU_OPTION_DOES_NOT_EXIST

    return OK


Main()
