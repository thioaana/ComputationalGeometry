import numpy as np
import matplotlib.pyplot as plt
import math
from bisect import bisect_left
import sys
import copy
import Week1Utilities

def Plotting(myPolygons) :
    # Plotting several Polygons
    for polygon in myPolygons :
        xPol = [];  yPol = []
        for vertex in polygon :
            xPol.append(vertex[0]); yPol.append(vertex[1])
        xPol.append(xPol[0])
        yPol.append(yPol[0])
        plt.plot(xPol, yPol)
    plt.show()

def PointAndVector(vStart, vEnd, myPoint):
    # Checks if the vector has 0 length and aborts
    if vStart[0] == vEnd[0] and vStart[1] == vEnd[1]:
        print("The vector has 0 length - Program aborts")
        sys.exit()

    # Creates the matrix and calulates the det
    a = np.array([vStart, vEnd, myPoint], dtype = np.int64)
    b = np.ones((3, 1), dtype = np.int64)
    d = np.hstack((a, b)) # append a column
    det = np.linalg.det(d)

    # For every case of det desides if the position of the Point
    if abs(det) < 0.00000001 : # Almost zero
        if myPoint[0]>=min(vStart[0], vEnd[0]) and myPoint[0]<=max(vStart[0], vEnd[0]): return "BORDER"
        else : return "OUTSIDE"
    if det > 0 : return "INSIDE"
    if det < 0 : return "OUTSIDE"

# Input - A Convex Polygon and a list of Points
# Output - BORDER, OUTSIDE or INSIDE. The poiition of every  Point in terms of Polygon
def PointAndConvexPolygon(poly, myPoint):
    # Find o point inside the Polygon
    # The point is the center mass of the three first vertices of the Polygon
    zX = (poly[0][0] + poly[1][0] + poly[2][0]) / 3
    zY = (poly[0][1] + poly[1][1] + poly[2][1]) / 3
    z = (zX, zY)

    newPoly = [[(p[0], p[1]), 0.0] for p in poly]
    newPoint = [(myPoint[0], myPoint[1]), 0.0]

    # Fills the 3rd coord of every poly/vertex which was initialized by 0.0
    # This is angle between the positive horizontal axis and the ray of the vertex and z
    for i in range(len(newPoly)) :
        newPoly[i][1] = math.atan2(newPoly[i][0][1] - z[1], newPoly[i][0][0] - z[0])

    # Sort the list-poly by the angle (3rd coord)
    newPoly.sort(key = lambda x: x[1])
    polyAngles = [x[1] for x in newPoly]

    # Fills the 3rd coord of every point which was initialized by 0.0
    # This is angle between the positive horizontal axis and the ray of the point and z
    # Finds in which arc the Point belong and calls PointAndVector function

    newPoint[1] = math.atan2(newPoint[0][1] - z[1], newPoint[0][0] - z[0])
    b = bisect_left(polyAngles, newPoint[1])
    if b == 0 or b == len(newPoly):    # The case where the angle of Point is below 1st vertex or over last vertex
        return PointAndVector(newPoly[len(newPoly)-1][0], newPoly[0][0], newPoint[0])
    else :
        return PointAndVector(newPoly[b-1][0], newPoly[b][0], newPoint[0])


def merge2Polygons(pol1, pol2) :
    resultantPolygon = []

    # Find a point inside pol1.
    zX = (pol1[0][0] + pol1[1][0] + pol1[2][0]) / 3
    zY = (pol1[0][1] + pol1[1][1] + pol1[2][1]) / 3
    zInPol1 = (zX, zY)

    zIsInsidePol2 = PointAndConvexPolygon(pol2, zInPol1) # Find if zInPol1 is inside pol2.
    if zIsInsidePol2 == "INSIDE"  :
        # if z is in pol2
#       # The vertices are sorted by the angle around z.
#         # Apply to the resulting sorted list, Graham's scan.
#     # if z is not inside pol2 :
#         # Compute tangents through z to pol2.
#     # Check if z is on the border of pol2.
    return resultantPolygon


if __name__ == '__main__':
    # Reads and define the Polygons
    # The Polygon is a list of tuples. Every tuple includes the the coords (x, y) of a vertex

    n = 0 # Number of Polygons
    while n < 2 :
        n = int(input("Enter the number of Polygons : "))

    # -5 4 -3 3 2 2 8 2 5 5 -1 7
    # -5 -1 -1 -4 4 -2 1 1 -3 2
    polygons = []
    for n1 in range(n):
        onePolygon = []
        m = 0
        while m < 3 :
            print("Polygon ", n1 + 1, end = " ")
            m = int(input(" - Enter the number of Vertices of the Polygon : "))
        userInput = input("Enter coords of all Vertices with space between : ").split()
        for i in range(m):
            onePolygon.append((int(userInput[2 * i]), int(userInput[2 * i + 1])))
        polygons.append(onePolygon)



    # Merging Polygons
    polygon1 = polygons[0]
    for i in range(1, len(polygons)) :
        polygon1 = merge2Polygons(polygon1, polygons[i])

    Plotting(polygons)