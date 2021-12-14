with open('input.txt') as f:
    lines = f.readlines()

# Variables
paper = [[]]
instructions = []

paperCoordinates = []
maxX = 0
maxY = 0

# Print Paper Helper


def printPaper():
    for x in range(maxX):
        line = ""
        for y in range(maxY):
            line += str(paper[x][y])
        print(line)


# Parse Input
readingPaper = True
for line in lines:
    if line == "\n":
        readingPaper = False
        continue

    if readingPaper:
        y, x = line.strip().split(",")

        x = int(x)
        y = int(y)

        maxX = max(maxX, x)
        maxY = max(maxY, y)

        paperCoordinates.append((x, y))
    else:
        direction, value = line.strip().split(" ")[2].split("=")
        instructions.append((direction, int(value)))

# Create Map
maxX += 1
maxY += 1
while maxX > len(paper):
    paper.append([])
for x in range(len(paper)):
    while maxY > len(paper[x]):
        paper[x].append(".")
for coordinate in paperCoordinates:
    x, y = coordinate
    paper[x][y] = "#"

# Fold Instructions
for instruction in instructions:
    direction, value = instruction
    startX = 0
    startY = 0
    if direction == "y":
        startX = value + 1
    else:
        startY = value + 1
    for x in range(startX, len(paper)):
        for y in range(startY, len(paper[x])):
            if paper[x][y] == "#":
                newX = x
                newY = y

                if direction == "y":
                    newX = (startX - 2) - (x - startX)
                else:
                    newY = (startY - 2) - (y - startY)

                paper[newX][newY] = "#"

    # Update size
    if direction == "y":
        maxX = startX - 1
    else:
        maxY = startY - 1

printPaper()
