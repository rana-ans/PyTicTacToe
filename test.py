
myglobalvariable = [0, 1, 2]

class Test:
    def __init__(self, myvariable):
        self.myvariable = myvariable
    
    def testing(self):
        print(f"Testing: {self.myvariable}")
    
    def updateval(self):
        myglobalvariable[0] += 2
        myglobalvariable[1] += 2
        myglobalvariable[2] += 2
        print(f"updated myglobalvariable to {myglobalvariable}")

if __name__ == "__main__":
    myclass = Test("myvariablevalue")
    myclass.testing()
    myclass.updateval()
