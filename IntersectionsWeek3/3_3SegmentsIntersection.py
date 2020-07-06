#uses python3

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

    def doIntersect(self, u):
        orient1 = self.getOrientation(self.pStart, self.pEnd, u.pStart)
        orient2 = self.getOrientation(self.pStart, self.pEnd, u.pEnd)
        orient3 = self.getOrientation(u.pStart, u.pEnd, self.pStart)
        orient4 = self.getOrientation(u.pStart, u.pEnd, self.pEnd)

        # General cases
        if orient1 != orient2 and orient3 != orient4 :
            return "COMMON_POINT"

        # Co-linear cases
        if ((orient1 == 0) and self.getOrientation(self.pStart, u.pStart, self.pEnd)) or\
           ((orient2 == 0) and self.getOrientation(self.pStart, u.pEnd, self.pEnd)) or\
           ((orient3 == 0) and self.getOrientation(u.pStart, self.pStart, u.pEnd)) or\
           ((orient4 == 0) and self.getOrientation(u.pStart, self.pEnd, u.pEnd)):
            return "COMMON_SEGMENT"
        return "NO_COMMON"


def getInput():
    st = input().split()
    return (int(st[0]), int(st[1])), (int(st[2]), int(st[3]))

if __name__ == "__main__" :
    v1 = vector(getInput())
    v2 = vector(getInput())
    intersection = v1.doIntersect(v2)
    print(intersection)

