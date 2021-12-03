# Dive!
# Part 1:
# The submarine can take a series of commands like forward, down or up.
# Up and down affect your depth, forward increases the horizontal position.
# Based on the inputs, calculate the horizontal and vertical position (depth) of the submarine.
# The final answer is the product of the horizontal and vertical position.

with open('inputDay2.txt', 'r') as f:
    instructions = f.read().splitlines()

instructionsList = [x.split(' ') for x in instructions]
instructionsParsed = [(x[0], int(x[1])) for x in instructionsList]

horizontalPosition = 0
depth = 0

for command in instructionsParsed:
    if command[0] == 'forward':
        horizontalPosition += command[1]
    elif command[0] == 'up':
        depth -= command[1]
    elif command[0] == 'down':
        depth += command[1]

print(horizontalPosition * depth)

# Part 2:
newHorizontalPos = 0
newDepth = 0
aim = 0

for command in instructionsParsed:
    if command[0] == 'up':
        aim -= command[1]
    elif command[0] == 'down':
        aim += command[1]
    elif command[0] == 'forward':
        newHorizontalPos += command[1]
        newDepth += aim * command[1]

print(newHorizontalPos * newDepth)
