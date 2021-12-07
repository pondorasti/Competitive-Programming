with open('input.txt') as f:
    lines = f.readlines()

fishes = []
for interval in lines[0].split(","):
    fishes.append(int(interval))

for _ in range(0, 80):
    newFishes = 0
    for i in range(0, len(fishes)):
        fishes[i] -= 1

        if fishes[i] < 0:
            newFishes += 1
            fishes[i] = 6

    for _ in range(0, newFishes):
        fishes.append(8)

print(len(fishes))
