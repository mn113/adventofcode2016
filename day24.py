#! /usr/bin/env python
# Find result of long-running instruction set

import itertools

# Load maze file into nested array:
pois = {}
with open('day24_input.txt') as fp:
    maze = fp.readlines()
    # Traverse maze and extract points of interest:
    for r in range(len(maze)):
        row = maze[r]
        for c in range(len(row)):
            char = row[c]
            if char in list('01234567'):
                pois[maze[r][c]] = (c,r)

print pois

def isHall(node):
    if maze[node[1]][node[0]] == '#':
        return False
    return True


def neighbours(coords):
    (x,y) = coords
    up    = (x, max(y-1, 0))
    down  = (x, min(y+1, 36))
    left  = (max(x-1, 0), y)
    right = (min(x+1, 183), y)
    # Only return Halls, never Walls:
    return [nb for nb in [up, down, left, right] if isHall(nb)]


def manhattan_dist(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Main algo:
def bfs(start, goal):
    dist_to = {start: 0}    # measures steps to each node
    to_visit = [start]
    came_from = {start: None}   # traces the path taken
    limit = manhattan_dist(start,goal)

    while len(to_visit) > 0:
        current = to_visit.pop()
        print "Visiting", current, dist_to[current] #, (1.0 * manhattan_dist(current,goal))/limit
        #if manhattan_dist(current,goal) > limit * 1.5:
            # Abandon this circuitous path:
            #continue

        if current == goal:
            print 'GOAL!', len(to_visit), "to see"
            # Keep searching, to guarantee shortest:
            #continue

        if dist_to[current] > 100:
            continue

        neighbs = neighbours(current)
        if len(neighbs) == 1 and neighbs[0] != goal:
            # Dead end:
            continue

        for nextNode in neighbs:
            # nextNode unseen:
            if nextNode not in dist_to.keys():
                # Add to queue:
                to_visit.append(nextNode)
                # Next node will cost 1 more step than this node did:
                dist_to[nextNode] = dist_to[current] + 1
                came_from[nextNode] = current

            # nextNode seen before:
            else:
                if dist_to[nextNode] > dist_to[current] + 1:
                    # Via current, we have found a new, shorter path to this known nextNode:
                    dist_to[nextNode] = dist_to[current] + 1
                    came_from[nextNode] = current

    # Finished seeing nodes now
    if goal in came_from.keys():
        print "DONE"
        return traceback(goal, came_from)
    else:
        return "No path found"


# Traceback function:
def traceback(goal, came_from):
    parent = came_from[goal]
    steps = 0
    print goal, "Goal"
    while parent:
        print parent, steps # Part 1 answer
        parent = came_from[parent]
        steps = steps + 1
    return steps


# Full node graph:
edges = {}
for a in pois.keys():
    for b in pois.keys():
        if b > a:
            edges[(a,b)] = bfs(pois[a], pois[b])
            print edges[(a,b)], "from", a, "to", b


def sum_edges(sequence):
    total = 0
    for i in range(len(sequence) - 1):
        a, b = sequence[i], sequence[i+1]
        total = total + edges[(min(a,b),max(a,b))]
    return total

# Try every sequence of the 8 nodes:
'''
routes = {}
for seq in itertools.permutations(list("1234567")):
    # Start at 0:
    seq = ['0'] + list(seq)
    routes[''.join(seq)] = sum_edges(seq)
# Sort and display:
for route in sorted(routes, key=routes.__getitem__):
    if routes[route] < 850:
        print route, ':', routes[route]      #
print '02754631 :', routes['02754631']
'''
# 02475631 = 844 - too high

# 0-2 = 12
# 2-4 = 148
# 4-7 = 188
# 7-5 = 74
# 5-6 = 240
# 6-3 = 70
# 3-1 = 112
print sum([12,148,188,74,240,70,112]) # 844 too high

print bfs(pois['1'],pois['3'])
