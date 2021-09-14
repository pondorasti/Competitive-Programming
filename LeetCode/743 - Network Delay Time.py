class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [math.inf] * n
        visited = {}
        nodes = [[] for _ in range(n)]

        # create adjacency list
        for time in times:
            source = time[0] - 1
            target = time[1] - 1
            weight = time[2]

            nodes[source].append((target, weight))

        # weighted BFS
        k -= 1
        queue = [k]
        dist[k] = 0
        while queue:
            parent = queue.pop(0)
            for child in nodes[parent]:
                if (parent, child[0]) not in visited:
                    queue.append(child[0])

                visited[(parent, child[0])] = True
                dist[child[0]] = min(dist[child[0]], dist[parent] + child[1])

        if math.inf in dist:
            return -1

        return max(dist)
