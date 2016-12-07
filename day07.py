#! /usr/bin/env python
# Detect ABBA-type sequences within strings

have_valid_abba = []

with open('day07_input.txt') as fp:
    for line in fp:
        validLine = False
        for i in range(len(line) - 3):

            # Assume all square brackets match each other:
            if line[i] == '[':
                bracketed = True
            elif line[i] == ']':
                bracketed = False

            # Not a bracket, so test ahead for an ABBA:
            elif line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[i+1]:
                # Good ABBA or bad ABBA?
                if not bracketed:
                    # Provisonally accept line:
                    validLine = True
                else:
                    # Reject line and stop inspecting:
                    validLine = False
                    break
        if validLine:
            have_valid_abba.append(line)

print have_valid_abba
print len(have_valid_abba)


# PART 2: ABA & BAB

have_valid_ababab = []

with open('day07_input.txt') as fp:
    for line in fp:
        ABAsequences = []
        BABsequences = []
        validLine = False
        bracketed = False
        for i in range(len(line) - 2):

            # Assume all square brackets match each other:
            if line[i] == '[':
                bracketed = True
            elif line[i] == ']':
                bracketed = False

            # Test ahead for an ABA (or BAB):
            elif line[i] == line[i+2] and line[i] != line[i+1]:
                # Remember sequence and bracket status:
                if not bracketed:
                    ABAsequences.append(line[i:i+2])
                else:
                    BABsequences.append(line[i:i+2])

            # For each ABA, check for a matching BAB:
            for x in ABAsequences:
                for y in BABsequences:
                    if x[0] == y[1] and y[0] == x[1]:
                        # We found our match
                        validLine = True
                        break

        if validLine:
            have_valid_ababab.append(line)

print have_valid_ababab
print len(have_valid_ababab)
