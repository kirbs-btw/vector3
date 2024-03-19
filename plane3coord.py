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