#! /usr/bin/env python
# Circle of elves stealing presents

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
import math
import sys

elves = {k:1 for k in range(3014603)}
l = len(elves.keys())
orig_l = l

'''
instead of dict {1:1, 2:1, ...}
could use array of seating positions: [1,2,3,4,5]
presents not counted
'''

k = 0
while l > 1:
    #print elves.keys(), l, "elves"
    #print "#", k, "to pick"

    # Find opposite seated elf:
    dist = math.floor(l/2)
    k_index = elves.keys().index(k)     # slow part?
    opp_index = int(k_index + dist) % l
    #print opp_index, "to lose",

    # Steal presents:
    victimKey = elves.keys()[opp_index]
    #print "(Elf", victimKey, ")"
    elves[k] = elves[k] + elves[victimKey]

    # Kick presentless elf:
    del elves[victimKey]
    l = l-1

    # Move ahead to next elf (looping round):
    k = (k+1)%orig_l
    while k not in elves.keys():
        k = (k+1)%orig_l

    # Live output of length to screen:
    sys.stdout.write("Elves remaining: %d%   \r" % (l) )
    sys.stdout.flush()

print "Part 2:", elves
