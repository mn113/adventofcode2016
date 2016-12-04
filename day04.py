#! /usr/bin/env python
# Check a checksum of most common letters in a string

def splitup(string):
    # Split up input:
    bracket1 = string.index("[")
    bracket2 = string.index("]")
    mainpart = string[:bracket1]
    checksum = string[bracket1 + 1:bracket2]
    sector = int(mainpart.split("-")[-1])
    return (mainpart, checksum, sector)


def validateString(string):
    spl = splitup(string)
    mainpart = spl[0]
    checksum = spl[1]
    sector = spl[2]
    #print mainpart
    #print checksum
    #print sector

    # Count letter occurrences:
    counts = {}
    for char in set(mainpart):
        if char.isalpha():
            counts[char] = mainpart.count(char)
    #print counts

    # Make checksum:
    # Double sort: alphabetical, then by count (descending):
    ranking = sorted(sorted(counts), key=counts.__getitem__, reverse=True)
    # Take the first 5:
    calcsum = ''.join(ranking)
    calcsum = calcsum[0:5]
    #print calcsum

    # Did it validate?
    if calcsum == checksum:
        return sector
    else:
        return False


# Shift cipher decoding:
def rot_x(string, x):
    decoded = []
    for c in string:
        if c.isalpha():
            decoded.append(chr(97 + ((ord(c) - 97 + x) % 26)))
        elif c == "-":
            decoded.append(" ")

    return ''.join(decoded)


# Count all valid input strings:
valid = 0
total = 0
sectorsum = 0
with open('day04_input.txt') as fp:
    for line in fp:
        total = total + 1
        #print "---"
        sector = validateString(line)
        if sector:
            valid = valid + 1
            sectorsum = sectorsum + sector

            # Decrypt strings:
            plaintext = rot_x(splitup(line)[0], sector)
            if plaintext.find("north") > -1:
                print plaintext, sector


print valid, "of", total, "strings were valid"
print sectorsum
