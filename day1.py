# Sonar Sweep
# Part 1:
# Count the number of times a depth measurement increases from the previous measurement.
# How many measurements are larger than the previous measurement?

with open('inputDay1.txt', 'r') as f:
    lines = f.read().splitlines()

linesInt = [int(x) for x in lines]

i = 1
increased = 0
while i < len(linesInt):
    print(f'Current depth: {linesInt[i]}')
    print(f'Previous depth: {linesInt[i-1]}')
    if linesInt[i] > linesInt[i-1]:
        print('Increased')
        increased += 1
    i += 1

# print(increased)

# Part 2:
# Use a three-element tuple to represent the current position of the sonar.
# For example, consider the input (1, 2, 3, 4)..
# You will compare the sum of (1, 2, 3) to the sum of (2, 3, 4).
# Since the sum of (2, 3, 4) is bigger than the sum of (2, 3, 4), the measurement increased.
# How many measurements are larger than the previous measurement?

i = 0
newIncreased = 0

while i + 3 < len(linesInt):
    currentWindow: tuple = (linesInt[i], linesInt[i+1], linesInt[i+2])
    nextWindow: tuple = (linesInt[i+1], linesInt[i+2], linesInt[i+3])
    print(f'Current window: {currentWindow}')
    print(f'Next window: {nextWindow}')
    if sum(currentWindow) < sum(nextWindow):
        print('Increased')
        newIncreased += 1
    i += 1

print(newIncreased)