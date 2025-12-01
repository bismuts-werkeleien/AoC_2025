import sys, re

num_digits=100

with open(sys.argv[1], "r") as file:
    rotations = [value.strip("\n") for value in file]

#print(rotations)
def rotate(s):
    if "L" in s:
        return -int(s[1::])
    return int(s[1::])

def method_43C(dial, new_dial, i):
    instr = rotate(i)
    if "R" in i:
        password = (dial+(instr))//num_digits
    else:
        password = abs(instr)//num_digits
        if dial != 0 and (new_dial == 0 or new_dial > dial):
            password += 1
    return password

# move dial
dial_pos=50
num_zeros=0
method_43=0
for i in rotations:
    instr = rotate(i)
    dial_new = (dial_pos + instr) % num_digits
    method_43 += method_43C(dial_pos, dial_new, i)
    if dial_new == 0:
        num_zeros += 1
    dial_pos = dial_new

print(f"Password: {num_zeros}")
print(f"Password using method 0x43C: {method_43}")

