import sys
import math

def multiply_p1(numbers, idx):
    res = 1
    for row in numbers:
        res *= row[idx]
    return res

def solve_worksheet(numbers, operations, part):
    sums_p1 = [ sum(x) for x in zip(*numbers) ]
    worksheet = []
    for i, op in enumerate(operations):
        if op == '+':
            if part == 1:
                worksheet.append(sums_p1[i])
            else:
                worksheet.append(sum(numbers[i]))
        else:
            if part == 1:
                worksheet.append(multiply_p1(numbers, i))
            else:
                worksheet.append(math.prod(numbers[i]))
    return worksheet


with open(sys.argv[1], "r") as file:
    inputs = [line for line in file.read().splitlines()]
    numbers = []
    for line in inputs[:-1]:
        numbers.append([int(i) for i in line.split()])
    operations = inputs[-1].split()

    #---- part 2
    cephalopods = [i for i in inputs[0][::-1]]
    for line in inputs[1:-1]:
        cephalopods = [a+b for a, b in zip(cephalopods, line[::-1])]
    
    numbers_p2 = []
    numbers_p2.append([])
    i = 0
    for c in cephalopods:
        if all(e == ' ' for e in c):
            # new line in worksheet
            numbers_p2.append([])
            i += 1
        else:
            numbers_p2[i].append(int(c))


worksheet = solve_worksheet(numbers, operations, 1)
worksheet_p2 = solve_worksheet(numbers_p2, reversed(operations), 2)

print(f"The worksheet gives a grad total of {sum(worksheet)}.\n")

print(f"The worksheet with cephalopod math gives a grad total of {sum(worksheet_p2)}.")
