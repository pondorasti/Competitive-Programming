with open('input.txt') as f:
    lines = f.readlines()


depths = []
for line in lines:
    depths.append(int(line))

ans = 0
prev = None


for i in range(3, len(depths)):
    if depths[i - 3] + depths[i - 2] + depths[i - 1] < depths[i - 2] + depths[i - 1] + depths[i]:
        ans += 1

print(ans)
