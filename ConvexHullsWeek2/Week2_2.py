import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import Week2Utilities

def Plotting(p, shape) :
    xP = []; yP = []
    for p1 in p :
        xP.append(p1[0]); yP.append(p1[1])

    # Plotting Polygon
    if shape == "POLYGONUp":
        plt.plot(xP, yP)
    if shape == "POLYGON":
        plt.plot(xP, yP)
        plt.show()
    # Plotting Points
    if shape == "POINTS" :
        plt.scatter(xP, yP)

def BuildConvexHullUpper(myPoints) :
    myPoints.sort(key = lambda x: x[0])
    LUpper = [myPoints[0], myPoints[1]]
    for i in range(2, len(myPoints)) :
        LUpper.append(myPoints[i])
        det = 1
        while len(LUpper) > 2 and det >= 0:
            # Creates the matrix and calulates the det
            a = np.array([LUpper[-3], LUpper[-2], LUpper[-1]], dtype = np.int64)
            b = np.ones((3, 1), dtype = np.int64)
            d = np.hstack((a, b)) # append a column
            det = np.linalg.det(d)
            if det > 0 :
                LUpper.remove(LUpper[-2])
            if det == 0 :
                temp = []
                temp.append(LUpper.pop());temp.append(LUpper.pop());temp.append(LUpper.pop())
                temp.sort()
                LUpper.extend(temp)
                LUpper.remove(LUpper[-2])
    return LUpper

def BuildConvexHullLower(myPoints) :
    myPoints.sort(key = lambda x: x[0])
    LLower = [myPoints[0], myPoints[1]]
    for i in range(2, len(myPoints)) :
        LLower.append(myPoints[i])
        det = -1
        while len(LLower) > 2 and det <= 0:
            # Creates the matrix and calulates the det
            a = np.array([LLower[-3], LLower[-2], LLower[-1]], dtype = np.int64)
            b = np.ones((3, 1), dtype = np.int64)
            d = np.hstack((a, b)) # append a column
            det = np.linalg.det(d)
            if det < 0 :
                LLower.remove(LLower[-2])
            if det == 0 :
                temp = []
                temp.append(LLower.pop());temp.append(LLower.pop());temp.append(LLower.pop())
                temp.sort()
                LLower.extend(temp)
                LLower.remove(LLower[-2])
    return LLower

if __name__ == '__main__':
    # Reads and define the Polygon The Polygon is a list of tuples.
    # Every tuple includes the the coords (x, y) of a vertex
    n = 0
    while n < 3 or n > 5000 :
        n = int(input("Enter the number of Vertices of the Polygon : "))
    userInput = input("Enter coords of all Vertices with space between :").split()

    points = []
    # points = [(-10, -2), (-7, 2), (-4, 3), (-6, 5), (-8, 7), (-2, 8), (2, 3), (4, 5), (6, 1), (7, -5), (2, -7), (-4, -4), (-8, -6), (-7, 1), (2, 5)]
    for i in range(n):
        points.append((int(userInput[2 * i]), int(userInput[2 * i + 1])))


    polUpper = BuildConvexHullUpper(points)
    polLower = BuildConvexHullLower(points)
    print(polUpper)
    print("PLo", polLower)
    Plotting(points, "POINTS")
    Plotting(polUpper, "POLYGONUp")
    Plotting(polLower, "POLYGON")