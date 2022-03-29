import re
import vector3

"""
using the vector3 lib via a custom command prompt
"""

class vectorRAM():
    def __init__(self):
        self.ram = []

    def append(self, item, name):
        self.ram.append([name, item])

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
        return

    if line.lower() == "stop":
        run.r = False

    if line.lower() == "/help":
        helpFunc()

    if re.search(" = vector3$", line):
        name = re.sub(" = vector3", "", line)
        ram.append(vector3.vector3(), name)

    if re.search(" = plane3", line):
        name = re.sub(" = plane3", "", line)
        ram.append(vector3.plane3(), name)

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

    if re.search("^dot ", line):
        names = re.sub("^dot ", "", line)
        nameArr = getNames(names)
        doCalc(nameArr, "dot")

    if re.search("^mid ", line):
        names = re.sub("^mid ", "", line)
        nameArr = getNames(names)
        doCalc(nameArr, "mid")

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
    elif method == "dot":
        resultNum = vector3.dotProduct(vA, vB)
    elif method == "mid":
        resultV = vector3.midVector3(vA, vB)
    else:
        print("Something went wrong")

    if resultV != None:
        resultV.print()
    elif resultNum != None:
        print(resultNum)

def helpFunc():
    text = "\n" \
           "Hello you called the /help function :)\n" \
           "Here are all functions explained!\n" \
           "we hope it helps\n" \
           "\n" \
           "To generate a vector3 type:\n" \
           "    name = vector3\n" \
           "\n" \
           "    to add values:\n" \
           "    name = 0, 0, 0\n" \
           "\n" \
           "cross:\n" \
           "    returns the cross product of the two vectors use it like\n" \
           "    cross nameVectorA nameVectorB\n" \
           "\n" \
           "add:\n" \
           "    returns the result of adding two vectors\n" \
           "    add nameVectorA nameVectorB\n" \
           "\n" \
           "calc:\n" \
           "    returns the vector between two vectors\n" \
           "    the first vectors is the start point\n" \
           "    the second the end point\n" \
           "use like this:\n" \
           "    calc nameVectorA nameVectorB\n" \
           "\n" \
           "len:\n" \
           "    returns the length of a vector\n" \
           "    len nameVector\n" \
           "\n" \
           "unit:\n" \
           "    returns the unit vector of the vector\n" \
           "    unit nameVector\n" \
           "\n" \
           "dot:\n" \
           "    returns dot product of two vectors\n" \
           "    dot nameVectorA nameVectorB\n" \
           "\n" \
           "mid:\n" \
           "    returns the mid point of two vectors\n" \
           "    mid nameVectorA nameVectorB\n"

    print(text)



    pass

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
ideas: 
    -entry function
        -showing the basic things
        
    (-implement planes)
    -implement lines
    -documentation
"""

"""
Bastian Lipka 
"""