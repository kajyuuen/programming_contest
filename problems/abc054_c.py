from collections import defaultdict
from collections import deque

N, M = map(int, input().split())

graph = defaultdict(list)
edges = []

# 無向グラフの表現
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    edges.append((a, b))

ans = 0

def dfs(graph, node_start, visited):
    global ans
    if len(set(visited)) == len(set(graph)):
        ans += 1
        return
    for node_end in graph[node_start]:
        # まだ訪れていない
        if node_end not in visited:
            dfs(graph, node_end, visited + [node_end])
    return

dfs(graph, 1, [1])
print(ans)
