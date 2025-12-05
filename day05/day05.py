import sys

with open(sys.argv[1], "r") as file:
    blocks = file.read().split("\n\n")
    ranges = blocks[0].split()
    ingredient_ranges = []
    for elem in ranges:
        borders = elem.split("-")
        ingredient_ranges.append(range(int(borders[0]), int(borders[1])+1))
    available_ingredients = [int(i) for i in blocks[1].split()]

#print(ingredient_ranges)

fresh_ingredients = 0
for ingredient in available_ingredients:
    for r in ingredient_ranges:
        if ingredient in r:
            fresh_ingredients += 1
            break

print(f"{fresh_ingredients} of the available ingredients are fresh\n")

ingredient_ranges = sorted(ingredient_ranges, key=lambda x : x.start)
considered = [ingredient_ranges[0]]
for r in ingredient_ranges[1:]:
    if considered[-1].stop >= r.start:
        interval = range(considered[-1].start, max(considered[-1].stop, r.stop))
        del considered[-1]
        considered.append(interval)
    else:
        considered.append(r)

fresh_ranges = sum([len(r) for r in considered])
print(f"Fresh ingredient ranges have {fresh_ranges} fresh IDs")
