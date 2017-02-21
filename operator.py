from .applicable import Applicable


class Operator(Applicable):

    def __init__(self, name, cost):
        Applicable.__init__(self, name)
        self.cost = cost

    @classmethod
    def from_prevail(cls, name, cost, prevail, effect):
        ap = cls(name, cost)
        ap.prevail = prevail
        ap.effect = effect
        ap.requirement = {}
        ap.achievement = {}
        for k, v in prevail.items():
            ap.requirement[k] = v
        for var, (fr, to) in effect.items():
            ap.achievement[var] = to
            if fr == -1:
                continue
            ap.requirement[var] = fr
        return ap

    @classmethod
    def from_requirement(cls, name, cost, requirement, achievement):
        ap = cls(name, cost)
        ap.requirement = requirement
        ap.achievement = achievement
        ap.prevail = {}
        ap.effect = {}
        for k, v in ap.requirement.items():
            if k in ap.achievement:
                ap.effect[k] = (ap.requirement[k], ap.achievement[k])
            else:
                ap.prevail[k] = ap.requirement[k]
        for k, v in ap.achievement.items():
            if k not in ap.requirement:
                ap.effect[k] = (-1, v)
        return ap

    def is_applicable(self, state):
        for (var, value) in self.requirement.items():
            if var not in state.assignment:
                continue
            if not state.assignment[var] == value:
                return False
        return True

    def __repr__(self):
        res = ("begin_operator\n"
               + "{}\n".format(self.name)
               + "{}\n".format(len(self.prevail)))
        for (var, value) in sorted(self.prevail.items(), key=lambda x: x[0]):
            res += "{} {}\n".format(var, value)
        res += "{}\n".format(len(self.effect))
        for (var, (fr, to)) in sorted(self.effect.items(), key=lambda x: x[0]):
            res += "0 {} {} {}\n".format(var, fr, to)
        res += ("{}\n".format(self.cost)
                + "end_operator\n")
        return res


if __name__ == '__main__':
    op = Operator.from_requirement("temp", 0, {0: 1, 1: 1}, {1: 2, 2: 1})
    print(op.prevail)
    print(op.effect)
