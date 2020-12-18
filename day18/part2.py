lines = ((x if x in ('*','+','(',')') else int(x) for x in line if x != ' ') for line in (x.strip() for x in open('input.txt')))
ops = {
    '+' : {'run': (lambda a, b: a + b), 'prio': 1},
    '*' : {'run': (lambda a, b: a * b), 'prio': 0},
}
results = []
for line in lines:
    rpn = []
    stack = []
    for token in line:
        if type(token) == int:
            rpn.append(token)
        elif token in ops:
            while len(stack) > 0 and stack[-1] != '(' and ops[stack[-1]]['prio'] >= ops[token]['prio']:
                rpn.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                rpn.append(stack.pop())
            stack.pop() if stack[-1] == '(' else None
    while len(stack) > 0:
        rpn.append(stack.pop())
    if len(stack) > 0:
        print('asd')
    for token in rpn:
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[token]['run'](a,b))
        else:
            stack.append(token)
    results.append(stack.pop())
print(sum(results))