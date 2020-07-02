#uses python3

import numpy as np
# import matplotlib.pyplot as plt
import sys

def getInput():
    [aX, aY, bX, bY, cX, cY] = [int(i) for i in input().split()]
    polygon = []
    polygon.append((aX, aY))
    polygon.append((bX, bY))
    polygon.append((cX, cY))
    n = int(input())
    points = []
    for i in range(n):
        temp = input().split()
        points.append((int(temp[0]), int(temp[1])))
    return polygon, points

def PointAndVector(vStart, vEnd, myPoint):
    # Sum
    # over
    # the
    # edges, (x2 − x1)(y2 + y1).If
    # the
    # result is positive
    # the
    # curve is clockwise,
    # if it's negative the curve is counter-clockwise.


    # Checks if the vector has 0 length and aborts
    if vStart[0] == vEnd[0] and vStart[1] == vEnd[1]:
        print("The vector has 0 length - Program aborts")
        sys.exit()

    a = np.array([vStart, vEnd, myPoint])
    b = np.ones((3, 1))
    d = np.hstack((a, b))  # append a column
    det = np.linalg.det(d)
    if abs(det) < 0.00000001:  # Almost zero
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
    elif det > 0:
        return "LEFT"
    else :  # np.linalg.det(d) < 0:
        return "RIGHT"
    #
    # # For every case of det desides if the position of the Point
    # if abs(det) < 0.00000001 : # Almost zero
    #     if myPoint[0]>=min(vStart[0], vEnd[0]) and myPoint[0]<=max(vStart[0], vEnd[0]): return "BORDER"
    #     else : return "OUTSIDE"
    # if det > 0 : return "INSIDE"
    # if det < 0 : return "OUTSIDE"
    #
    # #DEGENERATE CASES
    # if vStart[1] == vEnd[1] : return "LEFT" # Because we don't care about horizontal edges
    # if vEnd[1] == myPoint[1] : return "LEFT"# Because we don't care about intersections on the upper end of the edge
    #
    # if det < 0 : return "RIGHT"

def PointAndTriangle(polygon, myPoint):#(a, b, c, myPoint):
    # myCount = 0
    for v in range(len(polygon)):
        if v < len(polygon) - 1 :
            position = PointAndVector(polygon[v], polygon[v + 1], myPoint)
        else :
            position = PointAndVector(polygon[-1], polygon[0], myPoint)
        if position == "ON_SEGMENT": return "BORDER"
        if position in ["RIGHT", "ON_LINE"] : return "OUTSIDE" #myCount += 1

    return "INSIDE"
    # if myCount % 2 == 0 : return "OUTSIDE"
    # else : return "INSIDE"

if __name__ == '__main__':
    polygon, points = getInput()

    for p in points:
        print(PointAndTriangle(polygon, p))
        # print(PointAndTriangle(A, B, C, p))

    # for p in points:
    #     plt.scatter(p[0], p[1])
    # plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]])
    # plt.show()
