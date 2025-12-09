import sys

def in_tiles(t1, t2, p1, p2):
    return (max(t1, t2) <= p2 or min(t1, t2) >= p1)

with open(sys.argv[1], "r") as file:
    inputs = [line for line in file.read().splitlines()]
    boxes = []
    for line in inputs:
        boxes.append([int(i) for i in line.split(',')])

distances = []
rects_p2 = []
for i, box_1 in enumerate(boxes):
    for box_2 in boxes[i:]:
        a1, a2 = max([box_1[0], box_2[0]]), min([box_1[0], box_2[0]])
        b1, b2 = max([box_1[1], box_2[1]]), min([box_1[1], box_2[1]])
        distances.append([a1 - a2 + 1, b1 - b2 + 1])
        for j, t1 in enumerate(boxes):
            t2 = boxes[(j+1) % len(boxes)]
            if not (in_tiles(t1[0], t2[0], a1, a2) or in_tiles(t1[1], t2[1], b1, b2)):
                break
        else:
            rects_p2.append((a1 - a2 + 1)*(b1 - b2 + 1))

rects = [d[0]*d[1] for d in distances]
print(f"The largest rect is {max(rects)}")

print(f"The largest contained rect is {max(rects_p2)}")

