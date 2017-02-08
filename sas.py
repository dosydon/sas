import sys
import re
import copy
from .axiom import Axiom
from .operator import Operator
from collections import defaultdict
from abc import ABC, abstractmethod
import argparse
import itertools

class SAS(ABC):
    def __init__(self,**kwargs):
        prop_defaults = {
            "primary_var":defaultdict(dict),
            "secondary_var":defaultdict(dict),
            "initial_assignment":{},
            "goal":{},
            "axiom_layer":defaultdict(int),
            "metric":True,
            "version":3,
            "mutex_group":[],
            "axioms":set(),
            "operators":[],
        }
        for (prop, default) in prop_defaults.items():
            setattr(self, prop, kwargs.get(prop, default))

    @abstractmethod
    def __repr__(self):
        pass

    @classmethod
    def from_file(cls,filename):
        sas = cls()
        with open(filename,"r") as myfile:
            for line in myfile.readlines():
                m = re.match("begin_(.*)",line)
                m2 = re.match("end_(.*)",line)
                if m:
                    contents = [] 
                elif m2:
                    sas.parse(m2.group(1),contents)
                else:
                    contents.append(line.rstrip('\n'))
        return sas

    def parse(self,group,contents):
        if hasattr(self, "parse_"+group):
            f = getattr(self, "parse_"+group)
            f(contents)

    def parse_version(self,lines):
        assert(len(lines) == 1)
        self.version = int(lines[0])

    def parse_metric(self,lines):
        assert(len(lines) == 1)
        self.metric = int(lines[0])

    def parse_state(self,lines):
        for index,value in enumerate(lines):
            self.initial_assignment[index] = int(value)

    def parse_goal(self,lines):
        for line in (lines[1:]):
            nums = [int(num) for num in line.split(' ')]
            self.goal[nums[0]] = nums[1]

    def parse_mutex_group(self,lines):
        group = []
        for line in (lines[1:]):
            nums = [int(num) for num in line.split(' ')]
            group.append((nums))
        self.mutex_group.append(group)

    def parse_rule(self,lines):
        prevail = {} 
        effect = {} 

        num_prevail = int(lines[0])
        for line in lines[1:1+num_prevail]:
            (var,value) = [int(num) for num in line.split(' ')]
            prevail[var] = value

        for line in lines[num_prevail+1:num_prevail+2]:
            (var,fr,to) = [int(num) for num in line.split(' ')]
            if var in prevail and (not prevail[var] == fr):
                return 
            effect[var] = (fr,to)

        axiom = Axiom()
        axiom.from_prevail(prevail,effect)
        self.axioms.add(axiom)

    def version2str(self):
        return ("begin_version\n"
                + "{}\n".format(self.version)
                + "end_version\n")

    def metric2str(self):
        return ("begin_metric\n"
                + "{:d}\n".format(1 if self.metric else 0)
                + "end_metric\n")

    def mutex_group2str(self):
        res = '{}\n'.format(len(self.mutex_group))
        for group in self.mutex_group:
            res += ('begin_mutex_group\n'
                    + '{}\n'.format(len(group)))
            for var,value in group:
                res += "{} {}\n".format(var,value)
            res += 'end_mutex_group\n'
        return res

    def state2str(self):
        res = 'begin_state\n'
        for index,value in sorted(self.initial_assignment.items(),key=(lambda x: x[0] ) ):
            res +='{}\n'.format(value)
        res += 'end_state\n'
        return res

    def goal2str(self):
        res = 'begin_goal\n'
        res += '{}\n'.format(len(self.goal))
        for index,value in sorted(self.goal.items(),key=(lambda x: x[0] ) ):
            res +='{} {}\n'.format(index,value)
        res += 'end_goal\n'
        return res

    def rules2str(self):
        res = '{}\n'.format(len(self.axioms))
        for rule in sorted(self.axioms):
            res += "begin_rule\n"
            res += "{}\n".format(len(rule.prevail))
            for (var,value) in sorted(rule.prevail.items(),key=lambda x:x[0]):
                res += "{} {}\n".format(var,value)
            for (var,(fr,to)) in sorted(rule.effect.items(),key=lambda x:x[0]):
                res += "{} {} {}\n".format(var,fr,to)
            res += "end_rule\n"
        return res

    def is_essential(self,var):
        return self.axiom_layer[var] == -1

    def to_fully_specified(self,unique_name=True):
        sas = copy.deepcopy(self)
        sas.operators = []
        for op in self.operators:
            if op.is_fully_supecified():
                sas.operators.append(op)
            else:
                unspecified = op.unspecified_precond()
                values = [list(range(0,len(self.primary_var[var]))) for var in unspecified]
                for item in itertools.product(*values):
                    specified = {var:item[i] for (i,var) in enumerate(unspecified)}
                    new_op = copy.deepcopy(op)
                    new_op.specify_precond(specified)
                    if unique_name:
                        new_op.name = op.name + "$" + str(specified)
                    sas.operators.append(new_op)
        return sas
