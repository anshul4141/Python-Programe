class Person:
    def __init__(self):
        print("i am always execute")
        self.name = ""
        self.address = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address
