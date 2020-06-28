import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import Week2Utilities

def Plotting() :
    # Plotting Polygon
    xPol = []; yPol = []
    for pol in polygon :
        xPol.append(pol[0]); yPol.append(pol[1])
    xPol.append(xPol[0]); yPol.append(yPol[0])
    plt.plot(xPol, yPol)

    plt.show()

if __name__ == '__main__':
    # Reads and define the Polygon The Polygon is a list of tuples.
    # Every tuple includes the the coords (x, y) of a vertex
    m = 0
    while m < 3 or m > 500 :
        m = int(input("Enter the number of Vertices of the Polygon : "))
    userInput = input("Enter coords of all Vertices with space between :").split()

    polygon = []
    for i in range(m):
        polygon.append((int(userInput[2 * i]), int(userInput[2 * i + 1])))

    print(Week2Utilities.PolygonConvexOrNot(polygon))

    Plotting()
