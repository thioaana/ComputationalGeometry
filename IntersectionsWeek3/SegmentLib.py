# uses python3

class vector:
    def __init__(self, v):
        self.pStart = v[0]
        self.pEnd = v[1]

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
            return True, (int(Dx/D), int(Dy/D))
        else :
            if self.pStart[0] != self.pEnd[0] : # The self vector is NOT vertical
                projectionS = (min(self.pStart[0], self.pEnd[0]), max(self.pStart[0], self.pEnd[0]))
                projectionU = (min(u.pStart[0], u.pEnd[0]), max(u.pStart[0], u.pEnd[0]))

            else :
                projectionS = (min(self.pStart[1], self.pEnd[1]), max(self.pStart[1], self.pEnd[1]))
                projectionU = (min(u.pStart[1], u.pEnd[1]), max(u.pStart[1], u.pEnd[1]))
            intervalIntersection = min(projectionS[1], projectionU[1]) - max(projectionS[0], projectionU[0])
            if intervalIntersection < 0 :
                return False, (0, 0)
            elif intervalIntersection > 0 :
                return False, (0, 0) #A common segment of non-zero length
            else :
                if projectionS[1] == projectionU[0] : commonPoint = self.pEnd
                else : commonPoint = self.pStart
                return False, commonPoint #The intersection point is ", commonPoint
        return