with open('input.txt') as f:
    lines = f.readlines()

ans = 0
for line in lines:
    input, output = line.split(" | ")

    for word in output.split():
        length = len(word)
        if length == 2 or length == 4 or length == 3 or length == 7:
            ans += 1

print(ans)
