#! /usr/bin/env python
# Circle of elves stealing presents (Josephus problem)

# <- presents
# 1 1 1 1 1
# 2 0 1 1 1
# 2 0 2 0 1
# 0 0 2 0 3
# 0 0 5 0 0

# Each elf starts with 1 present:
elves = [1] * 5     # 3014603
l = len(elves)

i = 0
while 1:
    # Skip a present-less elf:
    if elves[i] == 0:
        # Move ahead (looping round):
        i = (i+1)%l

    else:
        # Find next present-bearing elf (looping back round if necessary):
        j = (i+1)%l
        while elves[j] == 0:
            # Skip the present-less:
            j = (j+1)%l
        # Steal presents (j->i):
        elves[i] = elves[i] + elves[j]
        elves[j] = 0

        # Check for total present ownership:
        if elves[i] == l:
            print "Part 1: Elf", i, "possesses", elves[i], "presents"
            break

        # Move ahead (looping round):
        i = (j+1)%l

print "---"

# Part 2
# x = 3014603
# Brute-force solving is too slow.
# Analysis of solutions for circles of 5-1000 revealed a repeating arithmetic progression
#  based on intervals of powers of 3
# Two simple formulas predict the winner for any input size

powers_of_3 = [3**t for t in range(15)]

def josephus_formula(x):
    lower3 = max([p for p in powers_of_3 if p < x])
    upper3 = min([p for p in powers_of_3 if p >= x])
    # Apply formula to 2 tranches:
    if x <= 2 * lower3:
        y = x - lower3 - 1
    else:
        y = (2 * x) - (3 * lower3) - 1
    return y

x = 3014603
print "Part 2:", x, "elves,", josephus_formula(x), "th elf wins"
