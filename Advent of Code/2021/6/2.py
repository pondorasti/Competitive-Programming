with open('input.txt') as f:
    lines = f.readlines()

fishes = {}
for i in range(0, 10):
    fishes[i] = 0

for interval in lines[0].split(","):
    fishes[int(interval)] += 1


for _ in range(0, 256):
    for i in range(0, 10):
        if i == 0:
            fishes[7] += fishes[i]
            fishes[9] += fishes[i]
        else:
            fishes[i - 1] += fishes[i]

        fishes[i] = 0

ans = 0
for i in range(0, 9):
    ans += fishes[i]
print(ans)
