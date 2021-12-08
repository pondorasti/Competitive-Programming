import math

with open('input.txt') as f:
    lines = f.readlines()

crabs = []
for interval in lines[0].split(","):
    crabs.append(int(interval))

minVal = min(crabs)
maxVal = max(crabs) + 1
crabFreq = [0 for _ in range(maxVal)]

for crab in crabs:
    crabFreq[crab] += 1


partialSums = [(0, 0) for _ in range(maxVal)]
reversedPartialSums = [(0, 0) for _ in range(maxVal + 1)]

partialSums[0] = (crabFreq[0], 0)
for i in range(minVal, maxVal):
    prevCrab, prevFuel = partialSums[i - 1]
    crabCount = prevCrab + crabFreq[i]
    for j in range(i, maxVal):
        partialSums[j] = (
            crabCount,
            partialSums[j][1] + crabFreq[i] * (j - i)
        )
for i in range(minVal + 1, maxVal):
    prevCrab, prevFuel = partialSums[i - 1]
    curCrab, curFuel = partialSums[i]
    partialSums[i] = (curCrab, prevFuel + curFuel)

reversedPartialSums[maxVal - 1] = (crabFreq[maxVal - 1], 0)
for i in reversed(range(minVal, maxVal)):
    prevCrab, prevFuel = reversedPartialSums[i + 1]
    crabCount = prevCrab + crabFreq[i]
    for j in reversed(range(minVal, i)):
        reversedPartialSums[j] = (
            crabCount,
            reversedPartialSums[j][1] + crabFreq[i] * (i - j)
        )

for i in reversed(range(minVal, maxVal - 1)):
    prevCrab, prevFuel = reversedPartialSums[i + 1]
    curCrab, curFuel = reversedPartialSums[i]
    reversedPartialSums[i] = (curCrab, prevFuel + curFuel)

ans = math.inf
for i in range(minVal, maxVal):
    ans = min(ans, partialSums[i][1] + reversedPartialSums[i][1])
print(ans)
