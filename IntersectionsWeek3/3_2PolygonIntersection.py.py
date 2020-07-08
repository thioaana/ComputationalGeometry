#uses python3

import matplotlib.pyplot as plt
import sys

def Plotting(polygon, c) :
    # Plotting Polygon
    xPol = []; yPol = []
    for pol in polygon :
        xPol.append(pol[0]); yPol.append(pol[1])
    xPol.append(xPol[0]); yPol.append(yPol[0])
    plt.plot(xPol, yPol, c)

    plt.show()

def getInput():
    m= int(input())
    polygon = []
    st = [int(i) for i in input().split()]
    for i in range(0, 2 * m, 2) :
        polygon.append((st[i], st[i + 1]))
    return polygon

def isRightTurn(vStart, vEnd, myPoint) :
    det = (vEnd[0] - vStart[0]) * (myPoint[1] - vStart[1]) - (myPoint[0] - vStart[0]) * (vEnd[1] - vStart[1])
    if det < 0 : return True
    else : return False

def intersectionPoint(eP, eQ) :
    # λ = dy / dx. y = λ * x + β. The equation is -dy*x + dx*y = β*dx. The 2nd part of the equation is called C.
    dxEP = eP[1][0] - eP[0][0]
    dyEP = eP[1][1] - eP[0][1]
    cEP = -dyEP * eP[0][0] + dxEP * eP[0][1]

    dxEQ = eQ[1][0] - eQ[0][0]
    dyEQ = eQ[1][1] - eQ[0][1]
    cEQ  = -dyEQ * eQ[0][0] + dxEQ * eQ[0][1]

    D = -dyEP * dxEQ + dxEP * dyEQ
    Dx = -dyEP * cEQ + dyEQ * cEP
    Dy = cEP * dxEQ - cEQ * dxEP
    return (Dy/D, Dx/D, )

def addVertices(eP, eQ) :
    # Both eP[0] and eP[1] lies on Q side of eQ. return eP[1]
    if not isRightTurn(eQ[0], eQ[1], eP[0]) and not isRightTurn(eQ[0], eQ[1], eP[1]) :
        return [eP[1]]

    # Only eP[1] lies on Q side of eQ. Return intersection point and eP[1]
    elif isRightTurn(eQ[0], eQ[1], eP[0]) and not isRightTurn(eQ[0], eQ[1], eP[1]):
        return [intersectionPoint(eP, eQ), eP[1]]

    # Only eP[0] lies on Q side of eQ. Return intersection point
    elif not isRightTurn(eQ[0], eQ[1], eP[0]) and isRightTurn(eQ[0], eQ[1], eP[1]):
        return [intersectionPoint(eP, eQ)]

    # Nor eP[0] neither eP[1] lies on Q side of eQ. Return nothing
    else : pass

    return

def SutherlandHogman(P, Q) :
    polygon = P[:]
    eQ = [Q[-1]]
    for q in range(len(Q)) :
        eQ.append(Q[q])
        if polygon :eP = [polygon[-1]]
        tempPolygon = []
        for p in range(len(polygon)) :
            eP.append(polygon[p])
            temp = addVertices(eP, eQ)
            if temp :tempPolygon.extend(temp)
            eP = [polygon[p]]
        polygon = tempPolygon[:]
        # Plotting(P, "b")  # For testing reasons
        # Plotting(Q, "g")  # For testing reasons
        # Plotting(polygon, "r")  # For testing reasons
        eQ = [Q[q]]
    return polygon

if __name__ == '__main__':
    P = getInput()
    Q = getInput()

    # Plotting(P, "b") # For testing reasons
    # Plotting(Q ,"g")  # For testing reasons
    # plt.show()

    intersection  = SutherlandHogman(P, Q)
    print(len(intersection))
    for v in intersection:
        print(round(v[0]), round(v[1]), end=" ")

