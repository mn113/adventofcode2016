#! /usr/bin/env python
# Find bot which compares two chip numbers

bots = {str(el): {'chips': [], 'highdest': None, 'lowdest': None} for el in range(210)}       # bot keys should range from 1 to 210 or so...
outputs = {str(el): [] for el in range(21)}       # output keys are 0-20
instructions = []

with open('day10_input.txt') as fp:
    # First time through, just process input values:
    for line in fp:
        if line[:5] == "value":        # Starting value
            words = line.split()
            value = int(words[1])
            botno = words[-1]
            # Assign value to a bot:
            bots[botno]['chips'].append(value)

        elif line[:3] == "bot":     # Instruction
            instructions.append(line)

for botno, data in bots.items():
    if len(data['chips']) > 0:
        print "bot", botno, bots[botno]


# Next, process distribution instructions:
for line in instructions:
    words = line.split()
    botno = words[1]
    # Store distribution info in bots object:
    bots[botno]['lowdest'] = (words[5], words[6])      # First part can be bot or output
    bots[botno]['highdest'] = (words[-2], words[-1])

for botno, data in bots.items():
    if data['highdest'] or data['lowdest']:
        print "bot", botno, bots[botno]


# Assign a value to a bot or output bin:
def give(value, dest):
    if dest[0] == "bot":
        bots[dest[1]]['chips'].append(value)
    elif dest[0] == "output":
        outputs[dest[1]].append(value)
    # Track specific chips:
    if value in [17,61]:
        print "chip", value, "went to", dest
        if dest in ancestors:
            print "^^^"
        ancestors.append(dest)


def howManyBotsHaveChips():
    count = 0
    for botno, data in bots.items():
        if len(data['chips']) > 0:
            count = count + 1
    return count


# Make the bots do their distribution:
rounds = 0
ancestors = []
while 1:
    for botno, data in bots.items():
        if len(data['chips']) == 2 and data['highdest'] and data['lowdest']:
            give(max(data['chips']), data['highdest'])
            give(min(data['chips']), data['lowdest'])
            bots[botno]['chips'] = [] # Empty bot's bin
    rounds = rounds + 1
    print ">", rounds, "rounds done."
    withchips = howManyBotsHaveChips()
    print ">", withchips, "bots have chips."
    # End condition:
    if withchips == 0 or rounds == 100:
        break

#print "-----"
#print bots  # empty?
print "-----"
print outputs
