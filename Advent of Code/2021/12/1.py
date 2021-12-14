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


def traverse(history):
    lastNode = history[-1]
    if lastNode == "end":
        paths.append(history)
        return

    for neighbour in graph[lastNode]:
        if neighbour.islower() and neighbour in history:
            continue
        if history.count(neighbour) < len(lines) * 2:
            traverse(history + [neighbour])


traverse(["start"])
# print(paths)
print(len(paths))
