import sys, re

with open(sys.argv[1], "r") as file:
    inputs = file.read().splitlines()[0].split(',')
    products = []
    for line in inputs:
        products.append(line.split('-'))

#print(products)

invalid_ids = []
invalid_p2 = []
for i, g in products:
    for r in range(int(i), int(g)+1):
        rs = str(r)
        f_h = rs[:len(rs)//2]
        s_h = rs[len(rs)//2:]
        if f_h == s_h:
            invalid_ids.append(r)
        if rs in (rs + rs)[1:-1]:
            invalid_p2.append(r)


print(f"Invalid IDs part1: {sum(invalid_ids)}, \ninvalid IDs part2: {sum(invalid_p2)}\n")

