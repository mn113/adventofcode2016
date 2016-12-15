#! /usr/bin/env python
# Find out when 6 rotating discs align

# Puzzle input:
'''
Disc #1 has 17 positions; at time=0, it is at position 1.
Disc #2 has 7 positions; at time=0, it is at position 0.
Disc #3 has 19 positions; at time=0, it is at position 2.
Disc #4 has 5 positions; at time=0, it is at position 0.
Disc #5 has 3 positions; at time=0, it is at position 0.
Disc #6 has 13 positions; at time=0, it is at position 5.
'''
#disc17 = 16  # checked at t=15
#disc7 = 2   # checked at t=16
#disc19 = 0  # checked at t=17
#disc5 = 3   # checked at t=18
#disc3 = 1   # checked at t=19
#disc13 = 12  # checked at t=20
#disc11 = 10          # at t=21

t = 15  # First 15 seconds are advanced manually
discs = [16,2,0,3,1,12,10]
step = 19   # The disc with 19 positions will only be 0 every 19 steps

limit = 3*5*7*11*13*17*19  # Entire disc system will repeat after this many steps
print "limit", limit

# Main loop:
while 1:
    t = t + step    # Move ahead by step seconds
    discs[0] = (discs[0] + step) % 17
    discs[1] = (discs[1] + step) % 7
    discs[2] = (discs[2] + step) % 19   # always 0
    discs[3] = (discs[3] + step) % 5
    discs[4] = (discs[4] + step) % 3
    discs[5] = (discs[5] + step) % 13
    discs[6] = (discs[6] + step) % 11

    if t > limit or (discs == [0,0,0,0,0,0,0]):
        print t, "seconds elapsed"
        print discs
        break

# subtract 1 from given time to get button-pressing time
