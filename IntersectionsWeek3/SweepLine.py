import BSTLib

class segment:
    def __init__(self, p1, p2):
        self.pStart = p1
        self.pEnd = p2
        if (p2[0] - p1[0]) != 0 :
            lamda = (p2[1] - p1[1]) / (p2[0] - p1[0])
            beta = p1[1] - lamda * p1[0]
            self.equation = (p2[1] - p1[1], -(p2[0] - p1[0]), - beta * (p2[0] - p1[0])) # (dy, -dx, -β*dx)
        else :
            self.equation = (1, 0, p1[0])
    def getStartPoint(self): return self.pStart
    def getEndPoint(self): return self.pEnd

    def doIntersect(self, u):
        # λ*x - y = -β. The 2nd part of the equation is called or else
        D  = self.equation[0] * u.equation[1] - self.equation[1] * u.equation[0]
        Dx = self.equation[2] * u.equation[1] - self.equation[1] * u.equation[2]
        Dy = self.equation[0] * u.equation[2] - self.equation[2] * u.equation[0]

        # Find projections on X or Y
        if self.pStart[0] != self.pEnd[0]:  # The self vector is NOT vertical. Examine projection on X
            projectionS = (min(self.pStart[0], self.pEnd[0]), max(self.pStart[0], self.pEnd[0]))
            projectionU = (min(u.pStart[0], u.pEnd[0]), max(u.pStart[0], u.pEnd[0]))
        else:  # The self vector IS vertical. Examine projection on Y
            projectionS = (min(self.pStart[1], self.pEnd[1]), max(self.pStart[1], self.pEnd[1]))
            projectionU = (min(u.pStart[1], u.pEnd[1]), max(u.pStart[1], u.pEnd[1]))
        intervalIntersection = min(projectionS[1], projectionU[1]) - max(projectionS[0], projectionU[0])

        if D == 0 and (Dx !=0 or Dy != 0):
            return False, None # The system is impossible, ie parallel lines
        elif D == 0 and Dx == 0 and Dy == 0 :
            # The system has more than one solutions, ie the segments lie on the same line.
            if intervalIntersection == 0 :
                if projectionS[1] == projectionU[0] : commonPoint = self.pEnd
                else : commonPoint = self.pStart
                return True, commonPoint # The intersection point is commonPoint
            else : return False, None
        else :
            return True, (Dx/D, Dy/D)

def orderFunctionForQ(p1, p2) :
    if p1[1] < p2[1]   : return -1
    elif p1[1] > p2[1] : return 1
    else :
        if p1[0] < p2[0]   : return -1
        elif p1[0] > p2[0] : return 1
        else : return 0

def orderFunctionForT(s1, s2) :
    if s1[0][0] < s2[0][0]   : return -1
    elif p1[0] > p2[0] : return 1
    else :
        if s1[1][0] < s2[1][0]   : return -1
        else : return 1

if __name__ == "__main__" :
    # v1 = segment((0,0), (0, 2))
    # v2 = segment((0,0), (1, 0))
    # f, g = v1.doIntersect(v2)
    # There are two balanced BST.
    # T: Point as Key and a tuple as Value. Tuple contains a string Upper/Lower/Intersection and a pointer to the Segment
    # Q: Teh same structure as T
    T = BSTLib.BSTBalancedTree(orderFunctionForT)
    Q = BSTLib.BSTBalancedTree(orderFunctionForQ)
    Intersections = {}
    segments = []
    for i in range(25) :
        st = input().split()
        p1 = (int(st[0]), int(st[1]))
        p2 = (int(st[2]), int(st[3]))
        if orderFunctionForQ(p1, p2) == -1 :
            temp = p1[:]
            p1 = p2
            p2 = temp
        segments.append(segment(p1, p2))
        Q.insert(p1, ("Upper", i))
        Q.insert(p2, ("Lower", i))

    # Loop until Q is empty
    while Q.getRoot() :
        # Get the next Event Point ie most upper point from Q - Queue Event
        curEventPoint = Q.getMaximumKey(Q.getRoot())
        Q.delete(curEventPoint.getKey())

        # Handle event
        T.insert(segments[curEventPoint.getValue()[1]], None)

        # Find left and right neighbors in T
        leftNeighbor = T.getMaximumKey(curEventPoint.getLeft())
        rightNeighbor = T._getSuccessor(curEventPoint.getRight())

        if curEventPoint.getValue()[0] == "Upper" :
            # Find Intersections between currSegment and neighbors
            found, intersection = currSegment.doIntersect(leftSegment)
            if found :
                Q.insert(intersection, ("Intersection", 0))
                if intersection not in Intersections :
                    Intersections[intersection]=[curEventPoint.getValue()[1], leftNeighbor.getValue()[1]]
                else :
                    if curEventPoint.getValue()[1] not in Intersections[intersection] :Intersections[intersection].append(curEventPoint.getValue()[1])
                    if leftNeighbor.getValue()[1] not in Intersections[intersection]: Intersections[intersection].append(leftNeighbor.getValue()[1])
            found, intersection = currSegment.doIntersect(rightSegment)
            if found :
                Q.insert(intersection, ("Intersection", 0))
                if intersection not in Intersections:
                    Intersections[intersection] = [curEventPoint.getValue()[1], rightNeighbor.getValue()[1]]
                else :
                    if curEventPoint.getValue()[1] not in Intersections[intersection] :Intersections[intersection].append(curEventPoint.getValue()[1])
                    if rightNeighbor.getValue()[1] not in Intersections[intersection]: Intersections[intersection].append(rightNeighbor.getValue()[1])
        elif curEventPoint.getValue()[0] == "Lower" :
            # Find Intersections between neighbors
            found, intersection = leftSegment.doIntersect(rightSegment)
            if found:
                Q.insert(intersection, ("Intersection", 0))
                if intersection not in Intersections:
                    Intersections[intersection] = [leftNeighbor.getValue()[1], rightNeighbor.getValue()[1]]
                else :
                    if leftNeighbor.getValue()[1] not in Intersections[intersection]: Intersections[intersection].append(leftNeighbor.getValue()[1])
                    if rightNeighbor.getValue()[1] not in Intersections[intersection]: Intersections[intersection].append(rightNeighbor.getValue()[1])
            # Delete curEventPoint from T
            T.delete(segments[curEventPoint.getValue()[1]])
        else : # Intersection Point
            # Write Code
            for i in Intersections[curEventPoint.getKey()] :
                T.delete(segments[i])
                segments[i] = (curEventPoint.getKey(), segments[i][1])
                T.insert(segments[i], None)
            print(curEventPoint.getKey())
