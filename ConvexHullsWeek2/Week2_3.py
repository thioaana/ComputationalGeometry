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
        xPol.append(pol[0]); yPol.append(pol[1])
    xPol.append(xPol[0])
    yPol.append(yPol[0])
    plt.plot(xPol, yPol)

    # Plotting Points
    for p in points:
        plt.scatter(p[0], p[1])
    plt.show()


def TengentsToPolygon(myPol, myPoints) :
    for p in myPoints :
        TangList = []
        for i in range(len(myPol)) :
            v1 = myPol[i]
            if i == 0 : v0 = myPol[len(myPol) - 1]; v2 = myPol[i + 1]
            if i == len(myPol) - 1 :  v0 = myPol[i - 1]; v2 = myPol[0]
            else : v0 = myPol[i - 1]; v2 = myPol[i + 1]

            # Creates the matrix and calulates the dets
            a = np.array([v0, v1, p], dtype=np.int64)
            b = np.ones((3, 1), dtype=np.int64)
            d = np.hstack((a, b))  # append a column
            det1 = np.linalg.det(d)

            a = np.array([v1, v2, p], dtype=np.int64)
            b = np.ones((3, 1), dtype=np.int64)
            d = np.hstack((a, b))  # append a column
            det2 = np.linalg.det(d)

            if det1 * det2 < 0:
                TangList.append(myPol[i])
            elif det1 * det2 == 0:
                TangList.append(myPol[i])
                i += 1
            if len(TangList) == 2 :
                print(TangList)
                break

if __name__ == '__main__':
    # Reads and define the Polygon
    # The Polygon is a list of tuples. Every tuple includes the the coords (x, y) of a vertex
    m = 0
    while m < 3 or m > 1000 :
        m = int(input("Enter the number of Vertices of the Polygon : "))
    userInput = input("Enter coords of all Vertices with space between : ").split()

    polygon = []
    for i in range(m):
        polygon.append((int(userInput[2 * i]), int(userInput[2 * i + 1])))

    # Reads and define the Points
    n = 0
    while n < 1 or n > 1000 :
        n = int(input("Enter the number of points : "))

    points = []
    for i in range(n):
        userInput = input("Enter coords of a point with space between :").split()
        points.append((int(userInput[0]), int(userInput[1])))

    TengentsToPolygon(polygon, points)
    Plotting()
4