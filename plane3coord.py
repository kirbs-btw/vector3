class plane3coord:
    def __init__(self, x1=0, x2=0, x3=0, n=0):
        """
        x1 + x2 + x3 = n
        :param x1:
        :param x2:
        :param x3:
        :param n:
        """
        self[0] = x1
        self[1] = x2
        self.x3 = x3
        self.n = n

    def normalForm(self):
        """
        gets the normal form
        :return: normal form
        """
        n1 = self[0]
        n2 = self[1]
        n3 = self[2]
        nV = [n1, n2, n3]

        s1 = 0
        s2 = 0
        s3 = 0

        if self[2] != 0:
            s3 = self.n / self[2]
        elif self[1] != 0:
            s2 = self.n / self[1]
        else:
            s1 = self.n / self[0]

        supportV = vector3(s1, s2, s3)
        normalPlane = plane3normal(nV, supportV)

        return normalPlane

    def paramForm(self):
        """
        gets the parameter form
        :return: parameter form
        """
        s1x1 = self.n / self[0]
        s2x2 = self.n / self[1]
        s3x3 = self.n / self[2]

        s1V = [s1x1, 0, 0]
        s2V = [0, s2x2, 0]
        s3V = [0, 0, s3x3]
        
        clampA = calcVector3(s1V, s2V)
        clampB = calcVector3(s1V, s3V)

        coordForm = plane3param(s1V, clampA, clampB)

        return coordForm

    def __str__(self):
        """
        prints the vector to visualize
        e.g.:
        (5x1) + (-7x2) + (1x3) = 18
        :return:
        """
        out = f"coord-form:         ({self[0]}x1) + ({self[1]}x2) + ({self[2]}x3) = {self.n}"
        print(out)
        
"""
credits to Bastian Lipka
-
A lib for calculations with vectors (3d) 
"""