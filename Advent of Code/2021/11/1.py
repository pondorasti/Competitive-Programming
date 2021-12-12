from typing import Match


with open('input.txt') as f:
    lines = f.readlines()


matrix = []
for line in lines:
    matrix.append([])
    for octo in line.strip():
        matrix[-1].append(int(octo))


def printMatrix():
    for i in range(len(matrix)):
        line = ""
        for j in range(len(matrix[i])):
            line += str(matrix[i][j])
        print(line)
    print()


ans = 0
dx = [0, 1, 0, -1, 1, -1, 1, -1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]
for _ in range(100):
    visited = set()
    isDirty = True
    isFirstPass = True
    while isDirty:
        isDirty = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if isFirstPass:
                    matrix[i][j] += 1

                if matrix[i][j] > 9:
                    matrix[i][j] = 0
                    visited.add((i, j))
                    isDirty = True
                    for k in range(len(dx)):
                        x = i + dx[k]
                        y = j + dy[k]
                        if x in range(len(matrix)) and y in range(len(matrix[i])):
                            if (x, y) not in visited:
                                matrix[x][y] += 1
        isFirstPass = False
    ans += len(visited)

# printMatrix()
print(ans)
