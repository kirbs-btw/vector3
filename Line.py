import math

class Line:
    def __init__(self, support, direction):
        self.sV = support
        self.dV = direction
    
    def lenV(self, v):
        return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    
    def unitV(self, v):
        x1 = v[0] / self.lenV(v)
        x2 = v[1] / self.lenV(v)
        x3 = v[2] / self.lenV(v)  
        return [x1, x2, x3]

    
    
    def point(self, s):
        x1 = self.sV[0] + self.dV[0] * s
        x2 = self.sV[1] + self.dV[1] * s
        x3 = self.sV[2] + self.dV[2] * s
        return [x1, x2, x3]

    def info(self):
        print(type(self))
        print("Support V: {}".format(self.sV))
        print("Direction V: {}".format(self.dV))
        
    def __str__(self):
        print('---class Line---')
        print('sV: {}'.format(self.sV))
        print('sD: {}'.format(self.sD))
        print('----------------')

