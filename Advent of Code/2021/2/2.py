with open('input.txt') as f:
    lines = f.readlines()

horizontal = 0
depth = 0
aim = 0
for line in lines:
    command = line.split(" ")[0]
    amount = int(line.split(" ")[1])

    if command == "down":
        aim += amount
    elif command == "up":
        aim -= amount
    elif command == "forward":
        horizontal += amount
        depth += aim * amount


print(horizontal * depth)
