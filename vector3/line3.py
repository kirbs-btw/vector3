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