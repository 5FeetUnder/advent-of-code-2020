lines = (x.strip() for x in open("input.txt"))

next(lines)
bus_ids = [id for id in next(lines).split(',')]
# bus_ids = ['7','13','x','x','59','x','31','19']
# bus_ids = ['17','x','13','19']
# bus_ids = ['67','7','59','61']
# bus_ids = ['67','x','7','59','61']
# bus_ids = ['67','7','x','59','61']
# bus_ids = ['1789','37','47','1889']

bus_ids = [(int(bus),i) for (bus,i) in list(zip(bus_ids,range(len(bus_ids)))) if bus != 'x']

max_bus = max(bus_ids)
headstart = 100000000000000

i = headstart - (headstart % max_bus[0])
correct = True
while True:
    for bus in bus_ids:
        if (i + bus[1] - max_bus[1]) % bus[0] != 0:
            correct = False
            break
    if correct:
        print('Solution: {}'.format(i-max_bus[1]))
        break
    else:
        i = i + max_bus[0]
        correct = True
    print(i - max_bus[1])

print(bus_ids)