import numpy as np

def print_cubes(cubes: list):
    for iw,w in enumerate(cubes):
        for iz,z in enumerate(w):
            print(f"z = {iz}, w = {iw}\n")
            for y in z:
                x_string = ''
                for x in y:
                    x_string += x
                print(f"{x_string}\n")

def get_neighbours(pos_w, pos_z, pos_y, pos_x, cubes):
    neighbours = 0
    for w in (0,1) if pos_w == 0 else (-1,0) if  pos_w == cubes.shape[0] - 1 else (-1,0,1):
        for z in (0,1) if pos_z == 0 else (-1,0) if  pos_z == cubes.shape[1] - 1 else (-1,0,1):
            for y in (0,1) if pos_y == 0 else (-1,0) if  pos_y == cubes.shape[2] - 1 else (-1,0,1):
                for x in (0,1) if pos_x == 0 else (-1,0) if  pos_x == cubes.shape[3] - 1 else (-1,0,1):
                    if not all([True if a == 0 else False for a in (w,x,y,z)]):
                        if cubes[pos_w + w][pos_z + z][pos_y + y][pos_x + x] == '#':
                            neighbours += 1
    return neighbours

def expand_cubes(a):
    a = np.insert(a, (0, len(a)), '.', axis=0)
    a = np.insert(a, (0, len(a[0])), '.', axis=1)
    a = np.insert(a, (0, len(a[0][0])), '.', axis=2)
    a = np.insert(a, (0, len(a[0][0][0])), '.', axis=3)
    return a

def shrink_cubes(c):
    n = 0
    for i,_ in enumerate(c.shape):
        c = np.rot90(c,axes=(0,i)) if i > 0 else c
        if all([True if a == '.' else False for d in c[0] for b in d for a in b]):
            c = np.delete(c,0,axis=0)
            n += 1
        if all([True if a == '.' else False for d in c[-1] for b in d for a in b]):
            c = np.delete(c,len(c)-1,axis=0)
            n += 1
        c = np.rot90(c,3,axes=(0,i)) if i > 0 else c
    if n == 0:
        return c
    else:
        return shrink_cubes(c)

cubes = np.array([[[[a for a in b.strip()] for b in open('Day 17/input.txt')]]])

for _ in range(6):
    cubes = expand_cubes(cubes)
    next_cubes = np.copy(cubes)
    for wi,w in enumerate(cubes):
        for zi,z in enumerate(w):
            for yi,y in enumerate(z):
                for xi,x in enumerate(y):
                    neighbours = get_neighbours(wi,zi,yi,xi,cubes)
                    if next_cubes[wi,zi,yi,xi] == '#' and neighbours not in (2,3):
                        next_cubes[wi,zi,yi,xi] = '.'
                    elif next_cubes[wi,zi,yi,xi] == '.' and neighbours == 3:
                        next_cubes[wi,zi,yi,xi] = '#'
    cubes = shrink_cubes(next_cubes)
    print(f"\nAfter {_ + 1} cycles:\n")
    print_cubes(cubes)
print(sum([1 for a in cubes.flat if a == '#']))