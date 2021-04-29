# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

givenDate = input()
dateSegments = givenDate.split(" ")
for index in range(len(dateSegments)):
    dateSegments[index] = int(dateSegments[index])

dayIndex = calendar.weekday(dateSegments[2], dateSegments[0], dateSegments[1])
day = calendar.day_name[dayIndex].upper()

print(day)
