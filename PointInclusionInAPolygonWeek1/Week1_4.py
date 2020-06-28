import numpy as np
import matplotlib.pyplot as plt
import math
from bisect import bisect_left
import sys
import Week1Utilities

def Plotting() :
    # Plotting Polygon
    xPol = []; yPol = []
    for pol in polygon :
        xPol.append(pol[0][0]); yPol.append(pol[0][1])
    xPol.append(xPol[0]); yPol.append(yPol[0])
    plt.plot(xPol, yPol)

    # Plotting Points
    for p in points:
        plt.scatter(p[0][0], p[0][1])
    plt.show()

if __name__ == '__main__':
    # Reads and define the Polygon
    # The Polygon is a list of lists. The inner list contains a tuple (coords) and a float (angle)
    # Every tuple includes the the coords (x, y) of a vertex
    m = 0
    while m < 3 or m > 20000 :
        m = int(input("Enter the number of Vertices of the Polygon : "))
    userInput = input("Enter coords of all Vertices with space between :").split()

    polygon = []
    # polygon = [[(-2, -3), 0.0], [(1, -4), 0.0], [(3, -2), 0.0], [(2, 1), 0.0], [(-2, 1), 0.0]]
    for i in range(m):
        polygon.append([(int(userInput[2 * i]), int(userInput[2 * i + 1])), 0.0])

    # Reads and define the Points
    n = 0
    while n < 1 or n > 50000 :
        n = int(input("Enter the number of points : "))

    points = []
    # points = [[(2, -3), 0.0], [(3, 0), 0.0], [(0, 0), 0.0], [(2, -1), 0.0]]
    for i in range(n):
        userInput = input("Enter coords of a point with space between :").split()
        points.append([(int(userInput[0]), int(userInput[1])), 0.0])

    Week1Utilities.PointAndConvexPolygon(polygon, points)

    Plotting()
