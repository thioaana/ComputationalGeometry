#uses python3

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

def fixOrientation(v0, v1):
    if v0[1] <= v1[1] :
        vStart = v0[:]
        vEnd = v1[:]
    else :
        vStart = v1[:]
        vEnd = v0[:]
    return vStart, vEnd

def PointAndVector(v0, v1, myPoint):
    vStart, vEnd = fixOrientation(v0, v1)

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

    # DEGENERATE CASES
    if vStart[1] == vEnd[1]: return "LEFT"  # Edge is horizontal and point is out of the line
    if vEnd[1] == myPoint[1]: return "LEFT" # Intersections on the upper end of the edge.

    if det > 0:
        return "LEFT"
    else :  # np.linalg.det(d) < 0:
        if myPoint[1] in range(vStart[1], vEnd[1]) : return "RIGHT"
        else : return "LEFT"

def PointAndTriangle(polygon, myPoint):#(a, b, c, myPoint):
    myCount = 0
    for v in range(len(polygon)):
        if v < len(polygon) - 1 :
            position = PointAndVector(polygon[v], polygon[v + 1], myPoint)
        else :
            position = PointAndVector(polygon[-1], polygon[0], myPoint)
        if position == "ON_SEGMENT": return "BORDER"
        if position in ["RIGHT"]:
            myCount += 1

    if myCount % 2 == 0 : return "OUTSIDE"
    else : return "INSIDE"

if __name__ == '__main__':
    polygon, points = getInput()

    for p in points:
        print(PointAndTriangle(polygon, p))

    # for p in points:
    #     plt.scatter(p[0], p[1])
    # plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]])
    # plt.show()
