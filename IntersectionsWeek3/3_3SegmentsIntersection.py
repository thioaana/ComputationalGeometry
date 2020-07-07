# uses python3

import sys

class vector:
    def __init__(self, v):
        self.pStart = v[0]
        self.pEnd = v[1]

    def getOrientation(self, p1, p2, p3):
        d = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])
        if d > 0 : return 1     # Counter Clockwise
        elif d <0 : return 2   # Clockwise
        else : return 0         # co-linear

    # q point lies on pr segment
    def onSegment(self, p, q, r):
        if ((q[0] <= max(p[0], r[0])) and (q[0] >= min(p[0], r[0])) and (q[1] <= max(p[1], r[1])) and (q[1] >= min(p[1], r[1]))):
            return True
        return False
    # def getCommonPoint(self, u) :
    #     def det(a, b) :
    #         return  a[0] * b[1] - a[1] * b[0]
    #
    #     # λ = dy / dx. y = λ * x + β. The equation is -dy*x + dx*y = β*dx. The 2nd part of the equation is called C.
    #     dxS = self.pEnd[0] - self.pStart[0]
    #     dyS = self.pEnd[1] - self.pStart[1]
    #     cS = -dyS * self.pStart[0] + dxS * self.pStart[1]
    #
    #     dxU = u.pEnd[0] - u.pStart[0]
    #     dyU = u.pEnd[1] - u.pStart[1]
    #     cU = -dyU * u.pStart[0] + dxU * u.pStart[1]
    #
    #     D = -dyS * dxU + dxS * dyU
    #     Dx = -dyS * c2 + dyU * c1
    #     Dy = c1 * dxU - c2 * dxS
    #
    #     if D != 0
    #         print("The intersection point is ", (dx/D, dy/D), ".")
    #     elif Dx != or Dy !=0 :
    #         print("No common points.")
    #     else :
    #         print("A common segment of non-zero length.")
    #     return
    #
    #
    #     l1 = (self.pEnd[1] - self.pStart[1]) / (self.pEnd[0] - self.pStart[0])
    #     l2 = (u.pEnd[1] - u.pStart[1]) / (u.pEnd[0] - u.pStart[0])
    #     c1 = -l1 * self.pStart[0] + self.pStart[1]
    #     c2 = -l2 * u.pStart[0] + u.pStart[1]
    #
    #     D  = det((-l1, 1), (-l2, 1))
    #     if D == 0: return (sys.maxsize, sys.maxsize)
    #     else :
    #         Dx = det((-l1, c1),(-l2, c2))
    #         Dy = det((c1, 1),(c2, 1))
    #         return (Dx/D, Dy/D)
    #
    #     xdiff = (self.pStart[0] - self.pEnd[0], u.pStart[0] - u.pEnd[0])
    #     ydiff = (self.pStart[1] - self.pEnd[1], u.pStart[1] - u.pEnd[1])
    #     div = det(xdiff, ydiff) # D
    #     if div == 0 : return (sys.maxsize, sys.maxsize)
    #     d = (det(*line1), det(*line2))
    #     x = det(d, xdiff) / div
    #     y = det(d, ydiff) / div


    def doIntersect(self, u):
        # λ = dy / dx. y = λ * x + β. The equation is -dy*x + dx*y = β*dx. The 2nd part of the equation is called C.
        dxS = self.pEnd[0] - self.pStart[0]
        dyS = self.pEnd[1] - self.pStart[1]
        cS = -dyS * self.pStart[0] + dxS * self.pStart[1]

        dxU = u.pEnd[0] - u.pStart[0]
        dyU = u.pEnd[1] - u.pStart[1]
        cU = -dyU * u.pStart[0] + dxU * u.pStart[1]

        D = -dyS * dxU + dxS * dyU
        Dx = -dyS * cU + dyU * cS
        Dy = cS * dxU - cU * dxS

        if D != 0 :
            print("The intersection point is ", (int(Dx/D), int(Dy/D)), ".")
        else :
            if self.pStart[0] != self.pEnd[0] : # The self vector is NOT vertical
                projectionS = (min(self.pStart[0], self.pEnd[0]), max(self.pStart[0], self.pEnd[0]))
                projectionU = (min(u.pStart[0], u.pEnd[0]), max(u.pStart[0], u.pEnd[0]))

            else :
                projectionS = (min(self.pStart[1], self.pEnd[1]), max(self.pStart[1], self.pEnd[1]))
                projectionU = (min(u.pStart[1], u.pEnd[1]), max(u.pStart[1], u.pEnd[1]))
            intervalIntersection = min(projectionS[1], projectionU[1]) - max(projectionS[0], projectionU[0])
            if intervalIntersection < 0 :
                print("No common points.")
            elif intervalIntersection > 0 :
                print("A common segment of non-zero length.")
            else :
                if projectionS[1] == projectionU[0] : commonPoint = self.pEnd
                else : commonPoint = self.pStart
                print("The intersection point is ", commonPoint, ".")
        return

        # orient1 = self.getOrientation(self.pStart, self.pEnd, u.pStart)
        # orient2 = self.getOrientation(self.pStart, self.pEnd, u.pEnd)
        # orient3 = self.getOrientation(u.pStart, u.pEnd, self.pStart)
        # orient4 = self.getOrientation(u.pStart, u.pEnd, self.pEnd)
        #
        # # General cases
        # if orient1 != orient2 and orient3 != orient4 :
        #     getCommonPoint(u, intersectionPoint)
        #     print("The intersection point is ", u.pStart, "."); return
        #
        # # Co-linear cases
        # if ((orient1 == 0) and self.onSegment(self.pStart, u.pStart, self.pEnd)) or\
        #    ((orient2 == 0) and self.onSegment(self.pStart, u.pEnd, self.pEnd)) or\
        #    ((orient3 == 0) and self.onSegment(u.pStart, self.pStart, u.pEnd)) or\
        #    ((orient4 == 0) and self.onSegment(u.pStart, self.pEnd, u.pEnd)):
        #     if u.pStart in [self.pStart, self.pEnd] : print("The intersection point is ", u.pStart, "."); return
        #     elif u.pEnd in [self.pStart, self.pEnd] : print("The intersection point is ", u.pEnd, "."); return
        #     else :
        #         print("A common segment of non-zero length."); return
        # print("No common points."); return


def getInput():
    st = input().split()
    return (int(st[0]), int(st[1])), (int(st[2]), int(st[3]))

if __name__ == "__main__" :
    v1 = vector(getInput())
    v2 = vector(getInput())
    intersection = v1.doIntersect(v2)
