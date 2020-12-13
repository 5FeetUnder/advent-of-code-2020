from math import gcd
bus_ids = [(int(bus),-i) for (i,bus) in enumerate([x.strip() for x in open("D:/Users/Azure Meso/Documents/Programmierung/Advent of Code 2020/Day 13/input.txt")][1].split(',')) if bus != 'x']

def kgv(x,y):
    return x * y // gcd(x, y)

def combined_sequence(a, b, c, d):
    while b != d:
        next_b_or_d = lambda u, v, w : u + ((v - u - 1) // w + 1) * w
        b = next_b_or_d(b, d, a) if b < d else b
        d = next_b_or_d(d, b, c) if d < b else d
    return (kgv(a, c), b)

solution = (1, 0)
for bus in bus_ids:
    solution = combined_sequence(*solution, *bus)

print(solution)