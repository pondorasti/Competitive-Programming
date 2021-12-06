with open('input.txt') as f:
    lines = f.readlines()

diagram = dict()


def update(key):
    if key in diagram:
        diagram[key] += 1
    else:
        diagram[key] = 1


for line in lines:
    start, end = line.strip().split(" -> ")
    startX, startY = start.split(",")
    endX, endY = end.split(",")
    startX, startY, endX, endY = int(startX), int(startY), int(endX), int(endY)

    if (startX == endX and startY > endY) or (startY == endY and startX > endX):
        startX, endX = endX, startX
        startY, endY = endY, startY

    if startX == endX or startY == endY:
        for i in range(startX, endX + 1):
            for j in range(startY, endY + 1):
                update((i, j))

    if abs(startX - endX) == abs(startY - endY):
        for i in range(0, abs(endX - startX) + 1):
            x = startX + i if startX < endX else startX - i
            y = startY + i if startY < endY else startY - i
            update((x, y))


ans = 0
for key, value in diagram.items():
    if value >= 2:
        ans += 1
print(ans)
