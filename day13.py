#! /usr/bin/env python
# Calculate a maze and find shortest route through it

# Build empty maze holder:
maze = []
for i in range(45):
    maze.append([0]*45)

# Calculate maze square values:
magicnumber = 1350
for y in range(45):
    for x in range(45):
        num = (x+y)*(x+y) + 3*x + y + magicnumber
        ones = str(bin(num)).count('1')
        maze[y][x] = ones % 2
        # Print it out:
        if y == 40 and x == 32:
            print 'G',
        elif ones % 2:
            print '#',
        else:
            print '.',
    print ''


# BFS algo:
def isHall(node):
    return not maze[node[1]][node[0]]  # 0 is a hall

def neighbours(coords):
    (x,y) = coords
    up    = (x, max(y-1, 0))
    down  = (x, min(y+1, 44))
    left  = (max(x-1, 0), y)
    right = (min(x+1, 44), y)
    # Only return Halls, never Walls:
    return [nb for nb in [up, down, left, right] if isHall(nb)]

start = (1,1)
goal = (0,0)        # impossible goal, for part 2
seen = {start: 0}   # measures steps to each node
to_see = [start] # ok
came_from = {start: None}

# Main algo:
while len(to_see) > 0:
    current = to_see.pop()
    #print "Visiting", current

    if current == goal:
        print 'GOAL!'
        break

    for nextNode in neighbours(current):
        if nextNode not in seen.keys():
            to_see.append(nextNode)
            # Next node will cost 1 more step than this node did:
            seen[nextNode] = seen[current] + 1
            came_from[nextNode] = current

within50 = [n for n in seen.keys() if seen[n] <= 50]
print len(within50)  # Part 2 answer

# Traceback:
parent = came_from[goal]
steps = 1
while parent:
    print parent, steps # Part 1 answer
    parent = came_from[parent]
    steps = steps + 1
