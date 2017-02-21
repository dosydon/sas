from .applicable import Applicable
class Axiom(Applicable):
    def __init__(self,name="axiom",cost=0):
        Applicable.__init__(self,name)
        self.cost = cost

    def __repr__(self):
        res = "begin_rule\n"
        res += "{}\n".format(len(self.prevail))
        for (var,value) in sorted(self.prevail.items(),key=lambda x:x[0]):
            res += "{} {}\n".format(var,value)
        for (var,(fr,to)) in sorted(self.effect.items(),key=lambda x:x[0]):
            res += "{} {} {}\n".format(var,fr,to)
        res += "end_rule\n"
        return res

    def __lt__(self,other):
        return str(self) < str(other)

if __name__ == '__main__':
    op = Axiom.from_requirement("temp",{0:1,1:1},{1:2,2:1})
    print(op.prevail)
    print(op.effect)
