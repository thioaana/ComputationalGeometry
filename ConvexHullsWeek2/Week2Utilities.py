import numpy as np
import math
import Week1Utilities

def PolygonConvexOrNot(poly):
    # Fills the 3rd coord of every poly/vertex which was initialized by 0.0
    # This is angle between the positive horizontal axis and the ray of the vertex and z
    for i in range(len(poly)) :
        if i == len(poly) - 1 :
            v0 = poly[i]; v1 = poly[0]
        else :
            v0 = poly[i]; v1 = poly[i+1]
        for j in range(len(poly)) :
            res = Week1Utilities.PointAndVector(v0, v1, poly[j])
            if res == "OUTSIDE" : return "NOT_CONVEX"
    return "CONVEX"
