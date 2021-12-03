with open('input.txt') as f:
    lines = f.readlines()

inf = "88888888888888888888888"
currentBit = 0
removedElements = 0
while len(lines) - 1 > removedElements:
    ones = 0
    zeros = 0
    for line in lines:
        if line[currentBit] == "0":
            zeros += 1
        elif line[currentBit] == "1":
            ones += 1

    # oxygenGeneratorRating: "0" if ones >= zeros else "1"
    # co2ScrubberRating: "1" if ones >= zeros else "0"
    bitToRemove = "1" if ones >= zeros else "0"
    for i in range(0, len(lines)):
        if lines[i][currentBit] == bitToRemove:
            lines[i] = inf
            removedElements += 1

    currentBit += 1

for line in lines:
    if line != inf:
        print(line)
        break

# oxygenGeneratorRating: 111101100011
# co2ScrubberRating: 011011100010
print(int("111101100011", 2) * int("011011100010", 2))
