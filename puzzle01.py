#! /usr/bin/env python
# Find grid location from a list of turns and steps
import sys

input = "R4, R1, L2, R1, L1, L1, R1, L5, R1, R5, L2, R3, L3, L4, R4, R4, R3, L5, L1, R5, R3, L4, R1, R5, L1, R3, L2, R3, R1, L4, L1, R1, L1, L5, R1, L2, R2, L3, L5, R1, R5, L1, R188, L3, R2, R52, R5, L3, R79, L1, R5, R186, R2, R1, L3, L5, L2, R2, R4, R5, R5, L5, L4, R5, R3, L4, R4, L4, L4, R5, L4, L3, L1, L4, R1, R2, L5, R3, L4, R3, L3, L5, R1, R1, L3, R2, R1, R2, R2, L4, R5, R1, R3, R2, L2, L2, L1, R2, L1, L3, R5, R1, R4, R5, R2, R2, R4, R4, R1, L3, R4, L2, R2, R1, R3, L5, R5, R2, R5, L1, R2, R4, L1, R5, L3, L3, R1, L4, R2, L2, R1, L1, R4, R3, L2, L3, R3, L2, R1, L4, R5, L1, R5, L2, L1, L5, L2, L5, L2, L4, L2, R3"
inlist = input.split(', ')

compass = ['N', 'E', 'S', 'W']
index = 0   # start facing North
collector = {'N':0, 'E':0, 'S':0, 'W':0}
directions = []
visited = [(0,0)]

for step in inlist:
    # Rotate R or L:
    if step[0] == 'R':
        index = (index + 1) % 4
    elif step[0] == 'L':
        index = (index - 1) % 4
    else:
        # Bad input
        break

    # Compass direction now known:
    dir = compass[index]
    # Second part is how far: (can be multiple digits!)
    num = int(step[1:])
    #print dir, num
    # Store:
    directions.append(dir + step[1:])
    # Add to total:
    collector[dir] = collector[dir] + num


# Test location for previous visit:
def testLoc(myloc):
    if myloc in visited:
        print myloc
        sys.exit("First repeat visit")
    else:
        visited.append(myloc)

def findCrossover():
    myloc = (0,0)
    # Track points visited:
    for d in directions:
        dir = d[0]
        num = int(d[1:])
        if dir == 'N':
            while num > 0:
                myloc = (myloc[0], myloc[1] + 1)    # y increased
                testLoc(myloc)
                num = num - 1
        elif dir == 'E':
            while num > 0:
                myloc = (myloc[0] + 1, myloc[1])    # x increased
                testLoc(myloc)
                num = num - 1
        elif dir == 'S':
            while num > 0:
                myloc = (myloc[0], myloc[1] - 1)    # y decreased
                testLoc(myloc)
                num = num - 1
        elif dir == 'W':
            while num > 0:
                myloc = (myloc[0] - 1, myloc[1])    # x decreased
                testLoc(myloc)
                num = num - 1


print collector                             # {'S': 103, 'E': 136, 'W': 69, 'N': 128}
print abs(collector['N'] - collector['S'])  # 25
print abs(collector['E'] - collector['W'])  # 67

findCrossover()
