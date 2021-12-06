earliestTimestamp = 939

inputString = "7,13,x,x,59,x,31,19"

busIds = inputString.split(",")

print(busIds)
minimumWaitingTime = 99999999999
answer = 0
for bus in busIds:
    if bus.isdigit():
        busId = int(bus)

        if earliestTimestamp % busId == 0:
            print(0)
            break

        waitingTime = busId - earliestTimestamp % busId
        if waitingTime < minimumWaitingTime:
            minimumWaitingTime = waitingTime
            answer = minimumWaitingTime * busId

print(minimumWaitingTime)
print(answer)
