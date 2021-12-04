with open('input.txt') as f:
    lines = f.readlines()

marks = []
boards = []
currentMark = 0
marked = set()
won = False
ans = 0

for line in lines:
    if marks == []:
        marks = line.strip("\n").split(",")
    elif line == '\n':
        boards.append([])
    else:
        lastBoard = len(boards) - 1
        boards[lastBoard].append(line.strip("\n").split())


def sumBoard(board):
    sum = 0
    for line in board:
        for number in line:
            if number not in marked:
                sum += int(number)

    return sum


def checkBoard(board):
    # rows
    for i in range(0, len(board)):
        streak = True
        for j in range(0, len(board[i])):
            if board[i][j] not in marked:
                streak = False
                break

        if streak:
            return sumBoard(board)

    # columns
    for j in range(0, len(board[0])):
        streak = True
        for i in range(0, len(board)):
            if board[i][j] not in marked:
                streak = False
                break

        if streak:
            return sumBoard(board)

    return None


while not won:
    marked.add(marks[currentMark])

    for board in boards:
        sum = checkBoard(board)
        if sum is not None:
            ans = sum * int(marks[currentMark])
            won = True

    currentMark += 1

print(ans)
