<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
import math
import sys

def Plotting() :
    # Plotting Polygon
    xPol = []; yPol = []
    for pol in polygon :
        xPol.append(pol[0]); yPol.append(pol[1])
    xPol.append(xPol[0]); yPol.append(yPol[0])
    plt.plot(xPol, yPol)

    plt.show()

def getInput():
    m= int(input())
    polygon = []
    st = [int(i) for i in input().split()]
    for i in range(0, 2 * m, 2) :
        polygon.append((st[i], st[i + 1]))
    return polygon

def isRightTurn(vStart, vEnd, myPoint) :
    det = (vEnd[0] - vStart[0]) * (myPoint[1] - vStart[1]) - (myPoint[0] - vStart[0]) * (vEnd[1] - vStart[1])
    if det < 0 : return True
    else : return False


def isPolygonConvex(polygon):
    for i in range(len(polygon)) :
        if i == len(polygon) - 1 :
            if isRightTurn(polygon[-1], polygon[0], polygon[1]) :return "NOT_CONVEX"
        elif i == len(polygon) - 2 :
            if isRightTurn(polygon[i], polygon[i + 1], polygon[0]):return "NOT_CONVEX"
        else :
            if isRightTurn(polygon[i], polygon[i + 1], polygon[i + 2]):return "NOT_CONVEX"
    return "CONVEX"

if __name__ == '__main__':
    polygon = getInput()
    print(isPolygonConvex(polygon))

=======
import numpy as np
import matplotlib.pyplot as plt
import math
import sys

def Plotting() :
    # Plotting Polygon
    xPol = []; yPol = []
    for pol in polygon :
        xPol.append(pol[0]); yPol.append(pol[1])
    xPol.append(xPol[0]); yPol.append(yPol[0])
    plt.plot(xPol, yPol)

    plt.show()

def getInput():
    m= int(input())
    polygon = []
    st = [int(i) for i in input().split()]
    for i in range(0, 2 * m, 2) :
        polygon.append((st[i], st[i + 1]))
    return polygon

def isRightTurn(vStart, vEnd, myPoint) :
    det = (vEnd[0] - vStart[0]) * (myPoint[1] - vStart[1]) - (myPoint[0] - vStart[0]) * (vEnd[1] - vStart[1])
    if det < 0 : return True
    else : return False


def isPolygonConvex(polygon):
    for i in range(len(polygon)) :
        if i == len(polygon) - 1 :
            if isRightTurn(polygon[-1], polygon[0], polygon[1]) :return "NOT_CONVEX"
        elif i == len(polygon) - 2 :
            if isRightTurn(polygon[i], polygon[i + 1], polygon[0]):return "NOT_CONVEX"
        else :
            if isRightTurn(polygon[i], polygon[i + 1], polygon[i + 2]):return "NOT_CONVEX"
    return "CONVEX"

if __name__ == '__main__':
    polygon = getInput()
    print(isPolygonConvex(polygon))

>>>>>>> refs/remotes/origin/master
    # Plotting() # For testing reasons