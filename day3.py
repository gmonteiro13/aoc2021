# Binary Diagnostic
# Part 1:
# You need to use the binary numbers in the diagnostic report to generate two new binary numbers..
# called the gamma rate and the epsilon rate. The power consumption can then be found by...
# multiplying the gamma rate by the epsilon rate.
# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding...
# position  of all numbers in the diagnostic report.

from collections import Counter

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

# gammaRate = int(''.join(str(bit) for bit in gammaRateList), 2)
# epsilonRate = int(''.join(str(bit) for bit in epsilonRateList), 2)
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
OGRBitList = []
CSRBitList = []
OGRTotalList = []
CSRTotalList = []
CSRList = binaryNumbers
i = 0
def iterateThruOGRBinaryList(i):
    for OGRNumber in OGRList:
        OGRBitList.append(getBit(OGRNumber, i))
    return OGRBitList

def iterateThruCSRBinaryList(i):
    for CSRNumber in CSRList:
        CSRBitList.append(getBit(CSRNumber, i))
    return CSRBitList
# def constructOGRBinaryTotalList(OGRList):
#     i = 0
#     while i < len(OGRList[i]):
#         OGRBitList = [iterateThruOGRBinaryList(i)]
#         allOGRBitList.extend(OGRBitList)
#         OGRBitList.clear()
#         i += 1
#     return allOGRBitList

while (len(OGRList) > 0):
    j = 0
    print(OGRList)
    while j < len(OGRList[j]):
        for OGRNumber in OGRList:
            OGRBitList.append(getBit(OGRNumber, j))
        # print(f'Printing the {i} OGR list: \t {OGRBitList}')
        OGRTotalList.extend(OGRBitList)
        # print(f'Printing the {i} OGR total list: \t {OGRTotalList[i]}')
        OGRBitList.clear()
        j += 1
        if j >= len(OGRList):
            break
    mostCommonBit = getMostCommonBit(OGRTotalList[i])
    OGRTotalList.clear
    print(dict(Counter(OGRTotalList[i])))
    OGRListCopy = [x for x in OGRList if x[i] == mostCommonBit]
    OGRList = OGRListCopy
    if len(OGRListCopy) == 1:
        break
    i += 1

i = 0

while (len(CSRList) > 0):
    j = 0
    print(CSRList)
    while j < len(CSRList[j]):
        for CSRNumber in CSRList:
            CSRBitList.append(getBit(CSRNumber, i))
        # print(f'Printing the {i} OGR list: \t {OGRBitList}')
        CSRTotalList.extend(CSRBitList)
        # print(f'Printing the {i} OGR total list: \t {OGRTotalList[i]}')
        CSRBitList.clear()
        j += 1
        if j >= len(CSRList):
            break
    mostCommonBit = getMostCommonBit(CSRTotalList[i])
    CSRTotalList.clear
    print(dict(Counter(CSRTotalList[i])))
    CSRListCopy = [x for x in CSRList if x[i] != mostCommonBit]
    CSRList = CSRListCopy
    if len(CSRListCopy) == 1:
        break
    i += 1

print(OGRList)
print(CSRList)
csr = int(''.join(str(bit) for bit in CSRList), 2)
ogr = int(''.join(str(bit) for bit in OGRList), 2)
print(f'The CSR list is: {CSRList}')
print(f'The ogr list is: {OGRList}')
print(f'CSR is: {csr}')
print(f'ogr is: {ogr}')
print(f'Life support rating is: {csr * ogr}')