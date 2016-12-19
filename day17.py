#! /usr/bin/env python
# Find shortest route through a maze of doors which are unlocked or locked based on MD5

#   0 1 2 3
# 0 A . . .
# 1 . . . .
# 2 . . . .
# 3 . . . Z

import hashlib
import sys

start = (0,0)   # (x,y)
goal = (3,3)
solutions = []
longestRoute = ''

def checkDoors(location, movesSoFar):
    global longestRoute

    print location
    print movesSoFar

    # End conditions:
    if len(movesSoFar) > 600:  # 600 too high!
        #return
        print len(longestRoute)
        sys.exit()
    if location == goal:
        solutions.append(movesSoFar)
        if len(movesSoFar) > len(longestRoute):
            longestRoute = movesSoFar
        return

    # Generate the hash:
    h = hashlib.md5('gdjjyniy' + movesSoFar).hexdigest()
    print h

    # Find which doors are open:
    doors = [False]*4
    doors[0] = h[0] in 'bcdef'   # up
    doors[1] = h[1] in 'bcdef'   # down
    doors[2] = h[2] in 'bcdef'   # left
    doors[3] = h[3] in 'bcdef'   # right
    print doors
    if doors == [False]*4:
        print "locked in!", location, movesSoFar
        return

    # Check availability of 4 rooms (up, down, left, right)
    # Move to them all, and recursively call this function
    if doors[0] and location[1] > 0:
        checkDoors((location[0], location[1] - 1), movesSoFar + 'U')
    if doors[1] and location[1] < 3:
        checkDoors((location[0], location[1] + 1), movesSoFar + 'D')
    if doors[2] and location[0] > 0:
        checkDoors((location[0] - 1, location[1]), movesSoFar + 'L')
    if doors[3] and location[0] < 3:
        checkDoors((location[0] + 1, location[1]), movesSoFar + 'R')


# Let's do it!
checkDoors(start, '')
# Find the shortest of the solution routes manually:
for sol in solutions:
    print sol
print len(solutions), "solutions found"
print max([len(sol) for sol in solutions]), "the longest"
