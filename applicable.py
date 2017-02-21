class Applicable:
    '''
    prevail: {var:value}
    effect: {var: (from,to)}
    requirement: {var:value}
    achievement: {var:value}
    '''
    def __init__(self,name):
        self.name = name

    @classmethod
    def from_prevail(cls, name, prevail, effect):
        ap = cls(name)
        ap.prevail = prevail
        ap.effect = effect
        ap.requirement = {} 
        ap.achievement = {} 
        for k,v in prevail.items():
            ap.requirement[k] = v
        for var,(fr,to) in effect.items():
            ap.achievement[var] = to
            if fr == -1:
                continue
            ap.requirement[var] = fr
        return ap

    @classmethod
    def from_requirement(cls, name, requirement, achievement):
        ap = cls(name)
        ap.requirement = requirement
        ap.achievement = achievement 
        ap.prevail = {}
        ap.effect = {}
        for k,v in ap.requirement.items():
            if k in ap.achievement:
                ap.effect[k] = (ap.requirement[k],ap.achievement[k])
            else:
                ap.prevail[k] = ap.requirement[k]
        for k,v in ap.achievement.items():
            if not k in ap.requirement:
                ap.effect[k] = (-1,v)
        return ap

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
