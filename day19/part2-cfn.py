from pyformlang.cfg import Production, Variable, Terminal, CFG
import re

var_re = re.compile(r'(\d+)')
ter_re = re.compile(r'.*([ab]).*')

lines = (x.strip() for x in open('part2.txt'))
rules = {x[0:x.index(':')]: x[x.index(':') + 2:] for x in lines if len(x) > 1 and ':' in x}
msgs = [x.strip() for x in open('part2.txt') if len(x) > 1 and ':' not in x]

rule_vars = set()
rule_prods = set()

for rule in rules:
    subs = rules[rule].split('|')
    rule_vars.add(Variable(rule))
    for sub in subs:
        if ter_re.match(sub):
            rule_prods.add(Production(Variable(rule), [Terminal(ter_re.match(sub).group(1))]))
        else:
            rule_prods.add(Production(Variable(rule), [Variable(x) for x in var_re.findall(sub)]))


ter_a = Terminal('a')
ter_b = Terminal('b')

cfg = CFG(rule_vars, {ter_a, ter_b}, Variable('0'), rule_prods)
print(sum([1 for msg in msgs if cfg.contains(msg)]))