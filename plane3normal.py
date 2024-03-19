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