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
    normalV = vector3(1, 2, 1)
    supportV = vector3(1, 3, 2)
    normalPlane = plane3normal(normalV, supportV)
    normalPlane.print()
    coordForm = normalPlane.coordForm()
    coordForm.print()

def coordtoNormal():
    coordPlane = plane3coord(1, 4, 5, 2)
    normalPlane = coordPlane.normalForm()
    normalPlane.print()

def plane():
    coordPlane = plane3coord(4, 4, 2, 1)
    plane = plane3(None, None, coordPlane)
    plane.print()

def coordToParam():
    coordPlane = plane3coord(5, 2, 1, 25)
    paramPlane = coordPlane.paramForm()
    paramPlane.print()

def createLine():
    supV = vector3(1, 3, 2)
    dirV = vector3(2, 1, 5)
    line = line3(supV, dirV)
    line.print()
    line.point(5).print()

def testVector():
    """
    inverts the vector
    :return: None
    """
    aV = vector3(1, 4 ,2)
    aV.invert().print()

def testMidandPointPlane():
    # mid point test
    vA = vector3(1, 3, 4)
    vB = vector3(2, 3, 1)

    vC = midVector3(vA, vB)
    vC.print()

    print("\n")

    # 3point plane test
    pointA = vector3(1, 2, 3)
    pointB = vector3(0, 5, 2)
    pointC = vector3(2, 1, 0)

    plane = point3plane(pointA, pointB, pointC)
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

def lineCross():
    lAVa = vector3(3, 4, 1)
    lAVb = vector3(2, 1, 3)

    lineA = line3(lAVa, lAVb)

    lBVa = vector3(1, 2, 3)
    lBVb = vector3(5, 3, 2)

    lineB = line3(lBVa, lBVb)

    compareLines(lineA, lineB)

def unitV():
    vA = vector3(2, 4, 4)
    vB = vA.unit().print()

def v3Test():
    vA = vector3(1)
    vA.print()

def testPlaneNew():
    planeCoord = plane3coord(1, 2, 3, 4)
    plane = plane3(planeCoord)
    plane.print()

if __name__ == '__main__':
   #testMidandPointPlane()
   #doPlaneParam()
   #doPlaneNormal()
   #coordtoNormal()
   #plane()
   #coordToParam()
   #createLine()
   #testVector()
   #testMidandPointPlane()
   #main()
   #lineCross()
   #unitV()
   #v3Test()
   testPlaneNew()
