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
