import re

commands = ([x.strip() for x in y.split('=')] for y in open('input.txt'))

class MemArray:
    def __init__(self):
        self.mask = {}
        self.cells = {}
    def set_mask(self, mask):
        self.mask[1] = [len(mask)-i-1 for i, x in enumerate(mask) if x == '1']
        self.mask[0] = [len(mask)-i-1 for i, x in enumerate(mask) if x == '0']
    def write_mem(self, address:int, value:int):
        for p in self.mask[1]:
            value = value | 1 << p
        for p in self.mask[0]:
            value = value & ~(1 << p)
        self.cells[address] = value
    def get_sum(self):
        res = 0
        for _, value in self.cells.items():
            res += value
        return res
    
mem = MemArray()
for command,value in commands:
    if command == 'mask': mem.set_mask(value)
    else:
        address = re.search(r"\[([\d]+)\]",command).group(1)
        mem.write_mem(int(address),int(value))
print(mem.get_sum())