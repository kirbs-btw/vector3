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