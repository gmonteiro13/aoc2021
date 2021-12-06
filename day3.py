# Binary Diagnostic
# Part 1:
# You need to use the binary numbers in the diagnostic report to generate two new binary numbers..
# called the gamma rate and the epsilon rate. The power consumption can then be found by...
# multiplying the gamma rate by the epsilon rate.
# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding...
# position  of all numbers in the diagnostic report.

from collections import Counter
from types import new_class

with open('inputDay3.txt', 'r') as f:
    binaryNumbers = f.read().splitlines()

binaryBitList = []
binaryTotalList = []
gammaRateList = []
epsilonRateList = []
i = 0

def getBit(n, position):
    return n[position]

def iterateThruBinaryList(i):
    for binaryNumber in binaryNumbers:
        binaryBitList.append(getBit(binaryNumber, i))
    return binaryBitList

while i < len(binaryNumbers[i]):
    binaryBitList = [iterateThruBinaryList(i)]
    # print(f'Printing the {i} binary list: \t {binaryBitList}')
    binaryTotalList.extend(binaryBitList)
    # print(f'Printing the {i} binary total list: \t {binaryTotalList[i]}')
    binaryBitList.clear()
    i += 1

def getMostCommonBit(binaryList):
    return Counter(binaryList).most_common(1)[0][0]

for binaryList in binaryTotalList:
    mostCommonBit = int(getMostCommonBit(binaryList))
    gammaRateList.append(mostCommonBit)
    if mostCommonBit == 1:
        epsilonRateList.append(0)
    else:
        epsilonRateList.append(1)

gammaRate = int(''.join(str(bit) for bit in gammaRateList), 2)
epsilonRate = int(''.join(str(bit) for bit in epsilonRateList), 2)
# print(f'The gamma rate list is: {gammaRateList}')
# print(f'The epsilon rate list is: {epsilonRateList}')
# print(f'Gamma Rate is: {gammaRate}')
# print(f'Epsilon Rate is: {epsilonRate}')
# print(f'Power Consumption is: {gammaRate * epsilonRate}')

# Part 2:
# Next, we should verify the life support rating, which can be determined by..
# multiplying the oxygen generator rating (OGR) by the CO2 scrubber rating (CSR).
# To find the OGR, we need to determine the most common value in the current bit position...
# and keep only numbers with that bit in that position. If there is a tie, the OGR is 1.
# To find the CSR, we need to determine the least common value in the current bit position...
# and keep only numbers with that bit in that position. If there is a tie, the CSR is 0.

OGRList = binaryNumbers
CSRList = binaryNumbers
i = 0

while i < 12:
    print('Im in the loop')
    mostCommonBit = int(getMostCommonBit(binaryTotalList[i]))
    for list in OGRList[:]:
        if mostCommonBit != int(list[i]):
            OGRList.remove(list)
    print('out of the loop')
    print(f'The OGRList is: {OGRList}')
    i += 1

print(OGRList)
