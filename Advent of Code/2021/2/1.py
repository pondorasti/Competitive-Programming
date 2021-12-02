with open('input.txt') as f:
    lines = f.readlines()

horizontal = 0
depth = 0
for line in lines:
    command = line.split(" ")[0]
    amount = int(line.split(" ")[1])

    if command == "down":
        depth += amount
    elif command == "up":
        depth -= amount
    elif command == "forward":
        horizontal += amount


print(horizontal * depth)
