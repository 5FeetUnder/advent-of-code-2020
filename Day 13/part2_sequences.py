from math import gcd
bus_ids = [(int(bus),-i) for (i,bus) in enumerate([x.strip() for x in open("D:/Users/Azure Meso/Documents/Programmierung/Advent of Code 2020/Day 13/input.txt")][1].split(',')) if bus != 'x']

def kgv(x,y):
    return x * y // gcd(x, y)

def combined_sequence(a, b, c, d):
    while b != d:
        if b < d:
            b += ((d-b-1) // a + 1) * a
        else:
            d += ((b-d-1) // c + 1) * c
    return (kgv(a, c), b)

solution = (1, 0)
for bus in bus_ids:
    solution = combined_sequence(*solution, *bus)

print(solution)