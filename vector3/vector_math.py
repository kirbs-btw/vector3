import math

class vector3:
    """
    creates 3d Vectors in python
    """

    def __init__(self, x1=0, x2=0, x3=0):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def print(self):
        """
        prints the vector3 because printing
        :return:
        """

        values = [self.x1, self.x2, self.x3]
        print(values)

    def unit(self):
        """
        calculates the unit Vector

        :param vA: vector A
        :return: unit vector of A (return vector has len 1)
        """
        vectorLen = sumVector3(self)
        multi = 1 / vectorLen
        #print(multi)

        return multiplyVector3(self, multi)

    def invert(self):
        """
        inverts the current vector, does not change the vector it self
        :return:
        """
        x1 = -self.x1
        x2 = -self.x2
        x3 = -self.x3

        newV = vector3(x1, x2, x3)
        return newV


    def vis(self):
        """
        gets you the values of the vector as an array
        [1, -4, 7]
        :return: the values of the vector as an array [self.x1, self.x2, self.x3]
        """

        values = [self.x1, self.x2, self.x3]
        return values



class plane3param:
    def __init__(self, supportV3=vector3(), clampingA=vector3(), clampingB=vector3()):
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

        r3 = multiplyVector3(self.clampingA, r)
        s3 = multiplyVector3(self.clampingB, s)

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

        print(f"param-form:          x-> = {support.vis()} + r * {clampA.vis()} + s * {clampB.vis()}")

class plane3coord:
    def __init__(self, x1=0, x2=0, x3=0, n=0):
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

    def normalForm(self):
        """
        gets the normal form
        :return: normal form
        """
        n1 = self.x1
        n2 = self.x2
        n3 = self.x3
        nV = vector3(n1, n2, n3)

        s1 = 0
        s2 = 0
        s3 = 0

        if self.x3 != 0:
            s3 = self.n / self.x3
        elif self.x2 != 0:
            s2 = self.n / self.x2
        else:
            s1 = self.n / self.x1

        supportV = vector3(s1, s2, s3)
        normalPlane = plane3normal(nV, supportV)

        return normalPlane

    def paramForm(self):
        """
        gets the parameter form
        :return: parameter form
        """
        s1x1 = self.n / self.x1
        s2x2 = self.n / self.x2
        s3x3 = self.n / self.x3

        s1V = vector3(s1x1, 0, 0)
        s2V = vector3(0, s2x2, 0)
        s3V = vector3(0, 0, s3x3)

        clampA = calcVector3(s1V, s2V)
        clampB = calcVector3(s1V, s3V)

        coordForm = plane3param(s1V, clampA, clampB)

        return coordForm

    def print(self):
        """
        prints the vector to visualize
        e.g.:
        (5x1) + (-7x2) + (1x3) = 18
        :return:
        """
        out = f"coord-form:         ({self.x1}x1) + ({self.x2}x2) + ({self.x3}x3) = {self.n}"
        print(out)

class plane3normal:
    def __init__(self, nV=vector3(), supportV=vector3()):
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

    def coordForm(self):
        """
        gets the coordinate form
        :return: coordinate form
        """
        coordX1 = self.n.x1
        coordX2 = self.n.x2
        coordX3 = self.n.x3
        n = dotProduct(self.n, self.supportV)

        coordPlane = plane3coord(coordX1, coordX2, coordX3, n)

        return coordPlane

    def print(self):
        """
        prints the plane
        :return:
        """
        out = f"normal-form:        {self.n.vis()} * (xV - {self.supportV.vis()}) = 0"
        print(out)


class line3:
    def __init__(self, sV=vector3(), dV=vector3()):
        self.supportV = sV
        self.dirV = dV

    def point(self, r):
        """
        gets a point at the line
        :param r: real number
        :return: returns point as a vector3
        """
        newDirV = multiplyVector3(self.dirV, r)
        xV = addVector3(self.supportV, newDirV)
        return xV

    def print(self):
        """
        prints the line to visualize
        e.g.:

        g: x-> = [1, 3, 2] + r * [2, 1, 5]

        :return: none
        """
        txt = f"g: x-> = {self.supportV.vis()} + r * {self.dirV.vis()}"
        print(txt)

class plane3:
    """
    does a 3d  plane input one of the 3 ways to doc a plane and
    it fills the other two
    """

    def __init__(self, paramPlane=None, normalPlane=None, coordPlane=None):
        self.assignInputs(paramPlane, normalPlane, coordPlane)
        self.getForms()

    def assignInputs(self, planeA, planeB, planeC):
        if type(planeA) == type(plane3coord()):
            planeA, planeC = planeC, planeA
        if type(planeA) == type(plane3normal()):
            planeA, planeB = planeB, planeA
        if type(planeB) == type(plane3param):
            planeB, planeA = planeA, planeB
        if type(planeB) == type(plane3coord):
            planeB, planeC = planeC, planeB
        if type(planeC) == type(plane3param()):
            planeC, planeA = planeA, planeC
        if type(planeC) == type(plane3normal()):
            planeC, planeB = planeB, planeC

        self.param = planeA
        self.normal = planeB
        self.coord = planeC

    def getParam(self):
        """
        gets the param form of the plane
        :return: parameter form
        """
        if self.normal != None:
            self.param = self.normal.paramForm()
        elif self.coord != None:
            self.param = self.coord.paramForm()

    def getNormal(self):
        """
        gets Normal form of the plane
        :return: normal form
        """
        if self.param != None:
            self.normal = self.param.normalForm()
        elif self.coord != None:
            self.normal = self.coord.normalForm()

    def getCoord(self):
        """
        gets the coordinate form
        :return: coordinate form
        """
        if self.param != None:
            self.coord = self.param.coordForm()
        elif self.normal != None:
            self.coord = self.normal.coordForm()

    def getForms(self):
        """
        gets the missing forms
        :return:
        """
        if self.param != None and self.normal != None and self.coord != None:
            return

        if self.param == None and self.normal == None and self.coord == None:
            return

        if self.normal == None and self.coord == None:
            self.getNormal()
            self.getCoord()

        if self.param == None and self.coord == None:
            self.getParam()
            self.getCoord()

        if self.param == None and self.normal == None:
            self.getParam()
            self.getNormal()

    def print(self):
        """
        prints the planes to visualize
        :return: none - console out
        """
        if self.param == None and self.normal == None and self.coord == None:
            print(0)
        else:
            self.param.print()
            self.normal.print()
            self.coord.print()

def midVector3(vA, vB):
    """
    returns the mid point of two vectors
    :param vA: vector A - type = vector3
    :param vB: vector B - type = vector3
    :return: mit point of vA and vB as a vector3s
    """

    vM = multiplyVector3(addVector3(vA, vB), 0.5)
    return vM

def point3plane(vA, vB, vC):
    supportV = vA
    clampA = calcVector3(vA, vB)
    clampB = calcVector3(vA, vC)

    plane3 = plane3param(supportV, clampA, clampB)

    return plane3


def compareLines(g1, g2):
    # I     g1.sV.x1 + g1.dV.x1 = g2.sV.x1 + g2.dV.x1
    # II    g1.sV.x2 + g1.dV.x2 = g2.sV.x2 + g2.dV.x2
    # III   g1.sV.x2 + g1.dV.x2 = g2.sV.x2 + g2.dV.x2

    # get the value of s
    g1sVx1 = g1.supportV.x1 * g1.dirV.x2 - g1.supportV.x2 * g1.dirV.x1
    g2sVx1 = g2.supportV.x1 * g1.dirV.x2 - g2.supportV.x2 * g1.dirV.x1
    g2dVx1 = g2.dirV.x1 * g1.dirV.x2 - g2.dirV.x2 * g1.dirV.x1

    g1sVx1 = (g1sVx1 - g2sVx1) / g2dVx1  # value of s

    # get the value of r
    g2x2 = (g2.supportV.x2 + g2.dirV.x2 * g1sVx1) - g1.supportV.x2
    g2x2 = g2x2 / g1.dirV.x2  # value of r

    pointR = g1.point(g2x2)
    pointS = g2.point(g1sVx1)

    if pointR == pointS:
        return pointR
    else:
        print(pointR.vis())
        print(pointS.vis())
        print("lines don´t cross")
        return None


def sumVector3(vX):
    """
    vector sum
    :param vX: vector
    :return: a real number
    """

    vSum = math.sqrt(vX.x1 ** 2 + vX.x2 ** 2 + vX.x3 ** 2)
    return vSum


def multiplyVector3(vA, n):
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
credits to Bastian Lipka
-
A lib for calculations with vectors (3d) 
"""