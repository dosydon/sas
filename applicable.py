class Applicable:
    '''
    prevail: {var:value}
    effect: {var: (from,to)}
    requirement: {var:value}
    achievement: {var:value}
    '''
    def __init__(self,name):
        self.name = name

    def from_prevail(self,prevail,effect):
        self.prevail = prevail
        self.effect = effect
        self.requirement = {} 
        self.achievement = {} 
        for k,v in prevail.items():
            self.requirement[k] = v
        for var,(fr,to) in effect.items():
            self.achievement[var] = to
            if fr == -1:
                continue
            self.requirement[var] = fr
        return self

    def from_requirement(self,requirement,achievement):
        self.requirement = requirement
        self.achievement = achievement 
        self.prevail = {}
        self.effect = {}
        for k,v in self.requirement.items():
            if k in self.achievement:
                self.effect[k] = (self.requirement[k],self.achievement[k])
            else:
                self.prevail[k] = self.requirement[k]
        for k,v in self.achievement.items():
            if not k in self.requirement:
                self.effect[k] = (-1,v)
        return self

    def is_applicable(self,state):
        for (var,value) in self.requirement.items():
            if not var in state.assignment:
                continue
            if not state.assignment[var] == value:
                return False
        return True

    def __repr__(self):
        return self.name

    def __lt__(self,other):
        return self.name < other.name

    def is_fully_supecified(self):
        for var,(fr,to) in self.effect.items():
            if fr == -1:
                return False
        return True

    def unspecified_precond(self):
        res = []
        for var,(fr,to) in self.effect.items():
            if fr == -1:
                res.append(var)
        return res

    def specify_precond(self,specified):
        prevail = self.prevail
        effect = self.effect
        for k,v in specified.items():
            fr,to = effect[k]
            assert(fr == -1)
            effect[k] = (v,to)
        self.from_prevail(prevail,effect)

