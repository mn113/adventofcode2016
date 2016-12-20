#! /usr/bin/env python
# Find lowest not-blacklisted IP address

blacklist = []
white_count = 0

with open('day20_input.txt') as fp:
    lines = fp.readlines()
    for line in lines:
        parts = line.split("-")
        blacklist.append((int(parts[0]), int(parts[1])))    # Store as tuple

blacklist.sort()

# Find first blacklisted range which doesn't overlap with the next one:
i = 0
for item in range(len(blacklist) - 1):
    print i, blacklist[i],
    end_cand = blacklist[i][1]
    # Terminate if largest value encountered:
    if end_cand == 4294967295:
        print "I'M DONE."
        break

    # Find gaps and measure them:
    if end_cand >= blacklist[i+1][1]:
        print "skips next..."
        while end_cand >= blacklist[i+1][1]:
            # Advance until not fully skipped:
            i = i + 1
            print i, blacklist[i], "[skipped]"
        if end_cand + 1 < blacklist[i+1][0]:
            # Gap after skips
            gap = blacklist[i+1][0] - end_cand - 1
            print "SKIP+GAP! (", gap ,") to..."
            white_count = white_count + gap

    elif end_cand + 1 == blacklist[i+1][0]:
        print "matches..."
    elif end_cand + 1 < blacklist[i+1][0]:
        gap = blacklist[i+1][0] - blacklist[i][1] - 1
        print "GAP! (", gap ,") to..."
        white_count = white_count + gap
    else:
        print "overlaps..."
    i = i + 1

print white_count, "valid IPs"
