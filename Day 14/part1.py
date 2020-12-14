commands = ([x.strip() for x in y.split('=')] for y in open('Day 14/input.txt'))
# commands = ([x.strip() for x in y.split('=')] for y in ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 'mem[8] = 11', 'mem[7] = 101', 'mem[8] = 0'])

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
        print(len(bin(value))-2)
        self.cells[address] = value
    def get_sum(self):
        res = 0
        for _, value in self.cells.items():
            res += value
        return res
    
mem = MemArray()
for command in commands:
    if command[0] == 'mask':
        mem.set_mask(command[1])
    else:
        mem.write_mem(int(command[0][command[0].find('[')+1:command[0].find(']')]),int(command[1]))
print(mem.get_sum())