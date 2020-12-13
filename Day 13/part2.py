lines = (x.strip() for x in open("input.txt"))

bus_ids = [id for id in lines[1].split(',')]
bus_ids = [(int(bus),i) for (bus,i) in list(zip(bus_ids,range(len(bus_ids)))) if bus != 'x']

headstart = 100000000000000

i = headstart - (headstart % bus_ids[0][0])
print(i % bus_ids[0][0])
correct = True
while True:
    for bus in bus_ids:
        if (i + bus[1]) % bus[0] != 0:
            correct = False
            break
    if correct:
        print('Solution: {}'.format(i))
        break
    else:
        i = i + bus_ids[0][0]
        correct = True
    print(i)