#! /usr/bin/env python
# Add dummy data to a binary string, and checksum it

inputstr = '10010000000110000'
disklength = 35651584

def dragonise(n):
    n_flipped = [str((int(char) + 1) % 2) for char in n]
    n_flipped.reverse()
    return n + '0' + ''.join(n_flipped)

def checksum(n):
    chk = []
    # Assess n pairwise:
    for i in range(0,len(n),2):
        if n[i] == n[i+1]:
            chk.append('1')
        else:
            chk.append('0')
    # Checksum is a string of 0/1s:
    return ''.join(chk)

# Expand the input string until it fills the disk:
while len(inputstr) < disklength:
    inputstr = dragonise(inputstr)

# Chop it down:
inputstr = inputstr[:disklength]

# Checksum until odd length:
chk = checksum(inputstr)
while len(chk) % 2 != 1:
    chk = checksum(chk)

print "Checksum:", chk
