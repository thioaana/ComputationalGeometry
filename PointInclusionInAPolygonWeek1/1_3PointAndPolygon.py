import numpy as np
import matplotlib.pyplot as plt
import sys

# Input - Two vertices (coords) of an edge and a point (coords)
# Output  - BORDER : Point on the edge, OUTSIDE : Ray from point on the left will not itersects the edge and INSIDE : Ray will intersect the edge
def PointAndVector(v0, v1, myPoint):
    # Checks if the vector has 0 length and aborts
    if v0[0] == v1[0] and v0[1] == v1[1]:
        print("The vector has 0 length - Program aborts")
        sys.exit()

    # vStart is the lower vertix and vEnd is the upper vertix
    if v0[1] <= v1[1] :
        vStart = v0; vEnd = v1
    elif v0[1] > v1[1] :
        vStart = v1; vEnd = v0

    if vStart[1] == vEnd[1] : return "OUTSIDE" # Ignore horizontal edges
    if myPoint[1] < vStart[1] or myPoint[1] > vEnd[1] : return "OUTSIDE" # Ignore cases where point is beyond edge in order of y axis

    a = np.array([vStart, vEnd, myPoint], dtype = np.int64)
    b = np.ones((3, 1), dtype = np.int64)
    d = np.hstack((a, b)) # append a column
    det = np.linalg.det(d)

    if abs(det) < 0.00000001 : return "BORDER"  # Almost zero
    if det > 0 :  return "OUTSIDE"
    if det < 0 :
        if vEnd[1] == myPoint[1] : return "OUTSIDE"# Ignore intersections on the upper end of the edge
        else : return "INSIDE"

# Input - A Polygon and a Point
# Output - BORDER, OUTSIDE or INSIDE. The poistion of the Point in terms of Polygon
def PointAndPolygon(poly, myPoint):
    #Create the edges of the polygon
    edges = []
    for i in range(len(poly)-1):
        edges.append((poly[i], poly[i+1]))
    edges.append((poly[len(poly) - 1], poly[0]))

    myCount = 0
    for edge in edges :
        position = PointAndVector(edge[0], edge[1], myPoint)
        if position == "BORDER": return "BORDER"
        if position == "INSIDE" : myCount += 1

    if myCount % 2 == 0 : return "OUTSIDE"
    else : return "INSIDE"

if __name__ == '__main__':
    # Reads and define the Polygon
    m = 0
    while m < 3 or m > 200 :
        m = int(input("Enter the number of Vertices of the Polygon : "))
    userInput = input("Enter coords of all Vertices with space between :").split()

    polygon = []
    # polygon = [(-3, -1), (3, -1), (3, 5), (0, 2), (-3, 4)]
    for i in range(m):
        polygon.append((int(userInput[2 * i]), int(userInput[2 * i + 1])))

    # Reads and define the Points
    n = 0
    while n < 1 or n > 200 :
        n = int(input("Enter the number of points : "))

    points = []
    for i in range(n):
        userInput = input("Enter coords of a point with space between :").split()
        points.append((int(userInput[0]), int(userInput[1])))

    for p in points:
        print(PointAndPolygon(polygon, p))

    # PLOTTING
    # Plotting Polygon
    xPol = []; yPol = []
    for pol in polygon :
        xPol.append(pol[0]); yPol.append(pol[1])
    xPol.append(xPol[0]); yPol.append(yPol[0])
    plt.plot(xPol, yPol)

    # Plotting Points
    for p in points:
        plt.scatter(p[0], p[1])
    plt.show()
