import vector3 as vm


def main():
    vectorA = [1, 2, 3]
    vectorB = [0, 2, 1]
    print(vm.invert(vectorA))  
    print(vm.unit(vectorA))
    print(vm.midVector3(vectorA, vectorB))
    print(vm.sumVector3(vectorA, vectorB))
    print(vm.multiplyVector3(vectorA, vectorB))
    print(vm.calcVector3(vectorA, vectorB))
    print(vm.addVector3(vectorA, vectorB))
    print(vm.dotProduct(vectorA, vectorB))
    print(vm.crossProduct(vectorA, vectorB))
    
    

def testLine():
    # test of the things
    """
    v1g1 = [100.19999999999999, 50, 49.8]
    v2g1 = [50, 50, 49.8]
    
    v1g2 = [0.5, 0, 49.8]
    v2g2 = [1.5, 1, 49.8] 
    
    a = ComplexLine(v1g1, v2g1)
    b = ComplexLine(v1g2, v2g2)
    
    print(intersection(a, b))
    
    """

    # testing the current line 
    gaS = [100.2, 50.0, 49.8]
    gaD = [-50.2, 0.0, 0.0]

    gbS = [0.5, 0, 49.8]
    gbD = [1, 1, 0]
    a = vm.Line(gaS, gaD)
    b = vm.Line(gbS, gbD)
    print(vm.intersection(a, b))

if __name__ == '__main__':
    testLine()
    # main()