with open('input.txt') as f:
    lines = f.readlines()

gamma = ""
epsilion = ""
for digit in range(0, 12):
    ones = 0
    zeros = 0
    for line in lines:
        if line[digit] == "0":
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        gamma += "0"
        epsilion += "1"
    else:
        gamma += "1"
        epsilion += "0"

ans = int(gamma, 2) * int(epsilion, 2)
print(ans)
