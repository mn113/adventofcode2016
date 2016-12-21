#! /usr/bin/env python
# Scramble a password using many instructions

import sys

class ScrambleText:
    """ A string, with scrambling operations """

    def __init__(self, text):
        self.text = text

    # Swap two characters by their index:
    def swapPos(self, x, y):
        charx = self.text[x]
        chary = self.text[y]
        # List conversion for positional assignment:
        l = list(self.text)
        l[x] = chary
        l[y] = charx
        self.text = ''.join(l)
        return self

    # Swap two letters by value (all instances):
    def swapLetter(self, x, y):
        t = self.text
        t = t.replace(x, '_')   # NOT WORKING
        t = t.replace(y, x)
        t = t.replace('_', y)
        self.text = t
        return self

    # Rotate the string a given number of steps:
    def rotate(self, steps, left):
        # Handle moving right by negative steps left:
        if not left:
            steps = len(self.text) - steps
        # Rotate by slicing:
        self.text = self.text[steps:] + self.text[:steps]
        return self

    # Reverse a subsection of the string in place:
    def reverse(self, start, end):
        substring = self.text[start:end+1]
        # List conversion for reversal:
        l = list(substring)
        l.reverse()
        substring = ''.join(l)
        self.text = self.text[:start] + substring + self.text[end+1:]
        return self

    # Move a character to a new index:
    def movePos(self, x, y):
        charx = self.text[x]
        self.text = self.text[:x] + self.text[x+1:]         # Removal
        self.text = self.text[:y] + charx + self.text[y:] # Re-insertion
        return self

    def printMe(self):
        print self.text
        return self


def encode(password):
    # Make new password object:
    p = ScrambleText(password)
    # Process scrambling instructions:
    with open('day21_input.txt') as fp:
        lines = fp.readlines()
        for line in lines:
            words = line.split()
            #print words,
            if line[:13] == "swap position":
                p.swapPos(int(words[2]), int(words[5]))

            elif line[:11] == "swap letter":
                p.swapLetter(words[2], words[5])

            elif line[:12] == "rotate right":
                p.rotate(int(words[2]), False)

            elif line[:11] == "rotate left":
                p.rotate(int(words[2]), True)

            elif line[:12] == "rotate based":
                letterpos = p.text.index(words[-1])
                p.rotate(letterpos+1, False)
                # Stupid extra condition:
                if letterpos >= 4:
                    p.rotate(1, False)

            elif line[:7] == "reverse":
                p.reverse(int(words[2]), int(words[4]))

            elif line[:13] == "move position":
                p.movePos(int(words[2]), int(words[5]))
            #print password.text
    return p.text


# Part 1:
print "Part 1:", encode("abcdefgh")

# Part 2:
# Brute force by testing all permutations of 8 letters:
l1 = list('abcdefgh')
for c1 in l1:
    l2 = l1[:]
    l2.remove(c1)
    for c2 in l2: # len = 7
        l3 = l2[:]
        l3.remove(c2)
        for c3 in l3: # len = 6
            l4 = l3[:]
            l4.remove(c3)
            for c4 in l4: # len = 5
                l5 = l4[:]
                l5.remove(c4)
                for c5 in l5: # len = 4
                    l6 = l5[:]
                    l6.remove(c5)
                    for c6 in l6: # len = 3
                        l7 = l6[:]
                        l7.remove(c6)
                        for c7 in l7: # len = 2
                            l8 = l7[:]
                            l8.remove(c7)
                            c8 = l8[0]
                            # We should get 40,320 candidate strings
                            candidate = ''.join([c1,c2,c3,c4,c5,c6,c7,c8])
                            encoded = encode(candidate)
                            print "C:", candidate, "E:", encoded
                            if encoded == "fbgdceah":
                                # Part 2 password found
                                sys.exit("FOUND")
