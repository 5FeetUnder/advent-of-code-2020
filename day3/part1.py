forest = [[True if y == '#' else False for y in x.strip()] for x in open('input.txt')]
pos = (0,0)
trees = 0
for _ in forest:
    pos = (pos[0] + 1, (pos[1] + 3) % len(_))
    if pos[0] < len(forest):
        if forest[pos[0]][pos[1]]:
            trees += 1
print(trees)