import sys, re

with open(sys.argv[1], "r") as file:
    inputs = [line for line in file.read().splitlines()]
    banks = []
    for line in inputs:
        banks.append([int(i) for i in line])

#print(banks)

def p2(bank):
    n = len(bank)
    
    # get maximum of the first n-len_seq elements, has to be starting battery
    jolt = ""
    idx = 0
    for len_seq in range(11, -1, -1):
        elem = max(bank[idx:n-len_seq])
        idx += bank[idx:n-len_seq].index(elem) + 1
        jolt += str(elem)

    return int(jolt)


jolts = []
jolts_p2 = []
for bank in banks:
    jolts_p2.append(p2(bank))
    # Part 1
    max_battery = max(bank)
    max_idx = bank.index(max_battery)
    if max_idx < len(bank)-1:
        rest_bank = bank[max_idx+1:]
        max_rest = max(rest_bank)
        jolts.append(int(str(max_battery)+str(max_rest)))
    else:
        rest_bank = bank[:max_idx]
        max_rest = max(rest_bank)
        jolts.append(int(str(max_rest)+str(max_battery)))


print(f"Joltages: {jolts}, \nyielding a sum of {sum(jolts)}\n")


print(f"High Joltages: {jolts_p2}, \nyielding a sum of {sum(jolts_p2)}\n")
