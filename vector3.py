import math

class vector3:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def print(self):
        """
        prints the vector3 because printing
        :return:
        """

        values = [self.x1, self.x2,  self.x3]
        print(values)

    def vis(self):
        """
        gets you the values of the vector as an array
        [1, -4, 7]
        :return: the values of the vector as an array [self.x1, self.x2, self.x3]
        """

        values = [self.x1, self.x2, self.x3]
        return values

class plane3param:
    def __init__(self, supportV3, clampingA, clampingB):
        self.supportV = supportV3
        self.clampingA = clampingA
        self.clampingB = clampingB

    def point(self, r, s):
        """
        gets you a point at the plane in form of a vector 3
        to get the values printed type a .print() after your var
        :param r: value r --> real Number
        :param s: value s --> real Number
        :return: the vector of the point on the plane
        """

        r3 = multiplyVektor3(self.clampingA, r)
        s3 = multiplyVektor3(self.clampingB, s)

        return addVector3(addVector3(self.supportV, r3), s3)

    def normalVector(self):
        """
        does the cross product of clampingA and clampingB to get the
        normal vector
        :return: normal Vector of the plane
        """
        return crossProduct(self.clampingA, self.clampingB)

    def coordForm(self):
        """
        returns the coord Form of the plane
        :return: coord form of the plane
        """

        normalV = self.normalVector()
        n = -dotProduct(normalV, self.supportV)

        coordPlane = plane3coord(normalV.x1, normalV.x2, normalV.x3, n)
        return coordPlane

    def normalForm(self):
        """
        returns the normal form of the plane
        :return: normal form of the plane
        """
        n = self.normalVector()

        normPlane3 = plane3normal(n, self.supportV)
        return normPlane3

    def print(self):
        """
        prints the param form of the plane to vis for debug

        e.g.
        x-> = [2, 5, 1] + r * [0, 6, -5] + s * [5, -1, 0]

        :return:
        """
        support = self.supportV
        clampA = self.clampingA
        clampB = self.clampingB

        print(f"x-> = {support.vis()} + r * {clampA.vis()} + s * {clampB.vis()}")


class plane3coord:
    def __init__(self, x1, x2, x3, n):
        """
        x1 + x2 + x3 = n
        :param x1:
        :param x2:
        :param x3:
        :param n:
        """
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.n = n

    def print(self):
        """
        prints the vector to visualize
        e.g.:
        (5x1) + (-7x2) + (1x3) = 18
        :return:
        """
        out = f"({self.x1}x1) + ({self.x2}x2) + ({self.x3}x3) = {self.n}"
        print(out)

class plane3normal:
    def __init__(self, nV, supportV):
        self.n = nV
        self.supportV = supportV

    def paramForm(self):
        """
        converts Normal plane to param plane
        :return: returns new param plane
        """

        clampAx1 = 0
        clampAx2 = self.n.x3
        clampAx3 = -self.n.x2

        clampBx1 = self.n.x2
        clampBx2 = -self.n.x1
        clampBx3 = 0

        clampA = vector3(clampAx1, clampAx2, clampAx3)
        clampB = vector3(clampBx1, clampBx2, clampBx3)

        paramForm = plane3param(self.supportV, clampA, clampB)
        return paramForm

    def print(self):
        out = f"{self.n.vis()} * (xV - {self.supportV.vis()}) = 0"
        print(out)


def sumVector3(vX):
    """
    vector sum
    :param vX: vector
    :return: a real number
    """

    vSum = math.sqrt(vX.x1 ** 2 + vX.x2 ** 2 + vX.x3 ** 2)
    return vSum

def multiplyVektor3(vA, n):
    """
    multiply vector with number
    returns new vector does not deform old one
    :param vA: vector
    :param n: multiplier --> float or int no vektor
    :return: vector * multiplier
    """
    a1 = vA.x1 * n
    a2 = vA.x2 * n
    a3 = vA.x3 * n

    vB = vector3(a1, a2, a3)

    return vB



def calcVector3(vA, vB):
    """
    vB is the second vector and vA is the starting point
    vA --------> vB
    vC is the vector between thees two

    :param vectorA: vector A
    :param vectorB: vector B
    :return:
    """

    c1 = vB.x1 - vA.x1
    c2 = vB.x2 - vA.x2
    c3 = vB.x3 - vA.x3

    vC = vector3(c1, c2, c3)

    return vC

def addVector3(vA, vB):
    """
    Add two vectors
    a1 + b1
    a2 + b2
    a3 + b3

    :param vA: vektor A
    :param vB: vektor B
    :return:
    """

    c1 = vB.x1 + vA.x1
    c2 = vB.x2 + vA.x2
    c3 = vB.x3 + vA.x3

    vC = vector3(c1, c2, c3)

    return vC

def dotProduct(vA, vB):
    """
    calculates the scalar product of two vector3´s
    a1 * b1 + a2 * b2 + a3 * b3

    :param vA:
    :param vB:
    :return:
    """

    dotP = (vA.x1 * vB.x1) + (vA.x2 * vB.x2) + (vA.x3 * vB.x3)
    return dotP

def crossProduct(vA, vB):
    """
    does the cross product of vector A and vector B

    :param vA:
    :param vB:
    :return:
    """

    c1 = vA.x2 * vB.x3 - vA.x3 * vB.x2
    c2 = vA.x3 * vB.x1 - vA.x1 * vB.x3
    c3 = vA.x1 * vB.x2 - vA.x2 * vB.x1

    vC = vector3(c1, c2, c3)

    return vC

"""
testing area with examples how to use 
"""
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
    doPlaneNormal()

"""
credits to Bastian Lipka
-
A lib for calculations with vectors (3d) 
"""