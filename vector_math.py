import math

def unit(v):
        """
        calculates the unit Vector

        :param vA: vector A
        :return: unit vector of A (return vector has len 1)
        """
        vectorLen = sumVector3(v)
        multi = 1 / vectorLen

        return multiplyVector3(v, multi)

def invert(v):
    """
    inverts the current vector, does not change the vector it self
    :return:
    """
    x1 = -v[0]
    x2 = -v[1]
    x3 = -v[2]

    newV = [x1, x2, x3]
    return newV

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
    g1sVx1 = g1.supportV[0] * g1.dirV[1] - g1.supportV[1] * g1.dirV[0]
    g2sVx1 = g2.supportV[0] * g1.dirV[1] - g2.supportV[1] * g1.dirV[0]
    g2dVx1 = g2.dirV[0] * g1.dirV[1] - g2.dirV[1] * g1.dirV[0]

    g1sVx1 = (g1sVx1 - g2sVx1) / g2dVx1  # value of s

    # get the value of r
    g2x2 = (g2.supportV[1] + g2.dirV[1] * g1sVx1) - g1.supportV[1]
    g2x2 = g2x2 / g1.dirV[1]  # value of r

    pointR = g1.point(g2x2)
    pointS = g2.point(g1sVx1)

    if pointR == pointS:
        return pointR
    else:
        # "lines don´t cross 
        return None


def sumVector3(vX):
    """
    vector sum
    :param vX: vector
    :return: a real number
    """

    vSum = math.sqrt(vX[1] ** 2 + vX[1] ** 2 + vX[2] ** 2)
    return vSum


def multiplyVector3(vA, n):
    """
    multiply vector with number
    returns new vector does not deform old one
    :param vA: vector
    :param n: multiplier --> float or int no vektor
    :return: vector * multiplier
    """
    a1 = vA[0] * n
    a2 = vA[1] * n
    a3 = vA[2] * n

    vB = [a1, a2, a3]
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

    c1 = vB[0] - vA[0]
    c2 = vB[1] - vA[1]
    c3 = vB[2] - vA[2]

    vC = [c1, c2, c3]

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

    c1 = vB[0] + vA[0]
    c2 = vB[1] + vA[1]
    c3 = vB[2] + vA[2]

    vC = [c1, c2, c3]

    return vC


def dotProduct(vA, vB):
    """
    calculates the scalar product of two vector3´s
    a1 * b1 + a2 * b2 + a3 * b3

    :param vA:
    :param vB:
    :return:
    """

    dotP = (vA[0] * vB[0]) + (vA[1] * vB[1]) + (vA[2] * vB[2])
    return dotP


def crossProduct(vA, vB):
    """
    does the cross product of vector A and vector B

    :param vA:
    :param vB:
    :return:
    """

    c1 = vA[1] * vB[2] - vA[2] * vB[1]
    c2 = vA[2] * vB[0] - vA[0] * vB[2]
    c3 = vA[0] * vB[1] - vA[1] * vB[0]

    vC = [c1, c2, c3]

    return vC


"""
credits to Bastian Lipka
-
A lib for calculations with vectors (3d) 
"""