import re
import vector3

"""
using the vector3 lib via a custom command prompt
"""

class vectorRAM():
    def __init__(self):
        self.ram = []

    def appendV(self, vector, vectorName):
        self.ram.append([vectorName, vector])

    def get(self, name):
        vector = vector3.vector3()
        for i in self.ram:
            if i[0] == name:
                vector = i[1]
        return vector

    def update(self, name, values):
        currentV = self.get(name)

        currentV.x1 = values[0]
        currentV.x2 = values[1]
        currentV.x3 = values[2]
        index = 0

        for i in self.ram:
            if i[0] == name:
                ram.ram[index][1] = currentV
            index += 1

class run:
    def __init__(self, r=True):
        self.r = r

ram = vectorRAM()
run = run()

def checkInput(line):
    if line == "":
        #print("No Input")
        return

    if line.lower() == "stop":
        run.r = False

    if re.search(" = vector3$", line):
        name = re.sub(" = vector3", "", line)
        ram.appendV(vector3.vector3(), name)

    if re.search("^print ", line):
        name = re.sub("print ", "", line)
        ram.get(name).print()

    if re.search(" = [-1234567890]", line):
        data = getValuesName(line)
        ram.update(data[0], data[1])

    if re.search("^add ", line):
        names = re.sub("^add ", "", line)
        nameArr = getNames(names)
        doCalc(nameArr, "add")

    if re.search("^cross ", line):
        names = re.sub("^cross ", "", line)
        nameArr = getNames(names)
        doCalc(nameArr, "cross")

    if re.search("^calc ", line):
        names = re.sub("^calc ", "", line)
        nameArr = getNames(names)
        doCalc(nameArr, "calc")

    if re.search("^len ", line):
        name = re.sub("^len ", "", line)
        names = [name, ""]
        doCalc(names, "len")

    if re.search("^unit ", line):
        name = re.sub("^unit ", "", line)
        names = [name, ""]
        doCalc(names, "unit")

def doCalc(arr, method):
    vA = ram.get(arr[0])
    vB = ram.get(arr[1])

    resultV = None
    resultNum = None

    if method == "cross":
        resultV = vector3.crossProduct(vA, vB)
    elif method == "add":
        resultV = vector3.addVector3(vA, vB)
    elif method == "calc":
        resultV = vector3.calcVector3(vA, vB)
    elif method == "len":
        resultNum = vector3.sumVector3(vA)
    elif method == "unit":
        resultV = vA.unit()

    if resultV != None:
        resultV.print()
    elif resultNum != None:
        print(resultNum)

def getNames(line):
    nameA = ""
    nameB = ""
    switch = True

    for i in line:
        if i == " ":
            switch = False
        elif switch:
            nameA += i
        else:
            nameB += i
    names = [nameA, nameB]
    return names


def getValuesName(line):
    name = ""
    values = ""
    switch = True
    count = 0
    first = True
    for i in line:
        if i == " " and first:
            switch = False
            first = False
        elif not switch:
            count += 1
            if count == 2:
                switch = True
        elif switch and count >= 2:
            values += i
        elif switch:
            name += i

    values = convertValues(values)
    return [name, values]
def convertValues(line):
    a = ""
    b = ""
    c = ""
    count = 0

    for i in line:
        if i == ",":
            pass
        elif i == " ":
            count += 1
        elif count == 0:
            a += str(i)
        elif count == 1:
            b += str(i)
        else:
            c += str(i)

    if float(a) % 1 == 0:
        a = int(a)
    else:
        a = float(a)

    if float(b) % 1 == 0:
        b = int(b)
    else:
        b = float(b)

    if float(c) % 1 == 0:
        c = int(c)
    else:
        c = float(c)

    values = [a, b, c]

    return values

def main():
    commandLine = []
    while run.r:
        line = input(":")
        checkInput(line)
        commandLine.append(line)



if __name__ == '__main__':
    main()

"""
Bastian Lipka 
"""