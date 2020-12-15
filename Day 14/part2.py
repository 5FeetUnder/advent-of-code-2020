import re
commands = ([x.strip() for x in y.split('=')] for y in open('Day 14/input.txt'))

class MemArray:
    def __init__(self):
        self.bitmask = 0
        self.cells = {}
        self.floating_bits = []
    def set_mask(self, mask):
        self.floating_bits = [len(mask)-i-1 for i, x in enumerate(mask) if x == 'X']
        self.bitmask = int(''.join((x if x != 'X' else '0' for x in mask)), 2)
    def write_mem(self, address:int, value:int):
        address = address | self.bitmask
        addresses = [address]
        if len(self.floating_bits) > 0:
            for f in self.floating_bits:
                a_copy = [x for x in addresses]
                for a in a_copy:
                    addresses.append(a | 1 << f)
                    addresses.append(a & ~(1 << f))
            addresses = list(dict.fromkeys(addresses))
        self.cells.update({x:value for x in addresses})
    def get_sum(self):
        return sum(self.cells.values())
    
mem = MemArray()
for command in commands:
    if command[0] == 'mask':
        mem.set_mask(command[1])
    else:
        address = re.search(r"\[([\d]+)\]",command[0]).group(1)
        mem.write_mem(int(address),int(command[1]))
print(mem.get_sum())