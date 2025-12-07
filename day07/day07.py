import sys
from functools import cache

@cache
def quantum_paths(beam):
    while True:
        if beam[0] == len(field)-1:
            return 1
        if field[beam[0]][beam[1]] == '.':
            beam = (beam[0]+1, beam[1])
            continue
        if field[beam[0]][beam[1]] == '^':
            left = (beam[0]+1, beam[1]-1)
            right = (beam[0]+1, beam[1]+1)
            return quantum_paths(left) + quantum_paths(right)


with open(sys.argv[1], "r") as file:
    lines = file.read().splitlines()
    field = []
    for line in lines:
        field.append([p for p in line])


tachyons = [[(0, field[0].index('S'))]]
width = len(field[0])-1
splits = 0
timelines = quantum_paths((1, field[0].index('S')))

for i in range(1,len(field)):
    beams = set()
    for r,c in tachyons[-1]:
        if field[r+1][c] == '.':
            beams.add((r+1, c))
        elif field[r+1][c] == '^':
            if (r, c) in tachyons[-1]:
                splits += 1

                beams.add((r+1, max(0, c-1)))
                beams.add((r+1, min(c+1, width)))
    tachyons.append(list(beams))

print(f"There are {splits} beams split in the end")
print(f"There are {timelines} timelines in the end")

