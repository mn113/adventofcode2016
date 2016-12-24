#! /usr/bin/env python
# Find result of long-running instruction set

import sys
import time

def intOrRegisterValue(x):
    if x in 'abcd':
        return registers[x]
    else:
        return int(x)


registers = {x:0 for x in 'abcd'}
registers['a'] = 7  # Part 1
registers['a'] = 12  # Part 2
print "Start:" + str(registers)


with open('day23_input.txt') as fp:
    lines = fp.readlines()
    l = len(lines)
    i = 0
    while i < l:
        line = lines[i]
        sys.stdout.write(str(registers) + ' : ' + str(i) + ' : ' + line)
        sys.stdout.write('\r')
        sys.stdout.flush()
        #print registers
        #print i, '/', l, ':', line
        words = line.split()

        if words[0] == 'tgl':
            toggleDist = intOrRegisterValue(words[1])
            # Convert to integer:
            j = i + toggleDist

            if j < 0 or j >= l:
                # Out of range, start next loop immediately
                i = i + 1
                continue

            elif lines[j][:3] == 'inc': # Toggle inc to dec
                lines[j] = 'dec' + lines[j][3:]

            elif lines[j][:3] == 'dec': # Toggle dec to inc
                lines[j] = 'inc' + lines[j][3:]

            elif lines[j][:3] == 'tgl': # Toggle tgl to inc
                lines[j] = 'inc' + lines[j][3:]

            elif lines[j][:3] == 'jnz': # Toggle jnz to cpy
                lines[j] = 'cpy' + lines[j][3:]

            else:
                # cpy doesn't change when toggled
                pass
            print "Altered", j, lines[j]


        elif words[0] == 'inc':
            reg = words[1]
            registers[reg] = registers[reg] + 1

        elif words[0] == 'dec':
            reg = words[1]
            registers[reg] = registers[reg] - 1

        elif words[0] == 'cpy':
            src = words[1]
            dest = words[2]
            # Copy register?
            registers[dest] = intOrRegisterValue(src)

        elif words[0] == 'jnz':
            # Test:
            to_test = intOrRegisterValue(words[1])
            jumpval = intOrRegisterValue(words[2])

            if to_test != 0:
                i = i + jumpval
                continue    # start next loop immediately

        elif words[0] == 'ADD':
            times = 1
            if len(words) > 3:
                times = intOrRegisterValue(words[3])
            registers[words[2]] = registers[words[2]] + times * registers[words[1]]

        elif words[0] == 'ZER':
            registers[words[1]] = 0

        i = i + 1
        time.sleep(0.0)

print "---"
print registers
