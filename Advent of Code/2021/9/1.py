with open('input.txt') as f:
    lines = f.readlines()

matrix = []
for line in lines:
    matrix.append([])
    for depth in line.strip():
        matrix[len(matrix) - 1].append(int(depth))


ans = 0
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
            ans += 1 + matrix[i][j]


print(ans)
