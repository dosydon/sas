from .applicable import Applicable
class Axiom(Applicable):
    def __init__(self,name="axiom",cost=0):
        Applicable.__init__(self,name)
        self.cost = cost

    def __repr__(self):
        prevail = str(sorted(self.prevail.items()))
        effect = str(sorted(self.effect.items()))
        return prevail + " -> " +effect

    def __lt__(self,other):
        return str(self) < str(other)

if __name__ == '__main__':
    op = Axiom("temp")
    op.from_requirement({0:1,1:1},{1:2,2:1})
    print(op.prevail)
    print(op.effect)
