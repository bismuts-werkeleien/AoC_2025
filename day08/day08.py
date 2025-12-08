import sys
import math

with open(sys.argv[1], "r") as file:
    inputs = [line for line in file.read().splitlines()]
    boxes = []
    for line in inputs:
        boxes.append([int(i) for i in line.split(',')])

pairs = 1000
#test input
#pairs = 10
distances = []
for i, box_1 in enumerate(boxes[:-1]):
    j = i+1
    for box_2 in boxes[i+1:]:
        distance = math.sqrt(sum(((box_1[k] - box_2[k])**2) for k in range(3)))
        distances.append((i, j, distance))
        j += 1

distances = sorted(distances, key = lambda z: z[2])

circuits = []
p = 0
for a, b, _ in distances:
    p += 1
    updated = -1
    for i, c in enumerate(circuits):
        if (a in c or b in c) and updated == -1:
            circuits[i].update([a, b])
            updated = i
        elif (a in c or b in c) and updated != -1:
            #merge
            circuit = circuits[i]
            del circuits[i]
            circuits[updated].update(circuit)
        
    if updated == -1:
        circuits.append({a, b})

    # Part 1
    if p == pairs:
        circuits = sorted(circuits, key = lambda l: len(l), reverse=True)
        lengths = list(map(len, circuits[:3]))
        print(f"The three largest circuits multiply to {lengths[0]*lengths[1]*lengths[2]}")

    # Part 2
    if len(circuits[0]) == len(boxes):
        print(f"The x coordinates of the last two junktion boxes multiply to {boxes[a][0] * boxes[b][0]}")
        break

