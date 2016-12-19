#! /usr/bin/env python
# Find number of "trap" squares in a room grid

# ^ = trap
# L 1 2 3 4 ... n R

# L . ^ => trap
# L ^ ^ => trap
# ^ ^ . => trap
# . ^ ^ => trap
# . . ^ => trap
# ^ . . => trap
# ^ ^ R => trap
# ^ . R => trap

def isTrap(left, centre, right):
    lcr = left + centre + right
    if lcr in ['^^.','.^^','..^','^..']:
        return True
    return False

def calcNextLine(line):
    nextLine = ''
    # Process characters:
    for i in range(len(line)):
        centre = line[i]
        # Edge cases:
        if i == 0:
            left = '.'
            right = line[i+1]
        elif i == len(line) - 1:
            left = line[i-1]
            right = '.'
        else:
            left = line[i-1]
            right = line[i+1]

        # Build the next line:
        if isTrap(left, centre, right):
            square = '^'
        else:
            square = '.'
        nextLine = nextLine + square

    return nextLine


firstLine = '......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..'
room = []
room.append(firstLine)
rowNo = 0
safeTotal = firstLine.count('.')

# Generate trap map:
while rowNo < 399999:
    nextLine = calcNextLine(room[rowNo])
    room.append(nextLine)
    # Count non-traps:
    safeTotal = safeTotal + nextLine.count('.')
    rowNo = rowNo + 1

print len(room), "lines generated"
print safeTotal, "safe squares"         # 20009519 too low
