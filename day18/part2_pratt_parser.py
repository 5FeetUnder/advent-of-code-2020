nud, led, lbp = 'nud', 'led', 'lbp'
ops = {
    '+': {
        'lbp': 20,
        'led': lambda tokens, toki, left: left + expression_new(tokens, toki, 20)
    },
    '*': {
        'lbp': 10,
        'led': lambda tokens, toki, left: left * expression_new(tokens, toki, 10)
    },
    '(': {
        'lbp': 0,
        'nud': lambda tokens, toki, t: (expression_new(tokens, toki), inc(toki))[0]
    },
    ')': {
        'lbp': 0
    },
    '#': {
        'lbp': 0
    }
}

literal = { 'nud': lambda tokens, toki, t: int(t) }

def expression_new(tokens, toki, rbp=0):
    t = tokens[toki[0]]
    inc(toki)
    left = ops.get(t, literal)[nud](tokens, toki, t)
    while rbp < ops.get(tokens[toki[0]])[lbp]:
        t = tokens[toki[0]]
        inc(toki)
        left = ops.get(t, literal)[led](tokens, toki, left)
    return left

def inc(a):
    a[0] += 1

lines = (x.strip().replace(' ', '') + '#' for x in open('input.txt'))
result = []
for line in lines:
    toki = [0]
    result.append(expression_new(line, toki))

print(sum(result))