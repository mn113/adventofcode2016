#! /usr/bin/env python
# Find a password by using md5 hash of doorid + incrementor

import hashlib

doorid = "ugkcyxxp"
password = [None] * 8
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
    try:
        if int(h[5]) in range(8):
            idx = int(h[5])
            if password[idx] is None:
                #print "FOUND", h, incr
                password[idx] = h[6]
                print password, incr
    except ValueError:
        pass

# Start solving:
while password.count(None) > 0:
    findNextCharacter()

print ''.join(password), "is the password"
