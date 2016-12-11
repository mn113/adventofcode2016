#! /usr/bin/env python
# Decompress a text according to (AxB) markers

import re
# Regex for matching '(3x4)':
p = re.compile('\(([0-9]+)x([0-9]+)\)')


# Replace sequence with its repeated sequence:
def addRepeats(text, length, times):
    repeated = text[:length] * (times-1)
    return repeated + text


# Loop 1:
inputtext = 'ADVENTA(1x5)BC(3x3)XYZA(2x2)BCD(2x2)EFG(6x1)(1x3)AX(8x2)(3x3)ABCY'
#inputtext = open('day09_input.txt').readline()
pieces = []
while 1:
    # Regex search for next marker:
    m = p.search(inputtext)
    if m == None:
        # No more matches: remaining text must be counted
        pieces.append(len(inputtext))
        break
    # Count any characters preceding marker:
    pieces.append(m.start())
    # Analyse marker:
    print m.start(), ':', m.group(1), 'x', m.group(2)
    print inputtext[:m.end()]
    length = int(m.group(1))
    times = int(m.group(2))
    # Count repeated sequence length:
    pieces.append(length*times)
    # Cut marker itself off inputtext:
    inputtext = inputtext[m.end():]
    print inputtext
    # Transform post-marker string:
    inputtext = addRepeats(inputtext, length, times)
    # Chop off the repeated section, markers within it don't count:
    inputtext = inputtext[length*times:]
    print inputtext

print pieces
print sum(pieces)


# Loop 2:
inputtext = 'X(8x2)(3x3)ABCY'
pieces = []
multiplier = 1
while 1:
    # Regex search for next marker:
    m = p.search(inputtext)
    if m == None:
        # No more matches: remaining text must be counted
        pieces.append(len(inputtext))
        break
    # Count any characters preceding marker:
    pieces.append(m.start())
    # Analyse marker:
    print m.start(), ':', m.group(1), 'x', m.group(2), '(*', multiplier, ')'
    print inputtext[:m.end()]
    length = int(m.group(1))
    times = int(m.group(2))
    # Count repeated sequence length:
    pieces.append(length * times * multiplier)
    multiplier = multiplier * times
    # Cut marker itself off inputtext:
    inputtext = inputtext[m.end():]
    # Look ahead for absence of other markers:
    if p.search(inputtext[:length]) == None:
        # Only letters - reset:
        multiplier = 1

print pieces
print sum(pieces)
