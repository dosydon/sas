import re
import sys
import argparse
from .sas import SAS
from .operator import Operator
from .axiom import Axiom

class SAS1(SAS):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        res=''
        res+=self.variables2str()
        res+=self.state2str()
        res+=self.goal2str()
        res+=self.operators2str()
        res+=self.rules2str()
        return res

    def parse_variables(self,lines):
        num_vars =int(lines[0])
        for var_index,line in enumerate(lines[1:]):
            _,rang,axiom_layer = line.split(' ')
            self.axiom_layer[var_index] = int(axiom_layer)
            for domain_index in range(0,int(rang)):
                if self.axiom_layer[var_index] > -1:
                    self.secondary_var[var_index][domain_index] = 'dummy value'
                else:
                    self.primary_var[var_index][domain_index] = 'dummy value'

    def parse_operator(self,lines):
        prevail = {} 
        effect = {} 

        name = lines[0]
        num_prevail = int(lines[1])
        for line in lines[2:2+num_prevail]:
            (var,value) = [int(num) for num in line.split(' ')]
            prevail[var] = value

        num_effect = int(lines[num_prevail+2])
        for line in lines[num_prevail+3:num_prevail+num_effect+3]:
            num_conditions = int(line[0])
            rest = [int(num) for num in line.split(' ')][1:]
            for i in range(0,num_conditions):
                var, val = rest[:2]
                rest = rest[2:]
            (var,fr,to) = rest
            effect[var] = (fr,to)

        new_operator = Operator(name,1)
        new_operator.from_prevail(prevail,effect)
        self.operators.append(new_operator)

    def variables2str(self):
        num_primary_var = len(self.primary_var)
        num_secondary_var = len(self.secondary_var)
        num_var = num_primary_var + num_secondary_var
        res = ('begin_variables\n'
                + '{}\n'.format(num_var))
        for i in range(0,num_var):
            if self.axiom_layer[i] < 0:
                res += 'var{} {} {}\n'.format(i,len(self.primary_var[i]),self.axiom_layer[i])
            else:
                res += 'var{} {} {}\n'.format(i,len(self.secondary_var[i]),self.axiom_layer[i])
        res += 'end_variables\n'
        return res

    def operators2str(self):
        res = '{}\n'.format(len(self.operators))
        for op in self.operators:
            res += ("begin_operator\n"
                    + "{}\n".format(op.name)
                    + "{}\n".format(len(op.prevail)))
            for (var,value) in sorted(op.prevail.items(),key=lambda x:x[0]):
                res += "{} {}\n".format(var,value)
            res += "{}\n".format(len(op.effect))
            for (var,(fr,to)) in sorted(op.effect.items(),key=lambda x:x[0]):
                res += "0 {} {} {}\n".format(var,fr,to)
            res += "end_operator\n"
        return res

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("sas_file")
#     parser.add_argument('--output',default='output.sas')
    args = parser.parse_args()

    sas = SAS1.from_file(args.sas_file)
    copied = sas.to_fully_specified()
    copied.write(sys.stdout)
#     with open(args.output,"w") as f:
#         sas.write(f)

