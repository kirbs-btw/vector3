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
        vector = None
        for i in self.ram:
            if i[0] == name:
                vector = i[1]
        return vector

    def update(self, name, values):
        currentV = self.get(name)
        """
        currentV.x1 = values[0]
        currentV.x2 = values[1]
        currentV.x3 = values[2]
        """
        for i in self.ram:
            if i[0] == name:
                i[1] = currentV

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
    """
    if re.search(" = [(]"):
        values = [0, 1, 5]

        name = re.sub(" = [(]", "", line)
        ram.update(name, values)
    """
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