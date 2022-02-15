from vector3 import *

def doPlaneParam():
    sup3 = vector3(0, 1, 5)
    clamp3A = vector3(5, 7,1)
    clamp3B = vector3(2, -1, 2)

    plane = plane3param(sup3, clamp3A, clamp3B)

    newPoint = plane.point(4, 2)
    newPoint.print()

    newPoint = plane.normalVector()
    newPoint.print()

    coordPlane = plane.coordForm()
    coordPlane.print()

    normalPlane = plane.normalForm()
    normalPlane.print()

def doPlaneNormal():
    normalV = vector3(1, 5, 6)
    supportV = vector3(2, 5, 1)
    normalPlane = plane3normal(normalV, supportV)
    normalPlane.print()
    paramForm = normalPlane.paramForm()
    paramForm.print()
    newNormal = paramForm.normalForm()
    newNormal.print()

def plane():
    plane = plane3(None, None, None)
    plane.print()

def main():
    #len vector calc
    vA = vector3(1, 5, 7)
    vB = vector3(5, -1, 2)

    vA.print()

    print(sumVector3(vA))

    print(dotProduct(vA, vB))

    #calc vektor between two
    calcVector3(vA, vB).print()

    #add two vektors
    addVector3(vA, vB).print()

    crossProduct(vA, vB).print()


if __name__ == '__main__':
    plane()