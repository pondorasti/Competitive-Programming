with open('input.txt') as f:
    lines = f.readlines()

graph = {}
for line in lines:
    a, b = line.strip().split("-")

    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

paths = []


def traverse(history, isExempt):
    lastNode = history[-1]
    if lastNode == "end":
        paths.append(history)
        return

    for neighbour in graph[lastNode]:
        if neighbour == "start":
            continue
        elif neighbour.islower() and neighbour in history and isExempt:
            traverse(history + [neighbour], False)
        elif neighbour.islower() and neighbour in history:
            continue
        elif history.count(neighbour) < 5:  # < len(lines) * 2
            traverse(history + [neighbour], isExempt)


traverse(["start"], True)
# print(paths)
print(len(paths))
