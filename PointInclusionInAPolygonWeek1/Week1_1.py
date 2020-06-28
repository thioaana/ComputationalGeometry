import numpy as np
import matplotlib.pyplot as plt
import sys


def PointAndVector(v0, v1, myPoint):
    if v0[1] < v1[1] :
        vStart = v0; vEnd = v1
    elif v0[1] > v1[1] :
        vStart = v1; vEnd = v0
    else :
        print("The vector has 0 length - Program aborts")
        sys.exit()

    a = np.array([vStart, vEnd, myPoint])
    b = np.ones((3, 1))
    d = np.hstack((a, b)) # append a column
    if np.linalg.det(d) > 0 :
        return "LEFT"
    elif np.linalg.det(d) < 0:
        return "RIGHT"
    else :
        if p[1] < vStart[1] or p[1] > vEnd[1] :
            return "ON LINE"
        else :
            return "ON SEGMENT"

if __name__ == '__main__':
    userInput = input("Enter coords of A and B with space between :").split()
    A = (int(userInput[0]), int(userInput[1]))
    B = (int(userInput[2]), int(userInput[3]))


    n = 0
    while n < 1 or n > 1000 :
        n = int(input("Enter the number of points : "))

    points = []
    for i in range(n):
        userInput = input("Enter coords of a point with space between :").split()
        (x, y) = (int(userInput[0]), int(userInput[1]))
        points.append((x, y))

    for p in points:
        print(PointAndVector(A, B, p))

    for p in points:
        plt.scatter(p[0], p[1])
    plt.plot([A[0], B[0]], [A[1], B[1]])
    plt.show()
