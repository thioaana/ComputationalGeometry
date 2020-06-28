import numpy as np
import matplotlib.pyplot as plt
import sys

def PointAndVector(v0, v1, myPoint):
    # Checks if the vector has 0 length
    if v0[0] == v1[0] and v0[1] == v1[1]:
        print("The vector has 0 length - Program aborts")
        sys.exit()

    if v0[1] <= v1[1] :
        vStart = v0; vEnd = v1
    elif v0[1] > v1[1] :
        vStart = v1; vEnd = v0


    a = np.array([vStart, vEnd, myPoint], dtype = np.int64)
    b = np.ones((3, 1), dtype = np.int64)
    d = np.hstack((a, b)) # append a column
    det = np.linalg.det(d)
    if abs(det) < 0.00000001 : # Very close to 0
        if p[1] < vStart[1] or p[1] > vEnd[1] : return "ON LINE"
        else : return "ON SEGMENT"
    if det > 0 :  return "LEFT"

    #DEGENERATE CASES
    if vStart[1] == vEnd[1] : return "LEFT" # Because we don't care about horizontal edges
    if vEnd[1] == myPoint[1] : return "LEFT"# Because we don't care about intersections on the upper end of the edge

    if det < 0 : return "RIGHT"

def PointAndTriangle(a, b, c, myPoint):
    edges = [(a, b), (b, c), (a, c)]
    myCount = 0

    for edge in edges :
        position = PointAndVector(edge[0], edge[1], myPoint)
        if position == "ON SEGMENT": return "BORDER"
        if position == "RIGHT" : myCount += 1

    if myCount % 2 == 0 : return "OUTSIDE"
    else : return "INSIDE"

if __name__ == '__main__':
    userInput = input("Enter coords of A, B and C with space between :").split()
    # userInput = [1, 0, 0, 3, 3, 3]
    A = (int(userInput[0]), int(userInput[1]))
    B = (int(userInput[2]), int(userInput[3]))
    C = (int(userInput[4]), int(userInput[5]))

    n = 0
    while n < 1 or n > 1000 :
        n = int(input("Enter the number of points : "))

    points = []
    for i in range(n):
        userInput = input("Enter coords of a point with space between :").split()
        (x, y) = (int(userInput[0]), int(userInput[1]))
        points.append((x, y))

    for p in points:
        print(PointAndTriangle(A, B, C, p))

    for p in points:
        plt.scatter(p[0], p[1])
    plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]])
    plt.show()
