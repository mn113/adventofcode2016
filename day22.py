#! /usr/bin/env python
# Shift data around within a matrix

class Matrix:
    """ A matrix, or nested arrays of equal length """
    rows = 0
    cols = 0

    # Build up a matrix of values:
    def __init__(self, x, y, val):
        self.matrix = []
        self.rows = y
        self.cols = x
        for i in range(y):
            self.matrix.append([val]*x)

    def setNode(self, (x,y), values):
        self.matrix[y][x] = values

    def setAvail(self, (x,y), val):
        self.matrix[y][x]['avail'] = val

    def setUsed(self, (x,y), val):
        self.matrix[y][x]['used'] = val

    def getAvail(self, (x,y)):
        return self.matrix[y][x]['avail']

    def getUsed(self, (x,y)):
        return self.matrix[y][x]['used']

    # Add data to cell if it will fit:
    def addData(self, coords, data):
        avail = self.getAvail(coords)
        used = self.getUsed(coords)
        if avail >= data:
            self.setAvail(coords, avail - data)
            self.setUsed(coords, used + data)
            return True
        else:
            return False

    # Subtract data from cell:
    def takeData(self, coords, data):
        # The math check is performed on addData, so no check here
        self.setAvail(coords, self.getAvail(coords) + data)
        self.setUsed(coords, self.getUsed(coords) - data)

    # Move some data out of cell 1 and into cell 2 (if possible):
    def moveData(self, coords1, coords2):
        data = min(self.getUsed(coords1), self.getAvail(coords2))
        if self.addData(coords2, data):
            self.takeData(coords1, data)

    # Print nicely:
    def printAvail(self, rows):
        for row in self.matrix[:rows]:
            for cell in row:
                print cell['avail'],
            print ' '

    def printUsed(self, rows):
        for row in self.matrix[:rows]:
            for cell in row:
                print cell['used'],
            print ' '

# Part 1:
avails = []
useds = []

# Process input:
n = Matrix(33,31,0)
with open('day22_input.txt') as fp:
    for line in fp:
        # Parse line to figure out data:
        if line.startswith("/dev/grid"):
            bits = line.split()
            xy = bits[0].split("-")
            x = int(xy[1][1:])
            y = int(xy[2][1:])
            size = int(bits[1][:-1])
            used = int(bits[2][:-1])
            avail = int(bits[3][:-1])
            useds.append(used)
            avails.append(avail)
            # Insert data:
            n.setNode((x,y), {'used': used, 'avail': avail})

# Count pairs with 1.avail >= 2.used:
avails.sort()
avails.reverse()    # desc
useds.sort()        # asc
print "Avails:", avails[:10]    # 1 cell with 88
print "Useds:", len([u for u in useds if u <= 88]), "under 88T (including itself)"

# Part 2, moving data:
print "---"
print "Avail:"
n.printAvail(29)
print "Used:"
n.printUsed(29)

# "Empty" cell is at (3,28)
count = 0
# 3 moves will get it to (0,28)
for x in range(3,0,-1):
    n.moveData((x-1,28), (x,28))
    print "EC @", (x-1,28), n.getUsed((x-1,28)), "used,", n.getAvail((x-1,28)), "free"
    count = count + 1

# 28 moves will get it to (0,0)
for y in range(28,0,-1):
    n.moveData((0,y-1), (0,y))
    print "EC @", (0,y-1), n.getUsed((0,y-1,)), "used,", n.getAvail((0,y-1)), "free"
    count = count + 1

# 31 moves will get it to (31,0)
for x in range(0,31):
    n.moveData((x+1,0), (x,0))
    print "EC @", (x+1,0), n.getUsed((x+1,0)), "used,", n.getAvail((x+1,0)), "free"
    count = count + 1

# 5 moves will get the empty cell and the goal cell one step left. Do this 31 times
for x in range(31,0,-1):
    # Move empty cell:
    n.moveData((x+1,0), (x,0))   # right, GD going other way
    n.moveData((x+1,1), (x+1,0)) # down
    n.moveData((x,1), (x+1,1))   # left
    n.moveData((x-1,1), (x,1))   # left
    n.moveData((x-1,0), (x-1,1)) # up
    print "EC @", (x-1,0) ,"GD @", (x,0)
    count = count + 5

# One more move puts the goal data at (0,0)
n.moveData((1,0), (0,0))
print "GD @", (0,0)
count = count + 1

print "---"
print "Avail:"
n.printAvail(2)
print "Used:"
n.printUsed(2)

print count, "moves made"
# 212 too low
# 216 incorrect
