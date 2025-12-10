import sys
from copy import deepcopy
from scipy.optimize import linprog

def parse_joltages(line):
    return [int(x) for x in line.strip("{}").split(",")] 

def parse_buttons(line):
    return [int(x) for x in line.strip("()").split(",")] 

def parse_lights(line):
    light = []
    for l in line:
        if l == '.':
            light.append(0)
        else:
            light.append(1)
    return light


with open(sys.argv[1], "r") as file:
    inputs = [line for line in file.read().splitlines()]
    lights = []
    buttons = []
    joltages = []
    for line in inputs:
        l = line.split()
        lights.append(parse_lights(l[0][1:-1]))
        buttons.append([parse_buttons(t) for t in l[1:-1]])
        joltages.append(parse_joltages(l[-1]))


presses = []
for l, light in enumerate(lights):
    
    start = [0] * len(light)
    q = [(start, 0)]
    visited = [str(start)]
    while q:
        curr_light, pressed = q[0]
        del q[0]
        if curr_light == light:
            presses.append(pressed)
            break

        for button in buttons[l]:
            # without deepcopy q will only hold the same of two items
            toggled = deepcopy(curr_light)
            for press in button:
                toggled[press] = toggled[press] ^ 1
            new_light = str(toggled)
            if new_light not in visited:
                visited.append(new_light)
                q.append((toggled, pressed + 1))


print(f"The button presses required to configure indicator lights are {sum(presses)}.\n")


presses_p2 = []
for j, jolt in enumerate(joltages):
    # For each joltage, note down which button will turn on which position
    button_matrix = [[(idx in b) for b in buttons[j]] for idx in range(len(jolt))]
    # The button presses to minimize
    c = [1 for b in buttons[j]]
    presses_p2.append(round(linprog(c, A_eq=button_matrix, b_eq=jolt, integrality=1).fun))


# int(sum()) != sum(int()) -> round
print(f"The button presses required to configure the joltage levels are {sum(presses_p2)}.")
