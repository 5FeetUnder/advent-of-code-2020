forest = [[True if y == '#' else False for y in x.strip()] for x in open('input.txt')]
slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]
trees = 0
for slope in slopes:
    slope_trees = 0
    pos = (0,0)
    for _ in forest:
        pos = (pos[0] + slope[0], (pos[1] + slope[1]) % len(_))
        if pos[0] < len(forest):
            if forest[pos[0]][pos[1]]:
                slope_trees += 1
    trees = trees * slope_trees if trees != 0 else slope_trees
print(trees)