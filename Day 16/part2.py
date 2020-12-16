import re
import math

def find_match(a_list: list, b_list: list):
    if len(a_list) == 0:
        return [x for x in b_list]
    elif len(b_list) == 0:
        print('something\'s wrong')
        return [x for x in a_list]
    else:
        r_list = []
        for a in a_list:
            if a in b_list:
                r_list.append(a)
        return [x for x in r_list]

lines = [x.strip() for x in open('C:/Users/petsc/Documents/GitHub/advent-of-code-2020/Day 16/input.txt').readlines()]
split = lines.index('your ticket:')
rules_re = re.compile(r'(.+): (\d+)\D+(\d+)\D+(\d+)\D+(\d+)')
rules = {x[0]:[(int(x[1]),int(x[2])),(int(x[3]),int(x[4]))] for x in (rules_re.match(x).groups() for x in lines[:split-1])}
valid = {x:0 for y in [list(range(x[0],x[1]+1)) for y in rules.values() for x in y] for x in y}

nearby = ([int(y) for y in x.strip().split(',')] for x in lines[split+4:])
valid_nearby = [ticket for ticket in nearby if not len([x for x in ticket if x not in valid]) > 0]

positions = {x:[] for x in range(20)}

for ticket in valid_nearby:
    for i, value in enumerate(ticket):
        possible_rules = []
        for name,rule in rules.items():
            if (value >= rule[0][0] and value <= rule[0][1]) or (value >= rule[1][0] and value <= rule[1][1]):
                possible_rules.append(name)
        positions[i] = find_match(positions[i],possible_rules)
pos_len = 0
while pos_len != 20:
    for k, rs in positions.items():
        if len(rs) == 1:
            for key in positions:
                if key != k and rs[0] in positions[key]:
                    positions[key].remove(rs[0])
    pos_len = sum([len(x) for x in positions.values()])
my = [int(x) for x in lines[split+1].split(',')]
print(math.prod([x for i,x in enumerate(my) if 'departure' in positions[i][0]]))