#uses python3

# import matplotlib.pyplot as plt
import math
from bisect import bisect_left
import sys

def getInput():
    m= int(input())
    polygon = []
    st = [int(i) for i in input().split()]
    for i in range(0, 2 * m, 2) :
        polygon.append([(st[i], st[i + 1]), 0.0])

    n = int(input())
    points = []
    for i in range(n):
        temp = input().split()
        points.append([(int(temp[0]), int(temp[1])), 0.0])
    return polygon, points

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

def PointAndVector(vStart, vEnd, myPoint):
    # Checks if the vector has 0 length and aborts
    if vStart[0] == vEnd[0] and vStart[1] == vEnd[1]:
        print("The vector has 0 length - Program aborts")
        sys.exit()

    det = (vEnd[0] - vStart[0]) * (myPoint[1] - vStart[1]) - (myPoint[0] - vStart[0]) * (vEnd[1] - vStart[1])
    # In case det = zero (or almost)
    if abs(det) < 0.00000001:
        maxVertical = max(vStart[1], vEnd[1])
        minVertical = min(vStart[1], vEnd[1])
        if vStart[1] != vEnd[1]:  # In case of non - horizontal vector
            if myPoint[1] < minVertical or myPoint[1] > maxVertical:
                return "ON_LINE"
            else:
                return "ON_SEGMENT"
        else:  # In case of horizontal vector
            maxHorizontal = max(vStart[0], vEnd[0])
            minHorizontal = min(vStart[0], vEnd[0])
            if myPoint[0] < minHorizontal or myPoint[0] > maxHorizontal:
                return "ON_LINE"
            else:
                return "ON_SEGMENT"
    if det > 0:
        return "LEFT"
    else :
        return "RIGHT"

def PointAndConvexPolygon(poly, myPoints):
    # Find o point inside the Polygon
    # The point is the center mass of the three first vertices (no co-linear) of the Polygon
    zX = (poly[0][0][0] + poly[1][0][0] + poly[2][0][0]) / 3
    zY = (poly[0][0][1] + poly[1][0][1] + poly[2][0][1]) / 3
    z = (zX, zY)

    # Computes the 3rd element of every poly/vertex which was initialized by 0.0
    # This is angle between the positive horizontal axis and the ray of the vertex and z
    for i in range(len(poly)) :
        poly[i][1] = math.atan2(poly[i][0][1] - z[1], poly[i][0][0] - z[0])

    # Sort the list-poly by the angle (3rd element)
    poly.sort(key = lambda x: x[1])
    polyAngles = [x[1] for x in poly]

    # Fills the 3rd coord of every point which was initialized by 0.0
    # This is angle between the positive horizontal axis and the ray of the point and z
    # Finds in which arc the Point belong and calls PointAndVector function
    for i in range(len(myPoints)):
        myPoints[i][1] = math.atan2(myPoints[i][0][1] - z[1], myPoints[i][0][0] - z[0])
        b = bisect_left(polyAngles, myPoints[i][1])
        if b == 0 or b == len(poly):    # The case where the angle of Point is below 1st vertex or over last vertex
            position = PointAndVector(poly[len(poly)-1][0], poly[0][0], myPoints[i][0])
        else :
            position = PointAndVector(poly[b-1][0], poly[b][0], myPoints[i][0])
        if position in ["ON_SEGMENT", "INTERSECT_END_OF_EDGE"] : print("BORDER")
        if position in ["RIGHT", "ON_LINE", "OUT_OF_HORIZONTAL_LINE"] : print("OUTSIDE")
        if position in ["LEFT"]: print("INSIDE")

if __name__ == '__main__':
    # Reads and define the Polygon
    # The Polygon is a list of lists. The inner list contains a tuple (coords) and a float (angle)
    # Every tuple includes the the coords (x, y) of a vertex
    polygon, points = getInput()

    PointAndConvexPolygon(polygon, points)
    # Plotting() # For testing reasons