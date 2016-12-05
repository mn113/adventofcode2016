#! /usr/bin/env python
# Find a password by using md5 hash of doorid + incrementor

import hashlib

doorid = "ugkcyxxp"
password = []
incr = 0

def findNextCharacter():
    global incr

    h = ''
    # Keep incrementing and md5'ing until five zeroes begin the result:
    while h[:5] != "00000":
        # Generate md5 hash:
        h = hashlib.md5(doorid + str(incr)).hexdigest()
        #print incr, h
        incr = incr + 1

    # Store result:
    if h[5]:
        print "FOUND", h, incr
        password.append(h[5])

# Start solving:
while len(password) < 8:
    findNextCharacter()

print ''.join(password), "is the password"
