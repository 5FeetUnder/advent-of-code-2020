lines = (x.strip() for x in open("input.txt"))

earliest = int(next(lines))
bus_ids = [int(id) for id in next(lines).split(',') if id != 'x']

time_to_busses = {bus: bus - (earliest % bus) for bus in bus_ids}

next_bus = min(time_to_busses, key=time_to_busses.get)
print(next_bus * time_to_busses[next_bus])