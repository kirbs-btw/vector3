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
        values = [self.x1, self.x2, self.x3]
        return values

class plane3param:
    def __init__(self, supportV3, clampingA, clampingB):
        self.supportV = supportV3
        self.clampingA = clampingA
        self.clampingB = clampingB

    def point(self, r, s):
        r3 = multiplyVektor3(self.clampingA, r)
        s3 = multiplyVektor3(self.clampingB, s)

        return addVector3(addVector3(self.supportV, r3), s3)

    def normalVector(self):
        return crossProduct(self.clampingA, self.clampingB)

    def coordForm(self):
        normalV = self.normalVector()
        n = -dotProduct(normalV, self.supportV)

        coordPlane = plane3coord(normalV.x1, normalV.x2, normalV.x3, n)
        return coordPlane

    def normalForm(self):
        n = self.normalVector()

        normPlane3 = plane3normal(n, self.supportV)
        return normPlane3

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
        out = f"({self.x1}x1) + ({self.x2}x2) + ({self.x3}x3) = {self.n}"
        print(out)

class plane3normal:
    def __init__(self, nV, supportV):
        self.n = nV
        self.supportV = supportV

    def print(self):
        out = f"{self.n.vis()} * (xV - {self.supportV.vis()}) = 0"
        print(out)


def sumVector3(vX):
    """
    vector sum
    :param vX: vector
    :return:
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

def doPlane():
    sup3 = vector3(0, 1, 5)
    clap3A = vector3(5, 7,1)
    clap3B = vector3(2, -1, 2)


    plane = plane3param(sup3, clap3A, clap3B)

    newPoint = plane.point(4, 2)
    newPoint.print()

    newPoint = plane.normalVector()
    newPoint.print()

    coordPlane = plane.coordForm()
    coordPlane.print()

    normalPlane = plane.normalForm()
    normalPlane.print()
    
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
    doPlane()
