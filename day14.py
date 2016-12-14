#! /usr/bin/env python
# Generate hashes and test for presence of strings

import hashlib

#salt = "yjdafjpo"
salt = "yjdafjpo"
incr = 0
limit = 28000
hashes = []
candidates = [] # list of tuples (i,c,h)
validkeys = []
part = 2

# Key stretching: perform md5 hash multiple times:
def multihash(times, startval):
    h = startval
    for i in range(times):
        h = hashlib.md5(h).hexdigest()
    return h

# Keep incrementing and md5'ing until a triple is found:
while incr < limit:
    # Generate md5 hash:
    if part == 1:
        h = hashlib.md5(salt + str(incr)).hexdigest()
    else:
        h = multihash(2017, salt + str(incr))
    hashes.append(h)

    # Check for triples on this hash:
    for j in range(len(h)-2):
        if h[j] == h[j+1] and h[j] == h[j+2]:
            # Store index, letter value and hash of the triple:
            candidates.append((incr, h[j], h))
            break

    incr = incr + 1

print len(candidates), "candidates found up to", limit
print [c for c in candidates if c[0] < 100]

# Process candidates:
for cand in candidates:
    # Check next 1000 hashes:
    pos = cand[0]
    letter = cand[1]
    upper = pos + 1000
    if upper > limit:
        break
    while pos < upper:
        pos = pos + 1
        h = hashes[pos]

        # Test for triple-matching quintuples on this hash:
        for j in range(len(h)-4):
            if h[j:j+5] == letter*5:
                # Store candidate as valid key:
                print cand[0], cand[1], cand[2], pos, h
                validkeys.append(cand)
                break


print len(validkeys), "valid keys up to", limit
print [v[0] for v in validkeys]
