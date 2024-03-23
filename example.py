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
    
    
    

if __name__ == '__main__':
    main()