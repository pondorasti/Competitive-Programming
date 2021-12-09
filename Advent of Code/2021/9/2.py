with open('input.txt') as f:
    lines = f.readlines()

matrix = []
visited = []
for line in lines:
    matrix.append([])
    visited.append([])
    for depth in line.strip():
        matrix[len(matrix) - 1].append(int(depth))
        visited[len(visited) - 1].append(False)


lowPoints = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        isLow = True
        for k in range(0, len(dx)):
            x = i + dx[k]
            y = j + dy[k]

            if x in range(0, len(matrix)) and y in range(0, len(matrix[i])):
                if matrix[i][j] >= matrix[x][y]:
                    isLow = False
                    break

        if isLow:
            lowPoints.append((i, j))
            visited[i][j] = True

basinSizes = []
for point in lowPoints:
    queue = [point]
    size = 1

    while len(queue) != 0:
        i, j = queue.pop()
        for k in range(0, len(dx)):
            x = i + dx[k]
            y = j + dy[k]

            if x in range(0, len(matrix)) and y in range(0, len(matrix[i])):
                if not visited[x][y] and matrix[i][j] < matrix[x][y] and matrix[x][y] != 9:
                    queue.insert(0, (x, y))
                    visited[x][y] = True
                    size += 1

    basinSizes.append(size)

basinSizes.sort()
basinSizes.reverse()

ans = 1
for i in range(0, 3):
    ans *= basinSizes[i]
print(ans)

for i in range(0, len(matrix)):
    line = ""
    for j in range(0, len(matrix[i])):
        line += "1" if visited[i][j] else "0"
    # print(line)
