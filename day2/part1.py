import re

lines = (x.strip() for x in open('input.txt'))

reg_ex = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

valid = sum((1 for x in (reg_ex.match(x).groups() for x in lines) if x[3].count(x[2]) <= int(x[1]) and x[3].count(x[2]) >= int(x[0])))
print(valid)