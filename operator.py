from .applicable import Applicable

class Operator(Applicable):
    def __init__(self,name,cost):
        Applicable.__init__(self,name)
        self.cost = cost

if __name__ == '__main__':
    op = Operator("temp",0)
    op.from_requirement({0:1,1:1},{1:2,2:1})
    print(op.prevail)
    print(op.effect)
