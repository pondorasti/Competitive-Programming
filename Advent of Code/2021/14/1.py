import math

with open('input.txt') as f:
    lines = f.readlines()

template = ""
rules = []
readingRules = False

for line in lines:
    if line == "\n":
        readingRules = True
    elif not readingRules:
        template = line.strip()
    else:
        pattern, insertion = line.strip().split(" -> ")
        rules.append((pattern, insertion))

for _ in range(10):
    newTemplate = template
    offset = 0
    for i in range(2, len(template) + 1):
        currentPattern = template[(i - 2):i]
        for pattern, insertion in rules:
            if pattern == currentPattern:
                spliceIndex = i - 1 + offset
                newTemplate = newTemplate[:spliceIndex] + \
                    insertion + newTemplate[spliceIndex:]
                offset += 1
                break

    template = newTemplate

freq = {}
for element in template:
    if element in freq:
        freq[element] += 1
    else:
        freq[element] = 1

minEl = math.inf
maxEl = 0
for value in freq.values():
    minEl = min(minEl, value)
    maxEl = max(maxEl, value)

print(maxEl - minEl)
