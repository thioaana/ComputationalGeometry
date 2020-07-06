#uses python3
# Help : http://geomalgorithms.com/a15-_tangents.html#tangent_PointPoly()
import matplotlib.pyplot as plt

def Plotting() :
    # Plotting Polygon
    xPol = []; yPol = []
    for pol in polygon :
        xPol.append(pol[0]); yPol.append(pol[1])
    xPol.append(xPol[0])
    yPol.append(yPol[0])
    plt.plot(xPol, yPol)

    # Plotting Points
    for p in points:
        plt.scatter(p[0], p[1])
    plt.show()

def getInput():
    m = int(input())
    st = input().split()
    polygon = [(int(st[i]), int(st[i + 1])) for i in range(0, 2 * m, 2)]

    n = int(input())
    points = []
    for i in range(n):
        temp = input().split()
        points.append((int(temp[0]), int(temp[1])))
    return polygon, points

def computeDet(vStart, vEnd, myPoint) :
    return (vEnd[0] - vStart[0]) * (myPoint[1] - vStart[1]) - (myPoint[0] - vStart[0]) * (vEnd[1] - vStart[1])

def TengentsToPolygon(polygon, points) :
    tangents = []
    for p in points :
        tan = [0, 0] # [lTangent, rTangent
        detPrev = computeDet(polygon[0], polygon[1], p)
        for i in range(1, len(polygon)) :
            if i == len(polygon) - 1: detNext = computeDet(polygon[i], polygon[0], p)
            else : detNext = computeDet(polygon[i], polygon[i + 1], p)
            if detPrev <= 0 and detNext > 0 :
                if computeDet(p, polygon[i], polygon[tan[1]]) >= 0 :  tan[1] = i
            elif detPrev > 0 and detNext <= 0 :
                if computeDet(p, polygon[i], polygon[tan[0]]) <= 0:  tan[0] = i
            detPrev = detNext
        print(polygon[tan[0]][0], polygon[tan[0]][1], polygon[tan[1]][0], polygon[tan[1]][1])

if __name__ == '__main__':
    polygon, points = getInput()

    # Plotting() # For testing reasons
    TengentsToPolygon(polygon, points)

