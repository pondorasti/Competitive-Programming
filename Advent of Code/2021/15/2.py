import math

with open('input.txt') as f:
    lines = f.readlines()


# Read input
cave = []
for line in lines:
    cave.append([])
    for risk in line.strip():
        cave[-1].append(int(risk))


# Create tiled cave
size = len(cave)
tileSize = 5
tiledCave = []
dp = []
for i in range(size * tileSize):
    tiledCave.append([])
    dp.append([])
    for j in range(size * tileSize):
        tiledCave[-1].append(0)
        dp[-1].append(math.inf)
for i in range(size):
    for j in range(size):
        tiledCave[i][j] = cave[i][j]


# Create tiles
prevCave = cave
for tile in range(2, tileSize * 2):
    newCave = []

    for i in range(size):
        newCave.append([])
        for j in range(size):
            newValue = prevCave[i][j] % 9 + 1
            newCave[-1].append(newValue)

    prevCave = newCave
    start = max(0, tile - tileSize)
    end = min(tile, tileSize)
    for rowTile in range(start, end):
        colTile = end - 1 - rowTile + start

        for i in range(size):
            for j in range(size):
                normalizedI = i + rowTile * size
                normalizedJ = j + colTile * size
                tiledCave[normalizedI][normalizedJ] = newCave[i][j]


def printCave(c):
    for i in range(len(c)):
        line = ""
        for j in range(len(c[i])):
            line += str(c[i][j])
        print(line)


# Find smallest risk path
dp[0][0] = 0
for i in range(size * tileSize):
    for j in range(size * tileSize):
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + tiledCave[i][j])
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + tiledCave[i][j])

print(dp[-1][-1])
printCave(tiledCave)
