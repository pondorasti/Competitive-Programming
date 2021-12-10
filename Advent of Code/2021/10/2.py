from typing import Match


with open('input.txt') as f:
    lines = f.readlines()


def getPoints(char):
    match char:
        case ")":
            return 1
        case "]":
            return 2
        case "}":
            return 3
        case ">":
            return 4


def getCloseOpposite(char):
    match char:
        case ")":
            return "("
        case "]":
            return "["
        case "}":
            return "{"
        case ">":
            return "<"


def getOpenOpposite(char):
    match char:
        case "(":
            return ")"
        case "[":
            return "]"
        case "{":
            return "}"
        case "<":
            return ">"


def isClosing(char):
    return char == ")" or char == "]" or char == "}" or char == ">"


scores = []
for line in lines:
    stack = []
    isCorrupted = False
    for char in line.strip():
        if isClosing(char) and stack[-1] == getCloseOpposite(char):
            stack.pop()
        elif isClosing(char) and stack[-1] != getCloseOpposite(char):
            isCorrupted = True
            break
        else:
            stack.append(char)

    if not isCorrupted:
        lineAns = 0
        while len(stack) != 0:
            lineAns = lineAns * 5 + getPoints(getOpenOpposite(stack.pop()))
        scores.append(lineAns)

scores.sort()
print(scores[len(scores) // 2])
