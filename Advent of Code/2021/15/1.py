import math

with open('input.txt') as f:
    lines = f.readlines()

cave = []
dp = []
for line in lines:
    cave.append([])
    dp.append([])
    for risk in line.strip():
        cave[-1].append(int(risk))
        dp[-1].append(math.inf)

dp[0][0] = 0
for i in range(len(cave)):
    for j in range(len(cave)):
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + cave[i][j])
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + cave[i][j])

print(dp[-1][-1])
