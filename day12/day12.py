import sys
import numpy as np


with open(sys.argv[1], "r") as file:
    blocks = file.read().split("\n\n")
    shapes = []
    for block in blocks[:6]:
        lines = block.split("\n")
        shape = [[1 if s == '#' else 0 for s in l] for l in lines[1:]]
        shapes.append(np.array(shape))
    regions = []
    areas = []
    for line in blocks[6].split("\n")[:-1]:
        l = line.split(":")
        areas.append(tuple(int(a) for a in l[0].split("x")))
        regions.append([int(r) for r in l[-1].split()])


fits = 0
for i, a in enumerate(areas):
    area = a[0]*a[1]
    
    filled = 0
    for j, r in enumerate(regions[i]):
        filled += sum(sum(shapes[j]))*r
        if filled > area:
            break
    else:
        fits += 1
    
    """
    if sum(regions[i])*9 <= area:
        fits+=1
    """
    

print(f"The number of regions which can fit all presents is {fits}.\n")

