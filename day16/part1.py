import re

lines = [x.strip() for x in open('input.txt').readlines()]
split = lines.index('your ticket:')
rules_re = re.compile(r'\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)')
rules = (x for y in ([(int(x[0]),int(x[1])),(int(x[2]),int(x[3]))] for x in (rules_re.match(x).groups() for x in lines[:split-1])) for x in y)
valid = {x:0 for  y in [list(range(x[0],x[1]+1)) for x in rules] for x in y}

invalid = [int(x) for y in (x.strip().split(',') for x in lines[split+4:]) for x in y if int(x) not in valid]

print(sum(invalid))