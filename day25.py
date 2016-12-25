#! /usr/bin/env python
# Find input which generates 01010101... output

def runInstructions():
    global registers
    output = []
    correct8 = [[0,1,0,1,0,1,0,1,0,1,0,1], [1,0,1,0,1,0,1,0,1,0,1,0]]
    with open('day25_input.txt') as fp:
        lines = fp.readlines()
        l = len(lines)
        i = 0
        while i < l:
            line = lines[i]
            words = line.split()

            if words[0] == 'out':
                output.append(registers[words[1]])
                if len(output) >= 12:
                    print output
                    if output[:12] in correct8:
                        return True
                    else:
                        return False

            if words[0] == 'inc':
                reg = words[1]
                registers[reg] = registers[reg] + 1

            elif words[0] == 'dec':
                reg = words[1]
                registers[reg] = registers[reg] - 1

            elif words[0] == 'cpy':
                src = words[1]
                dest = words[2]
                # Copy register?
                if src in 'abcd':
                    #print src, registers[src]
                    registers[dest] = registers[src]
                # Copy integer?
                else:
                    registers[dest] = int(src)

            elif words[0] == 'jnz':
                to_test = words[1]
                skip = int(words[2])

                # Test:
                #print to_test
                if (to_test in 'abcd' and registers[to_test] != 0):   # Non-zero register
                    i = i + skip
                    continue    # start next loop immediately
                else:
                    try:
                        if int(to_test) != 0:   # Non-zero integer
                            i = i + skip
                            continue    # start next loop immediately
                    except ValueError:
                        pass

            elif words[0] == 'ADD':
                registers[words[2]] = registers[words[2]] + registers[words[1]]

            elif words[0] == 'ZER':
                registers[words[1]] = 0

            i = i + 1

registers = {x:0 for x in 'abcd'}

for q in range(1000):
    registers['a'] = q
    print "--- a =", q, "---"
    if runInstructions() == True:
        break
