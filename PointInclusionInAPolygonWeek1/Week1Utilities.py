import numpy as np
import math
from bisect import bisect_left

# Input - Two vertices (coords) of an edge and a point (coords)
# Output  - BORDER : Point on the edge, OUTSIDE : Ray from point on the left will not itersects the edge and INSIDE : Ray will intersect the edge
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
def PointAndConvexPolygon(poly, myPoints):
    # Find o point inside the Polygon
    # The point is the center mass of the three first vertices of the Polygon
    zX = (poly[0][0][0] + poly[1][0][0] + poly[2][0][0]) / 3
    zY = (poly[0][0][1] + poly[1][0][1] + poly[2][0][1]) / 3
    z = (zX, zY)

    # Fills the 3rd coord of every poly/vertex which was initialized by 0.0
    # This is angle between the positive horizontal axis and the ray of the vertex and z
    for i in range(len(poly)) :
        poly[i][1] = math.atan2(poly[i][0][1] - z[1], poly[i][0][0] - z[0])

    # Sort the list-poly by the angle (3rd coord)
    poly.sort(key = lambda x: x[1])
    polyAngles = [x[1] for x in poly]

    # Fills the 3rd coord of every point which was initialized by 0.0
    # This is angle between the positive horizontal axis and the ray of the point and z
    # Finds in which arc the Point belong and calls PointAndVector function
    for i in range(len(myPoints)):
        myPoints[i][1] = math.atan2(myPoints[i][0][1] - z[1], myPoints[i][0][0] - z[0])
        b = bisect_left(polyAngles, myPoints[i][1])
        if b == 0 or b == len(poly):    # The case where the angle of Point is below 1st vertex or over last vertex
            print(PointAndVector(poly[len(poly)-1][0], poly[0][0], myPoints[i][0]))
        else :
            print(PointAndVector(poly[b-1][0], poly[b][0], myPoints[i][0]))
