import sys

def paper(pos):
    if pos == '@':
        return 1
    return 0

def get_adjacents(y, x):
    adj = 0
    rows = len(grid)
    cols = len(grid[0])
    start_x = 0 if x == 0 else x-1
    end_x = x+1 if x == cols-1 else x+2
    
    if y == 0:
        adj = sum(grid[y][start_x:end_x]) + sum(grid[y+1][start_x:end_x])
    elif y == rows -1:
        adj = sum(grid[y][start_x:end_x]) + sum(grid[y-1][start_x:end_x])
    else:
        adj = sum(grid[y][start_x:end_x]) + sum(grid[y+1][start_x:end_x]) + sum(grid[y-1][start_x:end_x])

    adj -= grid[y][x]

    return adj


with open(sys.argv[1], "r") as file:
    inputs = [line for line in file.read().splitlines()]
    grid = []
    for line in inputs:
        grid.append([paper(pos) for pos in line])

def get_accessibles():
    accessible = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1 and get_adjacents(y, x) < 4:
                accessible += 1
    return accessible


print(f"There are {get_accessibles()} rolls of paper accessible.\n")

def remove_paper(accessible):
    to_be_removed = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1 and get_adjacents(y, x) < 4:
                to_be_removed.append((y, x))
                accessible += 1
    
    if len(to_be_removed) > 0:
        for pos in to_be_removed:
            grid[pos[0]][pos[1]] = 0
        return remove_paper(accessible)
    return accessible

accessible = remove_paper(0)

print(f"Now we can remove {accessible} rolls of paper.")

