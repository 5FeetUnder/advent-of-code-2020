earliest,bus_ids = open("input.txt").readlines()
earliest = int(earliest)
bus_ids = [int(bus) for bus in bus_ids.split(',') if bus != 'x']

time_to_busses = {bus:bus - (earliest%bus) for bus in bus_ids}

print(min(time_to_busses, key=time_to_busses.get) * time_to_busses[min(time_to_busses, key=time_to_busses.get)])