import re
import sys
import argparse
from .sas import SAS
from .operator import Operator
from .axiom import Axiom

class SAS3(SAS):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        res=''
        res+=self.version2str()
        res+=self.metric2str()
        res+=self.variables2str()
        res+=self.mutex_group2str()
        res+=self.state2str()
        res+=self.goal2str()
        res+=self.operators2str()
        res+=self.rules2str()
        return res

    def parse_variable(self,lines):
        m = re.match("var([0-9]+)",lines[0])
        var_index = int(m.group(1))
        axiom = int(lines[1])
        self.axiom_layer[var_index] = axiom
        num_values = int(lines[2])
        for domain_index,value in enumerate(lines[3:]):
            if axiom > -1:
                self.secondary_var[var_index][domain_index] = value
            else:
                self.primary_var[var_index][domain_index] = value

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

        cost = int(lines[-1])
        new_operator = Operator.from_prevail(name,cost,prevail,effect)
        self.operators.append(new_operator)

    def variables2str(self):
        res = ''
        num_primary_var = len(self.primary_var)
        num_secondary_var = len(self.secondary_var)
        num_var = num_primary_var + num_secondary_var
        res+='{}\n'.format(num_var)

        for i in range(0,num_var):
            if i in self.primary_var:
                res += ('begin_variable\n'
                        + 'var{}\n'.format(i)
                        + '-1\n'
                        + '{}\n'.format(len(self.primary_var[i])))
                for index,value in self.primary_var[i].items():
                    res+='{}\n'.format(value)
                res+='end_variable\n'
            elif i in self.secondary_var:
                res += ('begin_variable\n'
                        + 'var{}\n'.format(i)
                        + '{}\n'.format(self.axiom_layer[i])
                        + '{}\n'.format(len(self.secondary_var[i])))
                for index,value in self.secondary_var[i].items():
                    res+='{}\n'.format(value)
                res+='end_variable\n'
        return res

    def operators2str(self):
        res = '{}\n'.format(len(self.operators))
        for op in self.operators:
            res += str(op)
        return res

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("sas_file")
    parser.add_argument('--output',default='output.sas')
    args = parser.parse_args()

    sas = SAS3.from_file(args.sas_file)
    print(sas)

