inputString = "19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,643,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,13,x,x,x,x,23,x,x,x,x,x,x,x,509,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29"
busIds = inputString.split(",")

for index in range(len(busIds)):
    if busIds[index].isdigit():
        busIds[index] = int(busIds[index])

foundAnswer = False
startingTime = 0
while not foundAnswer:
    startingTime += 643

    print(startingTime)

    isContinous = True
    for index in range(len(busIds)):
        if isinstance(busIds[index], int):
            if startingTime % busIds[index] != busIds[index] - index:
                isContinous = False
                break

    if isContinous:
        foundAnswer = True

print(startingTime)
100000000000000
1000000000
