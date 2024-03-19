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