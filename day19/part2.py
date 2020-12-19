# this version is currently not working. see part2-cfn.py for working solution

import re
lines = (x.strip() for x in open('part1.txt'))
rules = {x[0:x.index(':')]: x[x.index(':') + 2:] for x in lines if len(x) > 1 and ':' in x}
msgs = [x.strip() for x in open('part1.txt') if len(x) > 1 and ':' not in x]
def propagate_rules(rule='0'):
    res = ''
    if 'a' in rules[rule]:
        return 'a'
    elif 'b' in rules[rule]:
        return'b'
    else:
        subs = re.findall(r'(\d+|\|)', rules[rule])
        for sub in subs:
            if sub == '|':
                res += '|'
            elif sub == '8':
                res += '(' + propagate_rules('42') + ')+'
            elif sub == '11':
                res += '(' + propagate_rules('42') + ')+' + '(' + propagate_rules('31') + ')+'
            else:
                res += '(' + propagate_rules(sub) + ')'
    if rule == '0':
        res = '^' + res + '$'
    return res
rules_re = re.compile(propagate_rules())
print(sum([1 for msg in msgs if rules_re.match(msg)]))