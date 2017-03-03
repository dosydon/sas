class ConditionalEffect:

    def __init__(self, conditions, head):
        self.conditions = conditions
        self.head = head

class ConditionalOperator:

    def __init__(self, name, cost, prevail, effect):
        self.name = name
        self.cost = cost
        self.prevail = prevail
        self.effect = effect

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

