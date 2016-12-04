#! /usr/bin/env python
# Which triangles are possible?

tricount = 0

f = open("day03_input.txt")
for line in f.readlines():	# returns list
    # Split to array of integers:
    tri = line.split()
    tri = [int(t) for t in tri]
    tri.sort()
    print tri,
    # Test by adding sides:
    if tri[0] + tri[1] > tri[2]:
        tricount = tricount + 1
        print "ok"
    else:
        print "bad"

print tricount, "valid triangles"
f.close()


# PART 2  - Read numbers vertically. 3 lines at a time. #
def testTriangles(buff):
    # Build a 3x3 nested list:
    numValid = 0
    group = []
    for line in buff:
        # Split to array of integers:
        threesome = line.split()
        threesome = [int(t) for t in threesome]
        group.append(threesome)

    # Test columns of list:
    for i in range(3):
        tri = [group[0][i], group[1][i], group[2][i]]
        tri.sort()
        print tri,
        # Test by adding sides:
        if tri[0] + tri[1] > tri[2]:
            numValid = numValid + 1
            print "ok"
        else:
            print "bad"

    return numValid

tricount = 0

threeLineBuffer = []
with open('day03_input.txt') as fp:
    for line in fp:
        threeLineBuffer.append(line)
        if len(threeLineBuffer) == 3:
            tricount = tricount + testTriangles(threeLineBuffer)
            threeLineBuffer = []

print tricount, "valid vertical triangles"
