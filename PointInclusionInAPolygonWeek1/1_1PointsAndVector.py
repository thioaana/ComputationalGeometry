#uses python3

# import matplotlib.pyplot as plt
# import sys

def getInput():
    [aX, aY, bX, bY] = [int(i) for i in input().split()]
    a = (aX, aY)
    b = (bX, bY)
    n = int(input())
    p = []
    for i in range(n):
        temp = input().split()
        p.append((int(temp[0]), int(temp[1])))
    return a, b, p

def PointAndVector(vStart, vEnd, myPoint):
    det = (vEnd[0] - vStart[0]) * (myPoint[1] - vStart[1]) - (myPoint[0] - vStart[0]) * (vEnd[1] - vStart[1])
    if np.linalg.det(d) > 0:
        return "LEFT"
    elif np.linalg.det(d) < 0:
        return "RIGHT"
    else:
        maxVertical = max(vStart[1], vEnd[1])
        minVertical = min(vStart[1], vEnd[1])
        maxHorizontal = max(vStart[0], vEnd[0])
        minHorizontal = min(vStart[0], vEnd[0])
        if vStart[1] != vEnd[1] : # In case of non - horizontal vector
            if p[1] < minVertical or p[1] > maxVertical:
                return "ON_LINE"
            else:
                return "ON_SEGMENT"
        else:  # In case of horizontal vector
            if p[0] < minHorizontal or p[0] > maxHorizontal:
                return "ON_LINE"
            else:
                return "ON_SEGMENT"

if __name__ == '__main__':
    A, B, points = getInput()
    for p in points:
        print(PointAndVector(A, B, p))

    # Plotting - For testing reasons
    # for p in points:
    #     plt.scatter(p[0], p[1])
    # plt.plot([A[0], B[0]], [A[1], B[1]])
    # plt.show()