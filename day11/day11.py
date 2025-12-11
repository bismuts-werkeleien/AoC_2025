import sys
import functools

from collections import defaultdict


with open(sys.argv[1], "r") as file:
    inputs = [line for line in file.read().splitlines()]
    devices = defaultdict(list)
    for line in inputs:
        l = line.split(':')
        devices[l[0]] = l[1].split()

@functools.cache
def dfs(curr, end, paths):
    if curr == end:
        paths+=1
        return paths
    else:
        return sum(dfs(neigh, end, paths) for neigh in devices[curr])


print(f"The number of paths from 'you' to 'out' is {dfs('you', 'out', 0)}.\n")

paths = dfs('svr', 'fft', 0) * dfs('fft', 'dac', 0) * dfs('dac', 'out', 0)
paths += (dfs('svr', 'dac', 0) * dfs('dac', 'fft', 0) * dfs('fft', 'out', 0))
print(f"The number of paths which visit 'dac' and 'fft' are {paths}.\n")
