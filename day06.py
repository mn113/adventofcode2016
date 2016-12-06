#! /usr/bin/env python
# Count most frequent letters in each string position

columns = {}    # Dict of arrays. Keys = 0-7

# Sort rows into columns:
with open('day06_input.txt') as fp:
    for row in fp:
        for col in range(len(row) - 1):     # chop newlines
            letter = row[col]
            # First character:
            if col not in columns.keys():
                columns[col] = [letter]
            # Subsequent:
            else:
                columns[col].append(letter)

# Count occurrences of each letter in an array and store total:
for key, col in columns.items():
    frequencies = {}
    # Operate on a set, no dupes:
    for letter in list(set(col)):
        frequencies[letter] = col.count(letter)

    # Result for this column now known:
    print min(frequencies, key=frequencies.__getitem__),

print "Done."
