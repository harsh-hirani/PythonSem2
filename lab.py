# p4 4 - Formulate a problem definition of your own and demonstrate functions as objects
class func:
    def __init__(self,props):
        self.props = props
        self.total = 0
        self.multiall = 1
    def sumAll(self):
        self.total = 0
        self.multiall = 1
        for e in self.props:
            self.total += e
        return self.total
    def multiAll(self):
        self.total = 0
        self.multiall = 1
        for e in self.props:
            self.multiall *= e
        return self.multiall
    def __str__(self) -> str:
        return "{'sum' :"+f"{self.sumAll()}"+",'multiAll' :"+f"{self.multiAll()}"+'}'
myobj = func([1,2,3,4,5])
print(myobj)
print(myobj.sumAll())
print(myobj.multiAll())