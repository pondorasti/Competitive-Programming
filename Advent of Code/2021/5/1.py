with open('input.txt') as f:
    lines = f.readlines()

diagram = dict()
for line in lines:
    start, end = line.strip().split(" -> ")
    startX, startY = start.split(",")
    endX, endY = end.split(",")
    startX, startY, endX, endY = int(startX), int(startY), int(endX), int(endY)

    if (startX == endX) or (startY == endY):
        if (startX == endX and startY > endY) or (startY == endY and startX > endX):
            startX, endX = endX, startX
            startY, endY = endY, startY

        for i in range(startX, endX + 1):
            for j in range(startY, endY + 1):
                if (i, j) in diagram:
                    diagram[(i, j)] += 1
                else:
                    diagram[(i, j)] = 1


ans = 0
for key, value in diagram.items():
    if value >= 2:
        ans += 1
print(ans)
