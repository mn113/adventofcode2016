#! /usr/bin/env python
# Transport all items to floor 4, avoiding dangerous situations
# (Missionaries/cannibals problem)

#4:
#3:
#2:   lp
#1: E   trc LPTRC
trips = 0
elev = 1
state = {   # tuple represents: (chip's floor, generator's floor)
    'V': (2,1),
    'W': (2,1),
    'X': (1,1),
    'Y': (1,1),
    'Z': (1,1)
}
goal = {key: (4,4) for key in 'VWXYZ'}

computedStates = {0: state}
newStates = []

def isValid(state):
    for k,v in state.items():
        # Stay between 1 and 4 please:
        if v[0] > 4 or v[0] < 1 or v[1] > 4 or v[1] < 1:
            print v, "out of bounds"
            return False
        if v[0] != v[1]:
            # Chip and its generator are apart
            for k2,v2 in state.items():
                if v2[0] == v[0]:
                    # Another generator will infect this chip
                    print "infection", state
                    return False
    print state, "ok"
    return True

# NEED TO STORE THEM ON EACH OTHER AND COUNT MOVES



# binary search
# 28 = too low
# 53 = too high
# 40 = too low
# 47 = correct
# part 2
# 61 = too low
# 71 = correct
