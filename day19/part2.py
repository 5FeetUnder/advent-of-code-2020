# this version is currently not working. see part2-cfn.py for working solution

import re
lines = [x.strip() for x in open('part2.txt')]
rules = {x[0:x.index(':')]: x[x.index(':') + 2:] for x in lines if len(x) > 1 and ':' in x}
msgs = (x.strip() for x in lines if len(x) > 1 and ':' not in x)
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
                res += '(?P<rule11>(' + propagate_rules('31') + ')+)'
            else:
                res += propagate_rules(sub)
        if '|' in subs:
            res = f'({res})'
    if rule == '0':
        res = '^' + res + '$'
    return res
# rules_re = re.compile(propagate_rules())
rule31_re = re.compile(propagate_rules('31'))
print(propagate_rules('31'))
valid_count = 0
for msg in msgs:
    rule31_count = len(rule31_re.findall(msg))
    print(rule31_count)
    rules_string = f"^({propagate_rules('42')})+({propagate_rules('42')}){{{rule31_count}}}({propagate_rules('31')}){{{rule31_count}}}$"
    if re.match(rules_string, msg):
        valid_count += 1
print(valid_count)

# print(sum([1 for msg in msgs if re.match(rules_re.sub(lambda match: f'({propagate_rules("42")}){{{len(rule31_re.findall(msg))}}}{match.group("rule11")}', msg), msg)]))