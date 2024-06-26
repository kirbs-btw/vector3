import math

def unit(v) -> list:
        """
        calculates the unit Vector

        :param vA: vector A
        :return: unit vector of A (return vector has len 1)
        """
        vectorLen = sumVector3(v)
        multi = 1 / vectorLen

        return multiplyVector3(v, multi)

def invert(v) -> list:
    """
    inverts the current vector, does not change the vector it self
    :return:
    """
    x1 = -v[0]
    x2 = -v[1]
    x3 = -v[2]

    newV = [x1, x2, x3]
    return newV

def midVector3(vA, vB) -> list:
    """
    returns the mid point of two vectors
    :param vA: vector A - type = vector3
    :param vB: vector B - type = vector3
    :return: mit point of vA and vB as a vector3s
    """

    vM = multiplyVector3(addVector3(vA, vB), 0.5)
    return vM

def len(vector) -> float:
    sum = math.sqrt(vector[1] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    return sum

def sumVector3(vX) -> float:
    """
    vector sum
    :param vX: vector
    :return: a real number
    """

    vSum = math.sqrt(vX[1] ** 2 + vX[1] ** 2 + vX[2] ** 2)
    return vSum


def multiplyVector3(vA, n) -> list:
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


def calcVector3(vA, vB) -> list:
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


def addVector3(vA, vB) -> list:
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


def dotProduct(vA, vB) -> float:
    """
    calculates the scalar product of two vector3´s
    a1 * b1 + a2 * b2 + a3 * b3

    :param vA:
    :param vB:
    :return:
    """

    dotP = (vA[0] * vB[0]) + (vA[1] * vB[1]) + (vA[2] * vB[2])
    return dotP


def crossProduct(vA, vB) -> list:
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


def point3plane(vA, vB, vC):
    # support Vector
    supportV = vA
    
    # calculating the clamping vectors form vA to vB and vA to vC
    clampA = calcVector3(vA, vB)
    clampB = calcVector3(vA, vC)

    # creating plane3param to use in plane
    param_plane = plane3param(supportV, clampA, clampB)
    plane = plane3(paramPlane=param_plane)
    
    return plane


"""
credits to Bastian Lipka
-
A lib for calculations with vectors (3d) 
"""