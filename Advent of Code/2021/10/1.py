from typing import Match


with open('input.txt') as f:
    lines = f.readlines()


def getPoints(char):
    match char:
        case ")":
            return 3
        case "]":
            return 57
        case "}":
            return 1197
        case ">":
            return 25137


def getOpposite(char):
    match char:
        case ")":
            return "("
        case "]":
            return "["
        case "}":
            return "{"
        case ">":
            return "<"


def isClosing(char):
    return char == ")" or char == "]" or char == "}" or char == ">"


ans = 0
for line in lines:
    stack = []
    for char in line.strip():
        if isClosing(char) and stack[-1] == getOpposite(char):
            stack.pop()
        elif isClosing(char) and stack[-1] != getOpposite(char):
            ans += getPoints(char)

            break
        else:
            stack.append(char)
print(ans)
