with open('input.txt') as f:
    lines = f.readlines()

ans = 0
prev = None
for line in lines:
    if prev and prev < int(line):
        ans += 1

    prev = int(line)

print(ans)
