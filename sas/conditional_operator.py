import copy
def get_flipped(value):
    return (2 - value) // 2

class ConditionalEffect:

    def __init__(self, conditions, head):
        self.conditions = conditions
        self.head = head

    def __repr__(self):
        res = "{}".format(len(self.conditions))
        for (var, value) in sorted(self.conditions.items()):
            res += " {} {}".format(var, value)
        var, fr, to = self.head
        res += " {} {} {}\n".format(var, fr, to)
        return res

    def __lt__(self, other):
        return str(self) < str(other)

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
        for effect in self.effect:
            res += str(effect)
        res += ("{}\n".format(self.cost)
                + "end_operator\n")
        return res

    def get_flipped(self, vars_to_flip):
        pre = copy.deepcopy(self.prevail)
        eff = copy.deepcopy(self.effect)
        for var in pre:
            if var in vars_to_flip:
                pre[var] = get_flipped(pre[var])

        cond_effs = []
        for e in eff:
            conditions = {}
            for var, val in e.conditions.items():
                if var in vars_to_flip:
                    conditions[var] = get_flipped(val)
                else:
                    conditions[var] = val
            var, fr, to = e.head
            if var in vars_to_flip:
                cond_effs.append( ConditionalEffect( conditions, (var, get_flipped(fr), get_flipped(to))) )
            else:
                cond_effs.append( ConditionalEffect( conditions, (var, fr, to)))
        return ConditionalOperator(self.name, self.cost, pre, cond_effs)
