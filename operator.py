from .applicable import Applicable

class Operator(Applicable):
    def __init__(self,name,cost):
        Applicable.__init__(self,name)
        self.cost = cost

    def __repr__(self):
        res = ("begin_operator\n"
                + "{}\n".format(self.name)
                + "{}\n".format(len(self.prevail)))
        for (var,value) in sorted(self.prevail.items(),key=lambda x:x[0]):
            res += "{} {}\n".format(var,value)
        res += "{}\n".format(len(self.effect))
        for (var,(fr,to)) in sorted(self.effect.items(),key=lambda x:x[0]):
            res += "0 {} {} {}\n".format(var,fr,to)
        res += ("{}\n".format(self.cost)
                + "end_operator\n")
        return res

if __name__ == '__main__':
    op = Operator("temp",0)
    op.from_requirement({0:1,1:1},{1:2,2:1})
    print(op.prevail)
    print(op.effect)
