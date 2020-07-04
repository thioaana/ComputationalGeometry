# uses python3

# import matplotlib.pyplot as plt

def Plotting(p, shape) :
    xP = []; yP = []
    for p1 in p :
        xP.append(p1[0]); yP.append(p1[1])

    # Plotting Polygon
    if shape == "POLYGONUp":
        plt.plot(xP, yP)
    if shape == "POLYGON":
        plt.plot(xP, yP)
        plt.show()
    # Plotting Points
    if shape == "POINTS" :
        plt.scatter(xP, yP)
        plt.show()

def getIput() :
    n = int(input())
    st = input().split()
    points = [(int(st[i]), int(st[i + 1])) for i in range(0, 2 * n, 2)]
    return points

def computeDet(vStart, vEnd, myPoint) :
    det = (vEnd[0] - vStart[0]) * (myPoint[1] - vStart[1]) - (myPoint[0] - vStart[0]) * (vEnd[1] - vStart[1])
    return det

def handleUpLow(d, st):
    if st == "Upper" :
        if d > 0 : return True
        elif d<0 : return False
    else :
        if d < 0 : return True
        elif d>0 : return False

def BuildConvexHull(myPoints, UpLow) :
    myP = myPoints[:]
    myP.sort(key = lambda x: x[0], reverse = True)
    LUpper = [myP.pop(), myP.pop()]
    while myP :
        LUpper.append(myP.pop())
        det = computeDet(LUpper[-3], LUpper[-2], LUpper[-1])
        while len(LUpper) > 2 and (handleUpLow(det, UpLow) or det == 0):
        # while len(LUpper) > 2 and det >= 0 :
            if det == 0:
                temp = [LUpper.pop(),LUpper.pop(),LUpper.pop()]
                temp.sort()
                LUpper.extend(temp)
                LUpper.remove(LUpper[-2])
            if handleUpLow(det, UpLow) :
            # if det > 0 :
                LUpper.remove(LUpper[-2])
            if len(LUpper) > 2 :
                det = computeDet(LUpper[-3], LUpper[-2], LUpper[-1])
    return LUpper

# def BuildConvexHullLower(myPoints) :
#     myPoints.sort(key = lambda x: x[0])
#     LLower = [myPoints[0], myPoints[1]]
#     for i in range(2, len(myPoints)) :
#         LLower.append(myPoints[i])
#         det = -1
#         while len(LLower) > 2 and det <= 0:
#             # Creates the matrix and calulates the det
#             a = np.array([LLower[-3], LLower[-2], LLower[-1]], dtype = np.int64)
#             b = np.ones((3, 1), dtype = np.int64)
#             d = np.hstack((a, b)) # append a column
#             det = np.linalg.det(d)
#             if det < 0 :
#                 LLower.remove(LLower[-2])
#             if det == 0 :
#                 temp = []
#                 temp.append(LLower.pop());temp.append(LLower.pop());temp.append(LLower.pop())
#                 temp.sort()
#                 LLower.extend(temp)
#                 LLower.remove(LLower[-2])
#     return LLower

if __name__ == '__main__':
    points = getIput()
    polUpper = BuildConvexHull(points, "Upper")
    polLower = BuildConvexHull(points, "Lower")
    if polUpper[-1] == polLower[-1] : del polUpper[-1]
    if polUpper[0] == polLower[0] :del polUpper[0]
    polygon = polLower
    while polUpper:
        polygon.append(polUpper.pop())
    print(len(polygon))
    print(polygon)
    # print(polUpper)
    # print("PLo", polLower)
    # Plotting(points, "POINTS")
    # Plotting(polUpper, "POLYGONUp")
    # Plotting(polLower, "POLYGON")